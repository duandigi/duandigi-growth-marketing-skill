---
name: action-approval-planner
description: Use this skill when converting an AI recommendation into a safe observe, investigate, prepare, approve, execute, verify, or rollback workflow for marketing, website, CRM, advertising, content, or data actions.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Action Approval Planner

## Purpose

Ensure AI-generated optimization is reviewable, reversible, authorized, and matched to the financial, privacy, platform, brand, and production risk of the action.

## Inputs

- Recommended action, affected provider, project, asset, and business objective
- Current connection capabilities and application roles
- Expected impact, cost, privacy, policy, brand, and production risk
- Backup, draft, feature flag, test, logging, verification, and rollback options

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Classify the action as observe, investigate, prepare, execute, publish, spend, contact, delete, access, or irreversible.
2. Determine the minimum provider permission and application role required.
3. Assign an approval tier based on money, audience, data, access, production, policy, and reversibility.
4. Require a preview, diff, draft, simulation, test environment, or dry run whenever feasible.
5. Define preconditions, approver, expiry, execution window, idempotency, and rollback.
6. Log the request, evidence, decision, executor, result, verification, and residual risk.
7. Return a machine-readable approval card and human summary.

## Required output

Return a concise, decision-oriented result containing:

- Action classification and approval tier
- Required capability, role, and approver
- Preview, preconditions, tests, and execution plan
- Verification, audit log, and rollback plan
- Expiry, stop conditions, and residual risk

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Never execute spend, publishing, bulk contact, deletion, access, or irreversible changes without explicit authorization.
- Do not let an AI agent approve its own high-impact action.
- Do not reuse an approval for a materially different scope, asset, budget, audience, or time period.
- Do not execute when backup, verification, or rollback requirements are unmet.

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
