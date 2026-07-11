# Duan Growth Skills

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-5B5BD6)](https://agentskills.io/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-111111)](https://code.claude.com/docs/en/skills)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)](CHANGELOG.md)

**Evidence-first Agent Skills for growth strategy, secure account integration, multi-channel data intelligence, AI evaluation, experimentation, approval, and ethical optimization.**

Duan Growth Skills helps AI agents move through a complete operating cycle:

> connect → map → validate → normalize → analyze → evaluate → experiment → approve → verify → learn

The project follows the open Agent Skills structure and includes portable skills, optional Claude Code agents, deterministic Python utilities, JSON contracts, mock connectors, examples, evals, and a community testing protocol.

[Đọc README tiếng Việt](README.vi.md)

## What v0.2 adds

Version 0.2.0 expands the original growth reasoning toolkit into an integration-ready multi-channel intelligence layer:

- account connection and least-privilege planning;
- explicit project-to-asset mapping;
- connection-health and data-quality gates;
- canonical cross-channel data contracts;
- SEO, paid media, social, local search, and CRM analysis;
- anomaly detection, attribution reconciliation, and explainable health scores;
- AI evaluation cards and executive growth reviews;
- bounded action approval with verification and rollback;
- mock connectors that require no real account or credential.

## Included skills — 30

### Growth strategy and experimentation

`growth-model-design`, `growth-funnel-analysis`, `growth-opportunity-finder`, `growth-experiment-design`, `growth-experiment-prioritization`, `growth-experiment-analysis`, `growth-loop-design`, `growth-metrics-diagnosis`, `growth-portfolio-management`, `growth-retrospective`, `growth-engineering-brief`, `growth-ethics-review`

### Integration and data intelligence

`account-connection-planner`, `project-asset-mapping`, `permission-scope-review`, `connection-health-monitor`, `marketing-data-quality-audit`, `cross-channel-data-normalization`

### Channel and AI evaluation

`ai-marketing-evaluator`, `channel-performance-audit`, `seo-channel-analysis`, `paid-media-analysis`, `social-channel-analysis`, `local-search-analysis`, `crm-funnel-analysis`, `marketing-anomaly-detection`, `cross-channel-attribution`, `marketing-health-scoring`, `executive-growth-summary`, `action-approval-planner`

## What this repository does not contain

- real access tokens, refresh tokens, passwords, cookies, private keys, or OAuth client secrets;
- production OAuth applications or provider approvals;
- unrestricted autonomous publishing, spending, messaging, deletion, or access changes;
- a guarantee that provider APIs, permissions, or metrics will remain unchanged.

Skills define reasoning and operating contracts. Real account access requires a separately deployed application, provider authorization, encrypted secret storage, collectors, scheduler, and approved execution adapters.

## Architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/AUTHENTICATION_AND_OAUTH.md`](docs/AUTHENTICATION_AND_OAUTH.md), and [`docs/AI_EVALUATION.md`](docs/AI_EVALUATION.md).

```text
Provider accounts → connections → asset mapping → collectors
→ raw data → normalization → data-quality gate
→ channel analysts → cross-channel AI evaluation
→ opportunity / alert / experiment / approval
→ human authorization → execution adapter → verification
```

## Install

### Claude Code plugin

After publication:

```text
/plugin marketplace add duandigi/duandigi-growth-marketing-skill
/plugin install duandigi-growth-marketing-skill@duan-growth
```

Local test:

```bash
claude --plugin-dir ./duandigi-growth-marketing-skill
```

Example commands:

```text
/duandigi-growth-marketing-skill:account-connection-planner
/duandigi-growth-marketing-skill:ai-marketing-evaluator
/duandigi-growth-marketing-skill:seo-channel-analysis
/duandigi-growth-marketing-skill:action-approval-planner
```

### Other Agent Skills-compatible clients

Copy selected folders from `skills/` into the client’s supported skills directory.

## Run the integration-ready demo

```bash
python scripts/validate_connections.py examples/multi-channel/mock-connection.json
python scripts/mock_connector.py list-assets examples/multi-channel/mock-connection.json
python scripts/mock_connector.py fetch examples/multi-channel/mock-connection.json
python scripts/normalize_marketing_data.py examples/multi-channel/mock-provider-data.json
python scripts/calculate_health_score.py examples/multi-channel/health-score-input.json
python scripts/detect_anomalies.py examples/multi-channel/anomaly-input.json
```

## Validate the repository

```bash
make validate
```

Validation checks skill metadata, eval coverage, unit tests, provider registry, examples, JSON contracts, and generated catalog.

## Security model

- read-only by default;
- secrets remain outside the repository and prompts;
- every asset is mapped to an organization and project;
- connection and data health gate downstream evaluation;
- high-impact actions require named human approval;
- approvals are scoped, expiring, logged, verifiable, and reversible where possible.

Read [`SECURITY.md`](SECURITY.md) and [`docs/APPROVAL_MODEL.md`](docs/APPROVAL_MODEL.md).

## Community evaluation

Use [`benchmarks/README.md`](benchmarks/README.md) to compare runs with and without a skill. Report both improvements and failures. Real-world sanitized cases, provider adapters, metric-definition tests, and non-SaaS examples are welcome.

## License

MIT. See [`LICENSE`](LICENSE). Provider names and APIs remain subject to their own terms and policies.

## Maintainer

Created by **Duan Digi** — [duandigi.com](https://duandigi.com)
