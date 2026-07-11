# Architecture

Duandigi Growth Marketing Skills v0.2 separates reasoning from credentials and execution.

```text
User authentication and organization roles
                    ↓
Provider authorization and connection registry
                    ↓
Project ↔ asset mapping
                    ↓
Collectors / webhooks / manual imports
                    ↓
Raw immutable records + source metadata
                    ↓
Normalization and data-quality layer
                    ↓
Channel analysis + anomaly detection
                    ↓
Cross-channel AI evaluation and health scoring
                    ↓
Opportunity / experiment / alert / approval card
                    ↓
Human approval → external execution adapter
                    ↓
Verification, rollback, and learning
```

## Trust boundaries

1. Skills contain instructions, not secrets.
2. Connectors access provider APIs but should not decide strategy.
3. Normalization preserves raw source lineage and provider-specific meaning.
4. AI evaluators may recommend actions but do not receive direct production authority by default.
5. Approval and execution are distinct capabilities.
6. Every project and asset is isolated by organization and role.

## Access modes

- **Observe:** read, import, normalize, analyze, and report.
- **Prepare:** create drafts, previews, diffs, plans, and approval requests.
- **Execute with approval:** perform a narrowly approved action, then verify and log it.

There is intentionally no unrestricted autonomous mode.
