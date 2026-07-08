# Troubleshooting a broken connector

Audience is FortiSOAR/Python-literate — this file stays connector-specific and doesn't
re-explain FortiSOAR basics.

## Start here: the log

Everything starts from the connectors log on the FortiSOAR appliance:

```bash
tail -f /var/log/cyops/cyops-integrations/connectors.log
```

**Don't trust the UI label.** The connector page often shows **"Connector Dependencies
Failed To Install"** even when the real cause is a plain code bug, not a missing
dependency. Clicking **Install** repeatedly won't fix a code error. Always read the log
to find the actual `ERROR` line before deciding what's wrong.

Two broad classes: **static errors** (connector fails to load / health-check) and
**dynamic errors** (loads fine, a specific action fails at runtime).

---

## Static errors (load / health-check time)

The connector won't load. The log shows the reason.

### Code issue — syntax/import error
Log looks like:
```
ERROR ... invalid syntax (connector.py, line 10)
connectors.core.base_connector.ConnectorError: invalid syntax (connector.py, line 10)
```
Fix: open the named file at the named line and fix the Python error (unterminated
string, stray text, bad indentation, missing import). Re-upload and re-test.

### Missing / wrong Python library
Log looks like:
```
ERROR ... Exception occurred while getting the connector instance ERROR :: No module named 'pytest'
```
Fix — install into the FortiSOAR integrations venv:
```bash
sudo -u fsr-integrations /opt/cyops-integrations/.env/bin/pip install <package>
```
If the package isn't in FortiSOAR's internal mirror, point pip at public PyPI:
```bash
sudo -u fsr-integrations /opt/cyops-integrations/.env/bin/pip install <package> \
  --extra-index-url https://pypi.python.org/simple
```
Then **add the package to `requirements.txt`** so it installs automatically on the next
version/upgrade — a manual pip install is not persisted across a reinstall.

> Note: "No module named 'X'" and a syntax error can *both* surface under the same
> "Dependencies Failed To Install" UI banner. The log line tells you which it is.

---

## Dynamic errors (runtime, per-action)

The connector loads and health-check passes, but a specific action fails when run —
usually because the third-party API drifted (endpoint moved, permissions changed, or the
response shape/content changed). These are visible in the playbook step's **Error
Output**, and sometimes need `connectors.log` too.

Worked example — a malformed/truncated JSON response:
```
CS-INTEGRATION-5: Error occurred while executing the connector action
ERROR :: Expecting ',' delimiter or '}': line 4 column 1 (char 64)
```
That's a JSON-parsing failure: the code called `.json()` on a body the server returned
that isn't valid JSON (or is an error/HTML page). Fix pattern:
1. **Reproduce** with the same inputs via **Test Actions**.
2. Inspect the raw response — validate `response.ok` and that the body is non-empty
   before `.json()`; surface non-2xx bodies as a `ConnectorError` with the status code
   (see `connector-py-patterns.md` → Resilience).
3. Tighten parsing / error handling in `operations.py`.
4. Re-verify with **Test Actions**.

---

## End-to-end checklist

1. Reproduce the failure (Test Actions, or run the playbook).
2. `tail -f /var/log/cyops/cyops-integrations/connectors.log` and find the specific
   `ERROR` line.
3. Classify: **static** (syntax/import → fix code; missing module → pip install + add to
   `requirements.txt`) or **dynamic** (API drift → fix parsing/handling in
   `operations.py`).
4. Apply the fix.
5. Re-run **Test Configuration** and **Test Actions**.
6. If the connector came from the Content Hub, iterate via **Add Version** (unique
   Name + API Identifier), not **Edit** — see `packaging-and-testing.md`.
