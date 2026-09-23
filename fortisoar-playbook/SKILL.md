---
name: fortisoar-playbook
description: Design, generate, and self-test FortiSOAR playbooks (workflow JSON). Use when the user mentions FortiSOAR, playbook, SOAR workflow, playbook collection, connector operations, playbook JSON import/export, or wants to automate a security process in FortiSOAR. Covers trigger setup, step types, routing, Jinja templating, instance connector discovery, static validation, live import-testing, and producing import-ready JSON.
---

# FortiSOAR Playbook Builder — v2.4

This skill helps design and generate FortiSOAR playbook JSON that can be imported
into FortiSOAR 7.6.x — and **verifies it against a live instance** before handing
it over. It is self-contained: all reference material is bundled in `reference/`,
`templates/`, and `scripts/` relative to this file.

**v2.7:** new "Iterating on an existing playbook" guidance + a duplicate guard in
`fsr_import_test.py` (`--allow-duplicates`) so a fix updates the existing playbook
instead of silently importing a new suffixed copy.
**v2.6:** after a live import test, the agent must ask the user whether to keep
the imported playbook/collection or clean it up — never auto-cleanup and never
silently leave artifacts.
**v2.5:** generated playbooks default to `"debug": true` (verbose per-step logging);
new configurations are created with `"default": true`; step names must be
alphanumeric/space/underscore only (no `?`).
**v2.4:** new configurations are created with `"default": true`; step names must
be alphanumeric/space/underscore only (no `?`); `debug` defaults to `false`.
**v2.3:** connector install API verified end-to-end on a live dev instance
(metadata source, install endpoint, async polling, permission probe). **v2.2:**
missing-connector handling (install-then-discover with user approval);
native-steps-first generation rule (Code Snippet = last resort). **v2.1:** every
API endpoint verified against a live 7.6.1 instance; MCP added as a second
discovery method. **v2.0:** instance discovery (real connector versions + config
UUIDs), clarification gate (no generation on vague requirements), agreed test plan
before generation, automated static validation, guarded live import-test loop.

## When to use

- User wants to build / create / generate a FortiSOAR playbook.
- User wants to modify or extend an existing playbook JSON.
- User asks how to accomplish X in FortiSOAR automation.
- User mentions FortiSOAR, SOAR playbook, workflow collection, connector step, etc.

Do NOT use for: generic Python/Ansible scripting unrelated to FortiSOAR, or for
configuring FortiSOAR appliance infrastructure (that is ops, not playbook design).

## Reference material (read these before generating)

This skill bundles five reference docs. **Always read the relevant ones before
producing JSON** — FortiSOAR hard-fails on invalid structure.

| File | Use for |
|---|---|
| `reference/playbook-json-schema.md` | The JSON export structure: shapes, every Workflow field, all 22 step types with argument skeletons + examples, routes, groups, picklists, positioning, validation rules. This is the authoritative schema. |
| `reference/connector-operations.md` | Catalog of all 3rd-party connector operations harvested from the official `fortinet-fortisoar` GitHub org (379 connectors, 3339 operations). For each connector: slug, version, operation → title, and parameters (name, title, required). **Read this before writing any connector-call step** to pick the exact `operation`/`operationTitle` and `params` keys. Full parameter detail (descriptions, data types, choices, defaults) is in `reference/connector-manifests.json`. |
| `reference/jinja-cookbook.md` | 50+ real production Jinja patterns (trigger input, params, REST request, step output, for_each item, picklist/fromIRI filters, arrow dates, list mutation, conditionals) harvested from 1367 official playbooks. Use as copy-paste templates. |
| `reference/guide-condensed.md` | Concepts from the official Playbooks Guide: trigger types, variables & Jinja, routing/conditions, connector operations, error handling, best practices, step-result Jinja patterns. |
| `reference/step-types-quickref.md` | One-page lookup: stepType UUID → label → argument skeleton + routing notes. Use for quick lookups while building. |

Templates live in `templates/`:
- `skeleton-collection.json` — Shape A: collection export wrapper (most common import format).
- `skeleton-playbook.json` — Shape B: single bare Workflow.
- `templates/snippets/*.json` — Ready-to-paste step JSON: `start-manual-button`,
  `start-on-create`, `start-referenced`, `start-rest`, `set-variable`,
  `connector-call`, `condition`, `call-playbook`, `add-comment`, `end-noop`,
  `manual-task`, `for-each-create`.
- `templates/get-uuid-config.json` — Helper referenced playbook for MCP-based
  discovery (Step 0, Method 2): returns connector ↔ configuration `config_id`
  pairs. Import once into the instance, run it, harvest the output.

## Scripts (v2)

