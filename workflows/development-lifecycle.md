# Workflow: Everyday Context and Selective Knowledge Maintenance

**Activation:** Applies during ordinary software engineering tasks **after** the AI agent has loaded the project's Second Brain connection or was explicitly instructed to read the vault. This workflow is a *behavioral instruction*, not a daemon, file watcher, or post-commit hook.

## 1. Identify the task before retrieving

1. Determine the specific project and scope. For a multi-project workspace, do not guess which app is being modified.
2. Read applicable project instructions (`AGENTS.md`) and any project-specific requirements.
3. Find the existing project note in `10-projects/` using its recorded project identity/path, **not only its filename**; check for collisions. If absent, do not silently create an extensive new audit. Onboard when requested, or propose onboarding if it will materially help.
4. Read only the task-relevant portions of that note, an active checkpoint (if relevant), and a few linked authoritative docs or relevant playbook entries. **For a trivial task, the project instructions and code may suffice.** Do not load every note.

## 2. Re-establish current truth

- Verify important boundaries, APIs, schemas, behaviors, dependency versions and assumptions against current source, manifests, tests and project-owned docs.
- Treat saved notes as clues, **not** live truth. If stale or contradictory, state the discrepancy and use relevant authoritative evidence to resolve what can be resolved.
- Observe user approvals and project safety/security rules. No automatic repo-wide audits.

## 3. Perform the requested development task

- Make only requested, authorized edits; report actual tests and outcomes.
- Do not change project source, tests, requirements, or deployment merely because an old note recommends a different architecture.

## 4. Decide whether to persist **meaningful** new knowledge

**Candidate knowledge to save when verified and authorized:**

- A materially changed architecture boundary or runtime dependency.
- Approved changes to API contracts, data schemas, storage or authentication flows.
- Security-relevant invariants or important business rules.
- A reproduced bug root cause and lasting regression prevention.
- Significant changes to setup, deployment constraints, or system behavior that affect future work.

**Do not save by default:** formatting, one-off terminal logs, temporary experiments, routine UI polish, already-documented facts, unverified claims as fact, or notes with no future retrieval value.

**Before writing**, all gates must pass:

1. The user's request is not read-only and project knowledge maintenance is already authorized (for example by approved onboarding/connection and the vault's privacy classification). If not, propose the update or ask once.
2. The change is material and supported by actually inspected evidence. If only a hypothesis, save as clearly unverified only when requested/appropriate.
3. The target vault is writable and the information is permitted to leave the application repository. Private/public Git visibility is not sufficient authorization for company data.
4. Read the existing note and identify the smallest merge. Never replace unrelated project memory.

When gates pass, make a small, scoped update to `10-projects/<slug>.md`; update source links and review coverage, reopen the saved note to verify; report the changed path. If no material change, **do not write**. An ordinary development task does not, by itself, require `save-progress` or broad `sync-knowledge`.

## 5. Checkpoints, conflicts, and failures

- `save-progress` is an explicit checkpoint for active tasks; use [that workflow](save-progress.md).
- If important knowledge is contradicted, correct the verified claim and retain meaningful historical decision context; mark other claims uncertain pending verification.
- If access, confidentiality, scope, or permissions are unclear, stop only the *knowledge-write* part and explain the blocker; don't claim auto-save worked.
- Do not modify canonical application docs or code as a side effect of the knowledge-maintenance step.

## Token efficiency

Targeted retrieval can reduce repeated exploration, but reading notes costs context tokens and may not improve usage for small tasks. Avoid mandatory full-vault reads and needless writes.
