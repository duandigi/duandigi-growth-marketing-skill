---
name: channel-performance-audit
description: Use this skill when auditing one marketing channel from account summary down to campaigns, content, audiences, queries, landing pages, conversions, qualified outcomes, revenue, and operational constraints.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Channel Performance Audit

## Purpose

Apply a consistent channel-audit frame while preserving the provider-specific metrics, mechanisms, and limitations of the selected channel.

## Inputs

- Channel objective, owner, budget, and target audience
- Provider, analytics, CRM, revenue, and landing-page data
- Campaign, content, asset, query, audience, device, location, and time dimensions
- Historical changes, experiments, and channel constraints

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Define the channel job: demand creation, demand capture, activation, retention, referral, or revenue support.
2. Validate data health, attribution boundaries, and the last complete period.
3. Review channel totals, trend, mix, efficiency, quality, and downstream business outcomes.
4. Drill down to the smallest actionable object supported by the data.
5. Identify winners, losers, concentration risk, saturation, decay, tracking gaps, and landing-page mismatch.
6. Compare channel performance against its own objective and constraints, not a universal benchmark.
7. Return prioritized actions and experiments with expected mechanism and approval level.

## Required output

Return a concise, decision-oriented result containing:

- Channel role and health summary
- Top-level and drill-down findings
- Efficiency, quality, and downstream outcome analysis
- Data and attribution limitations
- Prioritized actions, experiments, and stop rules

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not judge every channel by last-click revenue alone.
- Do not use generic industry benchmarks as proof that performance is good or bad.
- Do not optimize top-of-funnel metrics while ignoring lead quality, retention, or margin.
- Do not recommend write actions without an approval plan.

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
