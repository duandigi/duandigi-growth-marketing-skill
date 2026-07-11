-- Reference schema for a MySQL-compatible Duandigi Growth OS implementation.
-- Store encrypted secrets in a dedicated vault. This schema stores opaque secret references only.

CREATE TABLE organizations (
  id VARCHAR(64) PRIMARY KEY,
  name VARCHAR(190) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
  id VARCHAR(64) PRIMARY KEY,
  email VARCHAR(190) NOT NULL UNIQUE,
  display_name VARCHAR(190) NULL,
  status ENUM('active','invited','disabled') NOT NULL DEFAULT 'active',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE organization_members (
  organization_id VARCHAR(64) NOT NULL,
  user_id VARCHAR(64) NOT NULL,
  role ENUM('owner','admin','strategist','operator','content','analyst','client') NOT NULL,
  PRIMARY KEY (organization_id, user_id),
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE projects (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  name VARCHAR(190) NOT NULL,
  canonical_domain VARCHAR(255) NULL,
  timezone VARCHAR(64) NOT NULL DEFAULT 'Asia/Ho_Chi_Minh',
  currency CHAR(3) NOT NULL DEFAULT 'VND',
  status ENUM('active','paused','archived') NOT NULL DEFAULT 'active',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  INDEX idx_projects_org (organization_id)
);

CREATE TABLE connections (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  provider VARCHAR(64) NOT NULL,
  provider_account_id VARCHAR(190) NULL,
  access_mode ENUM('observe','prepare','execute_with_approval') NOT NULL DEFAULT 'observe',
  status ENUM('pending','healthy','degraded','action_required','revoked','unavailable') NOT NULL DEFAULT 'pending',
  secret_reference VARCHAR(255) NULL,
  granted_capabilities JSON NULL,
  expires_at DATETIME NULL,
  last_refresh_at DATETIME NULL,
  last_successful_sync_at DATETIME NULL,
  created_by VARCHAR(64) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  revoked_at DATETIME NULL,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (created_by) REFERENCES users(id),
  INDEX idx_connections_org_provider (organization_id, provider),
  INDEX idx_connections_status (status)
);

CREATE TABLE project_asset_mappings (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NOT NULL,
  connection_id VARCHAR(64) NOT NULL,
  provider VARCHAR(64) NOT NULL,
  asset_type VARCHAR(64) NOT NULL,
  asset_id VARCHAR(255) NOT NULL,
  asset_name VARCHAR(255) NULL,
  relationship ENUM('primary','secondary','shared','historical','excluded') NOT NULL,
  status ENUM('proposed','confirmed','rejected','archived') NOT NULL DEFAULT 'proposed',
  confidence DECIMAL(5,4) NULL,
  evidence JSON NULL,
  filters_json JSON NULL,
  approved_by VARCHAR(64) NULL,
  approved_at DATETIME NULL,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (connection_id) REFERENCES connections(id),
  FOREIGN KEY (approved_by) REFERENCES users(id),
  UNIQUE KEY uq_mapping (project_id, connection_id, asset_type, asset_id, relationship),
  INDEX idx_mapping_project (project_id),
  INDEX idx_mapping_asset (provider, asset_type, asset_id)
);

CREATE TABLE sync_runs (
  id VARCHAR(64) PRIMARY KEY,
  connection_id VARCHAR(64) NOT NULL,
  asset_id VARCHAR(255) NULL,
  status ENUM('queued','running','succeeded','partial','failed') NOT NULL,
  started_at DATETIME NULL,
  completed_at DATETIME NULL,
  last_complete_period DATE NULL,
  rows_read BIGINT NOT NULL DEFAULT 0,
  rows_written BIGINT NOT NULL DEFAULT 0,
  error_class VARCHAR(64) NULL,
  error_summary TEXT NULL,
  FOREIGN KEY (connection_id) REFERENCES connections(id),
  INDEX idx_sync_connection_time (connection_id, started_at)
);

CREATE TABLE raw_data_batches (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NULL,
  connection_id VARCHAR(64) NOT NULL,
  asset_id VARCHAR(255) NULL,
  provider VARCHAR(64) NOT NULL,
  period_start DATE NULL,
  period_end DATE NULL,
  object_storage_reference VARCHAR(512) NOT NULL,
  payload_hash CHAR(64) NOT NULL,
  schema_version VARCHAR(32) NOT NULL,
  received_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (connection_id) REFERENCES connections(id),
  INDEX idx_raw_project_period (project_id, period_start, period_end)
);

CREATE TABLE normalized_metrics (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NOT NULL,
  connection_id VARCHAR(64) NULL,
  provider VARCHAR(64) NOT NULL,
  asset_id VARCHAR(255) NULL,
  channel VARCHAR(64) NOT NULL,
  object_type VARCHAR(64) NULL,
  object_id VARCHAR(512) NULL,
  metric_date DATE NOT NULL,
  metric_name VARCHAR(96) NOT NULL,
  metric_value DECIMAL(28,8) NOT NULL,
  unit VARCHAR(32) NOT NULL,
  currency CHAR(3) NULL,
  grain VARCHAR(32) NOT NULL DEFAULT 'daily',
  attribution_model VARCHAR(96) NULL,
  attribution_window VARCHAR(96) NULL,
  last_complete_period BOOLEAN NOT NULL DEFAULT TRUE,
  dimensions_json JSON NULL,
  quality_flags JSON NULL,
  source_lineage JSON NOT NULL,
  transformation_version VARCHAR(32) NOT NULL,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (connection_id) REFERENCES connections(id),
  INDEX idx_metrics_project_date (project_id, metric_date),
  INDEX idx_metrics_channel_metric (project_id, channel, metric_name, metric_date),
  INDEX idx_metrics_object (project_id, object_type, object_id(190), metric_date)
);

CREATE TABLE evaluation_cards (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NOT NULL,
  scope_json JSON NOT NULL,
  finding TEXT NOT NULL,
  severity ENUM('info','low','medium','high','critical') NOT NULL,
  confidence DECIMAL(5,4) NOT NULL,
  evidence_json JSON NOT NULL,
  competing_explanations JSON NULL,
  missing_data JSON NULL,
  business_impact TEXT NULL,
  recommended_next_step TEXT NOT NULL,
  approval_tier TINYINT NOT NULL DEFAULT 0,
  status ENUM('open','accepted','dismissed','converted_to_task','resolved') NOT NULL DEFAULT 'open',
  evaluation_period_start DATE NULL,
  evaluation_period_end DATE NULL,
  model_metadata JSON NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  INDEX idx_eval_project_status (project_id, status, severity)
);

CREATE TABLE approval_actions (
  id VARCHAR(64) PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NOT NULL,
  provider VARCHAR(64) NOT NULL,
  asset_id VARCHAR(255) NOT NULL,
  action_type VARCHAR(96) NOT NULL,
  scope_json JSON NOT NULL,
  approval_tier TINYINT NOT NULL,
  status ENUM('draft','pending','approved','rejected','expired','executing','verified','failed','rolled_back') NOT NULL DEFAULT 'draft',
  requested_by VARCHAR(64) NOT NULL,
  approved_by VARCHAR(64) NULL,
  expires_at DATETIME NULL,
  preconditions JSON NULL,
  preview_json JSON NULL,
  verification_json JSON NULL,
  rollback_json JSON NULL,
  limits_json JSON NULL,
  result_json JSON NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  FOREIGN KEY (requested_by) REFERENCES users(id),
  FOREIGN KEY (approved_by) REFERENCES users(id),
  INDEX idx_approval_project_status (project_id, status, approval_tier)
);

CREATE TABLE audit_log (
  id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  organization_id VARCHAR(64) NOT NULL,
  project_id VARCHAR(64) NULL,
  actor_type ENUM('user','agent','system','provider') NOT NULL,
  actor_id VARCHAR(190) NOT NULL,
  event_type VARCHAR(96) NOT NULL,
  object_type VARCHAR(96) NULL,
  object_id VARCHAR(255) NULL,
  event_json JSON NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (organization_id) REFERENCES organizations(id),
  FOREIGN KEY (project_id) REFERENCES projects(id),
  INDEX idx_audit_org_time (organization_id, created_at),
  INDEX idx_audit_object (object_type, object_id)
);
