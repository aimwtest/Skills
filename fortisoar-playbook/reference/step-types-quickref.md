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
