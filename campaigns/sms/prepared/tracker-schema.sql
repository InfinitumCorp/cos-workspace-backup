-- Offline schema ONLY. No database instantiated and no real opt-outs supplied.
PRAGMA foreign_keys=ON;
CREATE TABLE consent_evidence (
 evidence_id TEXT PRIMARY KEY, e164 TEXT NOT NULL, evidence_path TEXT NOT NULL,
 evidence_sha256 TEXT NOT NULL, grant_timestamp_with_zone TEXT NOT NULL,
 disclosure_text TEXT NOT NULL, seller_scope TEXT NOT NULL,
 channel_scope TEXT NOT NULL, acquisition_method TEXT NOT NULL,
 verified_by TEXT NOT NULL, verified_at TEXT NOT NULL,
 current_number_ownership_checked_at TEXT NOT NULL,
 status TEXT NOT NULL CHECK(status IN ('verified','revoked','expired','needs_review'))
);
CREATE TABLE inbound_events (
 event_id TEXT PRIMARY KEY, gateway_id TEXT NOT NULL, e164 TEXT NOT NULL,
 received_at TEXT NOT NULL, ingested_at TEXT NOT NULL, raw_text TEXT NOT NULL,
 classification TEXT NOT NULL CHECK(classification IN ('optout','start_request','help','other','needs_review')),
 processed_at TEXT, evidence_path TEXT NOT NULL
);
CREATE TABLE suppressions (
 e164 TEXT PRIMARY KEY, status TEXT NOT NULL CHECK(status IN ('suppressed','review_hold')),
 reason TEXT NOT NULL, source_event_id TEXT REFERENCES inbound_events(event_id),
 effective_at TEXT NOT NULL, updated_at TEXT NOT NULL, operator TEXT NOT NULL,
 evidence_path TEXT NOT NULL
);
CREATE TABLE reconsent_reviews (
 review_id TEXT PRIMARY KEY, e164 TEXT NOT NULL, start_event_id TEXT REFERENCES inbound_events(event_id),
 new_consent_evidence_id TEXT REFERENCES consent_evidence(evidence_id),
 authorized_by TEXT, authorization_reference TEXT, decision TEXT NOT NULL CHECK(decision IN ('pending','denied','approved')),
 reviewed_at TEXT
);
-- START is a review request; it NEVER deletes suppression or changes consent automatically.
CREATE TABLE approval_records (
 approval_id TEXT PRIMARY KEY, kind TEXT NOT NULL CHECK(kind IN ('final_text','launch','budget')),
 actor TEXT NOT NULL, exact_words TEXT NOT NULL, transcript_reference TEXT NOT NULL,
 scope_json TEXT NOT NULL, content_sha256 TEXT NOT NULL, approved_at TEXT NOT NULL,
 expires_at TEXT, revoked_at TEXT
);
CREATE TABLE sync_checkpoints (
 gateway_id TEXT PRIMARY KEY, provider_cursor TEXT, fetched_at TEXT NOT NULL,
 processed_through TEXT NOT NULL, unresolved_count INTEGER NOT NULL CHECK(unresolved_count>=0)
);
CREATE TABLE delivery_ledger (
 idempotency_key TEXT PRIMARY KEY, e164 TEXT NOT NULL, wave INTEGER NOT NULL,
 message_sha256 TEXT NOT NULL, gateway_id TEXT NOT NULL,
 provider_quota_date TEXT NOT NULL, carrier_quota_date TEXT NOT NULL,
 units_reserved INTEGER NOT NULL, segments INTEGER NOT NULL,
 state TEXT NOT NULL CHECK(state IN ('reserved','submitted','delivered','failed','unknown','cancelled')),
 provider_message_id TEXT UNIQUE, last_update TEXT NOT NULL,
 consent_evidence_id TEXT NOT NULL REFERENCES consent_evidence(evidence_id),
 approval_id TEXT NOT NULL REFERENCES approval_records(approval_id)
);
-- Future transport must transactionally check suppression/consent/sync and reserve quota
-- immediately before submission. Unknown delivery status is held, NEVER retried blindly.
