# Documentation Audit Report — {{PROJECT_NAME}}

> **Template only.** Render it into a user-requested report or project-owned location after permission. This file is not a project instruction file. Do not fill fields from assumptions.

- Project path: `{{PROJECT_PATH}}`
- Audit date: `{{REVIEW_DATE}}`
- Mode: **read-only audit / approved implementation**
- Reviewed instructions and documentation: `{{REVIEWED_DOCS}}`
- Reviewed source/test areas: `{{REVIEWED_AREAS}}`
- Coverage and exclusions: `{{COVERAGE_LIMITATIONS}}`
- Executed verification: `{{COMMANDS_AND_RESULTS_OR_NOT_RUN}}`

## Documentation inventory

| Existing document | Purpose / readers | Current dependencies and inbound references | Evidence / status |
| --- | --- | --- | --- |
| `{{DOC_PATH}}` | {{PURPOSE}} | {{LINKS}} | {{VERIFIED_DOCUMENTED_OR_UNVERIFIED}} |

## Evidence-backed findings

| Finding | Claim source | Code/test or other evidence | Classification | Impact |
| --- | --- | --- | --- | --- |
| {{FINDING}} | `{{DOC_PATH}}` | `{{SOURCE_PATH}}` or "not verified" | Verified / documented only / inferred / unverified | {{IMPACT}} |

## Proposed documentation map

Describe the minimal navigation/ownership structure appropriate to this project. The file paths in the following table are placeholders, not prescribed layout.

| Current path | Proposed action | Destination/replacement | Evidence and unique content to preserve | Risk / verification | Approval needed |
| --- | --- | --- | --- | --- | --- |
| `{{OLD_PATH}}` | Retain / Revise / Merge / Create / Archive / Remove | `{{NEW_PATH_OR_NONE}}` | {{EVIDENCE}} | {{RISKS_AND_CHECKS}} | Yes / No |

## Migration gates

- [ ] User reviewed the project-specific proposed changes.
- [ ] User authorized documentation edits (specific paths/scope).
- [ ] Destructive removals/archiving authorized **separately**, if any.
- [ ] Restricted-information transfer to a shared vault authorized, if relevant.
- [ ] Original unique history/decisions have a confirmed preservation destination.
- [ ] Existing work and rollback approach reviewed.

## Implementation and verification (only after approval)

- Files modified, created, archived, or removed: {{ACTUAL_OPERATIONS}}
- Links, code claims, and commands validated: {{ACTUAL_CHECKS}}
- Checks unavailable or not run: {{SKIPPED_CHECKS}}
- Remaining inconsistencies and risks: {{REMAINING_GAPS}}
- Second Brain record changed (only if authorized): `{{PROJECT_NOTE_PATH_OR_NONE}}`
- Confirmation that saved files were reopened/checked: {{VERIFICATION}}

**Initial audit must stop before implementation and request approval.**
