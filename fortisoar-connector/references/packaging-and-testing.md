# Packaging, uploading & testing

How to get a connector folder into a running FortiSOAR and verify it.

## Table of contents
- [Three-way name match](#three-way-name-match)
- [Package the .tgz](#package-the-tgz)
- [Enable BYOC and upload](#enable-byoc-and-upload)
- [Add Version vs. Edit](#add-version-vs-edit)
- [Test Configuration / Test Actions](#test-configuration--test-actions)
- [Supporting files](#supporting-files)

---

## Three-way name match

The **connector folder name**, the `info.json` `"name"` field, and the **top-level
directory inside the `.tgz`** must all be identical (kebab-case). A mismatch makes the
connector fail to load or behave unpredictably.

---

## Package the .tgz

Package from the parent directory so the archive contains the connector folder as its
top-level entry:

```bash
COPYFILE_DISABLE=1 tar -czf sample-connector.tgz sample-connector/
```

**macOS gotcha:** without `COPYFILE_DISABLE=1`, macOS `tar` embeds AppleDouble
resource-fork files (`._*`) and `.DS_Store` into the archive, which FortiSOAR's
connector loader chokes on. Verify the archive is clean:

```bash
tar tzf sample-connector.tgz | grep -E '(\._|\.DS_Store)' && echo "BAD: AppleDouble/DS_Store present" || echo "OK: clean archive"
```

(Equivalent alternative: `tar --exclude='._*' --exclude='.DS_Store' -czf ...`.)

---

## Enable BYOC and upload

From FortiSOAR **7.6.4+**, uploading/editing custom connectors requires enabling the
feature first:

1. **System Configuration → Advanced Development Features → Build Your Own Connector
   (BYOC)** — acknowledge the risk notice and enable it.
2. **Content Hub / Connectors → Add Connector** → upload the `.tgz`.
3. Create a configuration (fill the config fields) and **Save**.

---

## Add Version vs. Edit

When iterating on a connector that came from the **Content Hub** (a downloaded/certified
connector), always click **Add Version** — **never Edit**. Clicking Edit on a
content-hub connector is the single most common mistake.

- Give the new version a **unique Name and API Identifier**. A common convention is to
  append `Test` to the name and `-test` to the API identifier (e.g. `sample-connector`
  → `sample-connector-test`).
- For a connector you authored yourself from scratch, editing your own in-progress
  version is fine — this rule is specifically about content-hub-sourced connectors.

---

## Test Configuration / Test Actions

Two buttons on the connector page, used before publishing a new version:

- **Test Configuration** — runs `check_health(config)` against a saved configuration.
  Green = auth/connectivity OK.
- **Test Actions** — runs a chosen operation with real inputs and shows the JSON output
  (Formatted / JSON tabs). Use this to verify each operation end-to-end without building
  a playbook.

Iteration loop: edit code → **Save** (or re-upload) → **Test Configuration** →
**Test Actions** → bump version / **Add Version** when the change is good.

---

## Supporting files

- **`requirements.txt`** — extra pip deps, bare names or pins, one per line. `requests`
  is already available in the runtime — don't list it. Only list packages the code
  imports. These are installed when the connector is installed/upgraded.
- **`images/`** — `small.png` (32×32) and `large.png` (80×80) RGBA PNGs, referenced by
  `icon_small_name`/`icon_large_name`. Must be supplied by a human. If you use different
  filenames (e.g. `medium.png`), update `info.json` to match.
- **`release_notes.md`** — short changelog bullets for the current version.
- **`playbooks/playbooks.json`** (optional) — sample playbooks, a JSON object with
  `"type": "workflow_collections"` and a collection + workflows array. Convention: name
  the collection `Sample - <Connector Label> - <version>`. Warn users to **clone** these
  before use — the sample collection is deleted on connector upgrade/delete.
- **`rpm/cyops-connector-<name>.spec`** — Fortinet-internal RPM packaging. **Not needed**
  for user-built connectors; ignore unless you're contributing to Fortinet's own build.
