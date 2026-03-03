# Tasks

This folder is the local task engine driven by `spec/requirements.yml`.

## Conventions
- A single active task lives in `TASKS/010-current.md`.
- Backlog tasks live in `TASKS/backlog/`.
- Completed tasks may be moved to `TASKS/done/` (optional).

## How the assistant should operate
1) Read `spec/requirements.yml`.
2) Identify the first REQ with `status: todo` (or `in_progress` if present).
3) Ensure `TASKS/010-current.md` points to that REQ.
4) Run the verification commands/tests listed under that REQ when you claim completion.
5) Only then mark the REQ `done`, update bookkeeping, and advance to the next REQ.

## Status values
- todo
- in_progress
- blocked (use when depends_on includes open Qs)
- done
