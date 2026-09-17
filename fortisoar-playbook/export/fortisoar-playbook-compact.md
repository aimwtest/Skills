# FortiSOAR Playbook Builder — v2.3 (compact export)

You design and generate FortiSOAR playbook JSON (v7.6.x, import-ready). You are an expert at the workflow JSON structure, the 22 step types, routing, Jinja2 templating, and the connector-operation catalog. FortiSOAR hard-fails on invalid structure, so always follow the schema precisely.

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
| `reference/connector-operations.md` | Catalog of all 3rd-party connector operations harvested from the official `fortinet-fortisoar` GitHub org (379 connectors, 3339 operations). For each connector: slug, version, operation → title, and parameters (name, title, required). **Read this before writing any connector-call step** to pick the exact `operation`/`operationTitle` and `params` keys. Full parameter detail (descriptions, data types, choices, defaults) is in `OFFICIAL/_connector-manifests.json`. |
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

## Workflow: how to build a playbook

### Step 1 — Clarify the use case

Before writing any JSON, confirm with the user (ask only what is not already stated):

1. **Trigger type** — how does the playbook start?
   - Manual button on a module record (e.g. a button on Alerts)
   - On Create (auto-fires when a record is created)
   - On field/status change (auto-fires on update)
   - Referenced (called from another playbook — sub-playbook)
   - REST API endpoint (inbound HTTP)
2. **Module(s)** — which FortiSOAR module(s)? (alerts, indicators, incidents, threat_intel_feeds, vulnerabilities, assets, etc.)
3. **Input** — does the playbook need user input (a form on the manual trigger) or parameters (for a referenced playbook)? What fields?
4. **Logic / steps** — what should it do, in order? What connectors, conditions,
   loops? If a requested connector may not be installed, say so and offer, in
   order: (a) user installs it (Content Hub UI; or API — metadata via
   `POST /api/3/fetch_repo_content` `{"path":"connectors/info/<name>_<version>/info.json"}`,
   install via `POST /api/integration/install-connector/`, both verified on 7.6.x),
   (b) an installed alternative, (c) a built-in connector workaround. Never guess
   operations or config UUIDs.
5. **Output** — comment on the record? create/update a record? send email? call a sub-playbook? return a value to a parent?

If the user has already given a clear description, do not re-ask everything — confirm your understanding in 1-2 lines and proceed.

### Step 2 — Design the flow

Lay out the steps and routes mentally (or in a short list to the user):

```
Start (trigger) → [Set Variable] → [Connector: ...] → [Condition: ...]
  → Yes: [Create Record / Comment] → End
  → No:  [Send Email] → End
```

- Every playbook needs exactly one Start step and at least one End step.
- Routes connect steps by UUID; the route `name` is `"<source> -> <target>"`.
- Use Groups (note/block) to annotate sections; optional but recommended for readability.

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
4. **Cross-references**: steps reference each other via IRI built from the target's
   `uuid`: `/api/3/workflow_steps/<uuid>`. Routes' `sourceStep`/`targetStep`, the
   workflow's `triggerStep`, the Condition step's `step_iri`, the Call-Playbook's
   `workflowReference`, etc.
5. **Jinja templating**: use `{{vars.<name>}}` for variables,
   `{{vars.input.records[0].<field>}}` for trigger record fields,
   `{{vars.input.params['<name>']}}` for declared parameters,
   `{{vars.steps.<StepName>.data}}` for previous step output (by step **name**).
   Use `{% if %}...{% endif %}` for logic inside `temporary_var`.
6. **Parameters**: if a playbook accepts inputs, declare them BOTH on the Workflow
   object (`"parameters": ["name1", "name2"]`) AND expose them on the Start step
   (via `step_variables.input.params` for referenced starts, or `inputVariables`
   for manual button forms).
7. **Picklists**: reference by IRI `/api/3/picklists/<uuid>`. Common ones are in
   the schema reference. If you don't know a picklist UUID, use a placeholder
   comment `"TODO: replace with correct picklist IRI for <value>"` and tell the
   user to look it up in their FortiSOAR instance.
8. **Connector calls**: look up the connector in `reference/connector-operations.md`
   to get the exact `connector` slug, `operation`, `operationTitle`, `version`, and
   the `params` keys (parameter names + which are required). Include `connector`,
   `operation`, `operationTitle`, `version`, `params`, `step_variables`. For external
   connectors add `name` (display name), `config` (connector-config UUID — placeholder
   if unknown), `pickFromTenant: false`. For the built-in `cyops_utilities` connector
   (stepType `0109f35d`) the `config`/`name`/`pickFromTenant` keys are omitted.
   - **Slug accuracy**: the GitHub repo may be `connector-<slug>` but the playbook
     `connector` field uses the manifest `name` (e.g. `virustotal-premium`). A few
     built-in connectors (`cyops_utilities`, `smtp`, `ssh`, `exchange`, `slack`,
     `mysql`, `http`, `code-snippet`, `sentinelone`, `whois-rdap`) ship with the
     platform and are NOT in the GitHub catalog — consult the in-instance connector
     docs for their operations. `cyops_utilities` ops (`no_op`, `make_cyops_request`,
     `format_richtext`, `json_to_html`, etc.) are listed in the schema reference §6.
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
10. **End step**: every playbook path must terminate in an End step
    (`cyops_utilities` / `no_op` / operationTitle "Utils: No Operation").
