# Changelog

All notable changes to this project will be documented in this file.

<!-- towncrier release notes start -->

## [0.1.0] - 2026-02-27

### Added

- Initial repository and Python project scaffolding.
- FastAPI application entry point and API routing structure.
- Health endpoint (`/api/v1/health`).
- Health endpoint test coverage.
- `pyproject.toml` project configuration with setuptools `src/` layout.
- Towncrier changelog tooling configuration.

### Changed

- Refactored source tree to `src/f1model` package layout.
- Updated imports to package-qualified `f1model.*` paths.
- Migrated dependency source of truth to `pyproject.toml`.
- Expanded `.gitignore` for local cache and packaging artifacts.

### Fixed

- Corrected API mounting and typing issues during initial app wiring.
