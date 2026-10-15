# Developer Second Brain — Agent Instructions

This file governs the **knowledge repository**. It is not automatically injected into unrelated code repositories. A project needs discoverable local instructions (`AGENTS.md` or an agent-supported equivalent) with a verified path to use the vault automatically in later sessions. The vault also distributes a [general-purpose project template](templates/project-agents.template.md), which is **not** this file. See [project integration](docs/project-integration.md).

## Mission and scope

- Maintain accurate, concise, **project-agnostic** engineering knowledge in Markdown.
- Never embed a real application's name, local directory, chosen framework, or business-specific assumptions as a universal rule. Generic paths in examples are placeholders only.
- Discover each project's actual stack, architecture, conventions, documentation, and requirements independently before applying guidance.
- Adapt retrieval and summaries to the target project; do not reorganize a codebase to match the vault's directories.
- Store project-specific discoveries only in that project's authorized `10-projects/` record, keeping canonical code and technical documentation inside its source repository.
- Preserve project context, meaningful decisions, and task progress across sessions; save authorized onboarding/progress results to disk, not only chat.
- Keep personal learning in PARA; shared reviewed engineering practices in `playbook/`; canonical application details in **each application repository**.
- Write professional English. Do not create empty knowledge files merely to fulfill a checklist.

## Core commands

| Prompt | Read workflow | Default effect |
| --- | --- | --- |
| `use developer-second-brain` or scan/onboard with it | [Project onboarding](workflows/project-onboarding.md) | Save permitted verified project note |
| `save-progress` | [Save progress](workflows/save-progress.md) | Save task checkpoint |
| `resume-progress` | [Resume progress](workflows/resume-progress.md) | Retrieve and verify last checkpoint |
| `sync-knowledge` | [Sync knowledge](workflows/sync-knowledge.md) | Reconcile project notes |
| `brain-status` | [Brain status](workflows/brain-status.md) | Read-only status |
| `audit-docs <project-path>` | [Documentation audit and modernization](workflows/documentation-modernization.md) | **Read-only documentation audit and proposal** |
| `migrate-docs <project-path>` | [Documentation audit and modernization](workflows/documentation-modernization.md) | Implement only **after approval** of the specific migration plan |

For an explicit first-time instruction setup, follow [project bootstrap](workflows/project-bootstrap.md). Follow [command precedence](workflows/README.md) for ambiguous scopes and read-only requests.

## Default behavior for **normal engineering prompts**

When this file (or the installed project bridge) applies, follow the [development lifecycle](workflows/development-lifecycle.md) **without requiring the user to type `use developer-second-brain` again**:

1. Identify the affected application and task. Retrieve only relevant existing project note(s), live checkpoint(s) and engineering guidance when useful; do not load the entire vault.
2. Verify material assumptions against current app `docs/`, source, manifests, and tests. Respect applicable project instructions and task-specific requirements.
3. Execute only the user's authorized implementation/review, then run relevant safe checks and report what actually ran.
4. If work **materially changes** architecture, interfaces, security assumptions, deployment behavior, important constraints, or a verified root cause, update the appropriate project memory **only when the vault is writable and storage has been authorized for that project**. No write on read-only tasks, trivial changes, or unapproved confidential work.
5. If persistence is blocked, say exactly what was not saved. Do not pretend a chat answer is persistent memory.

The default lifecycle is **not** an instruction to refactor the app, run commands without permission, watch files in the background, or save a checkpoint after every small edit. Use `save-progress` for a clear end-of-session checkpoint.

## Evidence and source of truth

- Read the application's existing docs before proposing duplicate notes. Prefer links to its maintained documentation.
- Distinguish **verified in inspected code/tests**, **documented only**, **proposed**, and **unverified**. An absence of tests does not prove working production behavior.
- Read existing project notes before merging; preserve useful details and mark superseded facts without silently wiping user content.
- Record stable source paths and last reviewed date; verify links when practical. Flag contradictions explicitly instead of silently choosing outdated notes.
- Never assume a whole project was reviewed when only a subset was examined.

## Safety and permissions

- Explicit `read-only`, `do not save`, `audit only`, or user denial of vault writes overrides any persistence default.
- Documentation audit/migration is **read-only until a specific file-by-file plan is approved**; see [documentation migration](docs/documentation-migration.md). Knowledge onboarding alone allows authorized vault notes only; a **separate explicit setup request** may authorize creation of a project `AGENTS.md` from the general template when none exists. **Never overwrite existing project instructions; propose a minimal integration and ask approval before editing them.** No project code, dependency, Git history, or deployment changes are implied by knowledge commands.
- Never copy passwords, keys, tokens, customer records, personal information, proprietary source code, or unapproved private company details to this vault. If sensitivity or sharing permissions are uncertain, ask before the write; use safe general metadata only if permitted.
- If the vault is inaccessible/unwritable or beyond the sandbox, report the blocker and request proper access, never bypass restrictions.
- No automatic commits, pushes, `git init`, destructive cleanup, or invented checks/results.

## Completion report

State relevant files read, exact knowledge files actually written (if any), what was verified vs uncertain, actual checks executed, and any blocked access or missing setup. Write workflows must reopen/verify their saved notes.
