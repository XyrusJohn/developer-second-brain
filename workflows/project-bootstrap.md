# Workflow: Safe Project Instruction Bootstrap

**Trigger:** Explicit first-time setup request, such as `use developer-second-brain to set up <project-path> and install project instructions`, or `bootstrap project instructions for <project-path>`.

**Goal:** Establish discoverable, project-owned engineering instructions linked to the shared vault, **without overwriting local instructions or touching application source code**. This is a one-time interactive setup procedure; cloning the vault does not execute it.

## 1. Identify and inspect

1. Resolve the existing, explicitly targeted project directory and the actual vault location; confirm the agent has permitted access to both. If ambiguous, ask for the project path.
2. Read the applicable parent and project-specific `AGENTS.md`, `CLAUDE.md`, `CLAUDE.local.md` and other instruction files where applicable; inspect local conventions before proposing changes.
3. Check whether the user asked for a read-only audit or explicitly authorized new instruction-file creation. `read-only` / `do not save` means **no files written**.
4. Check for restricted/confidential information: a separately maintained vault may be outside the target project's approved data boundary. Permission to create a bridge is **not** permission to export confidential knowledge.

## 2. Determine the installation strategy

- **No project `AGENTS.md` exists, installation expressly requested:** Create a new project-root `AGENTS.md` from [`templates/project-agents.template.md`](../templates/project-agents.template.md), adjusting the verified relative vault path. Preserve an applicable parent `AGENTS.md`; local instructions should extend, not silently contradict, it.
- **Project `AGENTS.md` already exists:** **Never replace it with the template.** Read it, identify gaps/conflicts, and propose a minimal additive vault bridge using [project integration](../docs/project-integration.md). Obtain approval for the specific edits before modifying the file.
- **Existing project bridge present:** Compare its path and instructions with the current vault workflow; leave it unchanged if current. Propose and request approval for any refresh.
- **Another coding agent:** Use that agent's *verified* instruction-discovery rules. For Claude Code, inspect any `CLAUDE.md` and its current loading behavior; if it would hide/override `AGENTS.md`, propose an additive `@AGENTS.md` import or another verified mechanism **only with approval**. Do not assume all versions behave alike or blindly overwrite `CLAUDE.md`.

## 3. Render and install safely

1. Calculate the relative path from the target **project-root `AGENTS.md` directory** to the vault. Do not assume `../developer-second-brain/` or hardcode a company/project path. For cross-drive or inaccessible paths, report the blocker and ask for a supported alternative.
2. For a new project `AGENTS.md`, substitute the **single** `{{SECOND_BRAIN_RELATIVE_PATH}}` placeholder in the template with the validated forward-slash relative path. Do not copy the vault's own `AGENTS.md` into the application: it governs a different directory and purpose.
3. Check that no template placeholders remain, no existing instruction file would be overwritten, and every referenced vault workflow exists.
4. Create only the approved target instruction file(s). Do not modify project code, dependencies, existing README/docs, hidden agent configuration, or Git state as a side effect.
5. Reopen installed files and verify contents/path. A second bootstrap must not duplicate bridges, replace customized instructions, or churn unchanged files.

**Optional, never mandatory:** The included `scripts/connect-project.py --project <path> --full-template` previews creation from the full template when no project `AGENTS.md` exists; `--apply` performs that requested create. The helper refuses full-template mode when the file already exists. In an existing-instructions project, the original preview-only bridge behavior remains available.

## 4. Confirm real agent discovery

- **Codex:** Open a **fresh session** rooted at the application; verify that it reads the applicable project `AGENTS.md`, locates the vault, and finds its corresponding project knowledge. Merely seeing a file on disk is not proof that a session loaded it.
- **Claude Code:** In a fresh session, verify that its currently supported instruction loading mechanism reads the required project instructions. Existing `CLAUDE.md` configuration may alter behavior.
- For other tools, explicitly confirm their discovery behavior. A generic Markdown file is not automatically a registered skill or command.
- If a tool, sandbox, or working-directory restriction prevents loading, disclose the blocker and propose a supported setup; don't imply universal automatic installation.

## 5. Result and optional knowledge onboarding

Report exact files created/modified, resolved vault path, whether instructions loaded in a real new session (**tested** or **not tested**), and any missing permissions or conflicts. If the user also requested knowledge onboarding, follow [project onboarding](project-onboarding.md) separately; persist only permitted, verified notes. No background synchronization is configured.
