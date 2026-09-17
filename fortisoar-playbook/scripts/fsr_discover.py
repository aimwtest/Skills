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

# Verified against FortiSOAR 7.6.x where possible; adjust per your Swagger.
CONNECTORS_CANDIDATES = [
    "/api/3/connectors?$limit=1000",
]
CONFIGS_CANDIDATES = [
    "/api/3/connector_configs?$limit=2000",
    "/api/integration/connectors/configs/",
]
PICKLISTS_CANDIDATES = [
    "/api/3/picklists?$limit=2000",
]


def norm_connector(item):
    return {
        "name": item.get("name") or item.get("connector_name"),
        "version": item.get("version"),
        "label": item.get("label") or item.get("display_name"),
        "installed": item.get("installed", True),
    }


def norm_config(item):
    connector = item.get("connector") or {}
    if isinstance(connector, str):  # IRI form
        connector = {"name": connector.rstrip("/").split("/")[-1]}
    return {
        "uuid": item.get("uuid"),
        "name": item.get("name") or item.get("config_name"),
        "connector": connector.get("name"),
        "healthy": item.get("healthy", item.get("health_status")),
    }


def norm_picklist(item):
    return {"uuid": item.get("uuid"), "name": item.get("name") or item.get("display")}


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
        _, _, data = try_candidates(client, "GET", CONNECTORS_CANDIDATES)
        profile["connectors"] = sorted(
            (norm_connector(c) for c in extract_items(data)),
            key=lambda c: (c["name"] or ""),
        )
    except ConfigError as e:
        profile["errors"].append(f"connectors: {e}")

    try:
        _, _, data = try_candidates(client, "GET", CONFIGS_CANDIDATES)
        profile["configs"] = sorted(
            (norm_config(c) for c in extract_items(data)),
            key=lambda c: (c["connector"] or "", c["name"] or ""),
        )
    except ConfigError as e:
        profile["errors"].append(f"configs: {e}")

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
