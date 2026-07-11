---
name: account-connection-planner
description: Use this skill when planning how users, organizations, and projects should connect external marketing, analytics, advertising, social, CRM, commerce, or website accounts without collecting provider passwords.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Account Connection Planner

## Purpose

Design a secure, least-privilege account connection plan that separates application login, provider authorization, project access, and production action rights.

## Inputs

- Organization, users, roles, and project list
- Providers and assets that must be connected
- Required read, prepare, and execute use cases
- Hosting, scheduler, encryption, and compliance constraints
- Existing OAuth clients, API approvals, service accounts, or connector plugins

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Separate sign-in to the product from authorization to third-party providers.
2. Inventory each provider, asset type, owner, account hierarchy, and required business outcome.
3. Choose the supported authorization pattern: OAuth authorization code, service account where explicitly supported, application password, signed webhook, or manual import.
4. Request read-only access first and use incremental authorization for additional capabilities.
5. Define token storage, refresh, revocation, connection health, audit logging, and account offboarding.
6. Map every connection to an organization and one or more projects; never infer ownership from an email domain alone.
7. Return an implementation sequence that starts with mock connectors and read-only production access.

## Required output

Return a concise, decision-oriented result containing:

- Connection inventory and provider matrix
- Authentication and authorization flow
- Required capabilities and least-privilege access mode
- Token-vault and revocation requirements
- Project mapping and role model
- Implementation phases, dependencies, and risks

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Never ask for or store a user’s primary Google, Meta, LinkedIn, or WordPress login password.
- Never put tokens, client secrets, application passwords, cookies, or private keys in a skill, prompt, log, example, or repository.
- Do not claim a provider supports a flow or permission without checking current official documentation.
- Do not enable write access merely because read access is available.

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
