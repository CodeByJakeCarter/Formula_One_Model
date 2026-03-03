# Decisions Log (Decision Gates)

This file records decisions made when a task hits ambiguity or crosses an architectural boundary.
Keep entries short, specific, and link them to REQ/Q IDs.

## Policy
- Any decision affecting **folder structure**, **entity schema**, **API contract**, or **reproducibility guarantees** must be recorded here (and promoted to an ADR if you maintain ADRs).
- SOFT decisions (tuning, heuristics) can be recorded here without requiring an ADR unless they later impact architecture.

---

## Template

### DEC-YYYY-MM-DD-###: <short title>
- Date: YYYY-MM-DD
- Related: REQ-###, Q-###
- Type: HARD / SOFT
- Context: <1–3 sentences>
- Options considered:
  1) <option>
  2) <option>
  3) <option>
- Decision: <chosen option>
- Rationale: <why>
- Consequences:
  - <what this enables>
  - <what this constrains>
- Verification: <how we know this decision works>
- Notes: <optional>

---

## Entries

### DEC-2026-03-03-001: Official Data Source Selection
- Date: 2026-03-03
- Related: REQ-001, Q-001
- Type: HARD
- Context: REQ-001 cannot proceed without a single official historical data source. The source determines ingestion schema assumptions, reproducibility behavior, and migration design.
- Options considered:
  1) Ergast/Jolpica API lineage as canonical source.
  2) FastF1-derived datasets as canonical source.
  3) Maintained static dataset snapshot in-repo as canonical source.
- Decision: Use Jolpica API (Ergast-compatible) as the canonical source.
- Rationale: Jolpica satisfies the required historical F1 reference dataset shape and is already accepted in ADR 0002, allowing REQ-001 to proceed with a consistent source of truth.
- Consequences:
  - REQ-001 is unblocked.
  - Ingestion implementation proceeds against Jolpica as canonical provider.
- Verification: Q-001 status is set to resolved in `spec/requirements.yml` and ADR 0002 remains consistent with this decision.
- Notes: ADR reference: `docs/adr/0002-jolpica-canonical-reference-source.md`.
