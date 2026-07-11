---
name: project-asset-mapping
description: Use this skill when mapping connected provider accounts and assets such as sites, properties, ad accounts, pages, profiles, locations, CRM pipelines, and WordPress installations to the correct projects.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Project Asset Mapping

## Purpose

Prevent cross-project data leakage and incorrect analysis by creating an explicit, reviewable mapping between organizations, projects, connections, and provider assets.

## Inputs

- Project catalog and canonical domains
- Connected provider accounts and discovered assets
- Asset identifiers, names, URLs, time zones, currencies, and owners
- User and role permissions
- Known shared assets or cross-domain funnels

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Normalize the project identifier and canonical domain before mapping assets.
2. List all discoverable assets from each authorized connection without auto-assigning them.
3. Score candidate matches using exact domain, verified URL, account name, owner confirmation, and historical configuration.
4. Require human confirmation for ambiguous, shared, or high-impact assets.
5. Record primary, secondary, shared, historical, and excluded relationships.
6. Validate time zone, currency, attribution window, and conversion definitions for each mapping.
7. Produce a mapping diff whenever an assignment changes.

## Required output

Return a concise, decision-oriented result containing:

- Project-to-asset mapping table
- Confidence and evidence for every mapping
- Ambiguous or unmapped assets
- Shared-asset rules and data-isolation boundaries
- Approval requirements and mapping-change diff

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not map assets solely by similar names.
- Do not expose assets from one organization to another organization’s users.
- Do not silently remap assets after a provider renames an account.
- Do not merge currencies, time zones, or conversion definitions without explicit normalization.

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
