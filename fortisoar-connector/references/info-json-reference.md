# info.json reference

`info.json` is the connector manifest. It has three top-level areas: **metadata**
(what the connector is), **configuration** (the fields on the connector's config
page), and **operations** (the actions shown in playbooks). Every `name` in the file
must be unique within its section.

## Table of contents
- [Metadata](#metadata)
- [configuration.fields](#configurationfields)
- [operations](#operations)
- [Worked example](#worked-example)

---

## Metadata

Top-level keys describing the connector.

| Key | Required | Notes |
|-----|----------|-------|
| `name` | yes | Unique API name, **kebab-case** (e.g. `crowdstrike-falcon`). Must match the connector folder name and the `.tgz` top-level dir. |
| `version` | yes | SemVer string, e.g. `1.0.0`. |
| `label` | yes | Display name shown in the UI, e.g. `CrowdStrike Falcon`. |
| `description` | yes | What the connector/product does. `\n` allowed. |
| `publisher` | yes | Author/org. Use `Community` (or your org) for user-authored connectors. |
| `contributor` | no | Individual contributor name, if any. |
| `cs_approved` | no | Fortinet-internal certification flag. **Default `false`** for user-authored connectors — you are not Fortinet CS. |
| `cs_compatible` | no | Declares compatibility with FortiSOAR. `true` is fine. |
| `icon_small_name` | yes | Filename in `images/`, 32×32 PNG. Conventionally `small.png`. |
| `icon_large_name` | yes | Filename in `images/`, 80×80 PNG. Conventionally `large.png`. |
| `category` | yes | Free-text grouping shown in Content Hub, e.g. `Threat Intelligence`, `IT Service`, `Compute Platform`, `Miscellaneous`. Pick the closest fit. |
| `help_online` | no | URL to online docs. Leave `""` if none. |
| `ingestion_supported` | no | `true` if the connector can feed data ingestion. See below. |
| `ingestion_modes` | no | e.g. `["scheduled"]`. Only meaningful when `ingestion_supported` is `true`. |

### Ingestion (`ingestion_supported` / `ingestion_modes`)
These are **flags**, not a separate code contract. Setting `ingestion_supported: true`
with `ingestion_modes: ["scheduled"]` tells FortiSOAR that one of the connector's
existing operations (e.g. `get_indicators`) can be invoked on a schedule to pull
records automatically. You do **not** write a special ingestion function or signature —
it is a normal operation. Leave both out (default off) unless the target system is
something you poll for records.

---

## configuration.fields

`configuration.fields` is a list of field objects that render the connector's
configuration page. The `name` of each field is the key you read from `config` in
`operations.py`.

Field object shape:

| Key | Required | Notes |
|-----|----------|-------|
| `title` | yes | Label shown to the user. |
| `name` | yes | Key you read from `config` in code. Unique within the fields list. |
| `type` | yes | One of `text`, `password`, `integer`, `checkbox` (also seen: `select`, `textarea`). |
| `required` | yes | `true`/`false`. |
| `editable` | yes | `true`/`false`. |
| `visible` | yes | `true`/`false`. |
| `value` | no | Default value. For `checkbox`, a boolean; for `text`, a string. |
| `placeholder` | no | Greyed-out hint text. |
| `tooltip` | no | Hover help. |
| `description` | no | Longer help text under the field. |
| `validation` | no | `{ "pattern": "<regex>", "patternError": "<message>" }` for `text` fields. |

Notes:
- `password` fields are stored **write-only** — code can read them, but the UI never
  displays the stored value back.
- A `verify_ssl` checkbox (default `true`) is a near-universal convention; include it
  and honor it in `_request`.

---

## operations

`operations` is a list of action objects. Each becomes a selectable action in
FortiSOAR playbooks and in **Test Actions**.

Operation object shape:

| Key | Required | Notes |
|-----|----------|-------|
| `operation` | yes | Internal name. **Must** match a key in the `operations` dict in `operations.py`. |
| `title` | yes | Display name in the playbook action picker. |
| `description` | yes | What the action does. |
| `category` | no | Playbook-step **icon** category: `investigation`, `containment`, `remediation`, `miscellaneous`. This is *different* from the top-level metadata `category`. |
| `annotation` | no | Usually the same string as `operation`; used for playbook wiring. |
| `enabled` | yes | `true` to expose the action. |
| `is_config_required` | no | `true` if the action needs a saved configuration (almost always). |
| `parameters` | yes | List of parameter objects — same shape as `configuration.fields`. `[]` if none. |
| `output_schema` | no | Sample-shaped dict describing the return value. |

### output_schema
`output_schema` is a **hint** that drives the playbook step-output picker (so playbook
authors can reference `{{ ... }}` fields downstream). It's a sample of the return
shape with empty/placeholder values, not a strict JSON Schema. It's refinable later —
don't block scaffolding to get it perfect; a rough shape from the operation's
description is fine, and an empty `{}` is acceptable to start.

Parameter object shape (identical to config fields, plus these are per-action inputs):
`title`, `name`, `type`, `required`, `editable`, `visible`, optional `value`,
`placeholder`, `tooltip`, `description`, `validation`.

---

## Worked example

A minimal but complete `info.json` — one config field group and one operation with a
parameter:

```json
{
  "name": "acme-siem",
  "version": "1.0.0",
  "label": "Acme SIEM",
  "description": "Acme SIEM ingests and correlates security events.",
  "publisher": "Community",
  "cs_approved": false,
  "cs_compatible": true,
  "icon_small_name": "small.png",
  "icon_large_name": "large.png",
  "category": "Analytics and SIEM",
  "help_online": "",
  "configuration": {
    "fields": [
      {
        "title": "Server URL", "name": "base_url", "type": "text",
        "required": true, "editable": true, "visible": true,
        "value": "https://acme.example.com",
        "tooltip": "Base URL of the Acme SIEM API.",
        "validation": {
          "pattern": "^https?://[^/]+(?:/[^/]+)*$",
          "patternError": "URL must start with http(s):// and not end with '/'."
        }
      },
      {
        "title": "API Key", "name": "api_key", "type": "password",
        "required": true, "editable": true, "visible": true,
        "tooltip": "API key used to authenticate."
      },
      {
        "title": "Verify SSL", "name": "verify_ssl", "type": "checkbox",
        "required": false, "editable": true, "visible": true, "value": true
      }
    ]
  },
  "operations": [
    {
      "operation": "get_alerts",
      "title": "Get Alerts",
      "description": "Fetches alerts created within a time window.",
      "category": "investigation",
      "annotation": "get_alerts",
      "enabled": true,
      "is_config_required": true,
      "parameters": [
        {
          "title": "Start Time", "name": "start_time", "type": "text",
          "required": true, "editable": true, "visible": true,
          "tooltip": "ISO-8601 start time."
        }
      ],
      "output_schema": {
        "alerts": [
          { "id": "", "severity": "", "created": "" }
        ],
        "total": ""
      }
    }
  ]
}
```
