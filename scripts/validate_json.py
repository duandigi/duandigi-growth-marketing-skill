#!/usr/bin/env python3
"""Perform lightweight validation for example project, opportunity, and experiment JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "project": ["project_id", "name", "business_model", "primary_goal", "north_star_metric"],
    "opportunity": ["opportunity_id", "project_id", "stage", "problem", "evidence", "target_metric"],
    "experiment": ["experiment_id", "project_id", "hypothesis", "primary_metric", "decision_rule", "status"],
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=REQUIRED)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    missing = [field for field in REQUIRED[args.kind] if field not in data]
    if missing:
        print(f"error: missing fields: {', '.join(missing)}", file=sys.stderr)
        return 1
    print(f"{args.path} is a valid {args.kind} example.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
