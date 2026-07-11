---
name: social-channel-analysis
description: Use this skill when analyzing organic or paid social performance across content, formats, topics, creators, pages, profiles, audiences, reach, engagement, traffic, leads, assisted outcomes, and content operations.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Social Channel Analysis

## Purpose

Determine which social activities create awareness, consideration, traffic, leads, retention, or referral rather than ranking posts by engagement alone.

## Inputs

- Platform content, profile, audience, reach, engagement, click, and video data
- Publishing cadence, format, topic, creator, campaign, and creative metadata
- Analytics, UTM, CRM, assisted-conversion, and revenue data
- Brand, moderation, platform-policy, and production constraints

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Define the role of each account and content pillar in the growth model.
2. Validate platform metrics, tracking links, attribution limitations, and content taxonomy.
3. Analyze reach quality, engagement quality, traffic, lead quality, assisted outcomes, follower or audience growth, and operational efficiency.
4. Drill down by format, topic, hook, CTA, creator, posting time, distribution method, and destination page.
5. Detect fatigue, overreliance on vanity engagement, weak message-match, inconsistent cadence, and content that assists later conversion.
6. Separate organic learning from paid amplification effects.
7. Recommend content experiments, distribution changes, repurposing, landing-page alignment, or measurement fixes.

## Required output

Return a concise, decision-oriented result containing:

- Social channel role and health summary
- Content-pillar, format, topic, and CTA findings
- Awareness, traffic, lead, and assisted-outcome analysis
- Operational and measurement constraints
- Prioritized content and distribution experiments

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not treat likes, comments, or followers as business outcomes without context.
- Do not recommend fake engagement, impersonation, unsolicited bulk messaging, or policy evasion.
- Do not compare platform reach as if it represented deduplicated people across networks.
- Do not attribute later branded search entirely to social without evidence.

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
