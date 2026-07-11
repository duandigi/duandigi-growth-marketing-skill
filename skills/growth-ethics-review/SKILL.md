---
name: growth-ethics-review
description: Use this skill when reviewing a growth idea, experiment, automation, message, incentive, tracking plan, or loop for manipulation, spam, privacy, accessibility, discrimination, brand, legal, or platform-policy risk.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Ethics Review

## Purpose

Protect durable growth by rejecting tactics that create hidden harm or unmanageable risk.

## Inputs

- Proposed tactic or experiment
- Target audience and channel
- Data collected and permissions
- Incentives, messaging, automation, and expected behavior


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Identify affected users, non-users, employees, partners, platforms, and communities.
2. Check informed choice, truthfulness, reversibility, privacy, accessibility, fairness, and data minimization.
3. Screen for spam, fake social proof, dark patterns, deceptive urgency, impersonation, policy evasion, and exploitative targeting.
4. Assess likely harm severity, likelihood, detectability, and reversibility.
5. Classify the proposal as approve, approve with controls, redesign, or reject.
6. Specify controls, disclosures, consent, rate limits, monitoring, and escalation paths.
7. Document the decision and unresolved legal or platform questions.


## Required output

Return a concise, decision-oriented response containing:

- Risk classification
- Affected parties
- Risk findings
- Required controls
- Decision
- Open questions


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Treating legal compliance as the only ethical standard
- Using consent buried in unclear language
- Optimizing short-term conversion at the expense of user autonomy

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
