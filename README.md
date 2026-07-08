# Skills

A collection of reusable AI agent skills. Each subfolder is a self-contained skill.

## Available skills

| Skill | Description |
|---|---|
| [`fortisoar-playbook`](./fortisoar-playbook) | Design and generate FortiSOAR playbook (workflow) JSON. Bundles a JSON-schema reference, a connector-operations catalog (379 connectors / 3339 ops harvested from the official `fortinet-fortisoar` GitHub org), a Jinja cookbook, step-type quickref, and ready-to-paste templates. Works in opencode, Claude Code, Claude.ai Projects, Grok, Cursor, Continue, and any LLM. |

## Skill format

Each skill is a folder with:

```
<skill-name>/
├── SKILL.md            # frontmatter (name, description) + instructions
├── reference/          # bundled reference docs the agent reads on demand
└── templates/          # JSON skeletons + snippets the agent can paste
```

`SKILL.md` frontmatter:

```markdown
---
name: <skill-name>
description: One sentence — what it does AND when to trigger it.
---
```

## Usage

### opencode

Copy (or symlink) a skill folder into `~/.config/opencode/skills/` and restart opencode:

```bash
cp -r fortisoar-playbook ~/.config/opencode/skills/
```

Or point `opencode.json` at this repo:

```json
{ "skills": { "paths": ["~/skills"] } }
```

### Claude Code

```bash
cp fortisoar-playbook/SKILL.md /your/project/CLAUDE.md
cp -r fortisoar-playbook/reference /your/project/
cp -r fortisoar-playbook/templates /your/project/
```

### Claude.ai Projects (web)

- **Custom instructions**: paste the `## When to use` and `## Workflow` sections of `SKILL.md`.
- **Knowledge**: upload `reference/*.md` and `templates/**/*.json`.

### Grok (x.ai)

- **System prompt**: paste `SKILL.md` (compact enough).
- **Attachment**: attach `reference/connector-operations.md` when the task involves connector calls.

### Cursor / Continue / Cline / Copilot

Paste `SKILL.md` (or the `reference/*.md` files) into the respective rules file:
`.cursorrules`, `config.json` instructions, `.clinerules`, `.github/copilot-instructions.md`.

See each skill's own README/`SKILL.md` for specifics.
