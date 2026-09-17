#!/usr/bin/env python3
"""Import a generated playbook into a FortiSOAR instance and (optionally) execute a test plan.

This is the live half of the skill's self-test loop:
  1. import the collection/workflow JSON via the API (what the UI Import button does)
  2. optionally create test data, trigger the playbook, poll execution, evaluate criteria

Usage:
  python3 fsr_import_test.py <playbook.json> [--run --test-plan plan.json]
                             [--cleanup] [--allow-production] [--insecure]

SAFETY: refuses to run against an instance whose config says environment="prod"
unless --allow-production is passed. The skill instructs the agent to also get
explicit in-chat confirmation before targeting production.

Test plan JSON shape:
{
  "trigger": "manual|on_create|on_update|referenced|rest|schedule",
  "module": "alerts",
  "record_data": { ... },                     // synthetic record to create
  "existing_record": "/api/3/alerts/<uuid>",  // OR use an existing record
  "params": { ... },                          // referenced / rest triggers
  "success_criteria": [
    {"type": "job_status",  "equals": "Finished"},
    {"type": "step_status", "step": "Enrich IOC", "equals": "Success"},
    {"type": "record_field", "field": "status", "equals": "Resolved"}
  ]
}

If a candidate endpoint 404s on your instance, open https://<host>/swagger,
find the right path, and update the CANDIDATES below.
"""

import argparse
import json
import os
import sys
import time
import uuid as uuidlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fsr_common import (ConfigError, FSRClient, die, extract_items, load_config,
                        try_candidates)

IMPORT_CANDIDATES = [
    "/api/3/import",
]
EXECUTE_CANDIDATES = [  # trigger a workflow against a record / with params
    "/api/3/workflows/{wf}/execute",
    "/api/3/workflow/execute",
]
EXECUTION_LOG_CANDIDATES = [  # execution history for a workflow
    "/api/3/workflow_logs?$limit=50&$orderby=createdAt desc",
    "/api/3/workflow_execution_history?$limit=50",
]


def guard_environment(environment, allow_production, host):
    if environment.lower() in ("prod", "production") and not allow_production:
        die(f"config marks {host} as PRODUCTION. Re-run with --allow-production "
            f"ONLY after explicit user confirmation in chat.")
    if environment.lower() in ("prod", "production"):
        print(f"WARNING: running against PRODUCTION {host} — user confirmed.", file=sys.stderr)


def import_playbook(client, doc):
    """POST the export JSON; fall back to multipart file upload if raw JSON fails."""
    statuses = []
    for path in IMPORT_CANDIDATES:
        status, data = client.request("POST", path, body=doc)
        statuses.append((path, status))
        if 200 <= status < 300:
            return data
    # multipart attempt
    boundary = "----fsrskill" + uuidlib.uuid4().hex
    payload = json.dumps(doc).encode()
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
            f"filename=\"playbook.json\"\r\nContent-Type: application/json\r\n\r\n").encode() \
        + payload + f"\r\n--{boundary}--\r\n".encode()
    for path in IMPORT_CANDIDATES:
        status, data = client.request(
            "POST", path, raw_body=body,
            extra_headers={"Content-Type": f"multipart/form-data; boundary={boundary}"})
        statuses.append((path + " (multipart)", status))
        if 200 <= status < 300:
            return data
    die("import failed on all candidates: " +
        ", ".join(f"{p} -> HTTP {s}" for p, s in statuses) +
        ". Check /swagger for the import endpoint and update IMPORT_CANDIDATES.")


def find_imported_workflow(client, doc):
    """Locate the workflow we just imported, by uuid then by name."""
    wanted = {wf.get("uuid"): wf.get("name")
              for coll in doc.get("data", []) for wf in coll.get("workflows", [])}
    if not wanted and doc.get("@type") == "Workflow":
        wanted = {doc.get("uuid"): doc.get("name")}
    for wf_uuid, name in wanted.items():
        status, data = client.get(f"/api/3/workflows/{wf_uuid}")
        if status == 200:
            return wf_uuid, name
        status, data = client.get(f"/api/3/workflows?$limit=1&name={name}")
        items = extract_items(data)
        if status == 200 and items:
            return items[0].get("uuid"), name
    return None, None


def create_test_record(client, module, record_data):
    status, data = client.request("POST", f"/api/3/{module}", body=record_data)
    if not (200 <= status < 300):
        die(f"could not create test record in '{module}': HTTP {status}: "
            f"{json.dumps(data)[:400]}")
    iri = data.get("@id") or f"/api/3/{module}/{data.get('uuid')}"
    return iri


