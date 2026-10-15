# Upgrading an Existing Developer Second Brain to V1.4

**Preserve the working vault and any onboarded project data.** A starter archive is not a merge tool.

V1.4 builds on the V1.3 universal project template/bootstrap and retains the original five knowledge commands. It adds a documentation audit and safe migration workflow (`audit-docs` / `migrate-docs`), an evidence/report template, and compatible command routing.

## Recommended migration steps

1. **Back up your vault** with its existing `10-projects/` notes, checkpoints, custom notes, and uncommitted changes. Make a separate copy or verified recovery point; do not assume all knowledge is committed in Git.
2. **Extract the new V1.4 archive to another directory**. Compare first; do not blindly overwrite a populated working directory.
3. Add new files: `workflows/documentation-modernization.md`, `docs/documentation-migration.md`, `docs/upgrade-v1.4.md`, and `templates/documentation-audit.template.md`.
4. Merge changes to shared instructions, command routing, project onboarding, README/index, integration docs, tests, and optional `scripts/connect-project.py`. Preserve all existing user customizations. Keep `workflows/project-bootstrap.md` and `templates/project-agents.template.md` from V1.3 or add them when coming from V1.2.1.
5. **Never replace project-owned `AGENTS.md` automatically.** For existing project files, offer a minimal additive update only with the owner's explicit approval. For a new project without one, the V1.3 bootstrap template installation remains available.
6. Run `python -m unittest discover -s tests -v`. Verify the new workflow's links, project-independent wording, and instruction bridge references. These offline tests do not prove Codex or Claude Code will automatically load a sibling vault.
7. Open a fresh agent session in a disposable project and follow [acceptance tests](acceptance-tests.md). Try `audit-docs` and confirm **zero writes** before approval. Then approve a small scoped docs edit, run `migrate-docs`, inspect changed docs and authorized project memory.

## Original notes and documents are separate from starter files

Do not overwrite `10-projects/`, `00-inbox/`, `20-areas/`, `30-resources/`, or `40-archive/` to install a new version. Likewise, **do not delete an application's old `docs/` directory** during upgrade. Application documentation modernization is a different, user-approved process; follow [documentation migration](documentation-migration.md).

## Behavioral limits

V1.4 is Markdown workflows plus an optional local helper, not a background daemon or registered agent/skill. The project's working agent must have applicable instructions, filesystem access, and permissions. Old project bridge references to `workflows/README.md` can route new commands after the vault upgrade even if the bridge has not been refreshed, but explicit instruction-loading must still be tested.
