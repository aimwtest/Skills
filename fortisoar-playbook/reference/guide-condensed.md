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
