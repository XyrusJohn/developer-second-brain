# Connecting Developer Second Brain to Any Project

This is a project-independent Markdown knowledge repository; it may be cloned next to any software project whose agent can read the files. **Simply cloning it is not a global registration step.** Codex usually discovers applicable `AGENTS.md` in the working project, not in an arbitrary sibling directory. Automatic retrieval in later sessions requires a discoverable project instruction bridge or another agent-supported integration mechanism.

Reusable setup instructions are intentionally free of any one project's real name, technology stack, or business rules. Example directory names below are placeholders; use paths that actually exist on your machine.

## Suggested layout

```text
workspace/
├── developer-second-brain/   # independent knowledge repository
├── sample-app/               # independent application
└── sample-api/               # independent application
```

## First use: one-prompt project bootstrap (no script)

Start an AI coding agent in `workspace/` (or with explicit access to both repositories). Give it this instruction:

> Locate `./developer-second-brain/AGENTS.md`. For `[PROJECT_PATH]`, follow `workflows/project-bootstrap.md` and `workflows/project-onboarding.md`. I authorize creation of a new project `AGENTS.md` from `templates/project-agents.template.md` **if none exists**. Preserve existing instructions and ask approval before editing them. Inspect the source and docs, save permitted verified knowledge, and verify installed references. Do not modify application code.

The agent must resolve the actual paths and substitute the template's `{{SECOND_BRAIN_RELATIVE_PATH}}` using a path relative to the **new application's** `AGENTS.md` folder. A vault clone never automatically installs instructions. A generic trigger does not work until the agent can locate the vault at least once.

**Two distinct instruction files:**

- Vault [`AGENTS.md`](../AGENTS.md) governs the *knowledge repository itself*.
- [`templates/project-agents.template.md`](../templates/project-agents.template.md) is the *portable engineering instruction source*; it must be rendered into the target project's root **`AGENTS.md`** (not `project-AGENTS.md`, which Codex would not automatically recognize).

If an application's `AGENTS.md` **already exists**, the setup must **never copy the template over it**. Instead, propose the small bridge below; seek approval before modifying the existing file. If a bridge is already present and current, leave it alone. Repeated setup should be idempotent.

Knowledge onboarding itself is distinct from instruction setup: a simple `use developer-second-brain` request authorizes only permitted vault notes. **Creating project instructions requires an explicit setup request.** Sensitive data restrictions still apply to both.

## Manual integration (no script)

When approved, append this **short bridge** to the application's existing `AGENTS.md` without replacing its local instructions. Set the correct relative vault path for that project, and account for independently opened nested project roots:

```md
## Shared Developer Second Brain

Shared vault relative to this AGENTS.md: ../developer-second-brain/

For ordinary significant engineering tasks:
- Read the shared vault's workflows/development-lifecycle.md.
- Consult only relevant project memory and source links; verify against actual code.
- After material, verified changes, selectively update permitted project notes
  when vault storage is authorized. Never write on read-only tasks.

For the commands use developer-second-brain, save-progress, resume-progress,
sync-knowledge, and brain-status:
- Read the shared vault's workflows/README.md and matching workflow.
- Follow the shared vault's privacy, evidence, and permission rules.
- Never use knowledge workflows as authorization to change application code.
```

For example, if the workspace layout is `workspace/developer-second-brain` and `workspace/sample-app`, the relative path from `sample-app/AGENTS.md` is `../developer-second-brain/`. If the vault is at `workspace/developer-second-brain` and the target instructions are inside `workspace/sample-app/backend/`, adjust the path to `../../developer-second-brain/`.

**Important:** This text is not automatically inserted by a clone. A code agent can write it with your explicit approval, or you can add it manually. Restart/reopen the agent session to test instruction discovery. The agent may need read/write permission outside the current project sandbox.

## Optional setup helper for teams

If you prefer repeatable installation without manually editing Markdown, use the [optional Python helper](../scripts/README.md). It previews changes by default and modifies only the selected `AGENTS.md` after `--apply`:

```powershell
# From developer-second-brain/: preview, then explicit apply
py -3 .\scripts\connect-project.py --project ..\sample-app
py -3 .\scripts\connect-project.py --project ..\sample-app --apply
```

Already connected from V1.1? The helper **does not replace existing marked instructions by default**. Use its `--refresh` flag to **preview** a managed-block upgrade, then `--refresh --apply` only if you approve. It preserves unrelated text in `AGENTS.md` and does not scan code or upload information.

## Claude Code and other agents

Codex uses applicable `AGENTS.md` instructions from its project scope. A vault `AGENTS.md` in an unrelated sibling folder is not automatically active for the application.

Claude Code instruction discovery varies by version and settings. Current versions may read project `AGENTS.md` when no competing project `CLAUDE.md` exists; with an existing `CLAUDE.md`, it may use that instead. **Do not replace or duplicate that file automatically.** When necessary and explicitly approved, add a lightweight `@AGENTS.md` import to the existing `CLAUDE.md` or use another supported setting. Check your installed Claude Code version and verify the actual files loaded in a fresh session. The `@AGENTS.md` import syntax is Claude-specific, not a Codex feature.

For other coding agents, follow their documented instruction-loading mechanism. The portable template is Markdown, not a universally discovered or registered plugin/skill.

## Verification in a fresh session

1. Open the project using the same agent workflow you will use normally; verify its installed `AGENTS.md` has a resolved vault path and no template placeholders.
2. Say: “Tell me the Second Brain vault path and which project memory note is relevant. Read-only.” Confirm it loads the bridge and can open the vault file.
3. Onboard the project if needed; verify the note is actually on disk and its source references point to inspected files.
4. Start a **new session**; ask about a known saved decision **without mentioning the Second Brain**. Check that the agent reads existing context and verifies it against code.
5. Make a safe, material and authorized test change in a disposable project; verify it selectively updates the note. Test that a trivial change does not create meaningless updates, and a read-only task never writes.
6. Use `save-progress` / `resume-progress` in different sessions. Confirm timestamps, test results, and blockers match actual files.

See [acceptance tests](acceptance-tests.md) for the exact manual test matrix. Our local automated tests **cannot certify Codex's external runtime, sandbox, or cross-session behavior**.

## Documentation audit and migration after connection

Once the project's instructions are discoverable, `audit-docs [PROJECT_PATH]` follows the [documentation modernization workflow](../workflows/documentation-modernization.md) in **read-only** mode. It reviews current docs and relevant code, records coverage and evidence, and proposes a **file-by-file migration map**. A separate, explicitly approved plan is necessary before `migrate-docs` can revise, merge, archive, or remove documentation. Code and project instruction files remain out of scope. Use the [documentation migration guide](documentation-migration.md) and the [report template](../templates/documentation-audit.template.md).

If an old managed bridge doesn't mention the new commands, the updated command router can still be read through the existing link; an explicit bridge refresh is useful but does not justify overwriting user-owned instructions. Existing full-template installations should be reviewed and selectively updated by the project owner—no automatic replacement.

## Security and project ownership

Do not export client data, credentials, confidential architecture, or employer-owned implementation details without permission. The vault may be private but still outside the owning company's approved repository boundary. When in doubt, keep detailed knowledge in the application docs and ask for approval before copying it elsewhere.

Existing app architecture, requirements, tests, and approved ADRs remain authoritative. A Second Brain note is an evidence-based summary and navigation aid, **not** a replacement or a universal source of implementation truth.

## No hidden automation

The workflows are instructions for an active authorized agent, not standalone background programs. No external packages, continuous watchers, or background automations are installed by this repository.