def execute_workflow(client, wf_uuid, record_iri, params):
    payload = {}
    if record_iri:
        payload["records"] = [record_iri]
    if params:
        payload["params"] = params
    last = None
    for template in EXECUTE_CANDIDATES:
        path = template.format(wf=wf_uuid)
        status, data = client.request("POST", path, body=payload)
        last = (path, status, data)
        if 200 <= status < 300:
            return data
    p, s, d = last
    die(f"could not trigger workflow: last attempt {p} -> HTTP {s}: "
        f"{json.dumps(d)[:400]}. Check /swagger and update EXECUTE_CANDIDATES.")


def poll_execution(client, wf_uuid, timeout_s=120, interval_s=5):
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        for path in EXECUTION_LOG_CANDIDATES:
            status, data = client.get(path)
            if 200 <= status < 300:
                for item in extract_items(data):
                    if wf_uuid in json.dumps(item):
                        return item
        time.sleep(interval_s)
    return None


def evaluate_criteria(plan, execution, record_after):
    results = []
    for crit in plan.get("success_criteria", []):
        ctype = crit.get("type")
        ok, detail = None, ""
        if ctype == "job_status":
            actual = (execution or {}).get("status") or (execution or {}).get("state")
            ok = (actual == crit.get("equals"))
            detail = f"job status = {actual!r} (expected {crit.get('equals')!r})"
        elif ctype == "step_status":
            blob = json.dumps(execution or {})
            ok = crit.get("step") in blob and crit.get("equals", "Success") in blob
            detail = f"step '{crit.get('step')}' status '{crit.get('equals')}' in execution log"
        elif ctype == "record_field":
            actual = (record_after or {}).get(crit.get("field"))
            ok = (actual == crit.get("equals"))
            detail = f"record field '{crit.get('field')}' = {actual!r} (expected {crit.get('equals')!r})"
        else:
            detail = f"unknown criterion type '{ctype}' — skipped"
        results.append((ok, ctype, detail))
    return results


def main():
    ap = argparse.ArgumentParser(description="Import-test a FortiSOAR playbook")
    ap.add_argument("playbook")
    ap.add_argument("--run", action="store_true", help="also execute the test plan")
    ap.add_argument("--test-plan", help="test plan JSON (required with --run)")
    ap.add_argument("--cleanup", action="store_true",
                    help="delete test record + imported workflow afterwards")
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

    plan = None
    if args.run:
        if not args.test_plan:
            die("--run requires --test-plan <file>", code=1)
        with open(args.test_plan) as f:
            plan = json.load(f)

    client = FSRClient(host, key, insecure=args.insecure)

    # --- 1. import -------------------------------------------------------------
    print(f"Importing {args.playbook} -> {host} ...")
    import_result = import_playbook(client, doc)
    print(f"  import response: {json.dumps(import_result)[:600]}")
    wf_uuid, wf_name = find_imported_workflow(client, doc)
    if wf_uuid:
        print(f"  import OK: workflow '{wf_name}' ({wf_uuid})")
    else:
        print("  import returned success but workflow not found afterwards — "
              "check the response above for validation errors.", file=sys.stderr)
        sys.exit(1)

    created_record, execution = None, None

    # --- 2. execute test plan ---------------------------------------------------
    if plan:
        if plan.get("existing_record"):
            record_iri = plan["existing_record"]
        elif plan.get("record_data") and plan.get("module"):
            record_iri = create_test_record(client, plan["module"], plan["record_data"])
            created_record = record_iri
            print(f"  test record created: {record_iri}")
        else:
            record_iri = None

        print(f"  triggering workflow (trigger type: {plan.get('trigger')}) ...")
        execution_ack = execute_workflow(client, wf_uuid, record_iri, plan.get("params"))
        print(f"  execute response: {json.dumps(execution_ack)[:400]}")

        execution = poll_execution(client, wf_uuid)
        if execution is None:
            print("  no execution record found within timeout — playbook may not have fired "
                  "(trigger filters? active? test data matches?).", file=sys.stderr)

        record_after = None
        if record_iri:
            status, record_after = client.get(record_iri)
            if status != 200:
                record_after = None

        # --- 3. per-criterion report -------------------------------------------
        print("\n=== TEST RESULTS ===")
        results = evaluate_criteria(plan, execution, record_after)
        failed = 0
        for ok, ctype, detail in results:
            mark = "PASS" if ok else ("FAIL" if ok is False else "SKIP")
            if ok is False:
                failed += 1
            print(f"  [{mark}] {ctype}: {detail}")
        print(f"\n{len(results) - failed}/{len(results)} criteria passed")

    # --- cleanup -----------------------------------------------------------------
    if args.cleanup:
        if created_record:
            s, _ = client.request("DELETE", created_record)
            print(f"cleanup: deleted test record (HTTP {s})")
        if wf_uuid:
            s, _ = client.request("DELETE", f"/api/3/workflows/{wf_uuid}")
            print(f"cleanup: deleted imported workflow (HTTP {s})")

    if plan and any(ok is False for ok, _, _ in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