All scripts are python3 stdlib-only — no pip installs. They resolve FortiSOAR
credentials from `--host`/`--api-key` flags, `FORTISOAR_HOST`/`FORTISOAR_API_KEY`
env vars, or `<workspace>/.fortisoar/config.json` (see Step 0).

| Script | Purpose |
|---|---|
| `scripts/fsr_discover.py` | Pull the instance profile (installed connectors + versions, configuration names/UUIDs, picklists) into `.fortisoar/instance-profile.json`. |
| `scripts/fsr_validate.py` | Automate the Step 4 static checklist against a generated playbook JSON; with `--profile` also checks installed connectors, versions, and config UUIDs. Exit 1 on any ERROR. |
| `scripts/fsr_import_test.py` | Import the playbook into the instance via API; optionally execute a test plan (create test data → trigger → poll → per-criterion pass/fail). Refuses production unless explicitly allowed. |

Endpoint note: all endpoints in these scripts were verified against a live 7.6.1
instance. Auth is `Authorization: API-KEY <key>`. If your version behaves
differently, the instance's interactive API docs at `https://<host>/swagger` are
ground truth — update the paths at the top of the affected script.

## Workflow: how to build a playbook

### Step 0 — Instance profile (do this first, once per workspace)

Playbook steps that call connectors must bind to a **real installed connector
version** and a **real configuration UUID** — placeholders are the #1 cause of
broken imports. Two methods; prefer Method 1, use Method 2 when the agent
environment has FortiSOAR MCP servers configured.

**Method 1 — REST discovery script (works anywhere):**

1. Check for `<workspace>/.fortisoar/config.json` or `FORTISOAR_HOST` /
   `FORTISOAR_API_KEY` env vars.
2. If none exist, **ask the user for their FortiSOAR IP/hostname and API key**,
   and whether the instance is dev or production. Write:
   ```json
   // .fortisoar/config.json
   { "host": "https://<fsr-ip-or-host>", "api_key": "<key>", "environment": "dev" }
   ```
   Tell the user to add `.fortisoar/` to `.gitignore`. Never commit it, never log
   the key, never embed it in playbook JSON.
3. Run `python3 scripts/fsr_discover.py` (add `--insecure` for self-signed dev
   certs). Review `.fortisoar/instance-profile.json` with the user: which
   connectors are installed, which configs exist. Verified endpoints (7.6.1):
   `GET /api/integration/connectors/` (paged), `GET /api/integration/configuration/`
   (config UUIDs + health), `GET /api/3/picklists`. Auth header:
   `Authorization: API-KEY <key>`.

**Method 2 — FortiSOAR MCP servers (when configured):**

FortiSOAR 7.6.x exposes MCP endpoints (`/mcp/modules/`, `/mcp/soc/`,
`/mcp/utility/`, `/mcp/playbooks/`) with the same `Authorization: API-KEY <key>`
header. If the user's agent config (e.g. `opencode.json` `mcp` section) has
these configured, you can call MCP tools directly instead of the script —
same profile fields: installed connectors + versions, configuration names/UUIDs,
picklists. A ready-made helper is bundled: `templates/get-uuid-config.json`
(a referenced playbook that returns connector↔config_id pairs); import it once,
run it via the playbooks MCP, and harvest its output. Persist the results to
`.fortisoar/instance-profile.json` in the same shape the script writes, so the
rest of the workflow (validation, generation) is method-agnostic.

**Connector missing? Install-then-discover (dev only, with user approval):**

If the needed connector is not in the profile, you may offer to install it — but
only on a dev instance and only after explicit in-chat user approval. Installing
pulls OS-level dependencies onto the appliance, so never auto-install, and never
install on prod without the same explicit confirmation Step 4.5 requires.

Verified API flow (verified end-to-end against a live 7.6.x dev instance):

1. **Fetch install metadata**: `POST /api/3/fetch_repo_content` with
   `{"path": "connectors/info/<name>_<version>/info.json"}` returns `name`,
   `label`, `version`, `description`, `category`, `publisher`, and the critical
   `rpm_name` (`cyops-connector-<name>-<version>`). Browse
   `{"path": "connectors/info/"}` (autoindex HTML) to list every available
   connector+version. (Note: the prettier `content-hub/<name>-<ver>/...` repo
   tree has NO `rpm_name`; and `/api/integration/connectors/<name>/<version>/`
   only covers connectors the instance already knows — not-installed ones
   return "No matching connector by name".)
2. **Install**: `POST /api/integration/install-connector/?format=json` with
   `{"name", "label", "version", "rpm_name", "category", "description",
   "publisher"}` (PUT for an update of an already-installed connector).
   Minimal field: `rpm_name` alone passes validation, but send the full set
   like the UI does. The call is async — 200 returns immediately
   (`{"message": "Installing connector <name> version <ver>"}`); poll
   `GET /api/integration/connectors/?name=<name>` until `status` moves
   `In-Progress` → `Completed` (observed ~35 s for a small connector).
