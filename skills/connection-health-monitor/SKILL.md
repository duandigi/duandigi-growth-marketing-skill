---
name: connection-health-monitor
description: Use this skill when diagnosing or monitoring whether external marketing-data connections are authorized, reachable, correctly mapped, fresh, complete, and safe to use.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Connection Health Monitor

## Purpose

Distinguish business-performance problems from broken, expired, delayed, misconfigured, or partially authorized data connections.

## Inputs

- Connection status, last successful sync, token expiry, and refresh results
- Provider response codes and quota information
- Expected data cadence and asset mapping
- Recent schema, permission, ownership, or account changes

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Check authorization state, token refresh, account ownership, and required capabilities.
2. Verify provider reachability, quota, pagination, and the last complete data period.
3. Compare expected and observed assets, rows, dimensions, and metric freshness.
4. Classify failures as authorization, permission, mapping, quota, provider, schema, scheduler, or data-lag issues.
5. Define retry, backoff, re-consent, fallback import, and escalation behavior.
6. Block downstream AI evaluation when the missing data could reverse the conclusion.
7. Return a provider-specific health state and remediation action.

## Required output

Return a concise, decision-oriented result containing:

- Connection health status: healthy, degraded, action required, or unavailable
- Last complete data period and freshness lag
- Failure classification and evidence
- Automated recovery and human remediation steps
- Downstream analyses that must be paused or caveated

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not label a marketing channel as declining when its connector is incomplete or stale.
- Do not repeatedly retry authentication failures in a way that locks accounts or floods APIs.
- Never include access tokens or private provider payloads in diagnostics.
- Do not conceal partial syncs behind a healthy aggregate status.

- Do not claim guaranteed growth or present an estimate as observed fact.
- Do not reveal secrets, personal data, private provider payloads, or cross-project information.
- When an action can spend money, publish, contact people, alter access, modify production, or delete data, prepare an approval request instead of executing automatically.

## Completion check

Before finishing, verify that the output:

- answers a specific business or implementation decision;
- uses the correct organization, project, asset, date range, time zone, and currency;
- separates performance problems from data, connection, and attribution problems;
- includes evidence, uncertainty, affected scope, and a measurable next step;
- respects least privilege, approval, audit, and rollback requirements;
- is no longer than necessary for the decision.
