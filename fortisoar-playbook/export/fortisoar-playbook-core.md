# FortiSOAR Playbook Builder — Core Skill (v2.3)

Combined export for Claude (Code CLAUDE.md / Claude.ai Projects) and Grok (system prompt / custom instructions). This file is the self-contained skill body; the large connector-operations catalog ships separately as a knowledge upload.

---

## 0. Skill manifest (from SKILL.md)

---
name: fortisoar-playbook
description: Design, generate, and self-test FortiSOAR playbooks (workflow JSON). Use when the user mentions FortiSOAR, playbook, SOAR workflow, playbook collection, connector operations, playbook JSON import/export, or wants to automate a security process in FortiSOAR. Covers trigger setup, step types, routing, Jinja templating, instance connector discovery, static validation, live import-testing, and producing import-ready JSON.
---

# FortiSOAR Playbook Builder — v2.3

This skill helps design and generate FortiSOAR playbook JSON that can be imported
into FortiSOAR 7.6.x. It is self-contained: all reference material is bundled in
`reference/` and `templates/` relative to this file.

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

## A. Reference: playbook-json-schema.md

# FortiSOAR Playbook JSON Export — Structure Reference

Survey of ~95 JSON files (383 Workflow objects, 21 distinct stepType UUIDs). This
is the authoritative schema for generating import-ready playbook JSON.

---

## 1. Top-Level Structures (3 export shapes)

### Shape A — Collection export (most common; recommended for generation)

```json
{
  "type": "workflow_collections",
  "data": [
    {
      "@context": "/api/3/contexts/WorkflowCollection",
      "@type": "WorkflowCollection",
      "name": "My Collection",
      "description": null,
      "visible": true,
      "image": null,
      "uuid": "<collection-uuid>",
      "deletedAt": null,
      "importedBy": [],
      "recordTags": [],
      "workflows": [ {Workflow}, ... ]
    }
  ],
  "exported_tags": []
}
```

### Shape B — Single playbook (bare Workflow object)

```json
{
  "@type": "Workflow",
  "name": "...",
  ...
  "steps": [...], "routes": [...], "groups": [...]
}
```

### Shape C — Collection metadata only (`collection.metadata.json`)

A WorkflowCollection record **without** `workflows`. Used as a side-car when a
folder holds many single-playbook files. Skip this shape when generating unless
the user specifically wants a folder-of-playbooks layout.

---

## 2. Workflow Object Fields

| Field | Meaning |
|---|---|
| `@type` | Always `"Workflow"`. |
| `name` | Display name (unique within collection). |
| `aliasName` | Alternate alias; usually `null`. |
| `tag` | Category hashtag (e.g. `"#Subroutine"`); usually `null`. |
| `description` | Free-text; often `null`. |
| `triggerLimit` | Rate-limit; `null` (server-configured). |
| `isActive` | Boolean — enabled. |
| `debug` | Boolean — debug logging. |
| `singleRecordExecution` | Boolean — run once per input record vs batch. **In 1367 real exports this is `false` 100% of the time**; set `false`. |
| `remoteExecutableFlag` | Boolean — invokable remotely (MSSP). **`false` in 100% of real exports**; set `false`. |
| `parameters` | Array of **string** parameter names (playbook input contract). |
| `synchronous` | Boolean — block caller (sync) vs async. **`false` in 100% of real exports**; set `false`. |
| `collection` | IRI of owning collection `/api/3/workflow_collections/<uuid>`. |
| `versions` | Array of `WorkflowVersion` snapshots; **always `[]` on generation** — the server creates version 1 on import. Never replay snapshots. |
| `triggerStep` | IRI of the Start step `/api/3/workflow_steps/<uuid>`. |
| `steps` | Array of `WorkflowStep`. |
| `routes` | Array of `WorkflowRoute`. |
| `groups` | Array of `WorkflowGroup`. |
| `priority` | Picklist IRI — priority. `2b563c61-...` = Medium. **Often `null`** in real exports (null in ~60%, Medium in ~40%); both import cleanly. |
| `playbookOrigin` | Picklist IRI — origin. `15c1e8c9-22bf-4e66-8fbb-0a502d4a4a3f` = "Custom" (most common); `b6d710a9-a8ec-41ec-8817-fe9fa062fcdd` = alternate origin. **Always present** in real exports. |
| `isEditable` | Boolean. Optional. |
| `uuid` | Workflow UUID (builds `/api/3/workflows/<uuid>`). |
| `id` | Numeric DB id. Optional on newer exports. |
| `owners` | Array of owner IRIs; usually `[]`. |
| `isPrivate` | Boolean. |
| `deletedAt` | Soft-delete ts; `null`. |
| `lastModifyDate` | Unix epoch seconds. Optional. |
| `importedBy` | Array; `[]`. |
| `recordTags` | Array of tag strings. |

---

## 3. Step Types (22 distinct stepType UUIDs)

Every `WorkflowStep` has this base shape:

```json
{
  "@type": "WorkflowStep",
  "name": "...",
  "description": null,
  "arguments": { ... },       // shape depends on stepType
  "status": null,
  "top": "40",                // visual Y (STRING, pixels)
  "left": "40",                // visual X (STRING, pixels)
  "stepType": "/api/3/workflow_step_types/<uuid>",
  "group": null,              // IRI of WorkflowGroup, or null
  "uuid": "<step uuid>"
}
```

### Quick UUID → label table (full details below)

| stepType UUID | Label | Count |
|---|---|---|
| `f414d039-bb0d-4e59-9c39-a8f1e880b18a` | Start — manual button / source trigger | 74 |
| `ea155646-3821-4542-9702-b246da430a8d` | Start — On Create trigger | 39 |
| `9300bf69-5063-486d-b3a6-47eb9da24872` | Start — field/status-change trigger | 7 |
| `b348f017-9a94-471f-87f8-ce88b6a7ad62` | Start — Referenced (called by another playbook) | 63 |
| `df26c7a2-4166-4ca5-91e5-548e24c01b5f` | Start — REST API inbound trigger | 3 |
| `04d0cf46-b6a8-42c4-8683-60a7eaa69e8f` | Set Variable (+ for_each loop body) | 427 |
| `0109f35d-090b-4a2b-bd8a-94cbc3508562` | Connector call — cyops_utilities (incl. no_op End) | 166 |
| `0bfed618-0316-11e7-93ae-92361f002671` | Connector call — named external connector | 195 |
| `4c0019b2-055c-44d0-968c-678a0c2d762e` | Send Email (SMTP connector) | 7 |
| `1fdd14cc-d6b4-4335-a3af-ab49c8ed2fd8` | Code Snippet (inline Python) | 70 |
| `74932bdc-b8b6-4d24-88c4-1a4dfbc524f3` | Reference a Playbook (call sub-playbook) | 83 |
| `ab3b2e02-5e77-4ed6-8ebd-580f390063a5` | Cross-tenant playbook call (MSSP) | 2 |
| `12254cf5-5db7-4b1a-8cb1-3af081924b28` | Condition (If / Decision / Branch) | 91 |
| `2597053c-e718-44b4-8394-4d40fe26d357` | Create Record (incl. add Comment, create Feed) | 105 |
| `7b221880-716b-4726-a2ca-5e568d330b3e` | Bulk ingest-feed insert | 6 |
| `b593663d-7d13-40ce-a3a3-96dece928722` | Update Record | 68 |
| `b593663d-7d13-40ce-a3a3-96dece928770` | Find Records (query) — note last digit `770` | 53 |
| `6832e556-b9c7-497a-babe-feda3bd27dbf` | Wait / Pause (time-based resume) | 17 |
| `fc04082a-d7dc-4299-96fb-6837b1baa0fe` | Awaiting Playbook — user input/approval (rich) | 8 |
| `a19333c2-c822-11ed-afa1-0242ac120002` | Awaiting Playbook — approval (simple/older) | 3 |
| `dc6ac63d-c5a5-472f-9eb4-6b18473a98b8` | Manual Task (create a `tasks` module record) | 47 |
| `ee73e569-2188-43fe-a7f0-1964ba82a4de` | **Parent type only — NEVER use on a step** | — |

---

### 3.1 `f414d039` — Start (Manual / Button trigger)

Fires when a user clicks an "Execute" button on a module record (e.g. on Alerts).

```json
{
  "name": "Start",
  "arguments": {
    "route": "<first-route-uuid>",
    "resources": ["alerts"],
    "__triggerLimit": true,
    "inputVariables": [],
    "step_variables": { "input": { "params": [], "records": "{{vars.input.records}}" } },
    "triggerOnSource": true,
    "displayConditions": { "alerts": { "sort": [], "limit": 30, "logic": "AND", "filters": [] } },
    "executeButtonText": "Execute",
    "noRecordExecution": false,
    "showToasterMessage": { "visible": false, "messageVisible": true },
    "triggerOnReplicate": false,
    "singleRecordExecution": true
  },
  "stepType": "/api/3/workflow_step_types/f414d039-bb0d-4e59-9c39-a8f1e880b18a"
}
```

- `resources`: array of module names the button appears on (`["alerts"]`, `["threat_intel_feeds"]`).
- `displayConditions`: per-resource filter for which records show the button.
- `inputVariables`: schema for an input form (see §8.2).
- `singleRecordExecution`: true = one playbook run per selected record.

### 3.2 `ea155646` — Start (On Create trigger)

Auto-fires after a record is created.

```json
{
  "name": "Start",
  "arguments": {
    "resource": "indicators",
    "resources": ["indicators"],
    "__triggerLimit": true,
    "step_variables": { "input": { "params": [], "records": ["{{vars.input.records[0]}}"] } },
    "triggerOnSource": true,
    "fieldbasedtrigger": {
      "sort": [], "limit": 30, "logic": "AND",
      "filters": [
        { "type":"object", "field":"typeofindicator",
          "value":"/api/3/picklists/c0beeda4-2c7a-4214-b7e5-53ba1649539c",
          "_value": { "@id":".../c0beeda4-...", "display":"IP Address", "itemValue":"IP Address" },
          "operator":"eq" }
      ]
    },
    "triggerOnReplicate": false
  },
  "stepType": "/api/3/workflow_step_types/ea155646-3821-4542-9702-b246da430a8d"
}
```

- `fieldbasedtrigger`: filter object; empty `filters` = triggers on any create.

### 3.3 `9300bf69` — Start (field/status-change trigger)

Fires when a record's field changes to a specific value.

