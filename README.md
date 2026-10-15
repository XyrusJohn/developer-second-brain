# Developer Second Brain

**Version 1.4.2 — Quick Commands + Beginner-Friendly Setup Guide**  
**Core features:** Universal Project Bootstrap + Safe Documentation Modernization  
**Format:** Portable, project-agnostic Markdown + Git knowledge repository, designed for coding agents such as Codex and Claude Code.

> **Start here.** This README explains exactly how to set up and use Developer Second Brain from a fresh download through daily coding, progress checkpoints, and documentation modernization. You do **not** need to install a database, register a global agent, or run a setup script. You **do** need to tell your coding agent where the vault is **once per project**, give it appropriate access, and verify the connection.

## Contents

1. [Understand the system first](#1-understand-the-system-first)
2. [Download or clone and arrange your folders](#2-download-or-clone-and-arrange-your-folders)
3. [Start your coding agent in the right place](#3-start-your-coding-agent-in-the-right-place)
4. [First-time setup: quick command or full installation](#4-first-time-setup-quick-command-or-full-installation)
5. [Check that onboarding really worked](#5-check-that-onboarding-really-worked)
6. [Use it during normal development](#6-use-it-during-normal-development)
7. [Save progress and resume in another session](#7-save-progress-and-resume-in-another-session)
8. [Audit and modernize existing project documentation](#8-audit-and-modernize-existing-project-documentation)
9. [Understand the folders and where notes belong](#9-understand-the-folders-and-where-notes-belong)
10. [Connect Codex, Claude Code, and other agents](#10-connect-codex-claude-code-and-other-agents)
11. [Optional manual/CLI project integration](#11-optional-manualcli-project-integration)
12. [Upgrade an existing Second Brain safely](#12-upgrade-an-existing-second-brain-safely)
13. [Troubleshooting and common questions](#13-troubleshooting-and-common-questions)
14. [Final checklist and reference links](#14-final-checklist-and-reference-links)

---

## 1. Understand the system first

Developer Second Brain has **three distinct roles**. Keeping them separate prevents instruction conflicts and accidental replacement of project documentation.

| Component | Location | Responsibility |
| --- | --- | --- |
| **Vault instructions** | `developer-second-brain/AGENTS.md` | Rules for storing, retrieving, verifying, and synchronizing knowledge **inside the vault**. |
| **Project engineering template** | `developer-second-brain/templates/project-agents.template.md` | Reusable starting instructions for **any** application; this file is a **template**, not an active project agent. |
| **Installed project instructions** | `[PROJECT]/AGENTS.md` | Actual engineering rules for the application. When connected, they point to the vault and its workflows. |

**Important:** The project template is rendered into a file named **`AGENTS.md`** in the application. Do **not** rename it `project-AGENTS.md` after installation, and do **not** copy the vault's own `AGENTS.md` into an application: they have different responsibilities.

The Second Brain is **not** an autonomous service. Markdown workflows provide instructions to an **active coding agent**. Simply running `git clone` will **not** auto-install instructions into neighboring projects or turn short phrases into shell commands. Future automatic retrieval is **conditional** on the agent actually loading applicable project instructions, having access to the vault, and having permission to save the relevant knowledge.

**Source of truth:** The application's current code, tests, approved requirements, and its maintained `docs/` remain authoritative. The vault holds concise, evidence-backed summaries and checkpoints; it is **not** a replacement for application documentation or a backup of source code. Keep reusable rules project-agnostic, and keep **project-specific** discoveries in the corresponding authorized project note.

## 2. Download or clone and arrange your folders

### Step 2.1 — Obtain the repository

Choose **one** method:

- **ZIP:** Extract the downloaded release so the directory is named `developer-second-brain` and contains `README.md`, `AGENTS.md`, `workflows/`, and `templates/` directly. Watch out for accidental double nesting such as `developer-second-brain/developer-second-brain/`.
- **Git:** If you have published or received a Git repository URL, open a terminal in your workspace and clone it:

  ```powershell
  git clone "YOUR-SECOND-BRAIN-REPOSITORY-URL" developer-second-brain
  ```

  Replace the quoted placeholder with a **real URL** you control or have permission to access. This project does not assume a particular GitHub URL or remote. You can also use a local folder without Git.

### Step 2.2 — Put the vault next to your projects (recommended)

For example, on Windows:

```text
C:\work\workspace\
├── developer-second-brain\
│   ├── AGENTS.md
│   ├── README.md
│   ├── templates\
│   │   └── project-agents.template.md
│   ├── workflows\
│   └── 10-projects\
├── sample-app\
│   └── ... application code ...
└── sample-api\
    └── ... application code ...
```

Here, `sample-app` and `sample-api` are **examples only**. Replace them with your real project directory names; nothing is hardcoded for a company, language, or stack. The vault can also live elsewhere if your agent can access it; in that case you must supply the **actual path**.

**Do not** put a full duplicate of the vault inside every project. One shared vault may support multiple independently owned projects, subject to your confidentiality and permission rules.

### Step 2.3 — Confirm the files exist

In PowerShell, from the containing workspace directory:

```powershell
Test-Path .\developer-second-brain\AGENTS.md
Test-Path .\developer-second-brain\workflows\project-bootstrap.md
Test-Path .\developer-second-brain\templates\project-agents.template.md
Test-Path .\sample-app
```

All four should return `True` **if you used the example paths**. If not, correct the paths before onboarding. This check reads files; it does not install anything.

## 3. Start your coding agent in the right place

For first-time setup, start Codex, Claude Code, or another coding agent in a workspace/session where it can access **both** the vault and the target application. If the agent's sandbox allows only the application directory, reading/writing a sibling vault might be blocked; request appropriate workspace access rather than bypassing sandbox restrictions.

With an installed CLI, a Windows example is:

```powershell
cd C:\work\workspace
codex
```

Or launch Claude Code in the same workspace if its CLI is installed:

```powershell
cd C:\work\workspace
claude
```

These are **examples**, not dependencies or commands installed by this repository. You can instead open both directories in your coding agent's IDE workspace and use its chat interface. Your tool may have different launch instructions.

**Why start at the workspace initially?** A sibling `developer-second-brain/AGENTS.md` is **not automatically discovered** while working inside `sample-app`. The first prompt explicitly points the agent to that file. After successful project integration, later sessions can normally start in the application directory.

## 4. First-time setup: quick command or full installation

This section explains **both ways to start**. Replace `[PROJECT_PATH]` with an actual project path, such as `./sample-app`. These are **chat prompts for a coding agent**, not PowerShell commands.

| Your situation | Use | Result |
| --- | --- | --- |
| Second Brain instructions are **already loaded/discoverable** | **Step 4.1 — Quick onboarding** | Creates/refreshes authorized, verified project knowledge |
| Fresh clone or app **not yet connected** | **Step 4.2 — Full first-time setup** | Installs or proposes the project instruction bridge **and** onboards knowledge |
| Need a new project `AGENTS.md` too, but the agent already knows the vault | **Step 4.1 — Explicit quick bootstrap** | Requests the separate project-bootstrap workflow |

### Step 4.1 — Option A: Quick onboarding command

**If your coding agent can already find Developer Second Brain and its workflows**, the original short command is still supported:

```text
use developer-second-brain [PROJECT_PATH]
```

For example, with the generic workspace layout from Section 2:

```text
use developer-second-brain ./sample-app
```

To onboard **multiple projects** into the **same shared vault**:

```text
use developer-second-brain ./sample-app and ./sample-api
```

The agent should resolve **each** path separately, inspect permitted code/docs/tests, and create or update an authorized, evidence-backed note for each project under `10-projects/`. It must not assume that one project's approval or accessible files apply to another.

**Important: `use developer-second-brain` alone means knowledge onboarding, not permission to install or overwrite the project's `AGENTS.md`.** The command is a natural-language trigger defined in [the command router](workflows/README.md) and [project onboarding workflow](workflows/project-onboarding.md). It is **not a globally registered Codex/Claude command**. If the agent cannot locate the vault yet, use the full setup prompt in Step 4.2.

If instructions are already loaded **and** you want onboarding **plus** project-agent installation, ask explicitly:

```text
use developer-second-brain to onboard ./sample-app and set up its
project instructions using workflows/project-bootstrap.md.
Create a new project AGENTS.md from the reusable template only if absent.
If instructions already exist, preserve them and propose a minimal
integration; ask for approval before editing existing files.
```

### Step 4.2 — Option B: Full first-time setup prompt (recommended for a fresh clone)

From the **containing workspace directory**, when both folders are accessible, copy this into your coding agent:

```text
Locate ./developer-second-brain/AGENTS.md and read it.
If that exact location does not exist, find the real accessible
Developer Second Brain path and tell me before proceeding.

Target project: [PROJECT_PATH]
Instruction setup mode: integrate (safe default)

Follow these Developer Second Brain workflows:
- workflows/project-bootstrap.md
- workflows/project-onboarding.md

Inspect the project's existing AGENTS.md, CLAUDE.md, and other applicable
coding-agent instructions first.

If no project-root AGENTS.md exists, I authorize creating a NEW one
from templates/project-agents.template.md using the verified relative
path to the shared Second Brain, provided it does not conflict with
existing agent-specific or parent instructions.

If instructions already exist, preserve them. Propose the smallest
compatible integration and ask for my approval BEFORE editing them.
Do not replace existing instructions during this setup.

Inspect permitted project code, tests, configuration, and documentation.
Save a concise, verified and authorized project note in
Developer Second Brain's 10-projects/ directory.
Reopen saved files; verify source references and the project-to-vault path.
Report what changed, what still requires approval, and what was not verified.

Do not modify application source code, delete project documentation,
install packages, stage/commit/push, or expose confidential information.
```

The above prompt uses **`integrate`** as the safe default: create a missing `AGENTS.md` with permission, or **propose** a minimal bridge for existing instructions. You have **not** approved overwriting an existing instruction file.

**About `create`, `integrate`, and `replace`:**

| Request | How to use it safely |
| --- | --- |
| `create` | Create a new project `AGENTS.md` **only when absent**; check any `CLAUDE.md` or parent rules before doing so. |
| `integrate` (default) | Preserve existing files; inspect and **request approval** for any proposed changes. A missing project `AGENTS.md` may be created with explicit permission. |
| `replace` | **Not an automatic bootstrap operation in this release.** If you want to replace an existing `AGENTS.md`/`CLAUDE.md`, request a **separate, explicit file-by-file review and approval**. Preserve a recoverable copy and any necessary project-specific rules. The standard bootstrap workflow must not overwrite it. |

### Step 4.3 — Existing project instructions vs no instructions

**Case A — No project `AGENTS.md`:** The agent reads [`templates/project-agents.template.md`](templates/project-agents.template.md), calculates the actual path to the vault, replaces the `{{SECOND_BRAIN_RELATIVE_PATH}}` placeholder, and creates **only** the newly authorized instruction file. It must reopen the result and verify references.

**Case B — Project already has `AGENTS.md`:** The agent **must not overwrite it**. It reads the current instructions, proposes a minimal Second Brain reference, and waits for approval. Do the same for a pre-existing `CLAUDE.md` when its loading behavior requires a bridge.

Example approval **after reviewing the proposed diff**:

```text
I approve adding only the reviewed Second Brain integration block
to this project's existing AGENTS.md. Preserve all other engineering
instructions. Do not modify application source or documentation.
```

### Step 4.4 — Set up or onboard more than one project

For **knowledge-only onboarding** of multiple already-connected projects, use the one-line example in Step 4.1. For **first-time instruction setup**, run the full setup prompt once per project (or explicitly list all target paths and require a separate review/approval for each existing instruction file). The shared vault should remain a **single** repository; do not duplicate it into every project.

### Step 4.5 — Verify the files created

With the generic layout from Section 2, after successful setup:

```text
workspace/
├── developer-second-brain/
│   └── 10-projects/
│       └── sample-app.md    # Actual saved, permitted project summary
└── sample-app/
    └── AGENTS.md            # New file, or existing file bridged after approval
```

The agent may choose a different stable, unambiguous note filename and must report the actual saved path. **A chat answer alone does not prove persistence.** Inspect the files and continue with the fresh-session test in Section 5.

## 5. Check that onboarding really worked

### Step 5.1 — Inspect the installed instructions

In the target project, verify:

- `AGENTS.md` exists (or the agent's explicitly approved native instruction mechanism is connected).
- It points to a real vault path relative to that specific file, e.g., `../developer-second-brain/` **only when that path is correct**.
- There is **no** remaining `{{SECOND_BRAIN_RELATIVE_PATH}}` placeholder.
- Existing engineering requirements have **not** been wiped out.
- The agent did not silently edit source code, docs, or Git state.

From the example application root, an illustrative path check is:

```powershell
Test-Path ..\developer-second-brain\workflows\README.md
Test-Path ..\developer-second-brain\10-projects\sample-app.md
```

### Step 5.2 — Run a read-only test inside the project

**Close the initial coding-agent session**, then open a **fresh** session **in the application project**. Ask:

```text
Read-only: Tell me the exact Developer Second Brain location
configured for this project. Identify the corresponding project note
and one source file it references. Do not modify any files.
```

The agent should locate the installed project instructions, read the correct vault note, and report actual references. If the vault cannot be accessed, stop and fix the working directory, path, or permissions; do not rely on supposed automatic discovery.

Then try:

```text
brain-status for this project — read-only
```

Expected: a report of **existing** project notes, review dates, and checkpoints. It should write **nothing**. A missing `10-projects/progress/` directory is normal before the first checkpoint.

**Why this test matters:** Seeing notes in an editor or Obsidian graph confirms Markdown references, **not** that a new Codex/Claude session actually loaded the correct instructions.

## 6. Use it during normal development

After you verify integration, work normally. You **should not need the onboarding prompt again for every feature**.

For example:

```text
Implement a notifications feature in this application.
First inspect existing APIs, architecture, and tests.
Preserve backward compatibility and verify the changes.
```

When the project instructions are actually loaded, the intended [development lifecycle](workflows/development-lifecycle.md) is:

1. Retrieve **only relevant** existing knowledge (not the entire vault).
2. Inspect the current application code/docs/tests; verify critical assumptions.
3. Perform only the authorized engineering task and run practical checks.
4. If a meaningful, **verified** change affects architecture, contracts, security, deployment, or important debugging knowledge, **selectively** update the related project note **if storage is authorized**.
5. Report exactly which code, documentation, and vault files were modified; never invent saved progress or test results.

A trivial CSS change, spelling fix, or refactor with no lasting knowledge value usually **does not** need a vault update. `save-progress` is a separate explicit checkpoint command and does not run after every ordinary prompt.

**To verify the intended automatic behavior in your own environment:** make a safe, material change in a disposable project; inspect the target project's `10-projects/<slug>.md` before and after. If it did not update, investigate instruction discovery, authorization, and tool access. This behavior is **guided by instructions**, not guaranteed by installing Markdown files.

## 7. Save progress and resume in another session

### At the end of a coding session

Give your agent this **chat prompt** (not a PowerShell command):

```text
save-progress for [PROJECT_PATH]
```

When authorized and accessible, the agent writes a factual checkpoint to:

```text
developer-second-brain/10-projects/progress/<project-slug>.md
```

A good checkpoint records what is actually done, relevant source paths, checks **actually run**, blockers, unresolved decisions, and next tasks. It does not create a Git commit or source-code backup.

### The next day or in a new session

Open your target app in your coding agent and say:

```text
resume-progress for [PROJECT_PATH]
```

The agent should read the prior checkpoint **and re-check the current repository**, because the code may have changed since the note was written. It restores context and recommends next work; it does **not** grant unlimited permission to modify or deploy code.

You can inspect saved notes without writing:

```text
brain-status
```

To explicitly refresh old notes after approved code changes:

```text
sync-knowledge for [PROJECT_PATH]
```

These prompts work only when the session can discover the Second Brain instructions or you give the full vault path explicitly.

## 8. Audit and modernize existing project documentation

This is a **separate workflow** from initial knowledge onboarding. You **do not** need to delete or empty any existing `docs/` folder first.

### Phase A — Request a read-only audit

Inside a connected project, ask:

```text
audit-docs [PROJECT_PATH]

Review existing README, docs, architecture notes and relevant code/tests.
Report actual coverage and evidence. Classify each existing document
as retain, revise, merge, create, archive, or remove. Propose a
file-by-file documentation migration plan, but DO NOT change any files.
```

The agent follows [`workflows/documentation-modernization.md`](workflows/documentation-modernization.md) and should deliver an inventory, source-supported findings, file-specific actions, risks, and a proposed layout. Use [`templates/documentation-audit.template.md`](templates/documentation-audit.template.md) for a consistent report. For a large codebase, expect **explicit coverage limits** rather than unsupported claims that every file has been audited.

| Classification | Meaning |
| --- | --- |
| **Retain** | Keep an accurate, useful document. |
| **Revise** | Correct out-of-date or misleading content. |
| **Merge** | Consolidate duplicates while retaining unique decisions. |
| **Create** | Add necessary documentation that is genuinely missing. |
| **Archive** | Preserve historical context without presenting it as current guidance. |
| **Remove** | Delete only when unnecessary and **explicitly approved**, after preserving important content. |

**No files should be changed during the initial audit**, including Second Brain notes, unless you separately and explicitly approve a write task. The words `migrate-docs` or “modernize” by themselves are **not** authorization to delete, move, or rewrite project files.

### Phase B — Review the proposed migration

Review the report and identify exact files/actions you authorize. You might approve only two small revisions rather than the entire plan.

For example:

```text
I approve ONLY these documentation changes from the audit plan:
- Revise docs/setup.md to match the verified installation commands.
- Update README.md links pointing to docs/setup.md.

Do not delete, archive, merge, or change any other documents.
Do not modify application code or project agent instructions.
```

These paths are **illustrative**; use actual audited files. For any proposed deletion or archival, approve its **exact source path and destination/action** separately. Preserve a recoverable copy and verify replacement content first.

### Phase C — Apply only the approved plan

```text
migrate-docs [PROJECT_PATH]

Apply only the previously approved file-by-file plan.
Verify changed Markdown links, referenced code paths and commands
where safe. Preserve historical decisions, record unresolved gaps,
and update the project's Second Brain note only if vault storage
is separately authorized.
```

The agent should list the **exact files modified**, verifications actually performed, unapproved items left untouched, and any vault notes updated. Project-owned `docs/` remains the canonical detailed reference; the vault keeps only a concise index/summary.

**If no approved plan exists:** `migrate-docs` should stay **read-only** and ask for approval. Read the [documentation migration guide](docs/documentation-migration.md) before attempting a large overhaul.

## 9. Understand the folders and where notes belong

A newly downloaded vault has **starter READMEs and workflows**; its actual captured knowledge folders may remain empty until useful knowledge exists. That is **normal**. Do not generate empty notes just to fill directories.

| Directory | What belongs here | Typical update |
| --- | --- | --- |
| [`00-inbox/`](00-inbox/README.md) | Rough ideas and untriaged discoveries | When asked to capture or triage new information |
| [`10-projects/`](10-projects/README.md) | Concise project summaries; `progress/` checkpoints | Onboarding, major verified changes, `save-progress` |
| [`20-areas/`](20-areas/README.md) | Long-running learning and responsibility areas | When those areas need tracking |
| [`30-resources/`](30-resources/README.md) | Generalizable, verified technical knowledge | When a genuinely reusable lesson is worth keeping |
| [`40-archive/`](40-archive/README.md) | Historical or completed notes | On authorized archival |
| [`playbook/`](playbook/README.md) | Curated standards and knowledge-note templates | Reviewed standards updates, not routine project edits |
| [`templates/`](templates/project-agents.template.md) | Reusable project instructions and audit report templates | Maintained intentionally, not edited per project |
| [`workflows/`](workflows/README.md) | Command procedures and everyday lifecycle | Maintained intentionally, not edited per feature |
| [`docs/`](docs/index.md) | Vault conventions and integration/upgrade guides | When the vault's procedures change |
| [`scripts/`](scripts/README.md) | Optional setup helper | Only when needed for integration behavior |

**Where does a feature's documentation go?** Full API/data-flow/design documentation goes into that **application's `docs/`**; a short, verified link and lasting decision can go into `10-projects/<slug>.md`. A cross-project lesson may belong in `30-resources/` **if relevant and approved**, but neither category should be auto-filled indiscriminately.

## 10. Connect Codex, Claude Code, and other agents

**Codex:** The installed app-level `AGENTS.md` is the standard discoverable instruction file when within Codex's applicable directory scope. The sibling vault's `AGENTS.md` **does not** automatically apply to the app. After onboarding, test retrieval from a fresh Codex session rooted in the application.

**Claude Code:** Do **not** assume it loads `AGENTS.md` exactly like Codex in every release or workspace. Inspect how **your installed version** handles `CLAUDE.md`, `AGENTS.md`, and imports. If a project already has a `CLAUDE.md`, preserve it; an explicit, approved lightweight reference/import to project instructions may be needed. Verify the actual file-loading behavior in a new session.

**Other agents:** Use their documented project-instructions feature, or give the vault path explicitly for a one-time session. The short phrases in this README are **natural-language prompts**, not shell executables or universally registered agent skills.

See [project integration and Claude guidance](docs/project-integration.md).

## 11. Optional manual/CLI project integration

**Skip this section if the one-prompt onboarding worked.** No Python script is required.

If you want an inspectable, repeatable local helper, it uses **Python 3 standard library only**. From `developer-second-brain/` in PowerShell:

**Project with no `AGENTS.md`: preview full reusable template, then explicitly apply it.**

```powershell
py -3 .\scripts\connect-project.py --project ..\sample-app --full-template
py -3 .\scripts\connect-project.py --project ..\sample-app --full-template --apply
```

**Project already has `AGENTS.md`: preview a minimal integration bridge and review it before applying.**

```powershell
py -3 .\scripts\connect-project.py --project ..\sample-app
py -3 .\scripts\connect-project.py --project ..\sample-app --apply
```

**Already has a previously managed bridge: preview a refresh, then approve and apply.**

```powershell
py -3 .\scripts\connect-project.py --project ..\sample-app --refresh
py -3 .\scripts\connect-project.py --project ..\sample-app --refresh --apply
```

The helper is **preview-only by default**, and `--full-template` **refuses to overwrite an existing `AGENTS.md`**. It does not audit code, install packages, modify project source, or save project knowledge. You still need a separate onboarding step and an actual agent-discovery test. If Python is not installed, ask the coding agent to propose and perform the approved setup instead.

For manual bridge details, refer to [Connecting Any Project](docs/project-integration.md#manual-integration-no-script).

## 12. Upgrade an existing Second Brain safely

**This matters if you already have project notes or checkpoints.** A starter ZIP contains templates and instructions; it is **not a merger** of a previous working vault.

1. **Back up** your active `developer-second-brain/`, including `10-projects/`, `10-projects/progress/`, other PARA notes, and any uncommitted changes.
2. **Extract the new ZIP into a different temporary folder**, e.g. `release-staging/developer-second-brain/`. Do **not** extract on top of your populated vault.
3. Compare versions. For a **documentation-only V1.4/V1.4.1 → V1.4.2 refresh**, bring over the revised `README.md` after reviewing any custom local README changes. The other V1.4 workflows/templates are unchanged.
4. For upgrades **from V1.2.1 or V1.3**, first follow [`docs/upgrade-v1.4.md`](docs/upgrade-v1.4.md) to add/merge the new project-bootstrap and documentation-modernization files, and preserve all existing project notes.
5. Review existing app `AGENTS.md` / `CLAUDE.md` bridges; **never overwrite them** with the new template. Only install reviewed improvements when approved.
6. Run the local integrity tests, then verify a new agent session can still locate the vault and real project notes.

Example prompt for an agent to **plan** a safe upgrade:

```text
Compare my existing populated Developer Second Brain with the newly
extracted release. Preserve all existing project knowledge, checkpoints,
custom notes, and project agent instructions. Produce a file-by-file
upgrade plan first. Do not overwrite or delete any files until I approve.
```

See [upgrade instructions](docs/upgrading.md) and [V1.4 feature migration](docs/upgrade-v1.4.md). Upgrading the Second Brain is **not** permission to delete or reorganize an application's `docs/` folder.

## 13. Troubleshooting and common questions

**Q: I cloned the vault, but Codex says it can't find `use developer-second-brain`.**  
A: The trigger is not a built-in command or universally installed skill. First give the **explicit vault `AGENTS.md` path** and run the full setup prompt in [Section 4.2](#step-42--option-b-full-first-time-setup-prompt-recommended-for-a-fresh-clone). Confirm both directories are accessible to the session.

**Q: `AGENTS.md` already exists in my project. Should I delete it?**  
A: **No.** Keep it. Ask the agent to propose the minimal Second Brain bridge and approve the specific diff. The reusable template is primarily for projects **without** an existing engineering instruction file.

**Q: Which `AGENTS.md` should I use?**  
A: **Both have different jobs:** `developer-second-brain/AGENTS.md` manages the knowledge vault; `[PROJECT]/AGENTS.md` manages application engineering and points to the vault. `templates/project-agents.template.md` is only the source template.

**Q: My project has `CLAUDE.md` too.**  
A: Preserve it; check current Claude Code discovery/import behavior for your installed version, and add an approved minimal bridge only if required. Do not blindly duplicate instructions.

**Q: `brain-status` says there is no progress directory. Is that an error?**  
A: No. `10-projects/progress/` is created **only after a meaningful checkpoint is saved**, for example through `save-progress`. The status command should treat an absent directory as “no checkpoints,” not as a reason to fabricate files.

**Q: Only `10-projects/` has generated content. Is that normal?**  
A: Yes. The other PARA folders are for **relevant** future knowledge. The vault should not generate filler files merely to populate folders.

**Q: Will every new feature automatically update the vault?**  
A: Not guaranteed. The loaded lifecycle calls for **selective** updates after significant, verified and authorized work. Check the actual note on disk. No background watcher operates when the agent is not running.

**Q: I ran `audit-docs`. Why didn't it rewrite my README or delete old docs?**  
A: Correct behavior: **the audit is read-only**. Approve the exact file-by-file plan first, then request `migrate-docs` for that approved scope.

**Q: The agent says it saved a note, but I cannot find it.**  
A: Ask for the **absolute saved path** and to reopen the file. Check its actual working directory, write permission, and whether it wrote into a different clone. A chat report is not proof of a filesystem write.

**Q: Vault is outside the agent's sandbox / on another drive.**  
A: Grant supported access, open a workspace containing both directories, or provide a permitted vault location. Do not bypass sandbox restrictions. A relative-path template might not be suitable across drives; use a verified supported integration method.

**Q: Is it safe to store company project knowledge?**  
A: Only if you have authorization to place that information in this vault, especially when it is personal or externally shared. Never copy credentials, customer data, or unauthorized proprietary details. Keep sensitive source-of-truth documentation within the owning project repository.

**Q: Will this reduce tokens or guarantee better answers?**  
A: No guaranteed savings or accuracy gain. It helps organize verifiable context, but agent retrieval patterns, prompt size, and quality depend on the real task and tooling.

## 14. Final checklist and reference links

### A successful first-time setup should look like this

- [ ] The vault exists and the coding agent can read its `AGENTS.md` and workflows.
- [ ] The application and vault paths are verified.
- [ ] A new application `AGENTS.md` was installed **only if absent and authorized**, or an existing one was preserved and safely integrated after approval.
- [ ] The installed integration points to the correct vault, with no unresolved placeholders.
- [ ] A concise, permitted, evidence-backed `10-projects/<slug>.md` exists and has been reopened.
- [ ] A **fresh** agent session in the project can actually locate the vault and project note.
- [ ] `brain-status` works read-only.
- [ ] Later, a `save-progress` checkpoint is actually written and `resume-progress` reads it from another session.
- [ ] `audit-docs` changes nothing until a file-by-file plan is approved; `migrate-docs` touches only approved documents.

### Related project documentation

- **Start / command router:** [`workflows/README.md`](workflows/README.md)
- **First-time installation:** [`workflows/project-bootstrap.md`](workflows/project-bootstrap.md)
- **Knowledge onboarding:** [`workflows/project-onboarding.md`](workflows/project-onboarding.md)
- **Everyday coding lifecycle:** [`workflows/development-lifecycle.md`](workflows/development-lifecycle.md)
- **Save / resume:** [`workflows/save-progress.md`](workflows/save-progress.md) · [`workflows/resume-progress.md`](workflows/resume-progress.md)
- **Status / sync:** [`workflows/brain-status.md`](workflows/brain-status.md) · [`workflows/sync-knowledge.md`](workflows/sync-knowledge.md)
- **Documentation audit and migration:** [`workflows/documentation-modernization.md`](workflows/documentation-modernization.md) · [`docs/documentation-migration.md`](docs/documentation-migration.md)
- **Integration, including Claude Code:** [`docs/project-integration.md`](docs/project-integration.md)
- **Upgrading:** [`docs/upgrading.md`](docs/upgrading.md) · [`docs/upgrade-v1.4.md`](docs/upgrade-v1.4.md)
- **Real agent acceptance tests:** [`docs/acceptance-tests.md`](docs/acceptance-tests.md)

### Optional offline integrity tests

From the Second Brain repository root, **if Python 3 is available**:

```powershell
py -3 -m unittest discover -s tests -v
```

Or on a system using `python3`:

```bash
python3 -m unittest discover -s tests -v
```

These check repository/test-helper behavior only. They **cannot certify** Codex/Claude's instruction discovery, sandbox access, or automatic knowledge updates in your actual workspace.

---

**Keep the process simple:** **Download/clone → First-time bootstrap + onboard → Verify in a fresh agent session → Code normally → Save progress when needed → Audit/migrate docs only with an approved plan.**
