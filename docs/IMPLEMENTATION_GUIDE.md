# Integration implementation guide

The repository is integration-ready but intentionally does not ship production OAuth credentials or provider-specific write adapters.

## Recommended implementation order

1. Application users, organizations, projects, and roles
2. Connection registry and encrypted secret references
3. Mock connector and provider capability registry
4. Google Search Console and GA4 read-only collectors
5. Project-to-asset mapping
6. Raw storage, normalization, and data-quality checks
7. Channel dashboards and AI evaluation
8. Approval queue and audit log
9. WordPress draft-only connector
10. Paid-media and social read-only connectors
11. Narrow execution adapters after provider review and real-world testing

## Shared-hosting deployment

A PHP/MySQL dashboard may run on shared hosting. Lightweight collectors can run with hosting cron or an external scheduler. Claude Code can perform local analysis and prepared changes while the computer is online. Real-time AI evaluation on the website requires an AI API or an always-on model runner.

## Mock-first rule

Every connector must pass the shared contract and tests against sanitized mock payloads before it is authorized against a real account.
