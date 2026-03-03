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
Q-001 has been resolved:
- Official data source: Jolpica API
- Decision reference: `DEC-2026-03-03-001`
- ADR reference: `docs/adr/0002-jolpica-canonical-reference-source.md`
