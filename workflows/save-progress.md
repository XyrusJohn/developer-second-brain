# Workflow: Save Progress

**Trigger:** `save-progress`, `checkpoint`.

**Success condition:** Current task state is written to `10-projects/progress/<slug>.md` or a concrete write/permission blocker is reported.

## Procedure

1. Identify the active project and actual task from the conversation and available workspace. If several projects or tasks are active and none is clear, ask which one to checkpoint.
2. Read the current `10-projects/<slug>.md` and existing checkpoint if present. Do not erase older relevant pending items or verified context.
3. Review available evidence (changed files, relevant test output, issue notes, task history, Git status **only if the repository is a Git repository**). Never assume a test passed just because code exists.
4. Update `10-projects/progress/<slug>.md` using the [progress template](../playbook/templates/progress.template.md). Record timestamp/date, current objective, verified completed work, work in progress, blockers, decisions, checks actually run, next concrete actions, and important source links.
5. If a previously recorded item is obsolete, mark it superseded or resolved with explanation; avoid uncontrolled log growth. Preserve significant prior decisions in the project docs or link to them.
6. Reopen the written file to confirm it exists and is readable; report exact location and remaining unknowns.

## Boundaries

- The command authorizes **only vault knowledge updates**, not source code, project docs, Git commits/pushes, or deployments. An ordinary development task does **not** trigger `save-progress` automatically; this remains an explicit checkpoint.
- Do not copy secrets, personal data, or unapproved confidential materials. Ask before storing sensitive work details outside the owning repo.
- If nothing was implemented or verified, say so and save only the real checkpoint, not invented progress.
- If the user explicitly says read-only or do not save, report a suggested checkpoint in chat without writing.
