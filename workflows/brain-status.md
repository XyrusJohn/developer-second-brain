# Workflow: Brain Status

**Trigger:** `brain-status`, `show brain status`.

**Always read-only.** Do not create placeholder notes or update `last-reviewed` as a side effect.

## Procedure

1. Inspect `10-projects/` notes and `10-projects/progress/` checkpoints that exist and are accessible. If the user names a project, scope the report to that project.
2. Report stored project names, file paths, latest documented review/checkpoint dates **as written**, missing linked files if checked, unverified findings, and outstanding work items.
3. Identify possible stale documentation from recorded dates or visible contradictions, without claiming a note is stale simply because it is old.
4. If vault paths are inaccessible, say so; never fabricate a knowledge inventory.

Report succinctly. No application code changes, no vault writes, no external sync, and no Git operations required.
