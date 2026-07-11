#!/usr/bin/env python3
"""Read sanitized mock provider assets and records through a connector-like CLI."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("command",choices=["health","list-assets","fetch"]); p.add_argument("connection",type=Path); a=p.parse_args()
    try:
        conn=json.loads(a.connection.read_text(encoding="utf-8")); fixture=Path(a.connection).resolve().parents[0] / Path(conn["metadata"]["fixture"]).name
        if not fixture.exists(): fixture=Path(__file__).resolve().parents[1] / conn["metadata"]["fixture"]
        data=json.loads(fixture.read_text(encoding="utf-8"))
    except Exception as exc: print(f"error: {exc}",file=sys.stderr);return 1
    if a.command=="health": out={"connection_id":conn["connection_id"],"status":conn["status"],"last_successful_sync_at":conn.get("last_successful_sync_at"),"mock":True}
    elif a.command=="list-assets": out={"connection_id":conn["connection_id"],"assets":data.get("assets",[])}
    else: out={"connection_id":conn["connection_id"],"records":data.get("records",[]),"mock":True}
    print(json.dumps(out,indent=2,ensure_ascii=False));return 0
if __name__=="__main__":raise SystemExit(main())
