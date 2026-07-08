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
