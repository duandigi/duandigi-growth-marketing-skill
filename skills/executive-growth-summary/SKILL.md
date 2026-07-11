---
name: executive-growth-summary
description: Use this skill when producing a daily alert, weekly growth review, monthly executive review, client report, or portfolio briefing from validated multi-channel evaluations and experiment results.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Executive Growth Summary

## Purpose

Turn complex channel and funnel evidence into a concise decision brief for owners, executives, clients, and operators.

## Inputs

- Validated project and portfolio evaluations
- Channel findings, anomalies, health scores, experiments, and approvals
- Business goals, audience, reporting period, and decision cadence
- Known data gaps, connection health, and previous commitments

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Define the audience, reporting period, comparison, and decisions required.
2. Lead with customer value, qualified outcomes, revenue, efficiency, risk, and major changes.
3. Summarize channel contributions without repeating every metric.
4. Explain why material changes likely occurred and state confidence and alternatives.
5. Report experiment decisions, unresolved issues, and learning that changes the playbook.
6. Limit priorities to actions with an owner, expected mechanism, evidence, and approval state.
7. Separate facts, interpretation, decisions, and appendices.

## Required output

Return a concise, decision-oriented result containing:

- Executive summary and key decisions
- What changed, why, and business impact
- Portfolio and project priorities
- Channel and funnel highlights
- Experiment results, risks, approvals, and next actions
- Data-quality and confidence note

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not bury critical tracking, compliance, spend, or revenue risks.
- Do not fill the report with channel metrics that do not affect a decision.
- Do not present AI interpretation as confirmed fact.
- Do not expose credentials, personal lead data, or confidential client details beyond the audience’s authorization.

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
