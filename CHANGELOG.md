# Changelog

## 0.1.2 - 2026-08-22

### Changed

- Replaced the package-local CLI tree renderer with ChatStyle's registered Click tree runtime.
- Added the top-level `chattree --tree-brief` contract alongside `--version` and `--tree`.
- Required bounded Click and `chatstyle>=0.2.0,<0.3.0`; ChatEnv remains absent because the package has no env/profile/config behavior.
- Expanded tests, bilingual docs, and CI to verify editable and built-wheel CLI contracts.

## 0.1.1 - 2026-08-12

### Changed

- Added generated root-only `chattree --tree` from the Click command surface.
- Added bilingual MkDocs docs, CLI tree pages, Preview Docs, Deploy Docs, CI docs gate, and workflow/docs contract tests.
- Removed unused direct ChatStyle/ChatEnv runtime dependencies; future config or interactive commands should add bounded dependencies when needed.

## 0.1.0 - 2026-07-05

### Added

- First real ChatTree release through GitHub Actions and PyPI Trusted Publisher.

## 0.0.1 - 2026-07-05

### Added

- Placeholder release to reserve the PyPI project name before Publisher setup.
