# ADR 0001: Project Architecture and Packaging Baseline

- Status: Accepted
- Date: 2026-02-27

## Context

This repository started as an empty project folder and was incrementally built into a FastAPI service with tests.
As the project evolved, import path consistency and packaging standards became key concerns.
The project needed a clear, professional structure that is easy to explain to reviewers and maintain over time.

## Decision

We adopt the following baseline architecture:

1. Source code lives under a `src/` layout.
2. The application package is `f1model` (`src/f1model/...`).
3. Imports use package-qualified paths (for example, `from f1model.main import app`).
4. Project metadata and dependency configuration are managed in `pyproject.toml`.
5. The project is installed in editable mode during development (`pip install -e ".[dev]"`).
6. Changelog management is handled with Towncrier using fragment files in `changelog.d/`.

## Consequences

### Positive

- Import behavior is consistent between tests, local execution, and tooling.
- The project follows modern Python packaging conventions.
- Tooling configuration is centralized in `pyproject.toml`.
- Changelog updates are easier to maintain and less error-prone.
- Architecture decisions are explicit and easier to communicate to employers/reviewers.

### Negative

- Slightly more setup overhead for contributors unfamiliar with `pyproject.toml` and editable installs.
- Release workflow now includes Towncrier fragment discipline.

## Notes

- Future ADRs should be added in this folder with increasing numeric prefixes:
  - `docs/adr/0002-...`
  - `docs/adr/0003-...`
