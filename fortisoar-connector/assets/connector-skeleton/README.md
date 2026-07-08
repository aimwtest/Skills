# Sample Connector

Native FortiSOAR connector for **\<Target Product / API\>**. One connector instance
represents a configuration (base URL, credentials); you can create multiple
configurations (for example per environment or per tenant).

## Structure

```
sample-connector/
├── info.json          # Metadata, configuration fields, operations
├── connector.py       # Connector class (execute, check_health) — dispatches to operations
├── operations.py      # One function per operation + the operations{} dispatch dict
├── constants.py       # Logger name, timeouts, URL/mapping constants
├── requirements.txt   # Extra pip dependencies (requests is already available)
├── release_notes.md   # Per-version changelog
└── images/
    ├── small.png      # 32x32 icon (you must supply this)
    └── large.png      # 80x80 icon (you must supply this)
```

## Configuration

| Field      | Description                                             |
|------------|---------------------------------------------------------|
| Server URL | Base URL of the target API (https://…, no trailing `/`) |
| API Key    | Credential used to authenticate                         |
| Verify SSL | Verify the server SSL certificate (default: true)       |

## Operations

| Operation  | Title      | Description                          |
|------------|------------|--------------------------------------|
| get_status | Get Status | Retrieves service status from the API |

## Packaging & import

1. Supply real `images/small.png` (32×32) and `images/large.png` (80×80).
2. Package the folder (macOS-safe — avoids AppleDouble `._*` files that break the loader):
   ```bash
   COPYFILE_DISABLE=1 tar -czf sample-connector.tgz sample-connector/
   tar tzf sample-connector.tgz | grep '\._' && echo "BAD: AppleDouble files present" || echo "OK"
   ```
3. In FortiSOAR: enable **System Configuration → Advanced Development Features → Build Your Own Connector** (7.6.4+), then **Content Hub / Connectors → Add Connector** → upload the `.tgz`.
4. Create a configuration, then use **Test Configuration** and **Test Actions** to verify.

> The connector folder name, the `info.json` `"name"` field, and the top-level directory
> inside the `.tgz` must all match.
