"""
Copyright start
MIT License
Copyright (c) 2026 <Your Organization>
Copyright end
"""

import requests
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME, DEFAULT_TIMEOUT

logger = get_logger(LOGGER_NAME)


def _headers(config):
    """Build auth headers from the connector configuration.

    Swap this for the target API's real auth scheme:
      - API key header (shown here): {"Authorization": "Bearer <key>"} or {"X-API-Key": <key>}
      - Basic auth:  pass auth=(user, password) to requests instead of a header
      - OAuth2:      fetch a token first, then send it as a Bearer header
    """
    return {
        "Authorization": "Bearer {}".format(config.get("api_key", "")),
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _request(config, method, path, params=None, json_body=None):
    """Execute an API request and return parsed JSON.

    `path` is appended to the configured base URL, e.g. "status" -> <base_url>/status.
    """
    base_url = (config.get("base_url") or "").rstrip("/")
    url = "{}/{}".format(base_url, path.lstrip("/"))
    verify = bool(config.get("verify_ssl", True))

    try:
        response = requests.request(
            method,
            url,
            headers=_headers(config),
            params=params,
            json=json_body,
            verify=verify,
            timeout=DEFAULT_TIMEOUT,
        )
    except requests.exceptions.RequestException as err:
        raise ConnectorError("Request to {} failed: {}".format(url, err))

    if not response.ok:
        # Prefer the API's error message, fall back to raw text.
        detail = response.text
        try:
            body = response.json()
            detail = body.get("message") or body.get("error") or detail
        except ValueError:
            pass
        raise ConnectorError("API error {}: {}".format(response.status_code, detail))

    # Guard against empty / non-JSON success bodies before calling .json().
    if not response.text or not response.text.strip():
        return {}
    try:
        return response.json()
    except ValueError:
        raise ConnectorError("Expected JSON but got: {}".format(response.text[:200]))


def get_status(config, params):
    """Example operation. Replace with real operations for the target API."""
    return _request(config, "GET", "status")


def check_health(config):
    """Lightweight connectivity/auth check invoked by the connector Health Check.

    Raise ConnectorError on failure; return (any value) on success.
    """
    _request(config, "GET", "status")
    return True


# Maps info.json "operation" names to their implementing functions.
# Every operation in info.json must have a matching entry here.
operations = {
    "get_status": get_status,
}
