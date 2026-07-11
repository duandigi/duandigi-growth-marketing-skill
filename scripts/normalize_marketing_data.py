#!/usr/bin/env python3
"""Normalize sanitized provider records into the shared marketing record contract."""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

METRIC_ALIASES = {"cost": "spend", "ad_spend": "spend", "click": "clicks", "impression": "impressions", "lead": "leads", "qualified_lead": "qualified_leads", "sale_value": "revenue"}
DEFAULT_UNITS = {"spend": "currency", "revenue": "currency", "ctr": "ratio", "conversion_rate": "ratio", "position": "number"}

def normalize(row, index=0):
    metric = METRIC_ALIASES.get(str(row.get("metric_name", row.get("metric", ""))).lower(), str(row.get("metric_name", row.get("metric", ""))).lower())
    required = ["organization_id", "project_id", "provider", "channel", "date"]
    missing = [k for k in required if not row.get(k)]
    if not metric: missing.append("metric")
    if "value" not in row: missing.append("value")
    if missing: raise ValueError("missing fields: " + ", ".join(missing))
    raw_id = "|".join(str(row.get(k, "")) for k in ["organization_id", "project_id", "provider", "asset_id", "date", "object_type", "object_id", metric, index])
    return {
        "record_id": row.get("record_id") or hashlib.sha256(raw_id.encode()).hexdigest()[:24],
        "organization_id": row["organization_id"], "project_id": row["project_id"], "provider": row["provider"],
        "connection_id": row.get("connection_id"), "asset_id": row.get("asset_id"), "channel": row["channel"],
        "object_type": row.get("object_type"), "object_id": row.get("object_id"), "date": row["date"],
        "metric_name": metric, "value": float(row["value"]), "unit": row.get("unit") or DEFAULT_UNITS.get(metric, "count"),
        "currency": row.get("currency"), "grain": row.get("grain", "daily"), "attribution_model": row.get("attribution_model"),
        "attribution_window": row.get("attribution_window"), "last_complete_period": bool(row.get("last_complete_period", True)),
        "dimensions": row.get("dimensions", {}), "quality_flags": row.get("quality_flags", []),
        "source_lineage": row.get("source_lineage", {"source_record_index": index}), "transformation_version": "0.2.0"
    }

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("input", type=Path); p.add_argument("--output", type=Path); a=p.parse_args()
    try:
        payload=json.loads(a.input.read_text(encoding="utf-8")); rows=payload.get("records", payload) if isinstance(payload, dict) else payload
        if not isinstance(rows, list): raise ValueError("input must be a list or an object with records")
        result={"records":[normalize(row, i) for i,row in enumerate(rows)]}
    except Exception as exc: print(f"error: {exc}", file=sys.stderr); return 1
    text=json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if a.output: a.output.write_text(text, encoding="utf-8")
    else: print(text, end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
