# Migration from v0.1 to v0.2

## Compatibility

The original 12 skill names remain unchanged. Their metadata version is updated to `0.2.0`, so existing direct invocations should continue to work.

## New workflow order

Before using growth or channel conclusions with live data, add these gates:

1. `account-connection-planner`
2. `project-asset-mapping`
3. `connection-health-monitor`
4. `marketing-data-quality-audit`
5. `cross-channel-data-normalization`
6. channel-specific analysis
7. `ai-marketing-evaluator`
8. `action-approval-planner`

## Required application changes

Production implementations should add organization and project isolation, connection metadata, encrypted secret references, asset mappings, raw data storage, normalized records, evaluation cards, approval records, and audit logs.

Do not migrate credentials into this repository. Existing tokens should stay in the deployed system's vault and be referenced only by opaque secret identifiers.
