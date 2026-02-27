# ADR 0002: Use Jolpica (Ergast-Compatible) as Canonical Reference Source

- Status: Accepted
- Date: 2026-02-27

## Context

The project requires structured historical Formula 1 reference data (drivers, races, results).

The original Ergast API is being deprecated and is no longer a reliable long-term dependency.

We need a stable, structured, publicly accessible data source.

The backend must remain decoupled from any single provider.

## Decision

Use Jolpica's Ergast-compatible API endpoint as the initial canonical reference data source.

Treat Jolpica as an ingestion provider only.

Persist all ingested data in the local database.

Store external identifiers (for example, `jolpica_driver_id`) for mapping and synchronization.

Do not couple internal schema directly to external response formats.

## Rationale

Jolpica preserves the familiar Ergast data shape.

It enables rapid bootstrapping of historical data.

Using an ingestion boundary prevents hard vendor lock-in.

Storing external IDs avoids fragile name-based matching.

## Consequences

### Positive

- Quick access to structured F1 historical data.
- Clear adapter boundary for future provider swaps.
- Portfolio-grade architectural decoupling.

### Negative / Risks

- Dependency on a volunteer-maintained service.
- Potential downtime or rate limits.
- Future provider swap will require adapter implementation.

### Mitigation

- Persist data locally.
- Design ingestion through a provider abstraction.
- Avoid runtime dependency on Jolpica availability.
