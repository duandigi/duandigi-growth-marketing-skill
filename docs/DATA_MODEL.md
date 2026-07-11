# Unified marketing data model

The canonical layer must support drill-down from portfolio to business outcome without pretending that provider metrics are identical.

## Core hierarchy

```text
organization → project → connection → provider account → asset
portfolio → project → channel → campaign/content/location → landing page → conversion → qualified outcome → revenue
```

## Evidence layers

Keep these separate:

1. **Provider-reported:** clicks, spend, platform-attributed conversions.
2. **Analytics-observed:** sessions, events, source/medium, landing-page behavior.
3. **CRM-qualified:** qualified leads, stage progression, wins, loss reasons.
4. **Business-confirmed:** booked work, invoiced revenue, margin, repeat, refund.
5. **Experiment evidence:** randomized, holdout, phased rollout, or before-after results.

## Canonical metric requirements

Every normalized record should identify:

- organization and project;
- provider, connection, asset, channel, and object;
- date/time boundary and time zone;
- metric name, value, unit, currency, and grain;
- source update time and last-complete-period status;
- attribution model/window where relevant;
- transformation version, lineage, and quality flags.

Never sum reach or users across platforms as deduplicated people. Never sum platform-attributed conversions as unique business outcomes.
