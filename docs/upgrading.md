# Upgrade Guide

**Latest:** [V1.4 upgrade guide](upgrade-v1.4.md) covers safe migration from V1.2.1 or V1.3, including new documentation modernization workflows. The historical steps below remain for older upgrades.

**Do not extract the new ZIP directly over a populated Second Brain without review.** Your `10-projects/` notes, progress checkpoints, and personal PARA notes are user data; preserve them.

## Upgrading from V1.1 to V1.2

### Safe migration

1. Make a backup of your existing `developer-second-brain/` repository, including uncommitted notes.
2. Extract V1.2 into a **separate folder** to inspect the new `README.md`, `AGENTS.md`, `workflows/development-lifecycle.md`, and `docs/`.
3. Review and merge the updated **instruction and workflow files** into your existing knowledge repository. Do not blindly replace `10-projects/`, `00-inbox/`, `20-areas/`, `30-resources/`, or `40-archive/` with an empty starter copy.
4. If V1.1 previously inserted an `AGENTS.md` bridge in your project, it will **not** gain the new everyday retrieval instructions by merely changing the Second Brain files. Update the existing bridge **after reviewing and approving the change**; use the [manual integration guide](project-integration.md#manual-integration-no-script) or [optional helper](../scripts/README.md) with `--refresh` preview.
5. Open a new AI session and follow the [acceptance tests](acceptance-tests.md): verify access, `brain-status`, cross-session retrieval, meaningful selective updates, read-only behavior, and progress checkpoints.

If you want Codex to do the migration, ask it to **compare V1.1 and V1.2, preserve all existing notes, propose the exact file changes, and wait for approval before editing project `AGENTS.md` files**. Never infer that a newly extracted archive already updated your working repositories.


## Upgrading from V1.2 to V1.2.1

V1.2.1 clarifies that the reusable documentation is fully project-agnostic; it does **not** change the five commands, onboarding persistence, or script interface.

1. Back up your existing vault (including uncommitted or untracked project notes).
2. Extract V1.2.1 into a **separate directory** for review.
3. Compare and selectively merge `README.md`, `AGENTS.md`, `docs/knowledge-conventions.md`, `docs/project-integration.md`, `workflows/project-onboarding.md`, and the project-note template. Keep existing project-specific knowledge and modified notes.
4. Keep `10-projects/`, PARA notes, and personal materials intact. Do **not** replace a populated knowledge vault with the starter archive.
5. Review the updated regression test, then run the existing local tests. Reopening any project bridge is not required solely because of the V1.2.1 wording change, unless that bridge is already stale.

The example application names in guidance are placeholders; real project names appear only inside the generated project records when authorized.

## Upgrading from V1.2.1 to V1.3

V1.3 adds a reusable **project engineering instruction template** and an explicit **project instruction bootstrap workflow**. The five original knowledge commands and existing saved note formats remain unchanged. An additional explicit setup trigger is optional.

1. Back up your current vault including `10-projects/`, its progress notes and any personal PARA data; do **not** extract the starter ZIP over a populated working tree.
2. Compare and selectively merge updated `README.md`, `AGENTS.md`, `workflows/project-onboarding.md`, `workflows/README.md`, `docs/project-integration.md`, the new `workflows/project-bootstrap.md`, and `templates/project-agents.template.md`. Update the optional integration helper only if you want its `--full-template` mode.
3. **Do not overwrite existing application `AGENTS.md` files** with the new template. A pre-existing short bridge can stay in place if it still references the correct vault and workflows. Review only necessary improvements with the owner.
4. For **new** projects without `AGENTS.md`, run the first-time setup prompt in the integration guide. Explicitly authorize new-file creation; verify the relative vault path and references before relying on it.
5. Run `python -m unittest discover -s tests -v` and the [live acceptance checklist](acceptance-tests.md). The offline tests do not verify Codex/Claude behavior in your runtime.

V1.3 starter contents deliberately contain no real application notes. Preserve your existing project records and never assume ZIP replacement merged them.
