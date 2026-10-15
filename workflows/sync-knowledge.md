# Workflow: Sync Knowledge

**Trigger:** `sync-knowledge`, `refresh second-brain`.

**Success condition:** The relevant persisted knowledge is confirmed current for the inspected scope, or updated with supported changes and a transparent report of gaps.

## Procedure

1. Identify the specified or unambiguous current project. Read existing `10-projects/<slug>.md`, optional checkpoint, and original project documentation.
2. Inspect relevant implementation/manifest changes, tests and recorded decisions since the note was last reviewed, where this can be established. Do not pretend an available Git diff covers history when there is no Git repository or baseline.
3. Compare each material claim in the note with the authoritative project evidence. Label **accurate**, **changed**, **uncertain**, **obsolete**, or **conflicting**.
4. Update only the knowledge files in the Second Brain. Preserve meaningful historical decisions and user-written notes; do not silently remove conflicting information.
5. Update review date, source references, and known scan limitations. Check saved links where feasible, then report changes and remaining inconsistencies.

## Boundaries

- Do not edit application source, existing app documentation, dependencies, test fixtures, Git state, or infrastructure through this workflow.
- A read-only override means provide a proposed diff/report without saving.
- Do not synchronize sensitive company/internal details to an unapproved vault; ask or limit to non-sensitive metadata.
- This **deeper reconciliation** workflow runs only when invoked; it is not continuous background monitoring. Ordinary tasks may still follow the narrower, permission-gated [everyday knowledge lifecycle](development-lifecycle.md).
