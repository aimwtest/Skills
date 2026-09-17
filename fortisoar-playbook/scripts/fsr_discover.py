#!/usr/bin/env python3
"""Discover a FortiSOAR instance's connector landscape and write an instance profile.

The profile (.fortisoar/instance-profile.json) is what the playbook generator
uses to bind connector steps to REAL installed versions and REAL configuration
UUIDs instead of placeholders.

Usage:
  python3 fsr_discover.py [--host H] [--api-key K] [--insecure] [--out PATH]

If a candidate endpoint 404s on your instance, open https://<host>/swagger,
find the right path, and update CANDIDATES below.
"""

import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fsr_common import (CONFIG_DIR, PROFILE_FILE, ConfigError, FSRClient,
                        die, extract_items, load_config, try_candidates)

# Verified against a live FortiSOAR 7.6.1 instance:
#   connectors : GET /api/integration/connectors/ (paginated via ?page=N)
#   configs    : GET /api/integration/configuration/ (config_id = the UUID a
#                playbook step's `config` needs; status = health; connector =
#                numeric connector id, joined via the connectors list)
#   picklists  : GET /api/3/picklists (hydra collection)
CONNECTORS_PATH = "/api/integration/connectors/"
CONFIGS_PATH = "/api/integration/configuration/"
PICKLISTS_CANDIDATES = [
    "/api/3/picklists?$limit=2000",
]


def norm_connector(item):
    return {
        "name": item.get("name"),
        "version": item.get("version"),
        "label": item.get("label"),
        "active": item.get("active"),
        "system": item.get("system"),
        "config_count": item.get("config_count"),
    }


def norm_config(connector_by_id, item):
    return {
        "uuid": item.get("config_id"),
        "name": item.get("name"),
        "connector": (connector_by_id.get(item.get("connector")) or {}).get("name"),
        "default": item.get("default"),
        "healthy": item.get("status") == 1,
    }


def norm_picklist(item):
    iri = item.get("@id", "")
    return {
        "uuid": iri.rstrip("/").split("/")[-1] if iri else item.get("uuid"),
        "name": item.get("itemValue") or item.get("name"),
        "list": item.get("listName", "").rstrip("/").split("/")[-1] or None,
    }


def fetch_all_connectors(client):
    """Walk the paginated /api/integration/connectors/ endpoint."""
    items, page = [], 1
    while True:
        status, data = client.get(f"{CONNECTORS_PATH}?page={page}")
        if not (200 <= status < 300):
            raise ConfigError(f"GET {CONNECTORS_PATH}?page={page} -> HTTP {status}: "
                              f"{str(data)[:300]}")
        items.extend(data.get("data", []))
        if not data.get("nextPage"):
            return items
        page += 1


def main():
    ap = argparse.ArgumentParser(description="Discover FortiSOAR instance profile")
    ap.add_argument("--host")
    ap.add_argument("--api-key")
    ap.add_argument("--insecure", action="store_true",
                    help="skip TLS verification (self-signed dev instances)")
    ap.add_argument("--out", default=PROFILE_FILE)
    args = ap.parse_args()

    try:
        host, key, environment = load_config(args.host, args.api_key)
    except ConfigError as e:
        die(str(e))

    client = FSRClient(host, key, insecure=args.insecure)
    if args.insecure:
        print("WARNING: TLS verification disabled (--insecure). Dev use only.", file=sys.stderr)

    profile = {
        "host": host,
        "environment": environment,
        "discovered_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "connectors": [],
        "configs": [],
        "picklists": [],
        "errors": [],
    }

    try:
        raw = fetch_all_connectors(client)
        profile["connectors"] = sorted(
            (norm_connector(c) for c in raw), key=lambda c: (c["name"] or ""))
        connector_by_id = {c.get("id"): c for c in raw if c.get("id") is not None}
        status, data = client.get(CONFIGS_PATH)
        if 200 <= status < 300:
            profile["configs"] = sorted(
                (norm_config(connector_by_id, c) for c in extract_items(data)),
                key=lambda c: (c["connector"] or "", c["name"] or ""))
        else:
            profile["errors"].append(
                f"configs: GET {CONFIGS_PATH} -> HTTP {status}: {str(data)[:300]}")
    except ConfigError as e:
        profile["errors"].append(f"connectors: {e}")

    try:
        _, _, data = try_candidates(client, "GET", PICKLISTS_CANDIDATES)
        profile["picklists"] = sorted(
            (norm_picklist(p) for p in extract_items(data)),
            key=lambda p: (p["name"] or ""),
        )
    except ConfigError as e:
        profile["errors"].append(f"picklists: {e}")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(profile, f, indent=2)

    print(f"Instance profile written to {args.out}")
    print(f"  connectors installed : {len(profile['connectors'])}")
    print(f"  connector configs    : {len(profile['configs'])}")
    print(f"  picklists            : {len(profile['picklists'])}")
    if profile["errors"]:
        print("  PARTIAL — some queries failed:", file=sys.stderr)
        for err in profile["errors"]:
            print(f"    {err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
