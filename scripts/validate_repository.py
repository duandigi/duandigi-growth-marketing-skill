#!/usr/bin/env python3
"""Validate version consistency, JSON integrity, provider registry, examples, and repository counts."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VERSION="0.2.0"
FORBIDDEN={"access_token","refresh_token","client_secret","password","application_password","private_key","cookie","authorization"}

def walk(value,path="$",errors=None):
    errors=[] if errors is None else errors
    if isinstance(value,dict):
        for k,v in value.items():
            if k.lower() in FORBIDDEN: errors.append(f"{path}.{k}: forbidden secret key")
            walk(v,f"{path}.{k}",errors)
    elif isinstance(value,list):
        for i,v in enumerate(value): walk(v,f"{path}[{i}]",errors)
    return errors

def main():
    errors=[]
    json_files=list(ROOT.rglob("*.json"))
    for p in json_files:
        try: data=json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc: errors.append(f"{p.relative_to(ROOT)}: invalid JSON: {exc}"); continue
        if "examples" in p.parts or "connectors" in p.parts: errors.extend(f"{p.relative_to(ROOT)}: {e}" for e in walk(data))
    skill_count=len([p for p in (ROOT/"skills").iterdir() if p.is_dir()])
    if skill_count!=30: errors.append(f"expected 30 skills, found {skill_count}")
    eval_count=0
    for p in (ROOT/"skills").glob("*/evals/evals.json"):
        eval_count+=len(json.loads(p.read_text(encoding="utf-8")).get("evals",[]))
    if eval_count!=90: errors.append(f"expected 90 evals, found {eval_count}")
    required_provider={"provider","auth_type","default_mode","assets","capabilities","notes","official_docs"}
    provider_files=list((ROOT/"connectors/providers").glob("*.json"))
    if len(provider_files)<7: errors.append("expected at least 7 provider registry files")
    for p in provider_files:
        data=json.loads(p.read_text())
        missing=required_provider-set(data)
        if missing: errors.append(f"{p.relative_to(ROOT)} missing {sorted(missing)}")
        if data.get("default_mode")!="observe": errors.append(f"{p.relative_to(ROOT)} must default to observe")
    version_checks={
        ".claude-plugin/plugin.json": lambda t: json.loads(t).get("version"),
        ".claude-plugin/marketplace.json": lambda t: json.loads(t)["plugins"][0].get("version"),
        "catalog.json": lambda t: json.loads(t).get("version"),
        "CITATION.cff": lambda t: re.search(r"^version:\s*(\S+)",t,re.M).group(1),
        "pyproject.toml": lambda t: re.search(r"^version\s*=\s*\"([^\"]+)\"",t,re.M).group(1),
    }
    for rel,fn in version_checks.items():
        try: value=fn((ROOT/rel).read_text(encoding="utf-8"))
        except Exception as exc: errors.append(f"{rel}: version check failed: {exc}"); continue
        if value!=VERSION: errors.append(f"{rel}: expected version {VERSION}, found {value}")
    required_examples=["mock-connection.json","mock-provider-data.json","normalized-records.json","evaluation-card.json","approval-action.json","health-score-output.json","anomaly-output.json"]
    for name in required_examples:
        if not (ROOT/"examples/multi-channel"/name).exists(): errors.append(f"missing example {name}")
    if errors:
        print("Repository validation failed:",file=sys.stderr)
        for e in errors: print(f"- {e}",file=sys.stderr)
        return 1
    print(f"Repository valid: {skill_count} skills, {eval_count} evals, {len(json_files)} JSON files, {len(provider_files)} provider registries.")
    return 0
if __name__=="__main__": raise SystemExit(main())