3. **Configure**: re-run discovery — the connector now appears with
   `config_count: 0`. Ask the user for the connector's configuration
   credentials (API keys, tokens — you cannot invent these). Create the
   configuration via `POST /api/integration/configuration/` with
   `{"name": "...", "connector": <numeric connector id>, "config": { ... }, "default": true}`
   — **always set `"default": true`** so the new config is the connector's
   unambiguous default (a non-default config can silently not-bind in the
   playbook). The response returns `config_id` (the UUID the step's `config`
   binds to). Then re-run discovery once more to harvest the real `config` UUID
   (or read `config_id` straight from the response).
4. Continue to Step 1. If the user declines the install, fall back to
   proposing an installed alternative or a built-in connector workaround.

The Content Hub UI (Content Hub > search > Install) remains a valid alternative
if the user prefers to click.

**No API access at all?** Fallback: ask the user to export one existing playbook
from their instance that uses a configured connector, and harvest real `config`
UUIDs from it. Say clearly that live validation (Step 4.5) is then unavailable.

### Step 1 — Clarify the use case (GATE: no generation until requirements are solid)

**If anything about the request is unclear, ask.** A vague one-liner
("enrich IOCs") is not a requirement. Ask one focused question at a time and keep
asking until every item below is nailed down. Do not proceed to Step 2, and
absolutely do not write JSON, while any of these is unknown or assumed:

1. **Trigger type** — how does the playbook start?
   - Manual button on a module record (e.g. a button on Alerts)
   - On Create (auto-fires when a record is created)
   - On field/status change (auto-fires on update)
   - Referenced (called from another playbook — sub-playbook)
   - REST API endpoint (inbound HTTP)
   - Scheduled (runs on a cron-like schedule — see Schedule API)
2. **Module(s)** — which FortiSOAR module(s)? (alerts, indicators, incidents, threat_intel_feeds, vulnerabilities, assets, etc.)
3. **Input** — user input form (manual trigger) or parameters (referenced)? What fields, with what example values?
4. **Logic / steps** — what should it do, in order? Which connectors (check them
   against the instance profile from Step 0 — if a requested connector is not
   installed, say so and offer, in order: (a) install-then-discover on dev with
   the user's approval (see Step 0), (b) an installed alternative, (c) a built-in
   connector workaround; never guess)? What conditions, what happens on each
   branch? What loops?
5. **Output** — comment on the record? create/update a record? send email? call a sub-playbook? return a value to a parent?
6. **Edge cases** — what should happen when a connector call fails, returns
   empty, or the record field is missing?

When you believe the requirement is solid, play it back in 3-6 lines
("Here's what I'll build: …") and get an explicit "yes". That playback is the gate.

### Step 2 — Design the flow AND the test plan

Present **two artifacts** for approval before generating:

**A. The flow:**
```
Start (trigger) → [Set Variable] → [Connector: ...] → [Condition: ...]
  → Yes: [Create Record / Comment] → End
  → No:  [Send Email] → End
```
- Every playbook needs exactly one Start step and at least one End step.
- Routes connect steps by UUID; the route `name` is `"<source> -> <target>"`.
- Use Groups (note/block) to annotate sections; optional but recommended.

**B. The test plan** — how we will prove the playbook works in Step 4.5:

| Element | Define |
|---|---|
| What to test | Scope: (a) import-only, (b) import + execute (default), (c) execute every branch |
| Test data | You generate it: synthetic record JSON with field values matching what the playbook's Jinja reads; one dataset per condition branch where feasible. User confirms or overrides values that must mean something to a real connector (e.g. an IOC that scores malicious vs clean). Fallback: an existing record IRI in dev. |
| Success criteria | Explicit pass/fail list, e.g. import OK → job status Finished → step "Enrich" Success → comment exists on record |

Trigger drives test data:

| Trigger | Test data | Default success criteria |
|---|---|---|
| Manual button | Synthetic record (or existing IRI) | Executes on record, job Finished |
| On Create | Script creates record with defined fields | Trigger fires, job Finished |
| On Update | Create → update watched field | Trigger fires on update, job Finished |
| Referenced | Call with declared test params | Returns expected output |
| REST endpoint | Sample JSON payload | Endpoint 200, job Finished |
| Scheduled | Trigger schedule immediately via API | Job Finished |

Get the user's approval on both artifacts. Then write the test plan to
`.fortisoar/test-plan-<playbook-name>.json` (shape documented in
`scripts/fsr_import_test.py`).

### Step 3 — Generate the JSON

