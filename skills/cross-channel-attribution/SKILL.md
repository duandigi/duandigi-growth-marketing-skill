---
name: cross-channel-attribution
description: Use this skill when reconciling provider-reported, analytics-observed, CRM-sourced, assisted, first-touch, last-touch, and revenue-confirmed contributions across marketing channels.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Cross Channel Attribution

## Purpose

Support budget and strategy decisions without pretending that one attribution model reveals the full causal value of every channel.

## Inputs

- Provider attribution reports and windows
- Analytics journeys, source or medium, UTMs, and cross-domain data
- CRM source, stage, revenue, repeat, and offline outcome data
- Identity, consent, cookie, device, and privacy limitations
- Experiments, holdouts, geo tests, incrementality evidence, and brand demand indicators

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Document the business question and every attribution model being compared.
2. Reconcile metric definitions, windows, currencies, time zones, and deduplication rules.
3. Keep provider claims, analytics observations, CRM source, and business outcomes as separate evidence layers.
4. Analyze first touch, last touch, assisted sequences, time lag, branded demand, and offline conversion where available.
5. Identify double counting, dark traffic, missing UTMs, cross-device loss, walled-garden limits, and source overwrite.
6. Use incrementality evidence when available and label attribution as descriptive when it is not causal.
7. Return a decision range, confidence, and measurement-improvement plan rather than false precision.

## Required output

Return a concise, decision-oriented result containing:

- Attribution-model comparison and reconciliation
- Channel contribution ranges and confidence
- Double-counting, missingness, and identity limitations
- Business decisions supported and unsupported by the data
- Incrementality and measurement roadmap

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not sum platform-attributed conversions as unique conversions.
- Do not call last-click contribution causal impact.
- Do not remove awareness channels solely because they have low last-click revenue.
- Do not expose individual journey or identity data unnecessarily.

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
