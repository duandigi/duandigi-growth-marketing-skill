# Reference application API contract

This is a resource model for `marketing.duandigi.com`, not a production implementation.

## Authentication and organizations

- `GET /api/v1/me`
- `GET /api/v1/organizations`
- `GET /api/v1/organizations/{organizationId}/projects`

Every request is authorized by application session, organization membership, project access, and action capability. Provider access tokens are never returned to clients or AI agents.

## Connections

- `POST /api/v1/connections/{provider}/authorize` — begin provider authorization
- `GET /api/v1/connections/{connectionId}/callback` — provider callback handled by the server
- `GET /api/v1/connections` — list non-secret connection metadata
- `POST /api/v1/connections/{connectionId}/revoke`
- `POST /api/v1/connections/{connectionId}/health-check`
- `GET /api/v1/connections/{connectionId}/assets`

## Project asset mapping

- `GET /api/v1/projects/{projectId}/assets`
- `POST /api/v1/projects/{projectId}/asset-mappings`
- `PATCH /api/v1/asset-mappings/{mappingId}`
- `POST /api/v1/asset-mappings/{mappingId}/approve`

Mapping endpoints return confidence and evidence. Ambiguous or shared assets are not auto-confirmed.

## Data and synchronization

- `POST /api/v1/connections/{connectionId}/sync`
- `GET /api/v1/sync-runs/{syncRunId}`
- `GET /api/v1/projects/{projectId}/metrics`
- `GET /api/v1/projects/{projectId}/data-quality`

Metric responses include provider, channel, object, date grain, unit, currency, source lineage, last-complete-period status, and quality flags.

## AI evaluation

- `POST /api/v1/projects/{projectId}/evaluations`
- `GET /api/v1/projects/{projectId}/evaluations`
- `GET /api/v1/evaluations/{evaluationId}`
- `POST /api/v1/evaluations/{evaluationId}/convert-to-task`
- `POST /api/v1/projects/{projectId}/health-score`
- `POST /api/v1/portfolio/executive-summary`

Evaluation requests must reference a validated data snapshot and evaluation period. Responses follow `schemas/evaluation-card.schema.json`.

## Approvals and execution

- `POST /api/v1/approval-actions`
- `POST /api/v1/approval-actions/{actionId}/approve`
- `POST /api/v1/approval-actions/{actionId}/reject`
- `POST /api/v1/approval-actions/{actionId}/execute`
- `POST /api/v1/approval-actions/{actionId}/verify`
- `POST /api/v1/approval-actions/{actionId}/rollback`

The server must check exact organization, project, provider, asset, action, limits, approver role, expiry, preconditions, and current connection capability at execution time. Approval does not bypass provider authorization or application role checks.

## Errors

Use machine-readable classes such as:

- `connection_authorization_required`
- `connection_permission_missing`
- `asset_mapping_ambiguous`
- `data_period_incomplete`
- `data_quality_insufficient`
- `approval_required`
- `approval_expired`
- `execution_precondition_failed`
- `provider_rate_limited`
- `provider_schema_changed`

Never put secrets or personal lead data in an error response.