```json
{
  "name": "Start",
  "arguments": {
    "resource": "netshot_output_reports",
    "resources": ["netshot_output_reports"],
    "__triggerLimit": true,
    "step_variables": { "input": { "params": [], "records": ["{{vars.input.records[0]}}"] } },
    "triggerOnSource": true,
    "fieldbasedtrigger": {
      "sort": [], "limit": 30, "logic": "AND",
      "filters": [
        { "type":"object", "field":"status", "value":"", "operator":"changed" },
        { "type":"object", "field":"status",
          "value":"/api/3/picklists/2f63f907-d342-4ad6-9a77-68c654bba2d2",
          "_value": { "@id":".../2f63f907-...", "display":"Pending", "itemValue":"Pending" },
          "operator":"eq" }
      ]
    },
    "triggerOnReplicate": false
  },
  "stepType": "/api/3/workflow_step_types/9300bf69-5063-486d-b3a6-47eb9da24872"
}
```

### 3.4 `b348f017` — Start (Referenced — called from another playbook)

No own trigger; invoked by a "Reference a Playbook" step. Parameters come via `step_variables.input.params`.

```json
{
  "name": "Start",
  "arguments": {
    "__triggerLimit": true,
    "step_variables": { "input": { "params": [] } },
    "triggerOnSource": true,
    "triggerOnReplicate": false
  },
  "stepType": "/api/3/workflow_step_types/b348f017-9a94-471f-87f8-ce88b6a7ad62"
}
```

### 3.5 `df26c7a2` — Start (REST API inbound trigger)

Playbook exposed as a REST endpoint. `route` is a **plain string name/path** (e.g. `"qradar"`, `"deferred/apt_test"`), NOT a UUID or IRI. `authentication_methods` is an array of strings; `[""]` (none) and `["Basic"]` are both observed.

```json
{
  "name": "Start",
  "arguments": {
    "route": "qradar",
    "__triggerLimit": true,
    "step_variables": {
      "input": {
        "params": {
          "api_body": "{{vars.request.data}}",
          "api_params": "{{vars.request.params}}"
        }
      }
    },
    "triggerOnSource": true,
    "triggerOnReplicate": false,
    "authentication_methods": [""]
  },
  "stepType": "/api/3/workflow_step_types/df26c7a2-4166-4ca5-91e5-548e24c01b5f"
}
```

In the playbook body, read the request via `{{vars.request.data}}`, `{{vars.request.params}}`, `{{vars.request.headers.<name>}}`, `{{vars.request.record}}` (if a record IRI was passed).

### 3.6 `04d0cf46` — Set Variable (most common step; also for_each loop body)

Set one or more named variables. Each key in `arguments` is a variable name → Jinja value.
With `for_each`, the step loops over a list (body field is `temporary_var`).

```json
// plain set
{
  "name": "setup env",
  "arguments": { "netshot_target_output_id": "{{vars.input.records[0].id}}" },
  "stepType": "/api/3/workflow_step_types/04d0cf46-b6a8-42c4-8683-60a7eaa69e8f"
}

// set from input params
{ "name": "What is the user",
  "arguments": { "admin_user": "{{vars.input.params['my_user_original']}}" } }

// for_each loop body using temporary_var + Jinja
{ "name": "Iterate into the FGT Array",
  "arguments": {
    "for_each": { "item": "{{vars.fortigate_output.0.output}}", "parallel": false, "condition": "" },
    "temporary_var": "{% if 'edit' in vars.item %}\n    {{vars.array_users.append( vars.item | regex_search('\"(.+?)\"') | replace('\"','') )}}\n{% endif %}"
  } }
```

- `for_each`: `{ "item": "{{vars.some_list}}", "parallel": false, "condition": "{{...}}", "__bulk": true, "batch_size": 100 }`.
- `step_variables`, `when`, `ignore_errors` also allowed.

### 3.7 `0109f35d` — Connector call (cyops_utilities / system connector)

For the built-in `cyops_utilities` connector. No `config`/`name`/`pickFromTenant` keys.
Common ops: `no_op` (End), `create_file_from_string`, `make_cyops_request` (REST),
`query_cyops_resource`, `json_to_html`, `ip_cidr_check`, `reverse_dns_lookup`, etc.

```json
// End / No-op step
{
  "name": "End",
  "arguments": {
    "params": [],
    "version": "3.5.0",
    "connector": "cyops_utilities",
    "operation": "no_op",
    "operationTitle": "Utils: No Operation",
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/0109f35d-090b-4a2b-bd8a-94cbc3508562"
}

// REST call via FortiSOAR API
{ "name": "Make REST Call",
  "arguments": {
    "params": { "iri":"/api/wf/api/jinja-editor/?format=json", "body":"{{vars.post_data}}", "method":"POST" },
    "version": "3.2.3", "connector": "cyops_utilities",
    "operation": "make_cyops_request", "operationTitle": "FSR: Make FortiSOAR API Call",
    "step_variables": []
  } }
```

### 3.8 `0bfed618` — Connector call (general / named external connector)

For 3rd-party connectors (fortigate-firewall, ssh, exchange, sentinelone, etc.).
Includes `name`, `config`, `pickFromTenant`.

```json
{
  "name": "Call FGT Command",
  "arguments": {
    "name": "Fortinet FortiGate",
    "config": "c39ff169-25f7-4309-9e3e-434faec7ce91",
    "params": {
      "port": 22, "timeout": 10,
      "cmd_list": "{{vars.my_command2}}",
      "password": "F0rtinet#123", "username": "admin",
      "interactive": false, "private_key": ""
    },
    "version": "5.4.0", "connector": "fortigate-firewall",
    "operation": "execute_command", "operationTitle": "Execute Command",
    "pickFromTenant": false, "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/0bfed618-0316-11e7-93ae-92361f002671"
}
```

### 3.9 `4c0019b2` — SMTP / Send Email connector step

Specialized for `smtp` connector. Ops: `send_email`, `send_email_new` (advanced).

```json
{
  "name": "Send Action Report",
  "arguments": {
    "config": "<smtp-config-uuid>",
    "params": {
      "cc":"", "to":"soc@test.local", "bcc":"", "from":"",
      "type":"Manual Input", "content":"<p>Report Template</p>",
      "subject":"Report", "iri_list":"",
      "body_type":"Rich Text", "file_name":"", "file_path":""
    },
    "version": "2.6.0", "from_str": "admin@example.com",
    "connector": "smtp", "operation": "send_email_new",
    "ignore_errors": true, "operationTitle": "Send Email (Advanced)",
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/4c0019b2-055c-44d0-968c-678a0c2d762e"
}
```

### 3.10 `1fdd14cc` — Code Snippet (inline Python)

Runs Python via the `code-snippet` connector, op `python_inline_code_editor`.

```json
{
  "name": "Strip_HTML",
  "arguments": {
    "config": "<code-snippet-config-uuid>",
    "params": {
      "python_function": "html_text = \"{{vars.email_result}}\"\ndef remove_html_tags(input):\n    import bs4\n    soup = bs4.BeautifulSoup(input, 'html.parser')\n    return soup.get_text()\nprint(remove_html_tags(html_text).strip())"
    },
    "version": "2.1.0", "connector": "code-snippet",
    "operation": "python_inline_code_editor", "operationTitle": "Execute Python Code",
    "step_variables": { "python_result": "{{vars.steps.Strip_HTML}}" }
  },
  "stepType": "/api/3/workflow_step_types/1fdd14cc-d6b4-4335-a3af-ab49c8ed2fd8"
}
```

### 3.11 `74932bdc` — Reference a Playbook (call sub-playbook)

Calls another playbook. `workflowReference` = IRI of target playbook.

```json
{
  "name": "get_fmg_devices",
  "arguments": {
    "arguments": { "connector_config": "{{vars.input.params['connector_config']}}" },
    "apply_async": false,
    "step_variables": [],
    "pass_parent_env": false,
    "pass_input_record": false,
    "workflowReference": "/api/3/workflows/<target-workflow-uuid>"
  },
  "stepType": "/api/3/workflow_step_types/74932bdc-b8b6-4d24-88c4-1a4dfbc524f3"
}
```

- `do_until`: retry/poll loop — the sub-playbook is re-invoked until `condition` evaluates true or `retries` is exhausted. Real example:
  ```json
  "do_until": { "delay": 5, "retries": 5, "condition": "{{vars.steps.Validate_Slack_Input_Form.validation == 1}}" }
  ```

### 3.12 `ab3b2e02` — Cross-tenant playbook call (MSSP)

Calls a playbook on a different tenant.

```json
{
  "name": "Test_Tenant_playbook_01",
  "arguments": {
    "tenant_id": "<tenant-id>",
    "tenantUuid": "/api/3/tenants/<tenant-uuid>",
    "step_variables": [],
    "playbook_alias_id": "<alias-uuid>",
    "playbook_alias_name": "0001-Playbook"
  },
  "stepType": "/api/3/workflow_step_types/ab3b2e02-5e77-4ed6-8ebd-580f390063a5"
}
```

### 3.13 `12254cf5` — Condition (If / Decision / Branch)

Each branch references a target step by IRI and carries a Jinja `condition`; one branch can be `"default": true`.

```json
{
  "name": "check_upgrade_package",
  "arguments": {
    "conditions": [
      { "option": "Yes",
        "step_iri": "/api/3/workflow_steps/<yes-step-uuid>",
        "condition": "{{ vars.fortigate_upgrade_version_index < vars.fortigate_upgrade_path_length }}",
        "step_name": "back_config" },
      { "option": "No", "default": true,
        "step_iri": "/api/3/workflow_steps/<no-step-uuid>",
        "step_name": "send_mail" }
    ],
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/12254cf5-5db7-4b1a-8cb1-3af081924b28"
}
```

### 3.14 `2597053c` — Create Record (incl. Comments, Feeds)

Create/upsert a record. Also used to add a comment (`collection: /api/3/comments`).

```json
// Add a comment to an alert
{
  "name": "Add Comment to the Alert",
  "arguments": {
    "resource": {
      "type": "/api/3/picklists/ff599189-3eeb-4c86-acb0-a7915e85ac3b",
      "alerts": "{{vars.input.params['alert_original']}}",
      "people": [],
      "content": "<p>Applied to user {{vars.admin_user}}</p>",
      "__replace": "", "isImportant": true, "peopleUpdated": false
    },
    "operation": "Overwrite",
    "collection": "/api/3/comments",
    "__recommend": [],
    "fieldOperation": { "recordTags": "Overwrite" },
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/2597053c-e718-44b4-8394-4d40fe26d357"
}

// Create a threat-intel feed (for_each bulk)
{
  "name": "Create Domain Feed",
  "arguments": {
    "for_each": { "item": "{{vars.ti_result_domain}}", "__bulk": true, "parallel": false, "condition": "", "batch_size": 100 },
    "resource": {
      "value": "{{vars.item}}",
      "source": "ThreatIntelXY", "__replace": "true",
      "confidence": 50,
      "reputation": "/api/3/picklists/50bfd06c-9aff-4f7d-b6d9-821339e31fe7",
      "typeOfFeed": "/api/3/picklists/18c5c903-eda5-494d-aa7e-f28b479681ac"
    },
    "operation": "Overwrite",
    "collection": "/api/3/upsert/threat_intel_feeds",
    "__recommend": [],
    "fieldOperation": { "recordTags": "Append" },
    "step_variables": []
  }
}
```

