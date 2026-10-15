# Workflow: Resume Progress

**Trigger:** `resume-progress`, `continue from checkpoint`.

## Procedure

1. Determine the project/task to resume. If unclear, ask which project; do not arbitrarily select a recent checkpoint from another project.
2. Read `10-projects/progress/<slug>.md`, the corresponding `10-projects/<slug>.md`, relevant application `AGENTS.md`, and linked project docs.
3. Inspect the actual repository state, changed files, and relevant code/tests before trusting the checkpoint. A saved note describes an earlier state, not a guaranteed current state.
4. Compare checkpoint claims with present evidence. Separate **still valid**, **changed/superseded**, and **unverified** items; surface conflicts clearly.
5. Present the current goal, next actions, and risks. `resume-progress` alone means **restore and verify context**, not blanket authorization for new code changes. Continue implementation only when the user also requested it or the prior task is unambiguously still authorized and low-risk; otherwise ask before editing.
6. After doing new authorized work, update the checkpoint when appropriate following [save-progress](save-progress.md); don't mark anything complete without evidence.

## Boundaries

`resume-progress` is not permission to discard user changes, change architecture, install dependencies, write to production, or deploy. If the saved checkpoint is absent, offer to onboard first; do not invent history. Preserve confidentiality boundaries.