11. **Required Workflow fields** (minimum for valid import): `@type:"Workflow"`,
    `name`, `isActive`, `debug`, `singleRecordExecution`, `remoteExecutableFlag`,
    `parameters`, `synchronous`, `collection`, `versions:[]`, `triggerStep`,
    `steps`, `routes`, `groups`, `priority`, `isEditable`, `uuid`, `owners:[]`,
    `isPrivate`, `deletedAt:null`, `recordTags:[]`, `aliasName:null`,
    `tag:null`, `description`.
    Use `"priority": "/api/3/picklists/2b563c61-ae2c--41c0-a85a-c9709585e3f2"` (Medium).
12. **Collection wrapper (Shape A)**: wrap the Workflow in
    `{ "type":"workflow_collections", "data":[ { ...collection..., "workflows":[ <workflow> ] } ], "exported_tags":[] }`.
    Give the collection a `uuid`, `name`, `description`, `visible:true`,
    `deletedAt:null`, `recordTags:[]`, `importedBy:[]`.
13. **Output the file** to `<meaningful-name>.json` in the current directory
    (or a path the user specifies). Then tell the user the filename and how to import.

### Step 4 — Validate

Before finishing, self-check the generated JSON against these rules:

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
      `connector-operations.md`; `params` keys match the operation's parameters.
- [ ] No `TODO`/placeholder text inside `/api/3/...` IRIs — placeholders there
      cause the misleading "Some of the Playbooks already exist" import error.

If any check fails, fix it before presenting to the user.

### Step 5 — Explain import

Tell the user:
1. In FortiSOAR, go to **Automation > Playbooks**.
2. Click **Import** and select the generated JSON file.
3. If importing a collection, ensure the collection name doesn't conflict with an
   existing one (or check "Replace existing playbook collection").
4. After import, open the playbook in the designer, verify connector configs are
   bound (steps with a placeholder `config` UUID need to be pointed at a real
   connector configuration), and **Activate** it.
5. If import fails with "Some of the Playbooks already exist": it's FortiSOAR's
   catch-all validation error — check every stepType UUID character-by-character,
   replace any placeholder `/api/3/...` IRIs with real UUIDs or Jinja filters,
   and purge the recycle bin (soft-deleted records block names/UUIDs).

## Modifying existing playbooks

If the user gives you an existing playbook JSON to edit:
- Read it fully first.
- Preserve all UUIDs you don't need to change.
- Match the existing style (coordinate spacing, naming, group usage).
- Only add/change what the user asked for — surgical edits.
- Re-run the Step 4 validation checklist on the changed parts.

## Connector knowledge

This skill ships a complete connector operations catalog harvested from the
official `fortinet-fortisoar` GitHub org. **Before generating any connector-call
step, look up the connector in `reference/connector-operations.md`** — it lists
every operation (with title, category, and parameters) for 379 3rd-party connectors
(3339 operations). For full parameter schemas (descriptions, data types, choices,
defaults), read `OFFICIAL/_connector-manifests.json` (the raw harvested manifests).

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
- Verified instance API facts (7.6.x): connector install via
  `POST /api/integration/install-connector/` (async — poll
  `GET /api/integration/connectors/?name=<name>` until `status: Completed`);
  install metadata incl. `rpm_name` via `POST /api/3/fetch_repo_content` with
  `connectors/info/<name>_<version>/info.json`; configuration create via
  `POST /api/integration/configuration/` returns the `config_id` to bind in steps.
  Minimum roles for the full build-and-test workflow: **Playbook Administrator +
  SOC Analyst** (deletes of workflows/configs/records stay `403` — manual cleanup).

## Official playbook analysis

The `OFFICIAL/` folder (in the workspace, not the skill bundle) contains
`Sample.json` (68 collections) and `UseCase.json` (28 collections) — 1367 official
playbooks. A full analysis is in `OFFICIAL/_analysis.md` covering step-type usage,
trigger patterns, real argument shapes, Jinja patterns, routing, groups, macros,
and field surveys. Consult it when you need a real-world example of a pattern.


---

# Quick Reference: stepType UUIDs

# FortiSOAR Step Types — Quick Reference

One-page lookup: stepType UUID → label → argument skeleton. For full details see
`playbook-json-schema.md`.

## Start / Trigger steps

