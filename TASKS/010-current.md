# CURRENT TASK

- Requirement: REQ-001 — Historical Data Ingestion
- Rigidity: HARD
- Depends on: Q-001

## Goal
Implement REQ-001 per `spec/requirements.yml`.

## Acceptance (from ledger)
- At least one full season can be loaded and queried.
- Core entities (Driver, Constructor, Race, Season, Result) are persisted.
- Deterministic reload produces identical dataset state (given the same source + seed/config).

## Decision Gate
This task is **blocked** until Q-001 is resolved:
- Q-001: What is the official data source?

Record the decision in `spec/decisions.md` (and ADR if required).
