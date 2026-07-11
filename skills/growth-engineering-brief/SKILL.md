---
name: growth-engineering-brief
description: Use this skill when translating a growth hypothesis into an implementation-ready brief for a landing page, free tool, calculator, onboarding change, tracking event, CRM automation, referral mechanism, integration, or WordPress change.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Engineering Brief

## Purpose

Bridge growth strategy and safe technical execution with measurable acceptance criteria.

## Inputs

- Approved hypothesis and experiment design
- Current system and constraints
- Tracking requirements
- Security, privacy, accessibility, rollback, and approval rules


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Define the user problem, target behavior, and experiment mechanism.
2. Describe scope, non-scope, user flow, states, content, data, and integrations.
3. Specify analytics events, properties, identity rules, consent, and QA queries.
4. Define acceptance criteria for function, tracking, accessibility, performance, and SEO where relevant.
5. List failure modes, security concerns, data retention, and platform-policy constraints.
6. Design feature flags, backups, rollback, and approval checkpoints.
7. Return an implementation brief; do not execute production changes unless separately authorized.


## Required output

Return a concise, decision-oriented response containing:

- Problem and hypothesis
- Functional scope
- User flow
- Data and tracking
- Acceptance criteria
- Risks
- Launch and rollback plan


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Writing code before requirements and tracking are clear
- Storing secrets in the brief
- Shipping without rollback

- Claim guaranteed growth or present an estimate as observed fact.
- Recommend spam, fake reviews, impersonation, deceptive urgency, dark patterns, policy evasion, or unauthorized production changes.
- Hide material uncertainty, tracking limitations, or possible harm.

When an action can spend money, publish content, contact people, change production systems, delete data, or alter access, produce a plan and request explicit authorization rather than executing automatically.

## Completion check

Before finishing, verify that the output:

- answers a specific growth decision;
- uses the supplied business context;
- separates evidence from assumptions;
- defines a measurable next step;
- includes risks, constraints, and missing data;
- is no longer than necessary for the decision.
