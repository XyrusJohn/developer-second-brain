# Knowledge Conventions

The vault should be a **retrievable, evidence-backed working memory**, not an archive of every AI conversation and terminal log.

## Classification and ownership

- **00-inbox:** Unsorted ideas or learning to triage later.
- **10-projects:** Short project summaries and active task checkpoints. The **project repo** owns code, full specifications, docs, ADRs, and tests.
- **20-areas:** Long-running development and learning responsibilities.
- **30-resources:** General reusable concepts, patterns, and research.
- **40-archive:** Completed/inactive material; not automatically current advice.
- **playbook:** Reviewed, broadly applicable engineering guidance and templates.
- **workflows:** Instructions for knowledge acquisition, retrieval, and maintenance.

Do not create copies of whole `docs/` directories inside the vault. Use a short source link and summary instead. Avoid special folder schemes imposed on existing projects.

## Project independence and portability

- Reusable playbooks, templates, workflows, and general resources must not embed any one real project's identity, framework, local filesystem path, or business rules as defaults.
- Generic examples and placeholders are allowed when explicitly labeled as illustrative; they never describe the user's actual codebase.
- Determine each project's structure, language(s), libraries, deployment environment, and documentation from evidence gathered during its own onboarding.
- Each `10-projects/` record may contain verified project-specific details, if privacy rules permit. This is intentionally different from reusable global guidance.
- Keep the project's authoritative documentation in that project's repository; use short summaries and verified links in the vault. Never impose one framework or folder layout on unrelated projects.

## Evidence quality

When relevant, include metadata such as:

```yaml
---
status: verified    # verified | documented-only | proposed | unverified | deprecated
last-reviewed: YYYY-MM-DD
scope: project
---
```

- **Verified:** Inspected source, tests actually executed, or other direct supporting evidence (specify which).
- **Documented only:** Existing docs describe the behavior, but no implementation confirmation was obtained.
- **Proposed:** An idea not yet approved or implemented.
- **Unverified:** Open claim or unclear coverage.
- **Deprecated:** Historical information not to be treated as current.

Dates are review timestamps, **not** automatic proof of freshness. Distinguish implementation facts from user requirements, plans, and AI recommendations. If a statement conflicts with code or authoritative specs, explain the conflict rather than choosing silently.

## Preservation rules

1. [Onboarding](../workflows/project-onboarding.md) saves permitted, verified project knowledge by default unless explicitly read-only.
2. [Everyday development](../workflows/development-lifecycle.md) reads relevant memory when useful; selectively persists meaningful **verified changes** only if storage is already authorized.
3. [Save progress](../workflows/save-progress.md) creates a distinct task checkpoint. It does not imply a Git commit or backup of the code.
4. [Sync knowledge](../workflows/sync-knowledge.md) does an intentional deeper comparison of stored claims with project evidence.
5. [Brain status](../workflows/brain-status.md) only inspects; it never writes or adjusts timestamps.
6. Before updating a file, inspect existing human notes and preserve useful context. Link primary code/docs using paths verified from the file location.
7. Avoid storing company-owned data outside authorized boundaries, credentials, personal records, large source excerpts, or transient outputs. Ask about confidentiality when unsure.
8. Keep focused notes in professional English; use `kebab-case.md` except conventional `README.md`, `AGENTS.md`.

## When *not* to write

Do not update the vault for trivial changes (formatting, UI colors), speculative bugs without evidence, read-only audits, routine shell commands, or unchanged content. Do not create placeholder note files just to satisfy a folder structure.

## Proof of persistence

A write workflow only succeeds when the agent **saves, reopens, and verifies** the intended note. Report the exact path and what was saved. If the path is unavailable or access is denied, report the blocker; a chat summary is not persistent memory.