Produce a single JSON file the user can import. Use **Shape A (collection export)**
unless the user asks for a bare single playbook.

#### Generation rules (MUST follow)

1. **UUIDs**: generate fresh random UUIDs (v4) for every `uuid` field — workflow,
   steps, routes, groups. Never reuse a UUID across objects within one playbook.
2. **stepType**: always a full IRI string `/api/3/workflow_step_types/<uuid>`.
   Look up the correct UUID in `reference/step-types-quickref.md`.
   - NEVER use `ee73e569-...` (it is a parent type, not usable on steps).
   - Watch the last-digit trap: `b593663d-...-770` = Find Records, `b593663d-...-722` = Update Record.
3. **Coordinates**: `top` and `left` are **strings**, not numbers (e.g. `"40"`,
   not `40`). Same for group `height`/`width`. Convention: Start at `top:"40",
   left:"40"`; flow rightward (`left += 400`) and downward (`top += 200`).
4. **Cross-references & step names**: steps reference each other via IRI built from
   the target's `uuid`: `/api/3/workflow_steps/<uuid>`. Routes' `sourceStep`/`targetStep`, the
   workflow's `triggerStep`, the Condition step's `step_iri`, the Call-Playbook's
   `workflowReference`, etc. **Step names may contain only alphanumeric characters,
   spaces, and underscores** — never `?`, `!`, `-`, `.`, or other punctuation. A
   `?` in a Condition step name (e.g. "Compromised?") is rejected by FortiSOAR;
   name it "Compromised" (or "Is Compromised") instead. Jinja references the step
   by name with spaces mapped to underscores (`vars.steps.<StepName>`), so keep
   names short, unique, and free of punctuation.
5. **Jinja templating**: use `{{vars.<name>}}` for variables,
   `{{vars.input.records[0].<field>}}` for trigger record fields,
   `{{vars.input.params['<name>']}}` for declared parameters,
   `{{vars.steps.<StepName>.data}}` for previous step output (by step **name**).
   Use `{% if %}...{% endif %}` for logic inside `temporary_var`.
6. **Parameters**: if a playbook accepts inputs, declare them BOTH on the Workflow
   object (`"parameters": ["name1", "name2"]`) AND expose them on the Start step
   (via `step_variables.input.params` for referenced starts, or `inputVariables`
   for manual button forms).
7. **Picklists**: reference by IRI `/api/3/picklists/<uuid>`. Use real UUIDs from
   the instance profile (Step 0) when available; otherwise common ones are in the
   schema reference. If you don't know a picklist UUID, use a placeholder
   comment `"TODO: replace with correct picklist IRI for <value>"` and tell the
   user to look it up in their FortiSOAR instance.
8. **Connector calls**: look up the connector in `reference/connector-operations.md`
   to get the exact `connector` slug, `operation`, `operationTitle`, `version`, and
   the `params` keys (parameter names + which are required). Include `connector`,
   `operation`, `operationTitle`, `version`, `params`, `step_variables`. For external
   connectors add `name` (display name), `config`, `pickFromTenant: false`.
   - **Config binding (v2)**: `config` MUST be the UUID of a real configuration
     from `.fortisoar/instance-profile.json` (or harvested from a user-provided
     export). `version` MUST match the installed version in the profile. If the
     connector is not in the profile's installed list, STOP and tell the user —
     do not generate the step with guessed values.
   - **Slug accuracy**: the GitHub repo may be `connector-<slug>` but the playbook
     `connector` field uses the manifest `name` (e.g. `virustotal-premium`). A few
     built-in connectors (`cyops_utilities`, `smtp`, `ssh`, `exchange`, `slack`,
     `mysql`, `http`, `code-snippet`, `sentinelone`, `whois-rdap`) ship with the
     platform and are NOT in the GitHub catalog — consult the in-instance connector
     docs for their operations. `cyops_utilities` ops (`no_op`, `make_cyops_request`,
     `format_richtext`, `json_to_html`, etc.) are listed in the schema reference §6.
   - For the built-in `cyops_utilities` connector (stepType `0109f35d`) the
     `config`/`name`/`pickFromTenant` keys are omitted.
9. **Native steps first, Code Snippet last resort**: implement logic using, in
   order of preference: (1) native step types + Jinja (Set Variable, Condition,
   loops, record CRUD — patterns in `reference/jinja-cookbook.md`); (2) built-in
   utility connectors (`cyops_utilities` ops such as `format_richtext`,
   `json_to_html`, `make_cyops_request`; `http`; etc.); (3) the Code Snippet
   connector — only when neither (1) nor (2) can express the logic. When a Code
   Snippet step is used, justify it in one line (step `description` + tell the
   user) stating why native steps can't do it. Rationale: native steps are
   visible in the designer, show per-step input/output when debugging, and
   survive upgrades better; sandboxed Python is opaque and harder to maintain.