### 3.15 `7b221880` — Bulk ingest-feed insert

High-volume record generation via ingest feeds.

```json
{
  "name": "INSERT Alert",
  "arguments": {
    "for_each": { "item": "{{vars.records_list}}", "__bulk": true, "parallel": false, "condition": "", "batch_size": 500 },
    "resource": {
      "name": "Alert 1",
      "type": "{{\"AlertType\" | picklist('Phishing', '@id')}}",
      "severity": "{{\"Severity\" | picklist('High', '@id')}}",
      "alertDetectionDate": "{{vars.item}}"
    },
    "_showJson": false,
    "collection": "/api/ingest-feeds/alerts",
    "__recommend": [],
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/7b221880-716b-4726-a2ca-5e568d330b3e"
}
```

### 3.16 `b593663d-...-722` — Update Record (last digit `2`)

Updates an existing record by IRI. `collection` is a Jinja IRI; `collectionType` declares the module.

```json
{
  "name": "Tag Feed with Block IP",
  "arguments": {
    "resource": { "__link": { "recordTags": ["/api/3/tags/EntraIDBlock"] } },
    "operation": "Append",
    "collection": "{{vars.input.records[0]['@id']}}",
    "__recommend": [],
    "collectionType": "/api/3/threat_intel_feeds",
    "fieldOperation": { "recordTags": "Append" },
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/b593663d-7d13-40ce-a3a3-96dece928722"
}
```

### 3.17 `b593663d-...-770` — Find Records (last digit `0`)

Queries the FortiSOAR DB for records matching filters.

```json
{
  "name": "Find Related Malicious Info",
  "arguments": {
    "query": {
      "sort": [], "limit": 30, "logic": "AND",
      "filters": [
        { "type": "primitive", "field": "alerts.id", "value": "{{vars.input.records[0].id}}", "operator": "eq" }
      ]
    },
    "module": "indicators?$limit=30",
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/b593663d-7d13-40ce-a3a3-96dece928770"
}
```

- Filter shape: `{ "type":"primitive"|"array"|"datetime"|"object", "field":"...", "value":"..."|[...], "operator":"eq"|"in"|"lt"|"neq"|"changed" }`.

### 3.18 `6832e556` — Wait / Pause

Pauses the playbook for a delay then resumes.

```json
{
  "name": "wait for upgrade",
  "arguments": {
    "rule": { "actions": [{"type":"resume_playbook","enabled":true,"channel_uuid":"e2ce87c2-c55a-11ec-9d64-0242ac120002"}], "is_active": true, "event_source": "crudhub" },
    "type": "TimeBased",
    "delay": { "days": 0, "hours": 0, "minutes": 5, "seconds": 0 }
  },
  "stepType": "/api/3/workflow_step_types/6832e556-b9c7-497a-babe-feda3bd27dbf"
}
```

### 3.19 `fc04082a` — Awaiting Playbook / User Input (rich)

Pauses and asks a user for input/approval; resumes on chosen option.

```json
{
  "name": "UserApprove",
  "arguments": {
    "type": "InputBased",
    "input": { "schema": { "title": "Approve?", "description": "Please confirm", "inputVariables": [] } },
    "record": "",
    "timeout": { "minutes": 30, "step_iri": "/api/3/workflow_steps/<timeout-step-uuid>" },
    "agent_id": null,
    "is_approval": false,
    "owner_detail": { "isAssigned": false, "emailRecipients": "{{vars.user}}" },
    "isRecordLinked": false,
    "step_variables": [],
    "response_mapping": {
      "options": [
        { "option": "Confirm", "primary": true, "step_iri": "/api/3/workflow_steps/<confirm-step-uuid>" },
        { "option": "Cancel", "step_iri": "/api/3/workflow_steps/<cancel-step-uuid>" }
      ],
      "duplicateOption": false,
      "customSuccessMessage": "Done"
    },
    "inputExternalUser": true,
    "email_notification": { "enabled": false, "smtpParameters": [] },
    "external_channel_list": ["/api/3/picklists/afb18b7f-510b-471a-9b9c-7f4646edd4bb"],
    "unauthenticated_input": true,
    "external_email_subject": "A FortiSOAR playbook is requesting your input"
  },
  "stepType": "/api/3/workflow_step_types/fc04082a-d7dc-4299-96fb-6837b1baa0fe"
}
```

### 3.20 `a19333c2` — Awaiting Playbook (simple/older approval)

```json
{
  "name": "Ask SA",
  "arguments": {
    "type": "InputBased",
    "input": { "schema": { "title": "Block or Not Block", "description": "...", "inputVariables": [] } },
    "record": "", "is_approval": true,
    "owner_detail": { "isAssigned": false },
    "isRecordLinked": false, "step_variables": [],
    "response_mapping": {
      "options": [
        { "option": "Approve", "primary": true, "step_iri": "/api/3/workflow_steps/<approve-uuid>" },
        { "option": "Reject", "primary": false, "step_iri": "/api/3/workflow_steps/<reject-uuid>" }
      ],
      "connecteStepsLength": 2,
      "customSuccessMessage": "Awaiting Playbook resumed successfully."
    },
    "email_notification": { "enabled": false, "smtpParameters": [] },
    "inline_channel_list": [], "external_channel_list": [],
    "unauthenticated_input": false
  },
  "stepType": "/api/3/workflow_step_types/a19333c2-c822-11ed-afa1-0242ac120002"
}
```

### 3.21 `dc6ac63d` — Manual Task (create a `tasks` module record)

Creates a human task record in the `tasks` module (assignee, due date, priority). Used in approval/change workflows. `collection` is always `"tasks"`.

```json
{
  "name": "Approver Approval To Implement",
  "arguments": {
    "message": {
      "tags": [],
      "type": "/api/3/picklists/ff599189-3eeb-4c86-acb0-a7915e85ac3b",
      "tenant": "",
      "content": "<p>Added task <a href=\"/modules/tasks/{{vars.steps.Approver_Approval_To_Implement.uuid}}\" target=\"_blank\" rel=\"noopener\">{{vars.steps.Approver_Approval_To_Implement.name}}</a> to <strong>'Approver Approval To Implement'</strong></p>",
      "records": "{{vars.input.records[0]['@id']}}",
      "parentstepid": "/api/3/workflow_steps/<this-step-uuid>"
    },
    "resource": {
      "name": "Approver Approval To Implement - {{vars.input.records[0].title}}",
      "dueBy": "{{vars.input.records[0].dueDate}}",
      "status": "/api/3/picklists/7669725a-28cc-4b19-98a3-9ca71e0f88f4",
      "priority": "/api/3/picklists/539083a6-01f6-4ff9-a588-778cfdad4671",
      "description": "Approval to proceed with the implementation.",
      "assignedOnDate": "{{arrow.utcnow().int_timestamp}}",
      "assignedToPerson": "{{vars.steps.Assignee_And_Approver_Name.input.approverApprovalToImplement}}"
    },
    "collection": "tasks",
    "step_variables": []
  },
  "stepType": "/api/3/workflow_step_types/dc6ac63d-c5a5-472f-9eb4-6b18473a98b8"
}
```

- `message.content` is HTML; it links back to the created task via `vars.steps.<ThisStepName>.uuid`.
- `message.parentstepid` is this step's own IRI.
- `resource.status` / `resource.priority` are task picklist IRIs (look up in-instance).
- `assignedToPerson` is usually a user IRI or a Jinja value resolving to one.

---

## 4. Routes (WorkflowRoute)

```json
{
  "@type": "WorkflowRoute",
  "name": "<sourceStepName> -> <targetStepName>",
  "targetStep": "/api/3/workflow_steps/<uuid>",
  "sourceStep": "/api/3/workflow_steps/<uuid>",
  "label": null,
  "isExecuted": false,
  "group": null,
  "uuid": "<route-uuid>"
}
```

- `label`: `null` for unconditional routes. For conditional routing (from a Condition
  step `12254cf5` or Awaiting-Playbook option), `label` carries the option text
  ("Yes"/"No"/"Approve"/"Reject"/custom).
- `name` is auto-generated `"<source> -> <target>"`.
- `isExecuted` is always `false` in exports.

### 4.1 Join / fan-in (parallel branch convergence)

**There is NO dedicated Join stepType.** Parallel branches converge by fan-in: any
ordinary step that is the `targetStep` of more than one route acts as the join.
Real export distributions: out-degree 1 (2928 routes), 2 (228), 3 (14); in-degree
1 (3241), 2 (68), 3 (10). A Set Variable, Condition, or End step receiving 2+
incoming routes is the canonical join target.

```
        /→ Branch A →\
Source ─                → Join (Set Var / End)
        \→ Branch B →/
```

### 4.2 For-each loop routing

A step with `for_each` has ONE outgoing route to the loop body's first step. The
body's final step routes either (a) back to the for_each step (continue iteration)
or (b) forward to a post-loop step. After iteration completes, the single forward
route proceeds. No join step type is needed.

```
for_each ─→ body[0] ─→ body[n] ─→ (back to for_each OR forward to post-loop)
```

---

## 5. Groups (WorkflowGroup)

Two types: `"note"` (annotations) and `"block"` (visual containers).

```json
{
  "@type": "WorkflowGroup",
  "name": "Step 1 - Define the Command",
  "description": "We want the Fortigate to show us the Admin users",
  "type": "note",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": true,
  "metadata": [],
  "reusable": false,
  "top": "180",
  "left": "1200",
  "height": "77",
  "width": "498",
  "uuid": "<group-uuid>",
  "recordTags": []
}
```

Steps link to a group via the step's `group` field (WorkflowGroup IRI).

Real exports always carry this full key set: `@type`, `name`, `description`, `type`
(`"note"` or `"block"`), `isCollapsed` (false), `hasTriggerStep` (false),
`hideInLogs` (false, occasionally true), `metadata` ([]), `reusable` (false),
`top`, `left`, `height`, `width` (all strings), `uuid`, `recordTags` ([]).
`color` is not used (always null/absent). `height:"0"` is common for pure notes.
No nested sub-groups are observed.

---

