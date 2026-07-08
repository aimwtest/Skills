---
name: fortisoar-connector
description: >-
  Develop, scaffold, extend, and troubleshoot FortiSOAR connectors — Fortinet SOAR
  Python integrations built from info.json + connector.py + operations.py and packaged
  as a .tgz. Use this whenever the user wants to build/create/scaffold a FortiSOAR
  connector for some product or API, add an operation to an existing connector, or debug
  a connector that fails to load or fails at runtime. Trigger on mentions of: FortiSOAR
  connector, ConnectorError, connectors.log, check_health, execute(config, operation,
  params), supported_operations, "Connector Dependencies Failed To Install", BYOC /
  Build Your Own Connector, Content Hub connector, cyops-integrations. Also trigger when
  the user describes writing a Python integration/plugin for FortiSOAR even without the
  word "connector". Do NOT use for FortiSOAR playbooks (workflow automation JSON) or
  FortiSOAR widgets (UI dashboards) — those are different artifacts with their own tools.
---

# FortiSOAR connector development

A FortiSOAR connector is a folder of Python + JSON that lets FortiSOAR talk to a
third-party system (fetch alerts, enrich data, take actions). This skill helps you
**scaffold** new connectors, **extend** existing ones, and **troubleshoot** broken ones.

Bundled resources — open the reference file when you reach the step that needs it, not
all up front:
- `references/info-json-reference.md` — full `info.json` schema (metadata, config fields, operations)
- `references/connector-py-patterns.md` — `connector.py`/`operations.py` conventions + auth snippets
- `references/packaging-and-testing.md` — `.tgz` packaging, BYOC upload, Test Actions
- `references/troubleshooting.md` — reading `connectors.log`, static vs. dynamic errors
- `assets/connector-skeleton/` — a working dummy connector to copy and fill in

## Triage — pick the mode first

- **Building a brand-new connector** → §1 Scaffold
- **Adding/changing operations on a connector folder already in the repo** → §2 Extend
- **A connector is installed and something is broken** → §3 Troubleshoot (skip scaffolding entirely)

---

## §1 Scaffold a new connector

### Ask first, in one batch
Before writing code, get these from the user (ask them together, not one at a time —
they're the things you genuinely can't guess):

1. **Target product/API** — name and **base URL**.
2. **Auth** — type (API key header? Basic? OAuth2 client-credentials? client cert?) and
   therefore which credential config fields are needed.
3. **Operations** — the actions they want, at least the first few, with what each does
   and its key parameters.
4. **Extra config fields** — anything beyond base URL + credentials (tenant ID, custom
   timeout, a `verify_ssl` toggle, etc.).

If the user is vague, propose a reasonable first set of operations from the product and
let them correct it — but don't invent the base URL or auth scheme.

### Defaults — apply without asking, state them so the user can correct
Don't block scaffolding to get every field perfect:
- `version`: `1.0.0`
- `cs_approved` / `cs_compatible`: `false` / `true` (you're not Fortinet CS)
- `publisher`: `Community` (or the user's org if they gave one)
- `is_config_required`: `true` on each operation
- `category` (metadata): best guess from the product's domain (e.g. `Threat
  Intelligence`, `IT Service`) — state it
- `output_schema`: rough best-effort from the operation description, or `{}` — refinable
- `verify_ssl` config field defaulting to `true`
- icons: `small.png` / `large.png` — the user must supply the actual art

### Build
1. Copy `assets/connector-skeleton/` to a new folder named `<kebab-case-name>/`. The
   folder name, `info.json` `"name"`, and (later) the `.tgz` top-level dir must match.
2. Fill in `info.json` per `references/info-json-reference.md` — metadata, one config
   field per credential/setting, one operation object per action.
3. Implement `operations.py` per `references/connector-py-patterns.md` — one
   `(config, params) -> dict` function per operation, wire each into the `operations`
   dict, adapt `_headers` to the real auth scheme, implement `check_health`.
4. Rename the class in `connector.py` and the `LOGGER_NAME` in `constants.py`.
5. List any extra pip deps in `requirements.txt` (not `requests` — already available).
6. Update `README.md` + `release_notes.md`; tell the user to drop real icons in `images/`.
7. Hand off to `references/packaging-and-testing.md` for `.tgz` + upload + testing.

Keep the default scaffold minimal — no `playbooks/` or `builtins.py` unless asked.

---

## §2 Extend an existing connector

1. **Read the existing `info.json` and `operations.py` first.** Match the connector's
   established auth helper, error handling, and naming — don't introduce a second,
   competing pattern in the same connector.
2. A new operation = **four** additions that must agree:
   - a new `(config, params) -> dict` function in `operations.py`
   - a new entry in the `operations` (or Wizard `supported_operations`) dict
   - a new operation object in `info.json` `operations` (matching `operation` name)
   - any new config fields / parameters it needs
3. Bump `version` in `info.json` and add a bullet to `release_notes.md`.
4. If the connector came from the Content Hub, publish via **Add Version**, not Edit
   (see `references/packaging-and-testing.md`).

---

## §3 Troubleshoot a broken connector

**Get the log first.** Ask the user for the relevant lines from
`/var/log/cyops/cyops-integrations/connectors.log` (`tail -f` it while reproducing) —
don't guess without the actual `ERROR` line.

Quick split (full detail in `references/troubleshooting.md`):
- **Static** (won't load / health-check fails): a code bug (`invalid syntax
  (connector.py, line N)` → fix that line) or a missing library (`No module named 'X'` →
  `pip install` into the integrations venv **and** add it to `requirements.txt`).
- **Dynamic** (loads fine, one action fails at runtime): the third-party API drifted —
  reproduce with **Test Actions**, tighten parsing/error handling in `operations.py`.

⚠️ The UI often says **"Connector Dependencies Failed To Install"** even for a pure code
bug. Don't trust the label — read the log line.

---

## File roles

| File | Role |
|------|------|
| `info.json` | Manifest: metadata, config fields, operations. Drives the UI. |
| `connector.py` | Thin dispatcher: `execute` routes `operation` → function; `check_health`. |
| `operations.py` | Business logic: `_request` helper, one function per operation, the `operations` dict. |
| `constants.py` | Logger name, timeouts, URL/mapping constants. |
| `requirements.txt` | Extra pip deps (not `requests`). |
| `images/` | `small.png` (32×32) + `large.png` (80×80), human-supplied. |

## Top gotchas

- **"Dependencies Failed To Install" lies** — it shows for code bugs too. Check
  `connectors.log` before touching pip.
- **Content-Hub connectors: Add Version, never Edit** — and give a unique Name + API
  Identifier (append `Test` / `-test`).
- **macOS packaging** — use `COPYFILE_DISABLE=1 tar -czf` (or `--exclude='._*'`) or the
  loader chokes on AppleDouble `._*` files.
- **Three-way name match** — connector folder name = `info.json` `"name"` = `.tgz`
  top-level dir.
- **Dict keys must match** — every `operation` in `info.json` needs a matching key in the
  `operations` dict, or you get "Unsupported operation".
