#!/usr/bin/env python3
"""Detect a simple complete-period anomaly using median and MAD plus a business threshold."""
from __future__ import annotations
import argparse, json, math, statistics, sys, uuid
from pathlib import Path

def detect(data):
    series=[p for p in data.get("series",[]) if p.get("complete",True)]
    minimum=int(data.get("minimum_history",6))
    if len(series)<minimum+1: raise ValueError(f"need at least {minimum+1} complete observations")
    current=series[-1]; history=[float(p["value"]) for p in series[:-1]]; observed=float(current["value"])
    median=statistics.median(history); deviations=[abs(x-median) for x in history]; mad=statistics.median(deviations)
    robust_z=0 if mad==0 and observed==median else (math.inf if mad==0 else 0.6745*(observed-median)/mad)
    pct=None if median==0 else (observed-median)/abs(median)
    zt=float(data.get("z_threshold",3)); pt=float(data.get("percent_threshold",.3))
    unusual=abs(robust_z)>=zt and (pct is None or abs(pct)>=pt)
    magnitude=abs(pct or 0)
    severity="info"
    if unusual: severity="critical" if magnitude>=.75 else "high" if magnitude>=.5 else "medium"
    return {"anomaly_id":"anom-"+uuid.uuid4().hex[:12],"scope_id":data.get("scope_id","unknown"),"metric_name":data.get("metric_name","unknown"),"period":current.get("period","unknown"),"observed_value":observed,"baseline_value":round(median,4),"percent_change":None if pct is None else round(pct,4),"severity":severity,"confidence":round(min(0.99, .5+min(abs(robust_z) if math.isfinite(robust_z) else 10,10)/20),3) if unusual else .5,"classification":"candidate_anomaly" if unusual else "within_expected_range","related_metrics":data.get("related_metrics",[]),"checks":["Verify connection health and last complete period","Check tracking, releases, campaigns, seasonality, and related business outcomes"]}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("path",type=Path);a=p.parse_args()
    try: data=json.loads(a.path.read_text(encoding="utf-8")); result=detect(data)
    except Exception as exc: print(f"error: {exc}",file=sys.stderr);return 1
    print(json.dumps(result,indent=2,ensure_ascii=False));return 0
if __name__=="__main__":raise SystemExit(main())