## 6. Connectors — observed `connector` + `operation` pairs

For the **full catalog** of ~80 connectors, every observed
`(connector, operation, operationTitle, version)` triple with counts, see
`reference/connector-operations.md`. That file is the authoritative source — use it
to pick the correct slug, operation name, native `operationTitle` prefix, and a
known-good `version` string. A condensed subset is listed below.

> **Slug accuracy note**: real export slugs differ from guesswork. Use the exact
> slugs below (e.g. `crowd-strike-falcon` not `crowdstrike-falcon`; `aws` and
> `aws-commands` are two distinct connectors; `fortinet-fortiai` and
> `fortinet-fortiai-proxy` are distinct).

| connector | representative operations |
|---|---|
| `cyops_utilities` | `no_op` (End), `make_cyops_request` (REST), `format_richtext`, `json_to_html`, `create_file_from_string`, `query_cyops_resource`, `updatemacro`, `extract_artifacts_new`, `extract_email_metadata_new`, `ip_cidr_check`, `reverse_dns_lookup`, `update_cyops_resource` |
| `code-snippet` | `python_inline_code_editor` |
| `fortigate-firewall` | `block_ip`, `block_url`, `execute_command`, `quarantine_host`, `update_policy`, `get_system_events` |
| `fortinet-fortimanager` | `get_incidents`, `get_incident_events`, `update_policy_package`, `create_ldap_server`, `delete_policy_package` |
| `fortinet-fortisiem` | `run_report`, `search_events`, `get_incident_details`, `get_incidents`, `get_device_info` |
| `fortinet-fortianalyzer` | `get_alerts_for_multiple_adoms`, `get_reports`, `get_device_info`, `count_alerts_for_multiple_adoms`, `get_schedules` |
| `fortinet-fortisandbox` | `get_scan_result_job`, `get_submission_job_list`, `submit_file`, `submit_urlfile`, `get_file_verdict` |
| `fortinet-fortiedr` | `get_event_list`, `isolate_collector`, `update_ipset`, `remediate_device` |
| `fortinet-fortirecon-easm` | `get_subdomains`, `get_issues_discovered`, `update_archived_issue`, `get_asset_asns` |
| `fortinet-fortiguard-threat-intelligence` | `threat_intel_search`, `ingest_feeds`, `threat_activities_statistics`, `ioc_search` |
| `microsoft-graph-mail` | `search_emails`, `delete_email`, `move_email`, `forward_email`, `get_folders` |
| `microsoft-teams` | `get_users_all_messages`, `send_message`, `get_channel`, `archive_team` |
| `slack` | `send_message`, `upload_file`, `create_channel`, `search_channel` |
| `crowd-strike-falcon` | `alert_search`, `detection_search`, `get_detection_details`, `get_alert_details`, `process_details` |
| `virustotal` | `query_ip`, `analysis_file`, `file_reputation`, `query_domain`, `query_url` |
| `aws` | `stop_instance`, `reboot_instance`, `start_instance`, `detach_volume`, `revoke_ingress` |
| `aws-commands` | `authorize_ingress`, `attach_volume`, `launch_instance`, `describe_instance` |
| `tenable-io` | `get_vuln_details`, `get_asset_export_status`, `download_asset_export_chunk`, `list_scans` |
| `qradar` | `query_qradar`, `get_offenses`, `get_source_ip`, `get_events_related_to_offense` |
| `smtp` | `send_email`, `send_email_new`, `send_richtext_email` |
| `exchange` | `send_email`, `delete_email`, `run_query` |
| `imap` | `fetch_email_new` |
| `ssh` | `run_remote_command` |
| `mysql` | `run_query`, `list_tables`, `list_columns` |
| `github` | `list_pull_request`, `create_repository`, `update_clone_repository`, `list_repository_collaborator` |
| `gitlab` | `create_issue_comment`, `list_project_merge_requests`, `clone_repository`, `merge_merge_request` |
| `servicenow` | `create_incident`, `get_assignment_group`, `get_users` |
| `activedirectory` | `get_specific_object_details`, `disable_user_account`, `reset_password`, `global_search` |
| `openai` | `get_vector_store`, `get_run_step`, `get_thread`, `create_vector_store`, `converse_with_openai` |
| `mitre-attack` | `get_mitre_data` |
| `csv-data-management` | `extract_data_from_csv`, `merge_two_csv_and_extract_data`, `join_two_csv_and_extract_data` |
| `file-content-extraction` | `extract_text`, `extract_indicators_from_file`, `create_xslx_file_from_json_data` |

**`operationTitle` naming convention**: titles follow `"<Prefix>: <Op>"` for
`cyops_utilities` (`Utils:`, `FSR:`, `CyOPs:`, `File:`, `Email:` — e.g.
`"Utils: No Operation"`, `"FSR: Make FortiSOAR API Call"`). Most external connectors
use the bare operation display name (e.g. `"Block IP Address"`, `"Get IP Reputation"`).

Each connector call also carries: `version` (e.g. `"3.2.6"` for cyops_utilities,
`"5.4.0"` for fortigate-firewall — see the catalog for per-connector known-good
versions), `config` (connector-config UUID — for external connectors), `params`
(operation-specific, Jinja-templated), `operationTitle` (human label),
`step_variables` (output mappings), and optionally `pickFromTenant`, `for_each`,
`ignore_errors`, `when`, `mock_result`.

---

## 7. Variables & Templating (Jinja2)

Root namespace is `vars`. Delimiters: `{{ ... }}` (expression), `{% ... %}` (statement).

| Pattern | Meaning |
|---|---|
| `{{vars.input.records}}` | Trigger input records (array). |
| `{{vars.input.records[0]}}` | First input record. |
| `{{vars.input.records[0].id}}` | Field of first input record. |
| `{{vars.input.records[0]['@id']}}` | IRI of first input record. |
| `{{vars.input.params['name']}}` | Declared playbook input parameter (bracket syntax). |
| `{{vars.input.params.name}}` | Declared playbook input parameter (dot syntax). |
| `{{vars.request.data}}` | REST trigger request body. |
| `{{vars.request.params}}` | REST trigger query params. |
| `{{vars.<varname>}}` | Any variable set by a Set-Variable step or step_variables. |
| `{{vars.steps.<StepName>.data}}` | Output of a previous step (by step **name**). |
| `{{vars.steps.<StepName>.output}}` | Alternative output handle (connector steps). |
| `{{vars.result}}` | Result of the immediately preceding query/find step. |
| `{{vars.item}}` | Current iteration item in a for_each loop. |
| `{{vars.array.append(x)}}` | Mutating append to a list (inside temporary_var Jinja blocks). |

Jinja statement blocks (in `temporary_var` / `step_variables` dummy keys):

```jinja
{% if 'edit' in vars.item %}
    {{vars.array_users.append( vars.item | regex_search('\"(.+?)\"') | replace('\"','') )}}
{% endif %}
```

Common filters: `| string`, `| split(" ")`, `| regex_search(...)`, `| replace(...)`,
`| ipv4`, `| length`, `| unique`, `| tojson`/`| toJSON`, `| random`,
`picklist("value", "@id")` / `picklist("value", "uuid")`, `fromIRI`,
`arrow.get(...).int_timestamp`, `| json_query("[*][\"@id\"][]")`, `| join(", ")`,
`| resolveRange(...)`, `| type_debug`, `| int`, `| abs`.

For 50+ real production expressions (REST request, arrow date, picklist, fromIRI,
loop item, step output, statement blocks) see `reference/jinja-cookbook.md`.

**Top production patterns** (observed frequency in real exports):

- `{{vars.input.records[0]}}` ×499 — first trigger record
- `{{vars.input.records[0]['@id']}}` ×370 — trigger record IRI
- `{{vars.result}}` ×295 — immediately preceding step result
- `{{vars.input.records[0].title}}` ×103 — trigger record field
- `{{arrow.utcnow().int_timestamp}}` ×79 — current epoch
- `{{vars.input.records[0].tenant['@id']}}` ×77 — tenant IRI
- `{{vars.item}}` ×74 — for_each loop item
- `{{vars.input.params['connector_config_id']}}` ×71 — declared param
- `{{None}}` ×65 — explicit null
- `{{globalVars.Demo_mode}}` ×59 — global macro value
- `{{vars.steps.Get_Correlated_Asset[0].assets | json_query('[*]["@id"][]')}}` ×52 — reshape step output
- `{% set _ = config_params.update(prod_config) %}` ×28 — mutate dict in Jinja

`step_variables` (output mapping): maps new variable names to expressions evaluated
against the step's result. These become `vars.<name>` downstream.

```json
"step_variables": {
  "fortigate_output": "{{vars.steps.Call_Command.data}}",
  "python_result": "{{vars.steps.StripHTML}}"
}
```

---

## 8. Parameters / Playbook Input

### 8.1 Workflow-level `parameters` array

Simple array of **string** parameter names:

```json
"parameters": ["my_user_original", "alert_original"]
```

### 8.2 Start-step input schema (`inputVariables`) — for manual button triggers

```json
"inputVariables": [
  {
    "name": "fDate",
    "type": "integer",
    "label": "Start Datetime",
    "dataType": "datetime",
    "formType": "datetime",
    "required": true,
    "defaultValue": { "differenceType": "months", "differenceValue": -1 }
  }
]
```

For picklist-type inputs, add a `dataSource` block describing the picklist source.

**Full observed `type` / `dataType` / `formType` combos** (from real exports):

| type | dataType | formType | Use |
|---|---|---|---|
| `string` | `text` | `text` | Free text input |
| `string` | `file` | `file` | File upload (`dataSource.model: "files"`, `templateUrl: "app/components/form/fields/file.html"`) |
| `string` | `datetime` | `datetime` | Date/time picker |
| `integer` | `datetime` | `datetime` | Numeric datetime |
| `boolean` | `checkbox` | `checkbox` | True/false toggle |
| `array` | `dynamicList` | `dynamicList` | Choose from `options: [...]` list (`templateUrl: "app/components/form/fields/dynamicList.html"`) |
| `picklists` | `multiselectpicklist` | `multiselectpicklist` | Multi-select from a picklist (`dataSource.model: "picklists"`, `dataSource.query` filters by `listName__name`) |
| `scenario` | `lookup` | `lookup` | Lookup against scenario records (`dataSource.model: "scenario"`) |

Common inputVariable keys present on most fields: `name`, `type`, `label`,
`tooltip`, `dataType`, `formType`, `required`, `_expanded`, `useRecordFieldDefault`,
`defaultValue`. Additional keys appear depending on type: `title`, `usable`,
`collection`, `searchable`, `templateUrl`, `lengthConstraint`, `allowedGridColumn`,
`mmdUpdate`, `dataSource`, `visibilityQuery` (with `filters` for conditional
visibility), `jinjaExpressionView`, `_addVisibilityConditions`, `options`,
`playbookField`, `moduleField`, `bulkAction`.

