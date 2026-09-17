#!/usr/bin/env python3
"""Import a generated playbook into a FortiSOAR instance and (optionally) execute a test plan.

Flow verified against a live FortiSOAR 7.6.1 instance:
  1. import  : POST /api/3/workflow_collections (collection shell)
               POST /api/3/workflows with nested steps/routes (whole playbook in one call)
               NOTE: the import-wizard endpoints (/api/import/, import_jobs) acknowledge
               but never process via API — direct CRUD is the reliable path.
  2. execute : POST /api/3/<module> (synthetic test record)
               POST /api/triggers/1/notrigger/<workflow-uuid>  -> {"task_id": ...}
  3. verify  : POST /api/wf/api/workflows/log_list/?format=json&task_id=<id> -> status
               GET  /api/3/<module>/<uuid> (record-field criteria)

Usage:
  python3 fsr_import_test.py <playbook.json> [--run --test-plan plan.json]
                             [--regen-uuids] [--cleanup] [--allow-production] [--insecure]

SAFETY: refuses to run against an instance whose config says environment="prod"
unless --allow-production is passed. The skill instructs the agent to also get
explicit in-chat confirmation before targeting production.

Re-imports: FortiSOAR rejects duplicate UUIDs (409). On re-runs either delete the
previous import first, or pass --regen-uuids to mint fresh UUIDs for every object.

Test plan JSON shape:
{
  "trigger": "manual|on_create|on_update|referenced|rest|schedule",
  "module": "alerts",
  "record_data": { ... },                       // synthetic record to create
  "existing_record": "/api/3/alerts/<uuid>",    // OR use an existing record
  "params": { ... },                            // extra trigger payload fields
  "success_criteria": [
    {"type": "job_status",  "equals": "finished"},
    {"type": "step_status", "step": "Enrich IOC", "equals": "success"},
    {"type": "record_field", "field": "status", "equals": "/api/3/picklists/<uuid>"}
  ]
}
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import uuid as uuidlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fsr_common import (ConfigError, FSRClient, die, extract_items, load_config)

UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")


def guard_environment(environment, allow_production, host):
    if environment.lower() in ("prod", "production") and not allow_production:
        die(f"config marks {host} as PRODUCTION. Re-run with --allow-production "
            f"ONLY after explicit user confirmation in chat.")
    if environment.lower() in ("prod", "production"):
        print(f"WARNING: running against PRODUCTION {host} — user confirmed.", file=sys.stderr)


def regen_uuids(doc):
    """Mint fresh UUIDs for objects OWNED by the export (workflow, steps, routes,
    groups, collection) and rewrite all references to them.

    UUIDs found in `uuid` fields of the export are the only ones replaced —
    picklist IRIs, connector config IDs, and other instance references are
    left untouched (they must keep pointing at real instance entities).
    """
    owned = set()
    def collect(obj):
        if isinstance(obj, dict):
            u = obj.get("uuid")
            if isinstance(u, str) and UUID_RE.fullmatch(u):
                owned.add(u)
            for v in obj.values():
                collect(v)
        elif isinstance(obj, list):
            for v in obj:
                collect(v)
    collect(doc)
    idmap = {u: str(uuidlib.uuid4()) for u in owned}
    pattern = re.compile("|".join(re.escape(u) for u in sorted(owned, key=len, reverse=True))) \
        if owned else None

    def walk(obj):
        if isinstance(obj, dict):
            return {k: walk(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [walk(v) for v in obj]
        if isinstance(obj, str) and pattern:
            return pattern.sub(lambda m: idmap[m.group(0)], obj)
        return obj
    return walk(doc)


def import_playbook(client, doc):
    """Create collection + workflow (nested steps/routes). Returns (wf_uuid, wf_name, coll_iri)."""
    workflows = []
    if doc.get("type") == "workflow_collections":
        for coll in doc.get("data", []):
            workflows.extend((coll, wf) for wf in coll.get("workflows", []))
    elif doc.get("@type") == "Workflow":
        workflows.append((None, doc))
    if not workflows:
        die("no workflows found in the playbook file", code=1)

    imported = []
    for coll, wf in workflows:
        coll_iri = None
        if coll is not None:
            name = coll.get("name")
            for attempt in range(3):
                body = {"name": name, "description": coll.get("description"),
                        "visible": True, "uuid": coll.get("uuid") if attempt == 0
                        else str(uuidlib.uuid4())}
                status, data = client.request("POST", "/api/3/workflow_collections", body=body)
                if status == 409:
                    q = urllib.parse.quote(name)
                    s2, d2 = client.get(f"/api/3/workflow_collections?$limit=1&name={q}")
                    items = extract_items(d2)
                    if items:
                        coll_iri = items[0].get("@id")
                        print(f"  collection '{name}' already exists — reusing")
                        break
                    # 409 but invisible => soft-deleted conflict; retry with new name
                    name = f"{coll.get('name')} ({uuidlib.uuid4().hex[:6]})"
                    print(f"  collection name conflicts with a soft-deleted record — "
                          f"retrying as '{name}'")
                    continue
                if not (200 <= status < 300):
                    die(f"collection create failed: HTTP {status}: {str(data)[:300]}", code=1)
                coll_iri = data.get("@id")
                break

        wf_body = {k: v for k, v in wf.items() if not k.startswith("@context")}
        wf_body["collection"] = coll_iri  # always point at the collection we just resolved
        if not wf_body.get("isActive"):
            wf_body["isActive"] = True  # test imports must be triggerable
            print("  note: forced isActive=true for the test import")
        status, data = client.request("POST", "/api/3/workflows", body=wf_body)
        if status == 409:
            die(f"workflow '{wf.get('name')}' conflicts with existing entities (409). "
                f"Delete the previous import (UI: Automation > Playbooks) or re-run "
                f"with --regen-uuids.", code=1)
        if not (200 <= status < 300):
            die(f"workflow create failed: HTTP {status}: {str(data)[:400]}", code=1)
        imported.append((data.get("uuid"), wf.get("name"), coll_iri))
    return imported


def find_workflow(client, wf_uuid, wf_name):
    """Verify via list endpoint (single-GET can be 403 for restricted keys)."""
    q = urllib.parse.quote(wf_name or "")
    status, data = client.get(f"/api/3/workflows?$limit=5&name={q}")
    for w in extract_items(data):
        if wf_uuid is None or w.get("uuid") == wf_uuid:
            return w
    return None


def create_test_record(client, module, record_data):
    status, data = client.request("POST", f"/api/3/{module}", body=record_data)
    if not (200 <= status < 300):
        die(f"could not create test record in '{module}': HTTP {status}: "
            f"{json.dumps(data)[:400]}", code=1)
    return data.get("@id"), data.get("uuid")


def execute_workflow(client, wf_uuid, record_uuid, params):
    payload = dict(params or {})
    if record_uuid:
        payload["records"] = [{"uuid": record_uuid}]
    status, data = client.request("POST", f"/api/triggers/1/notrigger/{wf_uuid}", body=payload)
    if not (200 <= status < 300):
        die(f"could not trigger workflow {wf_uuid}: HTTP {status}: {str(data)[:400]}. "
            f"(workflow inactive? trigger not manual?)", code=1)
    return data.get("task_id")


def poll_execution(client, task_id, timeout_s=120, interval_s=4):
    """Poll the wf-engine log for the task; returns (wf_entry, all_entries)."""
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        status, data = client.request(
            "POST", f"/api/wf/api/workflows/log_list/?format=json&task_id={task_id}", body={})
        if status == 200:
            items = extract_items(data)
            wf_entry = next((x for x in items if x.get("@type") == "Workflow"), None)
            if wf_entry and wf_entry.get("status") not in (None, "running", "in_progress", "pending", "active"):
                return wf_entry, items
        time.sleep(interval_s)
    return None, []


def evaluate_criteria(plan, wf_entry, entries, record_after):
    results = []
    for crit in plan.get("success_criteria", []):
        ctype, ok, detail = crit.get("type"), None, ""
        if ctype == "job_status":
            actual = (wf_entry or {}).get("status")
            ok = (actual == crit.get("equals"))
            detail = f"job status = {actual!r} (expected {crit.get('equals')!r})"
        elif ctype == "step_status":
            blob = json.dumps(entries)
            ok = crit.get("step") in blob and crit.get("equals", "success") in blob
            detail = f"step '{crit.get('step')}' status '{crit.get('equals')}' in execution log"
        elif ctype == "record_field":
            actual = (record_after or {}).get(crit.get("field"))
            ok = (actual == crit.get("equals"))
            detail = f"record field '{crit.get('field')}' = {actual!r} (expected {crit.get('equals')!r})"
        else:
            detail = f"unknown criterion type '{ctype}' — skipped"
        results.append((ok, ctype, detail))
    return results


def try_delete(client, iri, label):
    if not iri:
        return
    status, _ = client.request("DELETE", iri)
    if status == 403:
        print(f"cleanup WARNING: no DELETE permission for {label} — remove it in the UI",
              file=sys.stderr)
    else:
        print(f"cleanup: deleted {label} (HTTP {status})")


def main():
    ap = argparse.ArgumentParser(description="Import-test a FortiSOAR playbook")
    ap.add_argument("playbook")
    ap.add_argument("--run", action="store_true", help="also execute the test plan")
    ap.add_argument("--test-plan", help="test plan JSON (required with --run)")
    ap.add_argument("--regen-uuids", action="store_true",
                    help="mint fresh UUIDs before import (for re-runs without cleanup)")
    ap.add_argument("--cleanup", action="store_true",
                    help="delete test record + imported workflow/collection afterwards")
    ap.add_argument("--allow-production", action="store_true")
    ap.add_argument("--insecure", action="store_true")
    ap.add_argument("--host")
    ap.add_argument("--api-key")
    args = ap.parse_args()

    try:
        host, key, environment = load_config(args.host, args.api_key)
    except ConfigError as e:
        die(str(e))
    guard_environment(environment, args.allow_production, host)

    try:
        with open(args.playbook) as f:
            doc = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        die(f"cannot load {args.playbook}: {e}", code=1)
    if args.regen_uuids:
        doc = regen_uuids(doc)
        print("  regenerated all UUIDs for a fresh import")

    plan = None
    if args.run:
        if not args.test_plan:
            die("--run requires --test-plan <file>", code=1)
        with open(args.test_plan) as f:
            plan = json.load(f)

    client = FSRClient(host, key, insecure=args.insecure)

    # --- 1. import -------------------------------------------------------------
    print(f"Importing {args.playbook} -> {host} ...")
    imported = import_playbook(client, doc)
    wf_uuid, wf_name, coll_iri = imported[0]
    found = find_workflow(client, wf_uuid, wf_name)
    if not found:
        print("  import POSTs succeeded but workflow not visible in list — aborting",
              file=sys.stderr)
        sys.exit(1)
    print(f"  import OK: workflow '{wf_name}' ({wf_uuid}), active={found.get('isActive')}")
    if not found.get("isActive"):
        print("  NOTE: workflow is INACTIVE — it can be imported but not triggered. "
              "Set isActive=true in the export or activate in the UI.")

    created_record_iri = None
    results = []

    # --- 2. execute test plan ---------------------------------------------------
    if plan:
        if plan.get("existing_record"):
            record_uuid = plan["existing_record"].rstrip("/").split("/")[-1]
            created_record_iri = None
        else:
            created_record_iri, record_uuid = create_test_record(
                client, plan.get("module", "alerts"), plan.get("record_data", {}))
            print(f"  test record created: {created_record_iri}")

        print(f"  triggering workflow (trigger type: {plan.get('trigger')}) ...")
        task_id = execute_workflow(client, wf_uuid, record_uuid, plan.get("params"))
        print(f"  task_id: {task_id}")

        wf_entry, entries = poll_execution(client, task_id)
        if wf_entry is None:
            print("  no execution record found within timeout — playbook may not have fired "
                  "(trigger filters? active? test data matches?).", file=sys.stderr)

        record_after = None
        if created_record_iri or plan.get("existing_record"):
            iri = created_record_iri or plan["existing_record"]
            status, record_after = client.get(iri)
            if status != 200:
                record_after = None

        print("\n=== TEST RESULTS ===")
        results = evaluate_criteria(plan, wf_entry, entries, record_after)
        failed = 0
        for ok, ctype, detail in results:
            mark = "PASS" if ok else ("FAIL" if ok is False else "SKIP")
            if ok is False:
                failed += 1
            print(f"  [{mark}] {ctype}: {detail}")
        print(f"\n{len(results) - failed}/{len(results)} criteria passed")

    # --- cleanup -----------------------------------------------------------------
    if args.cleanup:
        try_delete(client, created_record_iri, "test record")
        try_delete(client, f"/api/3/workflows/{wf_uuid}", f"workflow '{wf_name}'")
        try_delete(client, coll_iri, "collection")

    if plan and any(ok is False for ok, _, _ in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
