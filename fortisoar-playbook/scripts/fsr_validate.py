#!/usr/bin/env python3
"""Static validator for FortiSOAR playbook JSON (automates the SKILL.md Step 4 checklist).

Usage:
  python3 fsr_validate.py <playbook.json> [--profile .fortisoar/instance-profile.json]

Checks (ERROR = will break import/execution; WARN = likely problem):
  JSON validity, unique UUIDs, triggerStep, route integrity, reachability,
  stepType UUIDs vs step-types-quickref.md, string coordinates, End step,
  workflow parameters, condition branches, versions:[], placeholder IRIs,
  connector operation/params vs connector-operations.md catalog,
  and (if --profile given) installed connector / version / config-UUID binding.

Exit code 1 if any ERROR, else 0.
"""

import argparse
import json
import os
import re
import sys

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUICKREF = os.path.join(SKILL_DIR, "reference", "step-types-quickref.md")
CATALOG = os.path.join(SKILL_DIR, "reference", "connector-operations.md")

UUID_RE = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
IRI_RE = re.compile(r"^/api/3/workflow_step_types/([0-9a-f-]{36})$")
PARENT_TYPE = "ee73e569-2188-43fe-a7f0-1964ba82a4de"
CYOPS_UTILS_TYPE = "0109f35d-090b-4a2b-bd8a-94cbc3508562"
EXTERNAL_CONN_TYPE = "0bfed618-0316-11e7-93ae-92361f002671"
START_TYPES = {  # trigger step types from quickref
    "f414d039-bb0d-4e59-9c39-a8f1e880b18a", "ea155646-3821-4542-9702-b246da430a8d",
    "9300bf69-5063-486d-b3a6-47eb9da24872", "b348f017-9a94-471f-87f8-ce88b6a7ad62",
    "df26c7a2-4166-4ca5-91e5-548e24c01b5f",
}
BUILTIN_CONNECTORS = {  # ship with platform; not in the GitHub catalog
    "cyops_utilities", "smtp", "ssh", "exchange", "slack", "mysql", "http",
    "code-snippet", "sentinelone", "whois-rdap",
}
REQUIRED_WORKFLOW_FIELDS = [
    "@type", "name", "isActive", "debug", "singleRecordExecution",
    "remoteExecutableFlag", "parameters", "synchronous", "collection",
    "versions", "triggerStep", "steps", "routes", "groups", "priority",
    "isEditable", "uuid", "owners", "isPrivate", "deletedAt", "recordTags",
    "aliasName", "tag", "description",
]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_valid_step_types():
    """All UUIDs in quickref except the 'NEVER use' section."""
    if not os.path.isfile(QUICKREF):
        return None
    valid, in_never = set(), False
    uuid_in_backticks = re.compile(r"`([0-9a-f-]{36})`")
    with open(QUICKREF) as f:
        for line in f:
            if line.startswith("## "):
                in_never = "NEVER use" in line
            if not in_never:
                valid.update(u for u in uuid_in_backticks.findall(line) if UUID_RE.match(u))
    return valid


def load_connector_catalog():
    """Parse connector-operations.md -> {slug: {version, ops: {op: {title, params}}}}."""
    if not os.path.isfile(CATALOG):
        return {}
    catalog, slug, version = {}, None, None
    row_re = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|[^|]*\|[^|]*\|\s*([^|]*?)\s*\|$")
    param_re = re.compile(r"`([^`]+)`\(([^)]*)\)")
    with open(CATALOG) as f:
        for line in f:
            m = re.match(r"^### `([^`]+)`", line)
            if m:
                slug, version = m.group(1), None
                catalog[slug] = {"version": None, "ops": {}}
                continue
            if slug:
                vm = re.match(r"^version (\S+)", line)
                if vm:
                    catalog[slug]["version"] = vm.group(1)
                    continue
                rm = row_re.match(line)
                if rm and rm.group(1) != "operation":
                    op, title, params_col = rm.group(1), rm.group(2).strip(), rm.group(3)
                    params = {p: ("REQ" in req) for p, req in param_re.findall(params_col)}
                    catalog[slug]["ops"][op] = {"title": title, "params": params}
    return catalog


def iri_uuid(iri):
    return iri.rstrip("/").split("/")[-1] if isinstance(iri, str) else None


def find_workflows(doc):
    if isinstance(doc, dict) and doc.get("type") == "workflow_collections":
        wfs = []
        for coll in doc.get("data", []):
            wfs.extend(coll.get("workflows", []))
        return wfs
    if isinstance(doc, dict) and doc.get("@type") == "Workflow":
        return [doc]
    return []


PLACEHOLDER_MARKERS = re.compile(r"TODO|PLACEHOLDER|REPLACE[_-]?ME|XXX", re.IGNORECASE)


