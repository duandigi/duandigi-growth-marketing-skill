#!/usr/bin/env python3
"""Validate non-secret connection metadata and reject embedded credentials."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

FORBIDDEN = {"access_token", "refresh_token", "client_secret", "password", "application_password", "private_key", "cookie", "authorization"}
REQUIRED = {"connection_id", "organization_id", "provider", "access_mode", "status"}
MODES = {"observe", "prepare", "execute_with_approval"}
STATUSES = {"pending", "healthy", "degraded", "action_required", "revoked", "unavailable"}

def walk(value, path="$"):
    errors = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key.lower() in FORBIDDEN:
                errors.append(f"{path}.{key}: embedded secret field is forbidden")
            errors.extend(walk(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for i, child in enumerate(value):
            errors.extend(walk(child, f"{path}[{i}]"))
    return errors

def validate(data):
    errors = []
    missing = sorted(REQUIRED - set(data))
    if missing: errors.append("missing fields: " + ", ".join(missing))
    if data.get("access_mode") not in MODES: errors.append("invalid access_mode")
    if data.get("status") not in STATUSES: errors.append("invalid status")
    ref = data.get("secret_reference")
    if ref is not None and not isinstance(ref, str): errors.append("secret_reference must be a string or null")
    errors.extend(walk(data))
    return errors

def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument("path", type=Path); a = p.parse_args()
    try: data = json.loads(a.path.read_text(encoding="utf-8"))
    except Exception as exc: print(f"error: {exc}", file=sys.stderr); return 2
    errors = validate(data)
    if errors:
        print("Connection validation failed:", file=sys.stderr)
        for error in errors: print(f"- {error}", file=sys.stderr)
        return 1
    print(f"{a.path} contains valid non-secret connection metadata."); return 0
if __name__ == "__main__": raise SystemExit(main())