10. **End step**: terminate every playbook path in an End step (`cyops_utilities` /
    `no_op` / operationTitle "Utils: No Operation") — official guidance. FortiSOAR
    tolerates playbooks without one, so existing exports may lack it; still include
    it in anything you generate.
11. **Required Workflow fields** (minimum for valid import): `@type:"Workflow"`,
    `name`, `isActive`, `debug`, `singleRecordExecution`, `remoteExecutableFlag`,
    `parameters`, `synchronous`, `collection`, `versions:[]`, `triggerStep`,
    `steps`, `routes`, `groups`, `priority`, `isEditable`, `uuid`, `owners:[]`,
    `isPrivate`, `deletedAt:null`, `recordTags:[]`, `aliasName:null`,
    `tag:null`, `description`.
    Use `"priority": "/api/3/picklists/2b563c61-ae2c-41c0-a85a-c9709585e3f2"` (Medium).
    Set `"debug": true` by default — debug mode logs verbose per-step input/output
    so the user can see exactly what each step did during design and testing.
12. **Collection wrapper (Shape A)**: wrap the Workflow in
    `{ "type":"workflow_collections", "data":[ { ...collection..., "workflows":[ <workflow> ] } ], "exported_tags":[] }`.
    Give the collection a `uuid`, `name`, `description`, `visible:true`,
    `deletedAt:null`, `recordTags:[]`, `importedBy:[]`.
13. **Output the file** to `<meaningful-name>.json` in the current directory
    (or a path the user specifies).

### Step 4 — Validate (automated)

Run the validator — it enforces the checklist below as code:

```bash
python3 scripts/fsr_validate.py <playbook.json> --profile .fortisoar/instance-profile.json
```

- [ ] Valid JSON (no trailing commas, no comments).
- [ ] Every step has a unique `uuid`; every route and group too.
- [ ] `triggerStep` IRI matches the Start step's UUID.
- [ ] Every route's `sourceStep`/`targetStep` match real step UUIDs.
- [ ] Every step (except Start) is reachable via a route.
- [ ] No step uses `ee73e569-...` as its stepType.
- [ ] `top`/`left` are strings.
- [ ] End step present and reachable.
- [ ] Parameters declared on Workflow match what the Start step exposes.
- [ ] Condition steps: every `conditions[].step_iri` points to a real step; one
      condition has `"default": true` if a default branch is wanted.
- [ ] `versions` is `[]` (never embed snapshots).
- [ ] Connector calls: `operation`/`operationTitle`/`version` match a real entry in
      `connector-operations.md`; `params` keys match the operation's parameters;
      required params present.
- [ ] **No `TODO` or placeholder text inside `/api/3/...` IRIs** — every picklist
      IRI, connector config, or step IRI must be either a real UUID or a Jinja
      expression. Invalid `/api/3/picklists/TODO-*` IRIs cause a misleading
      "Some of the Playbooks already exist" import error.
- [ ] **Every stepType UUID verified character-by-character** against
      `step-types-quickref.md`. A single-character typo (e.g. `472b` vs `472f`)
      produces an unrecognized step type and the same misleading import error.
- [ ] **(with `--profile`)** Connector installed on the instance, `version` matches
      installed version, `config` UUID exists in the instance's configurations.

Fix every ERROR and re-run until clean. Review WARNs and fix or justify each.

### Step 4.5 — Live import test (when API access exists)

Prove the playbook in the dev instance using the approved test plan:

```bash
python3 scripts/fsr_import_test.py <playbook.json> --run \
    --test-plan .fortisoar/test-plan-<name>.json --regen-uuids
```

Verified mechanics (7.6.1): import is direct CRUD (`POST /api/3/workflow_collections`
+ `POST /api/3/workflows` with nested steps/routes — the import-wizard endpoints
`/api/import/` + `import_jobs` acknowledge but never process via API); execution is
`POST /api/triggers/1/notrigger/<wf-uuid>`; polling is
`POST /api/wf/api/workflows/log_list/?task_id=<id>`.