def scan_placeholder_iris(obj, path="$"):
    """Flag TODO-style placeholder text inside /api/... IRIs.

    Only flags explicit placeholder markers — many legitimate IRIs end in
    non-UUID segments (/api/3/comments, /api/3/upsert/<module>, etc.).
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            scan_placeholder_iris(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            scan_placeholder_iris(v, f"{path}[{i}]")
    elif isinstance(obj, str) and obj.startswith("/api/") and PLACEHOLDER_MARKERS.search(obj):
        err(f"placeholder IRI at {path}: '{obj}'")


def check_workflow(wf, idx, valid_types, catalog, profile):
    tag = f"workflow[{idx}] '{wf.get('name', '?')}'"

    for field in REQUIRED_WORKFLOW_FIELDS:
        if field not in wf:
            err(f"{tag}: missing required field '{field}'")
    if wf.get("versions") != []:
        err(f"{tag}: 'versions' must be [] (never embed snapshots)")

    steps = [s for s in wf.get("steps", []) if isinstance(s, dict)]
    routes = [r for r in wf.get("routes", []) if isinstance(r, dict)]
    groups = [g for g in wf.get("groups", []) if isinstance(g, dict)]
    for kind, raw in (("steps", wf.get("steps")), ("routes", wf.get("routes")),
                      ("groups", wf.get("groups"))):
        if not isinstance(raw, list):
            err(f"{tag}: '{kind}' must be a list")
        elif len(raw) != len({"steps": steps, "routes": routes, "groups": groups}[kind]):
            err(f"{tag}: '{kind}' contains non-object entries")
    step_by_uuid = {s.get("uuid"): s for s in steps}

    # --- UUID uniqueness -----------------------------------------------------
    seen = {}
    for kind, objs in [("workflow", [wf]), ("step", steps), ("route", routes), ("group", groups)]:
        for o in objs:
            u = o.get("uuid")
            if not u:
                err(f"{tag}: {kind} missing uuid")
                continue
            if u in seen:
                err(f"{tag}: duplicate uuid {u} ({seen[u]} and {kind} '{o.get('name', '?')}')")
            seen[u] = f"{kind} '{o.get('name', '?')}'"

    # --- triggerStep ----------------------------------------------------------
    trigger_uuid = iri_uuid(wf.get("triggerStep", ""))
    if trigger_uuid not in step_by_uuid:
        err(f"{tag}: triggerStep IRI does not match any step uuid")
    elif valid_types is not None:
        st = step_by_uuid[trigger_uuid]
        m = IRI_RE.match(st.get("stepType", ""))
        if m and m.group(1) not in START_TYPES:
            warn(f"{tag}: triggerStep '{st.get('name')}' stepType is not a known trigger type")

    # --- routes + reachability ------------------------------------------------
    adj = {}
    for r in routes:
        src, tgt = iri_uuid(r.get("sourceStep", "")), iri_uuid(r.get("targetStep", ""))
        if src not in step_by_uuid:
            err(f"{tag}: route '{r.get('name', '?')}' sourceStep not a real step")
        if tgt not in step_by_uuid:
            err(f"{tag}: route '{r.get('name', '?')}' targetStep not a real step")
        adj.setdefault(src, []).append(tgt)
    reachable = set()
    stack = [trigger_uuid] if trigger_uuid in step_by_uuid else []
    while stack:
        cur = stack.pop()
        if cur in reachable:
            continue
        reachable.add(cur)
        stack.extend(adj.get(cur, []))
    for s in steps:
        if s.get("uuid") not in reachable:
            err(f"{tag}: step '{s.get('name', '?')}' is unreachable from trigger")

    # --- per-step checks ------------------------------------------------------
    end_found = False
    for s in steps:
        name = s.get("name", "?")
        st_iri = s.get("stepType", "")
        m = IRI_RE.match(st_iri)
        if not m:
            err(f"{tag}: step '{name}' stepType is not a full /api/3/workflow_step_types/ IRI")
            st_uuid = None
        else:
            st_uuid = m.group(1)
            if st_uuid == PARENT_TYPE:
                err(f"{tag}: step '{name}' uses parent stepType {PARENT_TYPE} (never usable)")
            elif valid_types is not None and st_uuid not in valid_types:
                err(f"{tag}: step '{name}' stepType UUID {st_uuid} not in step-types-quickref.md "
                    f"(typo? check character-by-character)")

        for coord in ("top", "left"):
            if not isinstance(s.get(coord), str):
                err(f"{tag}: step '{name}' '{coord}' must be a string, got {type(s.get(coord)).__name__}")

        args = s.get("arguments", {}) or {}
        if st_uuid == CYOPS_UTILS_TYPE and args.get("operation") == "no_op":
            end_found = True

        # Condition steps: step_iri targets must exist
        for cond in args.get("conditions", []) or []:
            cu = iri_uuid(cond.get("step_iri", ""))
            if cu not in step_by_uuid:
                err(f"{tag}: condition in step '{name}' points at unknown step_iri {cu}")
        if "conditions" in args and isinstance(args["conditions"], list):
            if not any(c.get("default") for c in args["conditions"]):
                warn(f"{tag}: condition step '{name}' has no default branch")

        # Connector steps
        connector = args.get("connector")
        if connector:
            check_connector_step(tag, name, st_uuid, args, catalog, profile)

    if not end_found:
        warn(f"{tag}: no End step (cyops_utilities / no_op) — official guidance is to "
             f"terminate every path in an End step, though FortiSOAR tolerates its absence")

    # --- parameters vs start step --------------------------------------------
    params = set(wf.get("parameters", []) or [])
    if params and trigger_uuid in step_by_uuid:
        start_args = step_by_uuid[trigger_uuid].get("arguments", {}) or {}
        sv = (start_args.get("step_variables") or {}).get("input") or {}
        exposed = set((sv.get("params") or {}).keys())
        exposed |= set((start_args.get("inputVariables") or {}).keys()
                       if isinstance(start_args.get("inputVariables"), dict) else [])
        missing = params - exposed
        if missing:
            warn(f"{tag}: workflow parameters {sorted(missing)} not exposed on start step "
                 f"(step_variables.input.params / inputVariables)")

    scan_placeholder_iris(wf)


def check_connector_step(tag, step_name, st_uuid, args, catalog, profile):
    connector = args.get("connector")
    label = f"{tag}: step '{step_name}' (connector '{connector}')"

    if st_uuid == EXTERNAL_CONN_TYPE:
        if not args.get("config"):
            err(f"{label}: external connector step missing 'config' UUID")
        if "name" not in args:
            warn(f"{label}: external connector step missing display 'name'")

    # --- catalog checks (3rd-party connectors only) ---------------------------
    if connector in BUILTIN_CONNECTORS:
        pass  # ops not fully catalogued; rely on profile/live test
    elif connector in catalog:
        entry = catalog[connector]
        op = args.get("operation")
        if op not in entry["ops"]:
            err(f"{label}: operation '{op}' not in catalog "
                f"(have: {', '.join(sorted(entry['ops'])[:8])}...)")
        else:
            op_entry = entry["ops"][op]
            if args.get("operationTitle") and args["operationTitle"] != op_entry["title"]:
                err(f"{label}: operationTitle '{args['operationTitle']}' != catalog title "
                    f"'{op_entry['title']}'")
            known = set(op_entry["params"])
            used = set((args.get("params") or {}).keys())
            for p in sorted(used - known):
                warn(f"{label}: param '{p}' not in catalog for operation '{op}'")
            for p in sorted(p for p, req in op_entry["params"].items() if req):
                if p not in used:
                    err(f"{label}: required param '{p}' missing for operation '{op}'")
        if entry["version"] and args.get("version") and args["version"] != entry["version"]:
            warn(f"{label}: version '{args['version']}' != catalog version '{entry['version']}'")
    else:
        warn(f"{label}: connector not in catalog and not a known built-in — verify slug")

    # --- instance profile checks ----------------------------------------------
    if profile:
        installed = {c["name"]: c for c in profile.get("connectors", [])}
        configs = profile.get("configs", [])
        if connector not in BUILTIN_CONNECTORS and connector not in installed:
            err(f"{label}: connector '{connector}' is NOT INSTALLED on the profiled instance")
        elif connector in installed and args.get("version"):
            inst_ver = installed[connector].get("version")
            if inst_ver and args["version"] != inst_ver:
                if connector in BUILTIN_CONNECTORS:
                    warn(f"{label}: version '{args['version']}' != installed '{inst_ver}' "
                         f"(platform connector — drift usually tolerated, verify operation exists)")
                else:
                    err(f"{label}: version '{args['version']}' != installed version '{inst_ver}'")
        cfg_uuid = args.get("config")
        if cfg_uuid and UUID_RE.match(str(cfg_uuid)):
            match = [c for c in configs if c.get("uuid") == cfg_uuid]
            if not match:
                err(f"{label}: config UUID {cfg_uuid} not found in instance configs")
            elif match[0].get("connector") not in (None, connector):
                err(f"{label}: config '{match[0].get('name')}' belongs to connector "
                    f"'{match[0].get('connector')}', not '{connector}'")


def main():
    ap = argparse.ArgumentParser(description="Validate FortiSOAR playbook JSON")
    ap.add_argument("playbook")
    ap.add_argument("--profile", help="path to instance-profile.json (enables live-instance checks)")
    args = ap.parse_args()

    try:
        with open(args.playbook) as f:
            doc = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot load {args.playbook}: {e}", file=sys.stderr)
        sys.exit(1)

    profile = None
    if args.profile:
        try:
            with open(args.profile) as f:
                profile = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            warn(f"could not load profile {args.profile}: {e} — skipping instance checks")

    workflows = find_workflows(doc)
    if not workflows:
        print("ERROR: no Workflow found (expected Shape A collection export or Shape B bare workflow)",
              file=sys.stderr)
        sys.exit(1)

    valid_types = load_valid_step_types()
    if valid_types is None:
        warn("step-types-quickref.md not found — skipping stepType whitelist checks")
    catalog = load_connector_catalog()
    if not catalog:
        warn("connector-operations.md not found — skipping connector catalog checks")

    for i, wf in enumerate(workflows):
        check_workflow(wf, i, valid_types, catalog, profile)

    for w in warnings:
        print(f"WARN : {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) across {len(workflows)} workflow(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
