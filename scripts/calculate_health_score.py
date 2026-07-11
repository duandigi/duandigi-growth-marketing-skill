#!/usr/bin/env python3
"""Calculate an explainable confidence-weighted marketing health score."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def band(score):
    if score is None: return "insufficient_data"
    if score >= 85: return "excellent"
    if score >= 70: return "healthy"
    if score >= 55: return "watch"
    if score >= 35: return "at_risk"
    return "critical"

def calculate(data):
    dims=data.get("dimensions", []); minimum=float(data.get("minimum_coverage", .65))
    available=[d for d in dims if d.get("available", True) and d.get("score") is not None and float(d.get("weight",0))>0]
    total_weight=sum(float(d.get("weight",0)) for d in dims)
    available_weight=sum(float(d.get("weight",0)) for d in available)
    coverage=available_weight/total_weight if total_weight else 0
    if coverage < minimum:
        return {"scope_id":data.get("scope_id","unknown"),"score":None,"band":"insufficient_data","confidence":round(coverage,3),"dimensions":dims,"caps_applied":[f"coverage {coverage:.1%} below {minimum:.1%}"],"change_drivers":[],"priority_actions":["Collect or validate missing critical dimensions"]}
    numerator=sum(float(d["score"])*float(d["weight"])*float(d.get("confidence",1)) for d in available)
    denominator=sum(float(d["weight"])*float(d.get("confidence",1)) for d in available)
    score=numerator/denominator if denominator else 0; caps=[]
    flags=data.get("critical_flags", [])
    cap_map={"critical_tracking_failure":49,"critical_connection_failure":49,"material_policy_risk":34,"revenue_data_unreliable":69}
    for flag in flags:
        if flag in cap_map and score>cap_map[flag]: score=cap_map[flag]; caps.append(f"{flag} capped score at {cap_map[flag]}")
    confidence=sum(float(d.get("confidence",1))*float(d["weight"]) for d in available)/available_weight
    return {"scope_id":data.get("scope_id","unknown"),"score":round(score,1),"band":band(score),"confidence":round(confidence*coverage,3),"dimensions":dims,"caps_applied":caps,"change_drivers":data.get("change_drivers",[]),"priority_actions":data.get("priority_actions",[])}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("path",type=Path); a=p.parse_args()
    try: data=json.loads(a.path.read_text(encoding="utf-8")); result=calculate(data)
    except Exception as exc: print(f"error: {exc}",file=sys.stderr); return 1
    print(json.dumps(result,indent=2,ensure_ascii=False)); return 0
if __name__=="__main__": raise SystemExit(main())
