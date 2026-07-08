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
