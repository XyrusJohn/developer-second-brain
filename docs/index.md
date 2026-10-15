# Knowledge Index

This repository preserves engineering and project knowledge without duplicating entire application repositories.

| Need | Read |
| --- | --- |
| Use core keywords (`use developer-second-brain`, `save-progress`, etc.) | [Command router](../workflows/README.md) |
| Ordinary coding with relevant memory and selective saving | [Everyday lifecycle](../workflows/development-lifecycle.md) |
| First-time project instructions (template, safe setup, no mandatory script) | [Bootstrap workflow](../workflows/project-bootstrap.md) |
| Connect a clone to an application; avoid mandatory scripts | [Project integration](project-integration.md) |
| Migrate an existing knowledge vault safely | [Upgrade guide](upgrading.md) |
| Audit, review, or migrate a project's documentation safely | [Documentation modernization workflow](../workflows/documentation-modernization.md) and [documentation migration guide](documentation-migration.md) |
| Produce an evidence-backed per-file documentation proposal | [Documentation audit report template](../templates/documentation-audit.template.md) |
| Verify new/fresh agent sessions, writes and read-only behavior | [Acceptance test checklist](acceptance-tests.md) |
| Browse onboarded project notes and checkpoints | [Projects](../10-projects/README.md) |
| Capture rough research for later review | [Inbox](../00-inbox/README.md) |
| Long-running growth and responsibility notes | [Areas](../20-areas/README.md) |
| Reusable technical knowledge | [Resources](../30-resources/README.md) |
| Completed/inactive knowledge | [Archive](../40-archive/README.md) |
| Curated standards and templates | [Playbook](../playbook/README.md) |
| Evidence, privacy, knowledge classification | [Knowledge conventions](knowledge-conventions.md) |

## Source of truth

Actual code, tests, requirements, and approved project decisions remain in the application repository. `10-projects/` stores verified summaries, lightweight navigation links, and explicit progress snapshots, not code backups.

## Discovery limitation

A sibling vault's `AGENTS.md` is **not automatically part of another project's instructions**. Read the [integration guide](project-integration.md) and verify that the agent can access the notes. The optional setup helper is never required for a one-off session with a direct path.