1. **Import** — the script imports and verifies visibility in the workflow list.
   On failure, map the error to a cause (see Step 5's known traps), fix the JSON,
   re-validate (Step 4), re-import. **Max 3 fix rounds**, then stop and show the
   user the raw error and your diagnosis. If a fix means re-importing a playbook
   that's already on the instance, do **not** just `--regen-uuids` — that mints a
   duplicate copy; follow "Iterating on an existing playbook" (below) to update in
   place instead. The script forces `isActive=true` on test imports so they can be
   triggered.
2. **Execute** — with `--run`, the script creates the test data, triggers the
   playbook, polls execution, and prints **per-criterion PASS/FAIL**. A failed
   criterion means the playbook (or the test data) is wrong — diagnose, fix,
   re-run. Do not declare success on "it imported" alone.
3. **Guardrails** — target only the instance from Step 0 marked `"environment":
   "dev"`. If the user explicitly asks to test against production, get explicit
   in-chat confirmation, then pass `--allow-production`. **Do not auto-cleanup** —
   after the test completes, ask the user whether to keep or clean up (item 5).
   **Permission note:** if the API key lacks Playbooks update/delete, the
   workflow itself can't be auto-cleaned (script warns) — delete test workflows
   in the UI, and purge the recycle bin (soft-deleted collections/workflows still
   block re-creation by name/uuid).
4. **No API access?** Skip this step, say so plainly, and hand over with the
   manual import instructions (Step 5) plus the test plan for the user to run
   through in the UI.
5. **Keep vs cleanup (always ask)** — once the test passes (or fails with a
   diagnosis), never silently leave artifacts or silently delete them. Ask the
   user which they want:

   - **Keep** — leave the imported collection + workflow (and test records) in
     place. Common when the user wants to review the playbook in the designer or
     is iterating. Tell them the exact collection name, and warn that FortiSOAR
     appends a random `(xxxxxx)` suffix when a soft-deleted record shares the
     name — purge the recycle bin to get a clean name.
   - **Clean up** — pass `--cleanup` (re-import with `--regen-uuids --cleanup`,
     or delete via the API/UI) to remove test records and the test collection.
     Where the key can't delete, give the user the exact items to remove in the
     UI and remind them to purge the recycle bin.

   If the user doesn't say, default to **ask** — never assume keep and never
   assume cleanup.
6. **On success, remind the user (every time the playbook is kept and working):**
   - Earlier iterations of this playbook are still in the **Recycle Bin**
     (soft-deleted) — they must be purged manually in the GUI (System > Recycle
     Bin). There is no API purge; the API only soft-deletes.
   - Re-importing after a fix re-uses the *same* playbook but may leave the
     collection with a random `(xxxxxx)` suffix unless the recycle bin was purged.
     The active list always holds only the latest, so this is cosmetic — but say
     so explicitly so the user isn't surprised by the changed name.
   - For a **stable name + stable UUID across updates**, use the GUI Import →
     "Replace existing playbook collection" (matches by UUID) rather than
     delete-then-re-import.

### Step 5 — Explain import

Tell the user:
1. In FortiSOAR, go to **Automation > Playbooks**.
2. Click **Import** and select the generated JSON file.
   (If Step 4.5 already passed, say the import is verified and this is only
   needed for their production instance.)
3. If importing a collection, ensure the collection name doesn't conflict with an
   existing one (or check "Replace existing playbook collection").
4. After import, open the playbook in the designer, verify connector configs are
   bound (should already be correct if Step 0 was done), and **Activate** it.
5. **If the import fails with "Some of the Playbooks already exist"**: this error
   is FortiSOAR's catch-all for import validation failures — it does NOT always
   mean a name/UUID conflict. Common causes: (a) invalid `/api/3/picklists/TODO-*`
   IRIs, (b) a typo in a stepType UUID, (c) soft-deleted records in the recycle
   bin. Check all stepType UUIDs against `step-types-quickref.md`, replace any
   placeholder IRIs with real UUIDs or Jinja picklist filters, and purge the
   recycle bin.

## Iterating on an existing playbook (update vs import-as-new)

The #1 trap when fixing a playbook is re-importing it as a brand-new copy.
FortiSOAR's direct-CRUD API cannot update a playbook in place: a deleted
collection/workflow is soft-deleted and keeps reserving **both its name and its
UUID**, so re-importing — especially with `--regen-uuids` — spawns a fresh
duplicate and the collection name gains a random `(xxxxxx)` suffix. The script
now refuses to do this silently (see below); the agent must pick the update path
deliberately.

**First import (or a genuinely separate copy):** normal import — no same-named
workflow exists, so the guard passes.

**Iterate / fix an already-imported playbook — update in place, don't copy:**
1. Keep the JSON's UUIDs stable — do **not** `--regen-uuids` when the goal is to
   update the same playbook. The UUIDs are the playbook's identity; regenerating
   them is exactly what turns "update" into "import a copy".
2. Update via one of:
   - **UI import wizard** — Automation > Playbooks > Import > select the file and
     check **"Replace existing playbook collection"** (matches by UUID). This is
     FortiSOAR's intended iteration path.
   - **Purge + re-import** — delete the stale copy, purge the recycle bin (System >
     Recycle Bin) to free the name+UUID, then re-import the JSON unchanged.
3. If the script stops with "a workflow with the same name already exists", that's
   the duplicate guard working. Do **not** reflexively add `--allow-duplicates` —
   that creates yet another copy. Use an update path above instead.

`--allow-duplicates` is only for when you truly want a second, independent copy of
the playbook (e.g. a variant under active development alongside the original).

**Why there is no clean API-only update:** single-workflow GET/PUT/DELETE return
`403` for the Playbook Administrator key, and even a successful collection DELETE
soft-deletes rather than freeing the name/UUID — there is no API purge for the
recycle bin. So update-in-place necessarily touches the UI once. Track which
collection/workflow UUIDs you deployed (the import log prints them) so a fix can
re-target the same playbook.

## Credential handling (rules)

- Ask for the FortiSOAR host + API key only when Step 0 runs; store them in
  `<workspace>/.fortisoar/config.json` with the user's knowledge.
- Never print the API key in chat or logs, never write it into playbook JSON,
  never commit `.fortisoar/` — remind the user to gitignore it.
- Scripts mark the instance `environment`; treat `"prod"` as import-only with
  explicit per-run user confirmation.

**Permissions the API key needs** (verified against 7.6.1; assign to a dedicated
service user):

**Minimum roles (verified end-to-end): `Playbook Administrator` + `SOC Analyst`.**
Playbook Administrator alone already covers discovery, connector install,
configuration create, import, trigger, and polling; SOC Analyst adds alert
Create/Read/Update for synthetic test data (without it, use `existing_record`
in test plans). Even with both, deletes of workflows, configurations, and test
records return `403` — plan manual UI cleanup for those (collections CAN be
deleted and cascade to their workflows).

Per-area detail:

| Area | Access | Used for |
|---|---|---|
| Connectors | Read | discovery: `/api/integration/connectors/`, `/api/integration/configuration/` |
| Connectors | Install | optional, Step 0 install-then-discover: `POST /api/integration/install-connector/` + `POST /api/3/fetch_repo_content` (repo metadata). Verified end-to-end (real install completed) with **Playbook Administrator as the only role** — no admin role required, and that role also covers the discovery Read needs. Permission probe: POST an empty payload; a `400` validation reply means authorized, a `403` means escalate the role's Connectors access |
| Picklists | Read | discovery + test data picklist IRIs |
| Playbooks / Workflows | Full CRUD + Execute | import (create), trigger, **cleanup** — verified: **Playbook Administrator alone** can list collections/workflows, import (collection + workflow create), trigger execution and poll `log_list`, and delete collections (which cascades to their workflows); but single-workflow GET/PUT/DELETE return `403`, leaving test workflows for manual UI cleanup (+ recycle-bin purge) |
| Connector configurations | Create | Step 0 install-then-discover: `POST /api/integration/configuration/` — verified with Playbook Administrator alone (returns the `config_id` to bind in playbook steps); mark new configs `"default": true`; configuration DELETE returns `403` → manual UI cleanup |
| Test module(s) (Alerts, …) | Create, Read, Update (Delete = `403`) | synthetic test records — verified: Playbook Administrator alone gets `403` on create; **adding SOC Analyst** enables alert Create/Read/Update but **not Delete** (test records need manual cleanup or a higher role). Without any module access, use `existing_record` in the test plan instead of generated records |
| Schedules | Read, Update | only for testing schedule-triggered playbooks |

## Modifying existing playbooks

If the user gives you an existing playbook JSON to edit:
- Read it fully first.
- Preserve all UUIDs you don't need to change.
- Match the existing style (coordinate spacing, naming, group usage).
- Only add/change what the user asked for — surgical edits.
- Re-run Step 4 validation (`fsr_validate.py`) on the whole file, and Step 4.5
  if the change affects connector steps or logic paths.

## Connector knowledge

This skill ships a complete connector operations catalog harvested from the
official `fortinet-fortisoar` GitHub org. **Before generating any connector-call
step, look up the connector in `reference/connector-operations.md`** — it lists
every operation (with title, category, and parameters) for 379 3rd-party connectors
(3339 operations). For full parameter schemas (descriptions, data types, choices,
defaults), read `reference/connector-manifests.json` (the raw harvested manifests).

- The GitHub repo is named `connector-<slug>`; the playbook `connector` field uses
  the manifest `name` (often the same, sometimes with a `-premium`/`-enterprise`
  suffix). When in doubt, match the slug in the catalog.
- Built-in connectors (`cyops_utilities`, `smtp`, `ssh`, `exchange`, `slack`,
  `mysql`, `http`, `code-snippet`, `sentinelone`, `whois-rdap`) ship with the
  platform and are NOT on GitHub. Their operations are partially documented in
  `reference/playbook-json-schema.md` §6; for the rest, ask the user to consult the
  in-instance connector docs (Settings > Connector Configurations, or the connector
  info dialog in the playbook designer).
- If you need a connector NOT in the catalog at all (very new or custom), ask the
  user to export its sample playbook or paste its operation list from the UI.
- The catalog is static; the **instance profile (Step 0) is live truth**. When
  they disagree (e.g. instance runs an older connector version), the profile wins.

## Official playbook analysis

The `OFFICIAL/` folder (in the workspace, not the skill bundle) contains
`Sample.json` (68 collections) and `UseCase.json` (28 collections) — 1367 official
playbooks. A full analysis is in `OFFICIAL/_analysis.md` covering step-type usage,
trigger patterns, real argument shapes, Jinja patterns, routing, groups, macros,
and field surveys. Consult it when you need a real-world example of a pattern.

## Changelog

**v2.7** — Addressed "import as new on every fix": a fix must update the existing
playbook, not spawn a copy. Added a "Iterating on an existing playbook" section
(update via UI "Replace existing playbook collection" or purge recycle bin +
re-import; keep UUIDs stable). `fsr_import_test.py` gains a duplicate guard that
refuses to import when a same-named workflow already exists, with
`--allow-duplicates` as the explicit opt-out; its collection-409 message now
points at recycle-bin purge.

**v2.6** — After a live import test, the agent must explicitly ask the user
whether to keep the imported collection/workflow or clean it up. Removed the
auto-`--cleanup` default; `--cleanup` is now opt-in after the user's choice.
Notes that FortiSOAR suffixes a soft-deleted name collision with a random
`(xxxxxx)`, and that purging the recycle bin restores the clean name.

**v2.4** — Three generation corrections from live-run feedback: (1) connector
configurations created during install-then-discover are marked `"default": true`
(non-default configs can silently not-bind); (2) step names allow only
alphanumerics, spaces, and underscores — `?` and other punctuation are rejected
(renamed the "Compromised?"-style Condition names); (3) `debug` is documented to
default to `true`.

**v2.3** — Connector install verified end-to-end on a live 7.6.x dev instance:
metadata via `POST /api/3/fetch_repo_content` (`connectors/info/<name>_<ver>/info.json`
carries `rpm_name`; the `content-hub/` tree does not), install via
`POST /api/integration/install-connector/` (async; poll
`GET /api/integration/connectors/?name=<name>` until `status: Completed`,
observed ~35 s), PUT for updates. Permission probe: POST empty payload →
`400` = authorized, `403` = not; install rights verified with **Playbook
Administrator as the only role** (real install completed). Same single role also
verified for playbook list + import (collection/workflow create, collection
delete); single-workflow GET/PUT/DELETE return `403`. Same role further
verified: picklists read, workflow trigger + `log_list` polling, and connector
configuration create (returns `config_id`) work; configuration DELETE and
module-record create (alerts) return `403` — use `existing_record` in test
plans. Adding **SOC Analyst** enables alert Create/Read/Update (Delete still
`403`). Minimal verified entitlement for the full workflow incl. synthetic test
data = **Playbook Administrator + SOC Analyst**; only workflow/config/record
deletes remain manual. Permissions table gains Connectors-Install and
Configurations-Create rows.

**v2.2** — Missing-connector handling: agent may offer install-then-discover on
dev with explicit user approval. New
generation rule 9: native step types + Jinja first, built-in utility connectors
second, Code Snippet last resort with mandatory justification.

**v2.1** — All endpoints verified against a live 7.6.1 instance. Discovery now
uses `/api/integration/connectors/` + `/api/integration/configuration/` (with
config health). Import-test rewritten to direct CRUD (`POST /api/3/workflows`
nested) after finding the import-wizard endpoints don't process API calls;
execution via `/api/triggers/1/notrigger/<uuid>`; polling via
`/api/wf/api/workflows/log_list/`. Added `--regen-uuids` (instance references
preserved), soft-delete name-conflict handling, forced `isActive` on test
imports. Step 0 gains Method 2: FortiSOAR MCP servers (`/mcp/*`), with bundled
helper playbook `templates/get-uuid-config.json`. Empirical API-key permission
table.

**v2.0** — Instance discovery (`fsr_discover.py`): connector steps bind to real
installed versions and configuration UUIDs. Clarification gate in Step 1: no
generation until requirements are played back and confirmed. Test plan agreed in
Step 2 (scope, generated test data, success criteria). Static validation automated
(`fsr_validate.py`). Live import-test loop with per-criterion pass/fail
(`fsr_import_test.py`), guarded against production. Credential handling rules.

**v1.0** — Initial: schema/catalog/Jinja references, templates, manual checklist.
