# WORKFLOW_OPERATING_MANUAL.md
# F1 Oracle – AI Workflow Operating Manual (Private)

This file is for the repository owner only.
It documents how to operate Tutor, Conductor, and Secretary modes correctly.

---

## Core State Files

The system relies on:

- spec/requirements.yml
- TASKS/010-current.md
- spec/decisions.md
- AI_RULES.md
- AI_ROLES/*

Never bypass these files when running the workflow.

Verification policy:
- Assistants must run tests using `./.venv/bin/python -m pytest -q`.
- Assistants must return raw stdout/stderr (no summarizing).

---

# ROLE USAGE GUIDE

## 1. Conductor Mode (Task Engine Control)

Use when:
- Starting a session
- Checking task status
- Advancing tasks
- Triggering Decision Gates

Prompt template:

"You are in Conductor Mode.
Evaluate the current task state and proceed according to the task engine rules.
Do not implement any code."

If blocked:
- It will generate a Decision Gate.
- You choose an option.
- It records the decision.
- Task becomes unblocked.

If done:
- It runs verification.
- Marks REQ done.
- Advances to next REQ.

---

## 2. Tutor Mode (Diagnosis Only)

Use when:
- Tests fail
- You’re confused
- Something behaves unexpectedly

Prompt template:

"You are in Tutor Mode.
Here is the failing output and relevant files.
Diagnose only.
Do not implement code."

Expected response:
1. Restate goal (active REQ)
2. Describe failure
3. Classify root cause
4. Explain minimal concept
5. Propose micro-experiment
6. Provide verification command

Tutor must not write implementation code unless explicitly requested.

---

## 3. Secretary Mode (Bookkeeping + Git)

Use when:
- A REQ is completed
- Decision is finalized
- You want commit prepared
- You want release recommendation

Prompt template:

"You are in Secretary Mode.
Update bookkeeping and prepare commit according to AI_RULES.md.
Do not modify src/ or tests/."

Secretary may:
- Update spec/requirements.yml status
- Update spec/decisions.md
- Update changelog
- Prepare commit message

Secretary must not change implementation code.

---

# Session Flow

1) Conductor: What’s next?
2) Implement manually.
3) Tutor if stuck.
4) Conductor to verify.
5) Secretary to commit.

---

# Hard Boundary Reminder

Any change affecting:
- Folder structure
- Schema
- API contract
- Reproducibility
- Backtesting protocol

Requires a Decision Gate entry first.

---

# Philosophy

- Architecture > Speed
- Determinism > Cleverness
- Explicit Decisions > Implicit Drift
- Learning > Automation

The AI is a disciplined collaborator, not an autonomous coder.
