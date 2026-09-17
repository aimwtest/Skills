#!/usr/bin/env python3
"""Shared helpers for the fortisoar-playbook skill scripts.

Stdlib only. Never prints the API key.

Config resolution precedence (highest first):
  1. CLI flags (--host / --api-key)
  2. Environment variables FORTISOAR_HOST / FORTISOAR_API_KEY
  3. <cwd>/.fortisoar/config.json  {"host": "...", "api_key": "...", "environment": "dev"}

NOTE on endpoints: FortiSOAR 7.6.x exposes interactive Swagger docs at
https://<host>/swagger — if a candidate endpoint below 404s against your
instance, check Swagger and update the CANDIDATES list in the calling script.
"""

import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

CONFIG_DIR = ".fortisoar"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
PROFILE_FILE = os.path.join(CONFIG_DIR, "instance-profile.json")


class ConfigError(Exception):
    pass


def load_config(host=None, api_key=None, require=True):
    """Resolve (host, api_key, environment) from CLI > env > config file."""
    cfg = {}
    if os.path.isfile(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                cfg = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(f"{CONFIG_FILE} is not valid JSON: {e}")

    host = host or os.environ.get("FORTISOAR_HOST") or cfg.get("host")
    api_key = api_key or os.environ.get("FORTISOAR_API_KEY") or cfg.get("api_key")
    environment = cfg.get("environment", "dev")

    if host:
        host = host.strip().rstrip("/")
        if not host.startswith(("http://", "https://")):
            host = "https://" + host
    if require and (not host or not api_key):
        raise ConfigError(
            "Missing FortiSOAR host and/or API key. Provide --host/--api-key, "
            "set FORTISOAR_HOST/FORTISOAR_API_KEY, or create .fortisoar/config.json"
        )
    return host, api_key, environment


class FSRClient:
    """Minimal FortiSOAR API client (API-key auth, stdlib urllib)."""

    def __init__(self, host, api_key, insecure=False, timeout=30):
        self.host = host
        self.timeout = timeout
        self.ctx = ssl.create_default_context()
        if insecure:
            self.ctx.check_hostname = False
            self.ctx.verify_mode = ssl.CERT_NONE
        self.headers = {
            # FortiSOAR API-key auth per 7.6.x API Guide, Access Keys chapter:
            #   Authorization: API-KEY <key>
            # (Bearer <token> is for session tokens from /auth/authenticate)
            "Authorization": f"API-KEY {api_key}",
            "Accept": "application/json",
        }

    def request(self, method, path, body=None, raw_body=None, extra_headers=None):
        """Returns (status, parsed_json_or_text). Never raises for HTTP errors."""
        url = self.host + path
        headers = dict(self.headers)
        if extra_headers:
            headers.update(extra_headers)
        data = None
        if raw_body is not None:
            data = raw_body
        elif body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, context=self.ctx, timeout=self.timeout) as resp:
                return resp.status, _parse(resp.read())
        except urllib.error.HTTPError as e:
            return e.code, _parse(e.read())
        except urllib.error.URLError as e:
            return -1, f"connection error: {e.reason}"

    def get(self, path):
        return self.request("GET", path)


def _parse(raw):
    text = raw.decode("utf-8", errors="replace")
    try:
        return json.loads(text)
    except ValueError:
        return text


def try_candidates(client, method, paths, body=None, raw_body=None, extra_headers=None):
    """Try candidate endpoint paths; return (path, status, data) of first 2xx.

    On total failure, raise with every status + a body excerpt so the user can
    check /swagger and update the candidate list.
    """
    attempts = []
    for path in paths:
        status, data = client.request(method, path, body=body, raw_body=raw_body,
                                      extra_headers=extra_headers)
        attempts.append((path, status, data))
        if 200 <= status < 300:
            return path, status, data
    lines = []
    for path, status, data in attempts:
        excerpt = json.dumps(data)[:300] if not isinstance(data, str) else data[:300]
        lines.append(f"  {method} {path} -> HTTP {status}: {excerpt}")
    raise ConfigError(
        "All candidate endpoints failed. Check https://<host>/swagger for the "
        "correct path and update the CANDIDATES list in this script.\n" + "\n".join(lines)
    )


def extract_items(data):
    """Accept hydra @graph / hydra:member, {'data': [...]}, or a plain list."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("@graph", "hydra:member", "data", "items", "results"):
            if isinstance(data.get(key), list):
                return data[key]
    return []


def die(msg, code=2):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)
