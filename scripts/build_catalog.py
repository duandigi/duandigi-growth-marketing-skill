#!/usr/bin/env python3
"""Build or verify a machine-readable skill catalog."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
OUTPUT = ROOT / "catalog.json"


def parse_frontmatter(text: str) -> dict[str, object]:
    block = text.split("---\n", 2)[1]
    result: dict[str, object] = {}
    metadata: dict[str, str] = {}
    in_metadata = False
    for line in block.splitlines():
        if line.startswith("metadata:"):
            in_metadata = True
            continue
        if in_metadata and line.startswith("  ") and ":" in line:
            key, value = line.strip().split(":", 1)
            metadata[key.strip()] = value.strip().strip('"').strip("'")
            continue
        in_metadata = False
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    if metadata:
        result["metadata"] = metadata
    return result


def build() -> dict[str, object]:
    entries = []
    for path in sorted(SKILLS.iterdir()):
        if not path.is_dir():
            continue
        meta = parse_frontmatter((path / "SKILL.md").read_text(encoding="utf-8"))
        entries.append(
            {
                "name": meta["name"],
                "description": meta["description"],
                "license": meta.get("license", "MIT"),
                "version": meta.get("metadata", {}).get("version", "unknown"),
                "path": f"skills/{path.name}",
            }
        )
    return {"repository": "duandigi/duan-growth-skills", "version": "0.2.0", "skills": entries}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if catalog.json is out of date")
    args = parser.parse_args()
    content = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            print("catalog.json is out of date; run python scripts/build_catalog.py", file=sys.stderr)
            return 1
        print("catalog.json is current.")
        return 0
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