**String input** (simplest):
```json
{ "name": "emailFile", "type": "string", "label": "Email File",
  "tooltip": "Upload email file, *.eml or *.msg", "dataType": "text",
  "formType": "text", "required": true, "_expanded": true,
  "moduleField": "fileEmail", "useRecordFieldDefault": true }
```

**Boolean input**:
```json
{ "name": "importRelationships", "type": "boolean", "label": "Import Relationships",
  "dataType": "checkbox", "formType": "checkbox", "required": false,
  "templateUrl": "app/components/form/fields/checkbox.html", "useRecordFieldDefault": false }
```

**Multiselect picklist input** (with dataSource):
```json
{ "name": "matricesToPull", "type": "picklists", "label": "Matrices To Pull",
  "dataType": "multiselectpicklist", "formType": "multiselectpicklist",
  "required": false, "collection": true, "searchable": false,
  "templateUrl": "app/components/form/fields/typeahead.multiselect.html",
  "dataSource": { "model": "picklists",
    "query": { "sort": [{"field":"orderIndex","direction":"ASC"}],
      "logic": "AND",
      "filters": [{"field":"listName__name","value":"Mitre ATT&CK Matrics","operator":"eq"}] } } }
```

### 8.3 `step_variables.input` on Start steps

```json
"step_variables": {
  "input": {
    "params": [],
    "records": "{{vars.input.records}}"
  }
}
```

