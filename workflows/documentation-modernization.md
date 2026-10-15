# Workflow: Documentation Audit and Safe Modernization

**Triggers:** `audit-docs <project-path>`, `review project documentation`, `documentation modernization`, or `migrate-docs <project-path>`.

**Default:** **Read-only audit and proposal.** The words `audit-docs`, `migrate-docs`, "modernize", or "rebuild documentation" **do not alone authorize deleting, moving, rewriting, or archiving existing documents**. An implementation phase requires review and explicit approval of the concrete plan. Follow [the migration guide](../docs/documentation-migration.md) and use [the report template](../templates/documentation-audit.template.md) where useful.

**Goal:** Maintain accurate, efficient, project-owned documentation grounded in the actual system, preserving important historical decisions and safely updating the shared Second Brain **after** authorized changes.

## Phase 0 — Scope, permission, and safety

1. Identify each explicitly requested target project; do not silently include siblings. If multiple projects are named, produce **separate inventories, findings, proposals, and approval scopes** for each.
2. Read applicable project and parent agent instructions, the project's README/docs, existing plans and ADRs, and any relevant Second Brain note. Treat these as evidence, not proof that the deployed system behaves identically.
3. Establish whether the user requested **audit only** or has already explicitly approved a **specific** migration proposal. On first run, default to read-only. If `read-only`/`do not save` appears, make no writes anywhere, including to the vault.
4. Do not alter source, tests, configs, dependencies, database data, infrastructure, Git state, `AGENTS.md`, or `CLAUDE.md` as a documentation side effect.
5. Protect confidential code and customer/business information; verify permission before writing summaries to an external/shared vault. Avoid sending private source to external services or research tools without approval.

## Phase 1 — Inventory and systematic evidence gathering (read-only)

1. Inventory maintained documentation (including README, `docs/`, ADRs, OpenAPI/schema descriptions, operational runbooks, diagrams, and any unusual document locations). Locate links, references, and deployment/setup entry points.
2. Establish a proportional review plan for large codebases: important entrypoints, manifests, configs, module boundaries, tests, relevant infrastructure, client/server/API integration, and user-facing flows. Record reviewed and skipped areas rather than claiming exhaustive coverage.
3. Compare important documentation claims against current source and tests; inspect historical decisions in existing documents and Git history **when accessible and relevant**, without inventing motives from code alone.
4. For external libraries/platform behavior or security-sensitive claims, prefer verified installed versions and authoritative official documentation. Report when external verification cannot be performed; never assert current compatibility without evidence.
5. Classify each finding as **verified in source/tests**, **documented only**, **inferred (needs confirmation)**, or **unverified**. Quote the smallest useful paths/line references, executed commands and outcomes, and any confidence limitations.

## Phase 2 — Proposal and approval gate (read-only)

Deliver a project-specific report using the [audit template](../templates/documentation-audit.template.md) and an explicit per-file action matrix:

- **Retain:** Accurate and useful; no edit needed.
- **Revise:** Correct stale or misleading content.
- **Merge:** Combine duplicate documents while preserving unique decisions/references.
- **Create:** Fill a demonstrated documentation gap; avoid empty or redundant pages.
- **Archive:** Preserve historical content that is not active guidance.
- **Remove:** Only truly redundant/obsolete content after explicit approval and successful preservation/validation.

For each proposed action, explain affected paths, source evidence, critical links, readers/dependencies, important information at risk, replacement destination, verification method, and any migration/rollback concern. Show a suggested documentation navigation structure consistent with the actual project; **do not force a universal directory layout**.

**STOP and request approval** before implementing. Ask separately for any destructive removal/archiving, changes to agent instructions, code, or sensitive vault writes. A general "make docs better" prompt is not per-file deletion approval.

## Phase 3 — Approved implementation (only with clear scope)

1. Confirm the currently approved file operations and existing working-tree changes; preserve unrelated edits and ensure a safe versioned recovery path or backup where appropriate. Never assume Git has committed untracked docs.
2. Apply small, reversible documentation-only updates in the approved scope. Retain original critical rationale and links; mark historical material clearly rather than silently erasing it.
3. Update references **within the approved scope** to renamed/moved pages; preserve external links, onboarding/setup paths, and important anchors when possible. Note any inbound external references that cannot be edited.
4. Do not delete originals merely because replacement files exist. Archive/remove only items explicitly approved **after** confirming unique information and references are preserved.
5. If actual source differs from proposed assumptions, stop or rescope and seek approval rather than silently improvising risky changes.

## Phase 4 — Validation and Second Brain reconciliation

1. Reinspect modified docs for correctness and consistency with real code and tests; validate relative links, headings/anchors, referenced filenames, diagrams, and commands where safe and practical.
2. Report **exactly which checks ran**, which were skipped, unresolved factual disputes, remaining stale docs, and rollback considerations.
3. When authorized to store project knowledge in the vault, update the **existing** `10-projects/<slug>.md` with a concise verified overview, important decisions, and links to the **project-owned canonical docs**. Do not copy detailed documentation or confidential material. If no approved vault storage exists, report the limitation and do not write.
4. Reopen files actually written; verify the vault links and updated document paths. A successful Markdown rewrite is not evidence of production correctness or a complete codebase review.
5. Report per project: inventory, reviewed coverage, approved edits applied, modified/archived/removed files, results, knowledge notes updated, unverified items and remaining work.

**Always:** The code, tests, approved requirements and project-owned documentation are authoritative; the shared Second Brain is an index and continuity layer. Repeated migration runs should avoid duplicate files and unnecessary edits.
