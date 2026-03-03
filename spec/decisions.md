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

### DEC-2026-03-03-001: Official Data Source Selection Pending
- Date: 2026-03-03
- Related: REQ-001, Q-001
- Type: HARD
- Context: REQ-001 cannot proceed without a single official historical data source. The source determines ingestion schema assumptions, reproducibility behavior, and migration design.
- Options considered:
  1) Ergast/Jolpica API lineage as canonical source.
  2) FastF1-derived datasets as canonical source.
  3) Maintained static dataset snapshot in-repo as canonical source.
- Decision: Pending user decision on Q-001.
- Rationale: No source has been formally selected yet; implementing ingestion before this choice would violate task-engine dependency rules.
- Consequences:
  - REQ-001 remains blocked.
  - Implementation and verification are deferred until Q-001 is resolved.
- Verification: Q-001 status changes from `open` to resolved and chosen source is recorded.
- Notes: If chosen source changes API contract or reproducibility guarantees, promote to ADR per repository policy.