- REST starts: `params` maps names to `{{vars.request.data[...]}}`.
- Referenced starts: `params` is `[]` (the called playbook's `parameters` list is the contract).

### 8.4 `displayConditions` (which records show the button)

Per-resource filter on manual Start steps:

```json
"displayConditions": {
  "alerts": {
    "sort": [], "limit": 30, "logic": "AND",
    "filters": [
      { "type":"object", "field":"status",
        "value":"/api/3/picklists/758925e7-629c-46d8-89db-fb36f5fbe88a",
        "_value": { "@id":".../758925e7-...", "display":"Investigating", "itemValue":"Investigating" },
        "operator":"eq" }
    ]
  }
}
```

### 8.5 `resources` (modules)

Start steps declare `resources` (array) / `resource` (string): `"alerts"`,
`"indicators"`, `"threat_intel_feeds"`, `"incidents"`, `"vulnerabilities"`, etc.

---

## 9. Common Picklist References

| Picklist UUID | Represents |
|---|---|
| `2b563c61-ae2c-41c0-a85a-c9709585e3f2` | Priority — "Medium" (workflow `priority`) |
| `15c1e8c9-22bf-4e66-8fbb-0a502d4a4a3f` | Playbook Origin — "Custom" |
| `ff599189-3eeb-4c86-acb0-a7915e85ac3b` | Comment type (resource.type on `/api/3/comments`) |
| `50bfd06c-9aff-4f7d-b6d9-821339e31fe7` | Reputation — "Malicious" |
| `758925e7-629c-46d8-89db-fb36f5fbe88a` | Alert status — "Investigating" |
| `fac53e73-8d16-4189-98d5-95fbd1555232` | Alert status — "Closed" |
| `7de816ff-7140-4ee5-bd05-93ce22002146` | Alert status — "Open" |
| `c0beeda4-2c7a-4214-b7e5-53ba1649539c` | Indicator type — "IP Address" |
| `18c5c903-eda5-494d-aa7e-f28b479681ac` | TypeOfFeed — domain feed |
| `afb18b7f-510b-471a-9b9c-7f4646edd4bb` | External channel list (awaiting playbook) |

If you don't know a picklist UUID, use a placeholder comment and tell the user to
look it up in their FortiSOAR instance.

---

## 10. Positioning (visual layout)

- `top` / `left` are **strings** (e.g. `"40"`), not numbers.
- Convention: Start at `top:"40", left:"40"`. Subsequent steps flow rightward
  (`left += 400`) and downward (`top += 200`).
- WorkflowGroup also has `height` and `width` (strings).
- Coordinates can grow large for wide playbooks (e.g. `left:"1750"`).

---

## 11. Validation Gotchas (READ before generating)

1. **`top`/`left`/`height`/`width` must be strings**, not numbers.
2. **Never use `ee73e569-...` as a stepType** — it is a parent type only.
3. **Last-digit UUID trap**: `b593663d-...-722` = Update Record, `b593663d-...-770` = Find Records.
4. **Parameters must be declared in two places**: the Workflow `parameters` array AND the Start step's `step_variables.input.params` (or `inputVariables` for manual forms).
5. **Step output references use the step NAME** (not UUID): `{{vars.steps.Call_Command.data}}`.
6. **Routes connect by IRI**: `/api/3/workflow_steps/<step-uuid>`.
7. **Every playbook path must terminate in an End step** (`cyops_utilities` / `no_op`).
8. **`collection` IRI on the Workflow** must match the collection's UUID in Shape A.
9. **Generate fresh UUIDs** for every object — never reuse within one playbook.
10. **Required Workflow fields for valid import**: `@type`, `name`, `isActive`, `debug`, `singleRecordExecution`, `remoteExecutableFlag`, `parameters`, `synchronous`, `collection`, `versions`, `triggerStep`, `steps`, `routes`, `groups`, `priority`, `isEditable`, `uuid`, `owners`, `isPrivate`, `deletedAt`, `recordTags`, `aliasName`, `tag`, `description`.
11. **`versions` must be `[]`** on generation — the server creates version 1 on import. Never embed historical snapshots.
12. **No dedicated Join stepType exists** — parallel branches converge by fan-in (a target step receiving 2+ incoming routes). See §4.1.
13. **For-each loops route implicitly** — the for_each step → body → (back to for_each OR forward). No join step needed. See §4.2.
14. **Connector slug accuracy**: use exact slugs from `connector-operations.md`. The GitHub repo name may differ from the playbook `connector` slug (e.g. `connector-virustotal-premium` repo → `virustotal-premium` slug; but some playbook slugs like `virustotal` are built-in variants not on GitHub).
15. **Built-in connectors** (`cyops_utilities`, `smtp`, `ssh`, `exchange`, `slack`, `mysql`, `http`, `code-snippet`, `sentinelone`, `whois-rdap`, etc.) ship with the platform — no GitHub repo. For the `cyops_utilities` connector step (stepType `0109f35d`), omit `config`/`name`/`pickFromTenant`. For other built-ins, include those keys as usual.


---

## B. Reference: step-types-quickref.md

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

- `for_each`: `{ "item": "{{vars.list}}", "parallel": false, "condition": "", "__bulk": true, "batch_size": 100 }`. Used on Set Variable, Create Record, Update Record, Bulk ingest, Connector calls, Reference-a-Playbook. NOT on Condition/Wait/Start.
- `when`: `"{{vars.x == 1}}"` — skip step if false. Most common on connector & email steps.
- `ignore_errors`: `true` — continue on failure. Most common on email & REST/connector steps.
- `step_variables`: `{ "out_var": "{{vars.steps.<Name>.data}}" }` — output mapping.
- `mock_result`: canned output string (requires `useMockOutput=true` in trigger).
- `do_until` (Reference-a-Playbook only): `{ "delay": 5, "retries": 5, "condition": "{{vars.steps.X.validation == 1}}" }` — retry/poll a sub-playbook until condition true.

## Routing notes (IMPORTANT)

- **There is NO dedicated Join stepType.** Parallel branches converge by fan-in: any ordinary step (Set Variable, Condition, End) that is the `targetStep` of multiple routes acts as the join. Out-degree >1 is common (228 routes fan out to 2 targets); in-degree >1 is the join (68 routes converge from 2 sources).
- **For-each loop routing**: the for_each step has ONE outgoing route to the loop body's first step. The body's last step routes either (a) back to the for_each step to continue iteration, or (b) forward to a post-loop step. Convergence after the loop is implicit — no join step type needed.
- **Condition routing**: each `conditions[].step_iri` points to a real step; the matching route's `label` carries the `option` text. One branch usually has `"default": true`. Typical shape = 2 branches (Yes/No).

## Common Jinja patterns

- Trigger record: `{{vars.input.records[0].field}}`
- Trigger record IRI: `{{vars.input.records[0]['@id']}}`
- Input param: `{{vars.input.params['name']}}`
- Step output: `{{vars.steps.<StepName>.data}}`
- Loop item: `{{vars.item.field}}`
- Picklist IRI: `{{"ListName" | picklist("value", "@id")}}`
- Date to epoch: `{{arrow.get(vars.date).int_timestamp}}`
- IRI to object: `{{'/api/3/alerts/<uuid>' | fromIRI}}`

For 50+ real production patterns see `reference/jinja-cookbook.md`.


---

## C. Reference: jinja-cookbook.md

# FortiSOAR Jinja Patterns — Cookbook

Real Jinja2 expressions harvested from 1367 official FortiSOAR playbooks (4551
distinct expressions observed). Use these as copy-paste templates when building
playbook steps. Delimiters: `{{ ... }}` (expression), `{% ... %}` (statement).

Root namespace is `vars`. Also available: `globalVars.<macro>` (collection macros),
`vars.request` (REST triggers), `vars.item` (for_each loop body).

---

## 1. Trigger input (the record(s) that started the playbook)

| Expression | Use |
|---|---|
| `{{vars.input.records}}` | All trigger records (array) |
| `{{vars.input.records[0]}}` | First trigger record (whole object) |
| `{{vars.input.records[0]['@id']}}` | IRI of first record (`/api/3/alerts/<uuid>`) |
| `{{vars.input.records[0].id}}` | Numeric id |
| `{{vars.input.records[0].uuid}}` | UUID |
| `{{vars.input.records[0].title}}` | Title field |
| `{{vars.input.records[0].sourceIp}}` | A custom field on the record |
| `{{vars.input.records[0].userName}}` | A custom field on the record |
| `{{vars.input.records[0].dueDate}}` | Due date field |
| `{{vars.input.records[0].tenant['@id']}}` | Tenant IRI of the record |

## 2. Declared parameters (referenced/REST/manual-form input)

| Expression | Use |
|---|---|
| `{{vars.input.params['name']}}` | Bracket syntax — use when name has special chars |
| `{{vars.input.params.name}}` | Dot syntax — use for simple names |
| `{{vars.input.params['connector_config_id']}}` | The most common param (connector config picker) |
| `{{vars.input.params.parameters.username}}` | Nested param object |
| `{{vars.input.params.style_colors.Malicious}}` | Nested config object |

## 3. REST trigger request

| Expression | Use |
|---|---|
| `{{vars.request.data}}` | Request body (parsed) |
| `{{vars.request.params}}` | Query parameters |
| `{{vars.request.record['@id']}}` | Record IRI passed in request |
| `{{vars.request.record.title}}` | Record field via REST |
| `{{vars.request.data.records}}` | Records array in body |
| `{{vars.request.headers.tz}}` | A request header |
| `{% set alert_id = vars.request.data.records[0]['@id'] %}` | Assign from REST body |

## 4. Previous step output

| Expression | Use |
|---|---|
| `{{vars.steps.<StepName>.data}}` | Output of a named step (most common) |
| `{{vars.steps.<StepName>.output}}` | Alternative output handle (connector steps) |
| `{{vars.steps.<StepName>.status}}` | Step status (`"Success"` / `"Failed"`) |
| `{{vars.steps.<StepName>.input.<field>}}` | A field the step was invoked with |
| `{{vars.steps.<StepName>[0].field}}` | Index into a step that ran in a loop |
| `{{vars.steps.<StepName>['@id']}}` | IRI of a record created by the step |
| `{{vars.steps.<StepName>['config_id']}}` | Config id used by a connector step |
| `{{vars.result}}` | Result of the immediately preceding step |
| `{{vars.result.data}}` | Data of the preceding step's result |
| `{{vars.result['@id']}}` | IRI from the preceding step's result |

### Reshape step output (json_query)

| Expression | Use |
|---|---|
| `{{vars.steps.Get_Correlated_Asset[0].assets \| json_query('[*]["@id"][]')}}` | Extract a list of `@id` from an array field |
| `{{vars.steps.Get_KEV_Alerts[0].kEVAlerts[0]['@id']}}` | Nested array indexing |
| `{% for item in vars.steps.Find_Source_Control_Settings %}` | Iterate a step's loop results |

## 5. For-each loop body (`vars.item`)

| Expression | Use |
|---|---|
| `{{vars.item}}` | The current item (whole) |
| `{{vars.item['@id']}}` | IRI of current item |
| `{{vars.item.value}}` | A field on the current item |
| `{{vars.item \| toJSON}}` | Serialize item to JSON |
| `{{vars.item.headers.subject}}` | Nested field on item |
| `{{vars.item.attachments \| json_query("[*].metadata.md5") \| join(', ')}}` | Extract + join a list field |

## 6. Picklist filters (resolve a display value to an IRI/uuid)

| Expression | Use |
|---|---|
| `{{"Severity" \| picklist("Medium")}}` | Returns picklist IRI for Medium severity |
| `{{"Severity" \| picklist("High", "@id")}}` | Explicitly request `@id` form |
| `{{"Severity" \| picklist("Critical", "uuid")}}` | Request `uuid` form |
| `{{"AlertStatus" \| picklist("Open")}}` | Alert status Open |
| `{{"AlertStatus" \| picklist("Closed")}}` | Alert status Closed |
| `{{"IndicatorReputation" \| picklist("Malicious", "uuid")}}` | Indicator reputation |
| `{{"Severity" \| picklist((["Minimal","Low","Medium","High","Critical"]\|random), "@id")}}` | Random pick (testing) |

## 7. fromIRI filter (resolve an IRI string to a record object)

| Expression | Use |
|---|---|
| `{{'/api/3/alerts/<uuid>' \| fromIRI}}` | Fetch record by IRI |
| `{{vars.currentUser \| fromIRI}}` | Resolve a user IRI |
| `{{(vars.currentUser \| fromIRI).firstname}}` | A field of the resolved record |
| `{{(vars.assetIRI \| fromIRI).criticality.itemValue}}` | Nested picklist field |
| `{{(vars.alert_data['@id']+'?$relationships=true') \| fromIRI}}` | With relationships |
| `{% set criticality = (item.criticality \| fromIRI) %}` | Assign resolved object |

## 8. Arrow date/time (epoch timestamps & formatting)

| Expression | Use |
|---|---|
| `{{arrow.utcnow().int_timestamp}}` | Current epoch seconds |
| `{{arrow.utcnow().timestamp}}` | Current epoch (float) |
| `{{arrow.get(vars.date).int_timestamp}}` | Parse a date string to epoch |
| `{{arrow.get(vars.responseDueDate).int_timestamp}}` | Parse a due date |
| `{{arrow.get(arrow.utcnow().shift(days=+vars.dueDays)).int_timestamp}}` | Add N days |
| `{{arrow.get(arrow.utcnow().shift(minutes=-vars.last_x_minute)).int_timestamp}}` | Subtract N minutes |
| `{{arrow.get(vars.data['incident_data']["incidentLastSeen"]).to("UTC").format("YYYY-MM-DD HH:mm:ss ZZ")}}` | Format in UTC |
| `{{arrow.get(arrow.utcnow().int_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')}}` | ISO 8601 format |
| `{{arrow.get(vars.report_details.published_ts).int_timestamp}}` | Parse a published timestamp |
| `{{arrow.get(vars.advisoryList \| json_query('[*]["release_date"][]') \| unique \| max).int_timestamp}}` | Max date from a list |
| `{{ arrow.get(vars.report_details.information_date, 'YYYY-MM-DD').int_timestamp }}` | Parse with explicit format |

### Expiry / TTL pattern (very common)

```
{{ arrow.now().int_timestamp + (vars.input.params['expiry'] | int) * 24 * 60 * 60 }}
```
Adds `expiry` days to now.

## 9. List/dict mutation (inside `temporary_var` Jinja blocks)

```jinja
{% if 'edit' in vars.item %}
    {{vars.array_users.append( vars.item | regex_search('\"(.+?)\"') | replace('\"','') )}}
{% endif %}
```

| Pattern | Use |
|---|---|
| `{{vars.recordIRI.append(vars.result['@id'])}}` | Append to a list var |
| `{{vars.alertList.append(vars.result['@id'])}}` | Accumulate IRIs |
| `{% set _ = config_params.update(prod_config) %}` | Merge dict (discard return) |
| `{% set _ = data.append((asset['@id'] + "?$relationships=true") \| fromIRI) %}` | Append resolved record |
| `{{vars.x.append(y)}}` inside `{% ... %}` | Any mutating append |

## 10. Conditional statements (`{% if %}` blocks)

```jinja
{% if vars.foundList | length != 0 %}
  {{vars.foundList}}
{% else %}
  {{None}}
{% endif %}
```

| Pattern | Use |
|---|---|
| `{% if vars.cat_summary \| length > 0 %}` | Non-empty list |
| `{% if vars.SPF_Record \| length == 0 -%}` | Empty list |
| `{% elif vars.Not_Permitted_IPs_for_SPF_SoftFail \| length != 0 -%}` | Elif branch |
| `{% for item in vars.steps.Find_Source_Control_Settings %}` | Loop over step results |
| `{% endfor %}` / `{% endif %}` / `{% else %}` | Block terminators |

## 11. Common filters (quick reference)

| Filter | Example |
|---|---|
| `\| length` | `{{vars.alerts \| length > 0}}` |
| `\| unique` | dedupe a list |
| `\| join(", ")` | join list to string |
| `\| split(" ")` | split string to list |
| `\| tojson` / `\| toJSON` | serialize to JSON string |
| `\| int` / `\| abs` | numeric cast |
| `\| regex_search('pat')` | regex match |
| `\| replace('a','b')` | string replace |
| `\| random` | pick random element |
| `\| resolveRange(map)` | map a value via a dict |
| `\| type_debug` | debug a variable's type |
| `\| ipv4` | validate/format IPv4 |

## 12. Global macros (`globalVars.<name>`)

Macros are collection-level reusable values. Reference as `globalVars.<name>`:

| Expression | Use |
|---|---|
| `{{globalVars.Demo_mode}}` | A boolean toggle macro |
| `{{globalVars.cicd_env}}` | An environment name macro |
| `{{globalVars.Current_Date}}` | A computed-date macro (`{{arrow.utcnow().timestamp}}`) |

---

## Condition expressions (for `12254cf5` Condition steps)

These go in `conditions[].condition`. They must evaluate to a boolean.

```jinja
{{ vars.foundFortinetWebFilterReputation or vars.useMockOutput }}
{{ vars.input_values.input1 == None }}
{{ vars.steps.Get_Whois_Information.status == "Success" or vars.useMockOutput }}
{{ vars.is_reputation_found }}
{{ vars.steps.IOC_Search.data.data | length > 0 }}
{{ ("Success" in vars.steps.Get_IP_Reputation.data.message and vars.steps.Get_IP_Reputation.status == "Success") or vars.useMockOutput }}
{{ vars.steps.Get_QRadar_Macros.data['hydra:totalItems'] == 0 }}
{{ vars.fetch_mode == 'By Updates In Last X Minutes' }}
{{ vars.inactive_service_list | length > 0 }}
{{ (vars.steps.CPU_Utilization.data | int ) >= ( vars.cpu_threshold | int) }}
{{ vars.steps.Virtual_Memory.data.svem.percent >= ( vars.virtual_memory_threshold | int ) }}
{{ true }}
```

- A branch with `"default": true` needs no `condition`.
- Reference the target step via `step_iri` (IRI) and `step_name` (display).


---

## D. Reference: guide-condensed.md

# FortiSOAR 7.6.1 Playbooks Guide — Condensed Reference

Condensed from the official FortiSOAR 7.6.1 Playbooks Guide (December 2024, 265 pages).
Use this for concepts, trigger types, Jinja patterns, best practices, and step-result
references. For exact JSON shapes, see `playbook-json-schema.md`.

---

## 1. What a Playbook Is

Playbooks automate security processes across external systems. They are "akin to a
functional programming language." The **Playbook Engine runs asynchronously** as an
independent service within FortiSOAR.

- **Playbook Collection** = a folder/container for organizing playbooks. Created via
  *Automation > Playbooks > New Collection*. Fields: Name, Description, icon, Tags.
  Collections are the unit for import/export/clone.
- **Playbook** = an individual sequence of steps within a collection. Names must be
  **unique within a collection**. Each has an Active/Inactive state.

### Visual Editor Model (Playbook Designer)
- **Trigger** = always the first step; defines *when* the playbook runs.
- **Steps** = discrete data-processing elements linked in sequences.
- **Routes** = arrows/connections between steps (with labels/conditions from Decision steps).
- **Blocks (Groups)** = visual containers grouping related steps. Cannot be nested; a step
  belongs to only one block.
- **Notes** = free-text annotations (can be hidden from logs).
- **Reference Blocks** = reusable saved blocks of steps (exportable/importable).

### Execution Priority
High / Medium (default) / Low. Sync reference playbooks inherit parent's priority.

### Logging
- Per-playbook: INFO (production) or DEBUG (design/debug).
- From 7.4.0, default for *failed* playbooks is DEBUG.

---

## 2. Step Types (by designer category)

Step categories: **Core**, **Evaluate**, **Execute**, **References**, **Email**, **Authentication**.

### Step Utilities (footer of every step)
- **Condition (`when`)** — Jinja expression; if unmet, step is *skipped*.
- **Variables** — store step output directly in a named variable (avoids a Set Variable step).
- **Loop** — `for each` (iterate array; `vars.item`) or `do until` (runs ≥1 time until
  condition met or retries exhausted; default 3 retries, 5s delay). Loop modes:
  **Bulk** (single API; default/recommended for Create/Update; batch size 100),
  **Sequential** (one API per record; aborts on first failure),
  **Parallel** (separate API requests via multiple threads).
- **Message** — custom step message (HTML or Markdown); added to record's collaboration
  panel; can be added to other records by IRI list; replicatable to tenant nodes (MSSP).
- **Mock Output** — substitute canned output (requires `useMockOutput = true` variable in trigger).
- **Ignore Error** — if Yes, step failure continues the playbook (status = "Finished with Error").

### Core
- **Create Record** — creates a record in any module. Date/Time fields must be epoch
  (`{{arrow.get(var).int_timestamp}}`). Don't link more than 99 records in one call.
- **Update Record** — update an existing record by IRI.
- **Find Records** — query with filters; limit default 30 (capped at 5000 from 7.0.0).
  `Include Correlated Records` off by default. `Limit Output` to fetch only needed fields.
- **Ingest Bulk Feed** — high-volume insert/update (ThreatIntel/Vulns/Assets). Faster than
  Create Record. OnCreate/OnUpdate triggers do NOT fire for bulk-feed records.
- **Set Variable** — name + value (Jinja). Scope is local to playbook + child playbooks.
  Reference: `{{vars.<name>}}`.

### Evaluate
- **Decision** — conditional routing. First match wins; if none match, Default route taken.
  Condition Builder (field/operator/value with AND/OR) or Advanced Jinja
  (e.g., `"x" in vars.variable`, `vars.variable == 5`).
- **Wait** — pause. `For Specified Time` (Days + H:M:S; max 7 days) or `Until a Condition is Met`.
- **Approval** — halts until approver accepts/rejects. Fields: Step Name, Medium, Approver type,
  Input Prompt Design (Title/Description/Jinja), Response Mapping ("Approve" always Primary),
  optional Escalation (max 7 days). Output: `{{vars.steps.<step>.approved}}`, `.message`, `.user`.
- **Manual Task** — pauses until a Task record's Status = Skipped/Completed.
  Output: `{{vars.steps.<step>['task_data']['@id']}}`, `{{vars.steps.<step>.status}}`.
- **Manual Input** — pop-up prompt for decisions/form inputs. Segments: Context (record-linked
  or global), Medium (FortiSOAR-only or external via Email/Slack/Teams), Input Prompt Design
  (Text/Picklist/Lookup/File/Date/Checkbox/etc.), Response Mapping, Escalation (max 7 days).

### Execute
- **Connector** — runs a connector operation. Two tabs: By Connector Names, or By Actions.
  Fields: Step Name, Target (Self/Agent), Configurations, Action, Inputs.
- **Utilities** — built-in functions: `Utils: Make REST API Call`, `FSR: Create/Upsert Record`,
  `File: Zip`, `Convert XML to Dictionary`, `Create Attachment from File`, `Download File from URL`,
  `Create File from String`. Note: Integrations API supports only POST calls.
- **Code Snippet** — runs custom Python via the Code Snippet connector.

### References
- **Reference a Playbook** — calls any playbook by name or IRI. Fields: Playbook Reference,
  Parent Data (Full ENV / Pass Input Record Only / Not Required [default]), optional Loop,
  `Run Asynchronously`. Returns the last executed step's output in `vars.steps.<step_name>.keyname`.
- **Trigger Tenant Playbook** — MSSP; triggers a playbook on a tenant node from the master.

### Email
- **Send Email** — uses built-in SMTP connector. Recipients = FortiSOAR teams/users or typed addresses.
- **Send Email (Advanced)** — adds Body Type: Plain Text / Rich Text / Email Template.

### Authentication
- **Set API Keys** — overrides the default Playbook Appliance keys for subsequent steps.

---

## 3. Triggers (six types)

Triggers define *when* a playbook executes; always the first step.

### On Create
Fires after a record is created/ingested. Asynchronous (non-blocking). Supports condition-based
triggering. Won't fire for IngestBulkFeed records.

### On Update
Fires after a record is updated. `IsChanged` operator available. Won't fire for IngestBulkFeed.

### On Delete
Fires after a record is deleted.

### Condition-based triggers (On Create/Update/Delete)
- `Trigger Condition`: All True (AND) or Any True (OR).
- Operators: Equals, Not Equals, Less Than/Before, Greater Than/After, Matches Pattern,
  Is Changed (update only), Contains/Contains All/Added (for Tags).
- Encrypted fields cannot be filtered. From 7.6.0 conditions can be based on record UUID.

### Custom API Endpoint
Arbitrary endpoint triggered by external REST POST. `Route` (alphanumeric; no special chars).
Authentication: Token/API-Key (default; HMAC), Basic Auth, No Authentication (not recommended).
Access query params via `api_params` and request body via `api_body`. Only POST allowed.

### Referenced
For playbooks called exclusively from a Reference a Playbook step. Gets data via
`input.params.<param_name>` from the parent.

### Manual Trigger
Click-to-start from within any module. Fields: Step Name, Trigger Button Label, Execution Behaviour
(`Requires record input` with "Run once for all" or "Run separately for each Record"; or
`Does not require record input`), Choose record modules, Configure Visibility Conditions,
Customize Playbook Trigger Message, User Prompt (custom input form with Text/Picklist/Lookup/
File/Date/Checkbox/EmailTemplateField types).

### Trigger Data / Variables (under `vars`)
| Key | Applies To |
|---|---|
| `input.records` (array; `input.records[0]` for single) | Manual, OnCreate, OnUpdate |
| `input.params['api_body']` | API trigger only |
| `input.params.<param_name>` | all (from Input Parameters) |
| `request.headers` (incl. `X-RUNBYUSER`) | all |
| `request.data`, `request.method` | all |
| `previous` (prior record version before change) | OnUpdate only |
| `currentUser` (IRI of triggering user) | all |
| `resource` (module) | database triggers |

From 6.0.0 all request parameters consolidated under `vars.input`.

---

## 4. Variables & Data Flow

### Variable namespaces (under `vars`)
- `vars.input.records` — array of triggering records (DB/Manual triggers).
- `vars.input.params.<name>` — input parameters (Tools > Parameters).
- `vars.input.params['api_body']` — request body for Custom API Endpoint.
- `vars.steps.<step_name>.<keyname>` — return value of a previous step. Array elements need index.
- `vars.request.headers['X-RUNBYUSER']` — IRI of triggering user.
- `vars.item.<field>` — current item in a `for each` loop.
- `vars.<custom_variable_name>` — variables via Set Variable or step Variables. Local to playbook + children.
- `globalVars.<name>` — global variables (cross-playbook), e.g., `Server_fqhn`, `CurrentDate`.

### Reserved words (do NOT use as variable names)
`items`, `result`, `input`, `request`, `values`, `keys`, `files`, `env`, `message`, `resources`,
`step_variables`, `do_until`, `ignore_errors`, `when`, `for_each`, `cyops_playbook_iri`,
`cyops_playbook_name`, `collaborationNote`, `inputVariables`, `displayConditions`.

### Jinja2 Templating
- `{{ ... }}` — output expression. `{% ... %}` — statement (for/if/elif/else/endif, set, block, break, continue, do).
- Filters: `{{ var | filter(args) }}`. Case-sensitive.
- To force a string result, enclose Jinja in quotes: `"{{vars.data | join(',')}}"`.
- From 7.4.0 Jinja is sandboxed (no private member access). Disable via `USE_SANDBOX_ENV: false` (not recommended).

### Key built-in functions/filters (FortiSOAR-specific)
- `arrow` (datetime): `{{ arrow.utcnow().int_timestamp }}` (use `int_timestamp` not `timestamp` from 7.0.0).
  `arrow.get(var).to('EST').format('YYYY-MM-DD HH:mm:ss ZZ')`, `arrow.get(var).shift(hours=+4)`.
- `uuid()`: `{{ uuid() }}`.
- `toJSON`/`tojson`, `from_json`, `to_nice_json`, `to_yaml`, `from_yaml`.
- `fromIRI`: resolve IRI to object: `{{ '/api/3/events/8' | fromIRI }}`. Supports recursion:
  `{{ ((vars.event.alert | fromIRI).owner | fromIRI).name }}`.
- `picklist("listName","value"[,"@id"])`: resolve picklist item to its `@id`.
- `extract_artifacts` (IOCs from string), `parse_cef`/`extract_cef`, `readfile`, `ip_range`,
  `counter`/`count_occurrence`, `loadRelationships(moduleName, [fields])`, `html2text`,
  `json2html(row_fields)`, `urlencode`/`urldecode`, `json_query` (JMESPath), `yaql('$.expr')`.
- Plus most Ansible/Jinja2 filters (ipaddr, ipv4/ipv6, hash, regex_search/findall/replace,
  min/max/unique/intersect/difference/union, map/select, groupby, sort, join, length).

### Jinja expression examples
```jinja
{% for item in vars.teamName %}{% if item == '/api/3/teams/<uuid>' %}Yes{% endif %}{% endfor %}

{% if cond %}...{% elif cond %}...{% else %}...{% endif %}
{# Always add an {% else %} None {% endif %} to avoid empty-string failures #}

{% set id = i['@id'] %}
{% do vars.res.append(vars.printThis) %}
```

---

## 5. Routes & Conditions

### Decision step routing
- Evaluates conditions sequentially; first match wins; others skipped; if none match, Default route.
- Each condition maps a `Condition` (Condition Builder or Advanced Jinja) to a `Select A Step to Execute`.
- Advanced Jinja: `"x" in vars.variable`, `vars.variable == 5`, `vars.variable != []`.

### Step-level Condition (`when`)
- `when` (without loop): applies at step level — first thing evaluated; if false, step skipped.
- `when` (inside `for each`): applies per item.

### Branching / parallel execution
- Parallel Branch Execution: independent paths run in parallel threads (`PARALLEL_PATH` default true).

### Loops
- `for each`: iterate array of objects; `vars.item`. One per step. Optional condition.
- `do until`: runs ≥1 time; until condition met or retries exhausted (default 3, 5s). Don't combine
  with `when` or `for_each`. Use with `Ignore Errors` for retry-until-success.
- Loop modes: Bulk (batch 100), Sequential (aborts on first failure), Parallel (multi-thread).
- Cross-iteration state: set `save_iteration_result = true` env var; access via
  `iteration_result_<step_name_with_underscore>`.
- Recursion guards: `skip_recursive_playbook_execution` (default true), `REF_SELF_PB_LOOP_LEVEL` (default 10).

---

## 6. Connector Operations

- **By Connector Names** tab or **By Actions** tab (action = annotation like "Submit Sample").
- Fields: Step Name, Target (Self / Agent), Configurations drop-down (or `{}` Jinja for dynamic
  config name), Action drop-down, Inputs.
- Multiple connector versions can coexist (x.y.z; if specified version not found, latest is used).
- Password-type config fields are encrypted.
- Connector configurations have RBAC: Private configs visible only to owning team.

### Utilities examples
- **FSR: Upsert Record**: IRI = `api/3/alerts`; Body = JSON with Jinja; Fields = uniqueness list
  e.g. `['name','status']`; Ignore Missing Fields defaults False.
- **FSR: Make FortiSOAR API Call**: used for REST calls incl. DELETE for file cleanup.

---

## 7. Playbook Parameters

- Declare via **Tools > Parameters** in the designer.
- Appear under Dynamic Values > Input/Output > Input > Parameters.
- For Custom API Endpoint triggers, `api_body` appears under Parameters.
- Passed to child playbooks via the Reference a Playbook step's input mapping.
- `Parent Data` option: Full ENV / Pass Input Record Only / Not Required (default).
- Recommended: explicitly define child input parameters rather than relying on env passthrough.
- `COPY_ENV_FOR_REFERENCE_WORKFLOW` (default false) toggles env passthrough globally.

---

## 8. Comments & Artifacts

### Step Messages (comments on records)
- Every step has a **Message** footer utility. HTML or Markdown.
- Added to the collaboration panel of the triggering record by default.
- Can be added to other records: array or comma-separated list of IRI(s).
- Can be posted into a specific message thread.
- MSSP: "Also send this message to specified tenant".

### Manual Input link in collaboration panel
```html
<p><a data-comment-collaboration-pendingdecision='true' data-pendingdecision-id='{{vars.steps.<step_name>.wfinput_id}}'>Manual Input Link</a></p>
```

### Creating artifacts / records
- Create Record step (any module, incl. Attachments).
- Utilities → Create Attachment from File / Create File from String / Download File from URL / File: Zip.
- Ingest Bulk Feed for high-volume.
- Files uploaded via Manual Input should be deleted after processing (Utilities → FSR: Make
  FortiSOAR API Call, DELETE method + file IRI).

---

## 9. Error Handling

- **Ignore Error** (per step) — if Yes, playbook continues; step status = "Finished with Error".
- Playbook statuses: Incipient, Active, Awaiting, Paused, Failed, Finished, Skipped, Terminated, Finished with error.
- **do until** loop: retries (default 3) + delay (default 5s) for retry-until-success patterns.
- **Rerun From Last Failed Step** button on failed playbooks (resumes from failed step).
- Debug mode: INFO (production) or DEBUG. Failed playbooks default to DEBUG (7.4.0+).
- **Trigger Playbook with Sample Data** in designer: `Pick from previous executions` (DEBUG only),
  `Select a module record or custom JSON`, `Execute with mock output`.

### Synchronous vs. Asynchronous
- Playbook Engine runs asynchronously.
- OnCreate triggers are asynchronous (non-blocking).
- Reference a Playbook: synchronous by default; `Run Asynchronously` makes parent continue.
- Child playbooks with a Wait step run synchronously with the parent.
- Loop modes: Bulk (single API), Sequential (serial), Parallel (multi-thread).

### Timeouts / termination
- `CELERYD_TASK_SOFT_TIME_LIMIT` (default 1800s) — soft limit.
- `CELERYD_TASK_TIME_LIMIT` (default 2400s) — hard limit (force-terminates).
- Awaiting playbooks auto-terminate after 7 days (`WF_MAX_WAITING_DAYS`).
- Wait step max = 7 days. Approval/Manual Input escalation max = 7 days.

---

## 10. Import/Export Format

- Playbooks and collections are exported/imported as **JSON**.
- Importing a collection: name must be unique unless "Replace existing playbook collection" checked.
- Global variables included with exports are listed on the Import dialog for review.
- Tags are upserted on import.
- `Yes, include versions` exports saved versions.
- BPMN import (BETA): imports BPMN XML (Flowable/Camunda/Signavio) → playbook. Mapping:
  SequenceFlows → Decision; Start Events → Manual Trigger; Gateways → Decision;
  User Tasks → Manual Task; Service Tasks → Create/Update Record; Script Tasks → Connector/Code Snippet;
  Mail Tasks → SMTP; HTTP Tasks → Utilities (REST).

### Export behavior
- Exporting resets Private playbooks to Public with blank owners — re-assign after import.
- Cloning a collection auto-updates references between playbooks in the same cloned collection;
  references to playbooks in OTHER collections are NOT auto-updated unless cloned simultaneously.

---

## 11. Best Practices

### Design / organization
- One collection per integration target; action collections (Forensics, Enrichment, Remediation);
  response-plan collections that sequence actions.
- Use **Blocks** to group steps logically (Configure / Investigate / Remediate).
- Use **Notes** to document complex steps.
- Use **Reference a Playbook** for reusable sub-playbooks; explicitly declare child input parameters.
- Place a **Decision** step immediately after the trigger to gate execution.
- After a Create Record step, add an immediate next step to assign desired team/user ownership
  (created records belong to the Playbook Appliance teams by default).
- Use the `Server_fqhn` global variable in Send Email steps so email links work.

### Performance
- Use **Bulk** mode (batch size 100) for bulk Create/Update in loops; reduce batch size on timeouts.
- Use **Parallel** loop mode for independent items; **Sequential** when you need to abort on first failure.
- `Find Records` capped at 5000 records; use pagination via API + loop for larger sets.
- Use `Limit Output` to fetch only needed fields.
- Don't link more than 99 records in a single call (use loop batches of 99).
- Use INFO logging in production; DEBUG only when designing/debugging.
- Avoid `Append` correlations in Create Record of Data Ingestion playbooks (use Overwrite).

### Naming / reserved
- Playbook names must be unique within a collection.
- Variable names: letters, numbers, underscores only.
- Tags cannot contain: `' , , " # ? /`.
- Connector endpoint route names: alphanumeric only.
- Use `int_timestamp` (not `timestamp`) for arrow DateTime Jinja from 7.0.0.
- Date/Time fields in Create/Update Record must be epoch: `{{arrow.get(var).int_timestamp}}`.

### Versioning / upgrade safety
- Save versions (max 20) with meaningful notes for revert capability.
- From 7.6.1, customized playbooks in Solution Packs are not overwritten during upgrades (a 'Base'
  version is created). Clone playbooks from connectors/Solution Packs before editing.

---

## 12. Advanced Topics

### Reusable playbooks
- Reference a Playbook step calls any playbook by name or IRI.
- Referenced trigger type marks a playbook as callable only from a Reference step.
- Child playbook output: Reference step returns the last executed step's output in
  `vars.steps.<step_name>.keyname`. Use a Set Variable at the end of the child to compose a return.
- Variables set in child playbooks do NOT carry over to the parent (except the last step's return value).

### MSSP / tenant considerations
- **Trigger Tenant Playbook** step: triggers a playbook on a tenant node from the master.
- `Only trigger at the node where record is` checkbox (7.4.2) on OnCreate/OnUpdate/OnDelete triggers.
- Step Messages: "Also send this message to specified tenant" replicates comments to tenant nodes.
- IngestBulkFeed records are not peer-replicable (master/tenant).
- Records created via playbook are owned by the Playbook Appliance teams; reassign if needed.

### Config file locations (for tuning)
- `/opt/cyops-workflow/sealab/sealab/config.ini` — `THREAD_POOL_WORKER` (8), `SYNC_DELAY_LIMIT` (60),
  `CELERYD_TASK_SOFT_TIME_LIMIT` (1800), `CELERYD_TASK_TIME_LIMIT` (2400), `PARALLEL_PATH` (true),
  `COPY_ENV_FOR_REFERENCE_WORKFLOW` (false), `USE_SANDBOX_ENV`, `REF_SELF_PB_LOOP_LEVEL` (10),
  `WF_MAX_WAITING_DAYS`, `LOG_PURGE_CHUNK_SIZE`.
- `/opt/cyops-api/config/parameters_prod.yaml` — `skip_recursive_playbook_execution` (true),
  `api_platform.collection.pagination.maximum_items_per_page` (5000, Find Records cap).
- `/etc/celery/celeryd.conf` — `CELERYD_OPTS` (default `-P=eventlet -c=30`).
- Logs: `/var/log/cyops/cyops-workflow/celeryd.log`, `/var/log/cyops/cyops-integrations/connectors.log`.

---

## Quick Reference: Step Result Jinja Patterns

| Need | Jinja |
|---|---|
| Triggering record field | `{{vars.input.records[0].name}}` |
| Triggering record IRI | `{{vars.input.records[0]['@id']}}` |
| Previous step output | `{{vars.steps.<step_name>.<keyname>}}` |
| Array element from step | `{{vars.steps.<step_name>[0].name}}` |
| Approval result | `{{vars.steps.<approval_step>.approved}}` |
| Approval message | `{{vars.steps.<approval_step>.message}}` |
| Approval user | `{{vars.steps.<approval_step>.user}}` |
| Manual Task ID | `{{vars.steps.<task_step>['task_data']['@id']}}` |
| Manual Task status | `{{vars.steps.<task_step>.status}}` |
| Loop item field | `{{vars.item.name}}` |
| Current user IRI | `{{vars.request.headers['X-RUNBYUSER']}}` |
| API trigger body | `{{vars.input.params['api_body']}}` |
| Custom variable | `{{vars.<var_name>}}` |
| Global variable | `{{globalVars.<name>}}` (e.g., `Server_fqhn`) |
| Picklist IRI | `{{"AlertType" | picklist("Phishing", "@id")}}` |
| Date to epoch | `{{arrow.get(vars.someDate).int_timestamp}}` |
| IRI to object | `{{'/api/3/alerts/<uuid>' | fromIRI}}` |
| Triggering user (IRI) | `{{vars.currentUser}}` |
