---
name: fortisoar-solution-pack
description: Build, validate, version and (separately) deploy a FortiSOAR solution pack ZIP from playbook/workflow exports and Scenario or other record sets. Use whenever the user wants to create, package, update, rebuild, version-bump, upload or ship a FortiSOAR solution pack or "content pack", turn exported playbooks (workflow JSON, collections) into an installable ZIP, write info.json / docs / checksums for a pack, check a pack ZIP before import, or asks "is the pack updated / is the zip ready / was it imported". Also use when the pack has to stay in sync with live workflow edits. Not for authoring the playbook logic itself (use fortisoar-playbook) or FortiSOAR connectors (use fortisoar-connector).
---

# FortiSOAR solution pack: build, check, ship

A solution pack is a ZIP of workflow collections, record sets and docs that FortiSOAR can install. Three things get confused and must be kept apart, because each is proven differently:

| Question | What proves it |
|---|---|
| Is the pack **built** and consistent? | Offline: tests, `scripts/check_pack.py`, checksums, a receipt with the ZIP's SHA-256 |
| Is the **live instance** running the same content? | Read-back of live workflows against the pinned candidate (0 differences) |
| Was the pack **imported**? | Only an actual import on the appliance. Direct PUTs to live workflows are NOT an import. |

Always answer "updated / ready / imported" as three separate statements. Never let a green offline check turn into "imported" or "works".

## Workflow

1. **Pin the sources.** Build the pack from exported workflow/record JSON files that live in the project, not from memory. Record each source's SHA-256 so a rebuild notices drift.
2. **Write the builders as pure functions** (export in, export out). They never contact the appliance and never read credentials. Operational helpers (live PUT, probes, runs) live outside the project, in a temp dir, and are never packaged. This keeps the pack reproducible and keeps secrets out of it.
3. **Test first.** Write the failing test for each change (new step, changed text, new field), watch it fail, then implement. Pack content is mostly strings inside JSON, so tests that compare the exact expected text in every place it appears (creator step, expected-value blocks) catch the "changed it in two of three places" bug.
4. **Validate.** Run the project's validator over the generated exports (graph integrity: unique UUIDs, routes only between existing steps, trigger step exists), then `scripts/check_pack.py PACK.zip`.
5. **Assemble the ZIP** from a fixed member set (see layout). Fail on any unexpected or missing member. Deterministic bytes: fixed timestamps, sorted members, fixed permissions, so the same inputs give the same SHA-256.
6. **Write a receipt** next to the ZIP: archive SHA-256, per-member hashes, source hashes, and `import_verified: false` until someone proves otherwise.
7. **Refuse to overwrite.** If the ZIP or receipt exists and differs, stop. Back up the old pair, delete the old pair deliberately, then rebuild, or choose a new version. This stops a stale artifact being mistaken for the current one.
8. **Report** the new SHA-256 and what changed.

## Layout (upload layout)

One enclosing directory named `<name>-<version>/`:

```
<name>-<version>/
  info.json
  README.md
  docs/setup.md  docs/usage.md  docs/checksums.sha256  docs/content-inventory.json
  playbooks/<Collection Name>/collection.metadata.json
  playbooks/<Collection Name>/<Workflow Name>.json      one file per workflow
  records/<apiName>/<apiName>0001.json                   e.g. records/scenario/scenario0001.json
```

`info.json` needs `name`, `version`, `type: "solutionpack"`, `label`, `publisher`, `contents` (`playbooks: [{name}]`, `recordSets: [{name, apiName, count}]`), plus `fsrMinCompatibility`, `certified`, `supportInfo`, `prerequisite`, `dependencies`. `count` must equal the records in the files, and every playbook collection named in `contents` needs its folder. Declare real prerequisites (connectors with versions, configured bindings, agents) in `prerequisite` and `docs/setup.md`; the pack must not install or upgrade them silently.

`docs/checksums.sha256` is `sha256  path` per line for every member except itself.

Things that bit us:
- A Scenario record export uses `name`, but the pack record format wants `title`. Map it deliberately, for the pack copy only.
- Scenario records point at workflows by `playbookIRI`; that workflow must be in the same pack. Ship `createdAlertsID: null` so a fresh install has no stale tracking.
- Keep object UUIDs stable across versions (update in place). New steps and routes get UUIDs from a committed mapping file, never random at build time, or every rebuild changes every hash.
- Ship workflows **inactive** unless the user says otherwise; an installed-but-inactive workflow is still not "safe", it only will not trigger.
- Test data uses documentation IPs (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) and `.invalid` hosts.

## Credentials and secrets

Credentials are for authentication only. Never print, copy, change or package them, and never put them in a pack, receipt, log note or ledger. Warn the user if appliance debug logging records passwords or tokens in plain text. `check_pack.py` flags secret-like text, but a human review of the ZIP is still the real control.

## Deploying changes to a live instance (separate from the pack)

When the user wants live workflows to match a new build, that is a separate step with its own approval each time:

1. Precheck: live equals the previous pinned candidate (so you know what you are overwriting), and the diff to the new one is only the steps you expect, with nothing added or removed unless intended.
2. Snapshot each workflow to disk, then PUT, preserving each step's and route's existing `@id`, `top` and `left`.
3. Read back and compare: 0 differences, active state, step and route counts unchanged.
4. Keep the previous candidate and ZIP as rollback backups.
5. Log it. A live PUT proves the live instance runs the content; it does **not** prove the pack imports.

Test runs create records. Clean them up with the project's own reset (never by hand-deleting), then confirm tracking is empty and shared or pre-existing records are intact. Temporary test tweaks (for example a shortened approval timeout) must be restored and read back.

## Checking a pack: `scripts/check_pack.py`

`python3 scripts/check_pack.py PACK.zip [--allow-active]` reads the ZIP only. It checks ZIP integrity, safe paths, `info.json` keys and `type`, the `<name>-<version>` directory, JSON validity, checksum consistency, workflow graph integrity, that Scenario records reference workflows in the pack, record counts against `contents`, and that workflows are inactive. It also lists secret-looking text for manual review. Exit 0 means well-formed, nothing more.

## Answering "is it ready / imported?"

Report these separately, with evidence:
- **Built:** ZIP path, SHA-256, receipt, tests and `check_pack.py` results.
- **Live matches:** which live workflows were read back against which candidate hash, and which were not touched.
- **Imported:** only if an import was actually done and its result read. Otherwise say plainly that it was never imported and that import acceptance is unverified. Importing needs the user's explicit approval, because it changes the appliance.

Keep a short ledger (what was approved, what ran, hashes, rollbacks) so a later session can answer these without guessing.
