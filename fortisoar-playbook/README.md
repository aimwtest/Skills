# fortisoar-playbook

**v2.0** — now with live instance discovery, automated validation, and an import-test loop.

A reusable AI-agent skill that designs, generates, **and self-tests** FortiSOAR
playbook (workflow) JSON — import-ready for FortiSOAR 7.6.x.

## What it gives you

- **Instance discovery (v2)** — `scripts/fsr_discover.py` pulls your instance's
  installed connectors, versions, configuration UUIDs, and picklists into a local
  profile, so generated connector steps bind to **real configs** instead of
  placeholders (the #1 cause of broken imports).
- **Automated validation (v2)** — `scripts/fsr_validate.py` enforces the whole
  pre-import checklist as code: UUID integrity, routing, stepType typos,
  placeholder IRIs, connector operation/params vs. the catalog, and (with the
  instance profile) installed-version and config-UUID checks.
- **Live import-test loop (v2)** — `scripts/fsr_import_test.py` imports the
  playbook into a dev instance via the API, optionally creates test data, triggers
  the playbook, and reports per-criterion pass/fail. Guarded against production.
- **Clarification gate + test plan (v2)** — the skill will not generate JSON on a
  vague request: it asks until the requirement is solid, plays it back, and agrees
  a test plan (scope, generated test data, success criteria) before building.
- **Schema reference** — every Workflow field, all 22 step types with argument
  skeletons + examples, routes, groups, picklists, positioning, validation rules.
- **Connector operations catalog** — 379 connectors / 3339 operations harvested
  from the official `fortinet-fortisoar` GitHub org. For each connector: the exact
  `operation` (→ playbook step `operation`), `title` (→ `operationTitle`),
  `version`, and `parameters` (name, title, required).
- **Full connector manifests** — `connector-manifests.json` carries the complete
  parameter schemas (descriptions, data types, choices, defaults) for every
  operation of every connector.
- **Jinja cookbook** — 50+ real production Jinja2 patterns (trigger input, params,
  REST request, step output, for-each item, picklist/fromIRI filters, arrow dates,
  list mutation, conditionals) harvested from 1367 official playbooks.
- **Step-type quickref** — one-page lookup: stepType UUID → label → argument
  skeleton + routing notes.
- **Templates** — skeleton collection + skeleton playbook + 12 ready-to-paste
  step snippets (manual button, on-create, referenced, REST, set-variable,
  connector-call, condition, call-playbook, add-comment, end-noop,
  manual-task, for-each-create).
- **Official playbook analysis** — a 4245-line study of 1367 official FortiSOAR
  playbooks (step-type usage, trigger patterns, real argument shapes, Jinja,
  routing, groups, macros, field surveys).

## Repository layout

```
fortisoar-playbook/
├── SKILL.md                                    # frontmatter + build workflow + rules
├── README.md                                   # this file
├── reference/
│   ├── playbook-json-schema.md                 # authoritative JSON schema (43 KB)
│   ├── connector-operations.md                 # 379-connector / 3339-op catalog (684 KB)
│   ├── connector-manifests.json                # raw harvested manifests, full params (4.9 MB)
│   ├── jinja-cookbook.md                       # 50+ real Jinja patterns
│   ├── step-types-quickref.md                  # one-page stepType lookup
│   ├── guide-condensed.md                      # concepts from the official Playbooks Guide
│   └── official-playbook-analysis.md           # study of 1367 official playbooks
├── scripts/                                    # v2: python3 stdlib-only, no pip installs
│   ├── fsr_common.py                           # shared config/auth/HTTP helpers
│   ├── fsr_discover.py                         # pull instance profile (connectors, configs, picklists)
│   ├── fsr_validate.py                         # automated pre-import validation
│   └── fsr_import_test.py                      # live import + execute + per-criterion report
└── templates/
    ├── skeleton-collection.json                # Shape A: collection export wrapper
    ├── skeleton-playbook.json                  # Shape B: bare Workflow
    └── snippets/
        ├── start-manual-button.json
        ├── start-on-create.json
        ├── start-referenced.json
        ├── start-rest.json
        ├── set-variable.json
        ├── connector-call.json
        ├── condition.json
        ├── call-playbook.json
        ├── add-comment.json
        ├── end-noop.json
        ├── manual-task.json
        └── for-each-create.json
```

## Usage

### opencode

Copy (or symlink) this folder into `~/.config/opencode/skills/` and restart opencode:

```bash
cp -r fortisoar-playbook ~/.config/opencode/skills/
```

Or point `opencode.json` at the repo:

```json
{ "skills": { "paths": ["~/Skills"] } }
```

### Claude Code

```bash
cp fortisoar-playbook/SKILL.md /your/project/CLAUDE.md
cp -r fortisoar-playbook/reference /your/project/
cp -r fortisoar-playbook/templates /your/project/
```

Then `claude` in that project.

### Claude.ai Projects (web)

- **Custom instructions**: paste the `## When to use` and `## Workflow: how to build
  a playbook` sections of `SKILL.md`.
- **Knowledge**: upload `reference/playbook-json-schema.md`,
  `reference/connector-operations.md`, `reference/jinja-cookbook.md`,
  `reference/step-types-quickref.md`, and all `templates/**/*.json`.

### Grok (x.ai)

- **System prompt**: paste `SKILL.md`.
- **Attachment**: when the task involves connector calls, attach
  `reference/connector-operations.md` to the message.

### Cursor / Continue / Cline / GitHub Copilot

Paste `SKILL.md` (and the `reference/*.md` files you need) into the respective
rules file: `.cursorrules`, `config.json` instructions, `.clinerules`,
`.github/copilot-instructions.md`.

## How the agent uses the connector catalog

Before generating a connector-call step, the agent looks up the connector in
`reference/connector-operations.md` to get the exact `operation`, `operationTitle`,
`version`, and `params` keys. So whichever platform you use, make sure that file
is reachable (uploaded as knowledge / attached as a file / in the project dir).
Without it the agent will guess operation names and produce invalid steps.

## Updating

The connector catalog and the analysis are derived from the official
`fortinet-fortisoar` GitHub org and the official playbook export files
(`Sample.json` 68 collections, `UseCase.json` 28 collections, 1367 playbooks).
Re-harvest by scanning the `connector-*` repos for `info.json` manifests; re-study
by parsing the export JSON. See the harvest methodology in the commit history of
this repo.

## License

MIT — see the parent repo's `LICENSE`.