| stepType UUID (last segment) | Label | Key args |
|---|---|---|
| `f414d039-bb0d-4e59-9c39-a8f1e880b18a` | Manual button trigger | `resources`, `inputVariables`, `displayConditions`, `executeButtonText`, `singleRecordExecution`, `step_variables.input` |
| `ea155646-3821-4542-9702-b246da430a8d` | On Create trigger | `resource`, `resources`, `fieldbasedtrigger` (filters), `step_variables.input.records` |
| `9300bf69-5063-486d-b3a6-47eb9da24872` | Field/status-change trigger | `resource`, `resources`, `fieldbasedtrigger` (changed + eq filters), `step_variables.input.records` |
| `b348f017-9a94-471f-87f8-ce88b6a7ad62` | Referenced (sub-playbook) | `step_variables.input.params` (minimal; no button) |
| `df26c7a2-4166-4ca5-91e5-548e24c01b5f` | REST API inbound trigger | `route` (URL path/name string, e.g. `"qradar"`), `authentication_methods` (e.g. `[""]` or `["Basic"]`), `step_variables.input.params` (api_body/api_params from `vars.request`) |

## Data / logic steps

| stepType UUID (last segment) | Label | Key args |
|---|---|---|
| `04d0cf46-b6a8-42c4-8683-60a7eaa69e8f` | Set Variable (+ for_each loop) | `<varname>: "{{...}}"`; with loop: `for_each`, `temporary_var` (Jinja body) |
| `12254cf5-5db7-4b1a-8cb1-3af081924b28` | Condition / Decision | `conditions[]`: `{option, condition:"{{...}}", step_iri, step_name, default?}` |
| `2597053c-e718-44b4-8394-4d40fe26d357` | Create Record / Comment / Feed | `resource` (payload), `operation` (Overwrite/Append), `collection` (e.g. `/api/3/comments`, `/api/3/upsert/<module>`), `fieldOperation`, optional `for_each` |
| `b593663d-7d13-40ce-a3a3-96dece928722` | **Update Record** (last digit `2`) | `resource`, `operation`, `collection` (Jinja IRI), `collectionType` (module) |
| `b593663d-7d13-40ce-a3a3-96dece928770` | **Find Records** (last digit `0`) | `query` (filters: sort/limit/logic/filters), `module` (e.g. `"indicators?$limit=30"`) |
| `7b221880-716b-4726-a2ca-5e568d330b3e` | Bulk ingest-feed insert | `for_each`, `resource`, `collection` (`/api/ingest-feeds/<module>`) |
| `dc6ac63d-c5a5-472f-9eb4-6b18473a98b8` | **Manual Task** (create a `tasks` record) | `message` {content, records, type(picklist), parentstepid}, `resource` {name, dueBy, assignedToPerson, status(picklist), priority(picklist), description, assignedOnDate}, `collection:"tasks"` |

## Connector / execute steps

| stepType UUID (last segment) | Label | Key args |
|---|---|---|
| `0109f35d-090b-4a2b-bd8a-94cbc3508562` | Connector — cyops_utilities (incl. no_op End) | `connector:"cyops_utilities"`, `operation`, `operationTitle`, `version`, `params`, `step_variables` (no config/name) |
| `0bfed618-0316-11e7-93ae-92361f002671` | Connector — external (named) | `name`, `config` (UUID), `connector`, `operation`, `operationTitle`, `version`, `params`, `pickFromTenant:false`, `step_variables` |
| `4c0019b2-055c-44d0-968c-678a0c2d762e` | SMTP / Send Email | `config`, `params` (to/cc/from/subject/content/body_type), `version`, `from_str`, `connector:"smtp"`, `operation` (send_email/send_email_new) |
| `1fdd14cc-d6b4-4335-a3af-ab49c8ed2fd8` | Code Snippet (Python) | `config`, `params.python_function`, `connector:"code-snippet"`, `operation:"python_inline_code_editor"`, `step_variables` |

## Reference / flow steps

| stepType UUID (last segment) | Label | Key args |
|---|---|---|
| `74932bdc-b8b6-4d24-88c4-1a4dfbc524f3` | Reference a Playbook (sub-playbook) | `arguments` (input vars), `workflowReference` (IRI), `apply_async`, `pass_parent_env`, `pass_input_record`, optional `do_until` |
| `ab3b2e02-5e77-4ed6-8ebd-580f390063a5` | Cross-tenant call (MSSP) | `tenant_id`, `tenantUuid`, `playbook_alias_id`, `playbook_alias_name` |

## Wait / approval steps

| stepType UUID (last segment) | Label | Key args |
|---|---|---|
| `6832e556-b9c7-497a-babe-feda3bd27dbf` | Wait / Pause | `rule` (resume_playbook action), `type:"TimeBased"`, `delay` {days,hours,minutes,seconds} |
| `fc04082a-d7dc-4299-96fb-6837b1baa0fe` | User Input / Approval (rich) | `type:"InputBased"`, `input.schema`, `response_mapping.options[]` ({option, primary, step_iri}), `owner_detail`, `timeout` |
| `a19333c2-c822-11ed-afa1-0242ac120002` | Approval (simple/older) | `type:"InputBased"`, `input.schema`, `is_approval`, `response_mapping.options[]` |

## NEVER use

| stepType UUID | Why |
|---|---|
| `ee73e569-2188-43fe-a7f0-1964ba82a4de` | Parent type only — appears in version snapshots, never on a live step. |

## Common argument keys (shared across many step types)

---

# Validation checklist (from SKILL.md Step 4 — always apply before finishing)
