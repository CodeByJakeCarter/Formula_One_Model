# CURRENT TASK

- Requirement: REQ-001 — Historical Data Ingestion
- Rigidity: HARD
- Depends on: Q-001

## Goal
Implement REQ-001 per `spec/requirements.yml`.

## Acceptance (from ledger)
- At least one full season can be loaded and queried.
- Core entities (Driver, Constructor, Race, Season, Result) are persisted.
- Deterministic reload produces identical dataset state (given the same source data + ingestion config).

## Decision Gate
Q-001 has been resolved:
- Official data source: Jolpica API
- Decision reference: `DEC-2026-03-03-001`
- ADR reference: `docs/adr/0002-jolpica-canonical-reference-source.md`

REQ-001 milestone definition has been fixed:
- Scope: full 2025 season coverage
- Reload behavior: idempotent rerun (no duplicates)
- Determinism: non-random ingestion; identical post-run dataset state with fixed source data + fixed config
- Decision reference: `DEC-2026-03-03-002`

Ingestion boundary placement has been fixed:
- Orchestration layer: `src/f1model/services/*`
- Persistence layer: `src/f1model/repositories/*`
- API route handlers are not ingestion orchestration
- Decision reference: `DEC-2026-03-03-003`
