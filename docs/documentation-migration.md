# Documentation Migration Guide — Any Project

Use this with [Documentation Audit and Safe Modernization](../workflows/documentation-modernization.md). It describes **documentation** migration within an application repository, not the process of upgrading the Second Brain itself (see [Vault Upgrade Guide](upgrading.md)). The project and naming examples are illustrative only.

## Core design

- **Start with a read-only audit.** "Migrate" is a request to assess and propose until the user approves the **specific file operations**. Never delete the old `docs/` directory first.
- Project-owned source, tests, approved requirements, design decisions, and runtime validation are the sources of truth. The Second Brain stores concise verified summaries and links, not another copy of application documentation.
- Respect the project's existing documentation conventions. Do not force a fixed folder taxonomy when it adds no value.
- Do not infer why an old architectural choice was made from code alone. Preserve useful history, dated decisions, and verified troubleshooting context, even if current behavior has changed.
- If this project contains restricted data, obtain explicit authorization before transferring any details into a shared/external vault.

## Safe sequence

### 1. Audit existing evidence (no writes)

Read existing README(s), technical documents, relevant ADRs, API specs, diagrams, project instructions, issue/acceptance plans, manifests, tests, and important source modules. For large repositories, record coverage by subsystem and remaining gaps. Identify broken links, contradictory claims, unverified setup commands, missing sections, and duplicated content.

### 2. Propose a file-by-file migration map (no writes)

Use the [audit-report template](../templates/documentation-audit.template.md). Classify each old file as **retain, revise, merge, create, archive, or remove**. For moved/merged docs, identify the replacement and all known inbound links. Provide supporting evidence and a rollback strategy. Propose updates to navigation/README and any docs index.

### 3. Approval checkpoint (stop)

Request specific authorization for the proposed documentation modifications and, separately, for **deletions**, modifications to project `AGENTS.md`/`CLAUDE.md`, changes to application code, or export of project knowledge to the shared vault. Do not treat a broad audit request as approval for all steps.

### 4. Make only approved documentation changes

Preserve existing user edits. Update/merge documents in small groups, validate replacements against code where possible, repair relative paths, and preserve historical reasoning. Archive when an archive destination is actually useful and authorized; Git alone may not preserve uncommitted/untracked files. Do not delete originals until unique content is accounted for and replacement links have been checked.

### 5. Validate and report

Verify documentation links and file references, commands when safe, diagrams, and source claims. State what was not executed (production access, unavailable services, platform builds, or partially reviewed modules). Report final file operations and any outstanding disagreements or gaps.

### 6. Update project memory, if authorized

Use the Second Brain project's existing `10-projects/<slug>.md` record, link to the updated authoritative documents, and preserve only stable verified decisions and important constraints. Avoid duplicating entire docs. If permissions or sandbox access block a vault write, say so explicitly.

## A practical invocation

From a connected AI agent session:

> `audit-docs [PROJECT_PATH]` — inventory, verify against code, classify, propose a migration plan, then STOP without modifying anything.

After examining the report:

> `migrate-docs [PROJECT_PATH]` — apply **the explicitly approved file-by-file plan** only; validate documents and update authorized Second Brain knowledge.

For multiple projects, name each explicitly and review their plans separately. An agent cannot guarantee exhaustive code analysis just because a single audit prompt says "entire codebase"; require a coverage report.

## Recovery rules

- Retain originals until their unique information has been merged, archived, or deliberately removed **under the user's approval**.
- Maintain a readable plan mapping former paths → final paths. Broken external URLs or references may require redirects or compatibility notes.
- Avoid staging, committing, rewriting Git history, or automatic backups outside the user's instructions. A previous commit is not proof that today's untracked documentation can be recovered.
- Keep the migration scope bounded; do not transform a docs cleanup into an application refactor.
