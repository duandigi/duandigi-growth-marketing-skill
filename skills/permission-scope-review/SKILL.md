---
name: permission-scope-review
description: Use this skill when reviewing OAuth scopes, API permissions, WordPress roles, service-account access, or connector capabilities for least privilege, user trust, and staged read or write access.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Permission Scope Review

## Purpose

Minimize access risk while preserving the exact capabilities required for analysis, preparation, and approved execution.

## Inputs

- Provider, use case, and requested scopes or permissions
- Current official provider documentation
- Connection access mode: observe, prepare, or execute with approval
- Data sensitivity, retention, and organizational role requirements

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Translate every requested scope into a concrete user-facing capability.
2. Remove scopes that do not support an active use case.
3. Prefer read-only variants and incremental authorization when available.
4. Identify sensitive, restricted, app-review, developer-token, or business-verification requirements.
5. Separate provider permission from application-level role and project authorization.
6. Document re-consent, revocation, token expiry, and degraded-mode behavior.
7. Return a minimal scope set with an explicit justification for each item.

## Required output

Return a concise, decision-oriented result containing:

- Requested-versus-required scope table
- Minimal recommended permission set
- Provider review or verification dependencies
- Read, prepare, and execute capability boundaries
- User-facing consent explanation

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Use current official provider documentation for permission names and requirements.
- Do not request write, messaging, publishing, or ad-management permissions for reporting-only use cases.
- Do not treat an access token as proof that the user is authorized inside the application.
- Do not hide broad permissions behind vague consent copy.

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
