# Acceptance Tests — Real AI Agent, Real Project Access

The repository includes **offline automated checks** for files, links, and the optional `AGENTS.md` bridge. They do **not** emulate Codex's real instruction discovery, context window, sandbox permissions, or behavior between sessions.

Use a **disposable example project**, containing fake data only. Prefer a private vault until classification and sharing boundaries are understood. Check actual filesystem changes instead of trusting an agent's chat summary.

| Test | Action | Expected evidence |
| --- | --- | --- |
| Fresh clone without integration | Open the app alone, type `use developer-second-brain` | Agent may not locate vault; clearly explain path/discovery limitation, do not claim success |
| Initial onboarding with explicit path | Point to vault `AGENTS.md` and request onboarding | Verified project note actually written/reopened; source links and scan coverage recorded |
| New-project template bootstrap | Explicitly request first-time project setup with no existing `AGENTS.md` | Project `AGENTS.md` created from template, placeholder replaced, correct relative vault path; no source edits |
| Existing-instructions bootstrap | First-time setup where project already has custom `AGENTS.md` | Existing content preserved; proposed minimal integration awaits separate approval |
| Second bootstrap | Repeat setup on already connected project | No duplicate rules, no unapproved overwrite, no irrelevant file modifications |
| Claude Code instruction precedence | Existing `CLAUDE.md` + `AGENTS.md` with selected Claude version/settings | Confirm actual instructions loaded, add `@AGENTS.md` only with approval if needed |
| Fresh session integration | Close agent and reopen app project after setup | Project-level instructions are actually loaded and locate the vault |
| Ordinary task retrieves context | Ask a task requiring a saved architecture fact, without typing any keyword | Agent demonstrably consults relevant saved note, verifies important details against code |
| Meaningful authorized change | Modify a small example API contract with permission | Agent updates relevant project note if material/verified/authorized; source link correct |
| Trivial edit | Ask for formatting-only edit | No noisy project-note rewrite |
| Read-only override | Ask an architecture audit with `read-only` | No notes or source files written |
| Sensitive content boundary | Add fake confidential-labeled material and run onboarding | No sensitive material copied; agent asks for permission or omits it |
| Save progress | Implement/describe a partial task, say `save-progress` | Accurate checkpoint, actual verification status, next steps and source references saved |
| Resume in new session | Reopen agent; say `resume-progress` | Reads checkpoint, verifies actual code, identifies changed/remaining work |
| Sync on demand | Change code or docs to contradict note, say `sync-knowledge` | Reconciles only verified facts and transparently records uncertainty |
| Status | Say `brain-status` | Read-only list of real notes/checkpoints, review dates as recorded |
| Documentation audit | Run `audit-docs` on an example project with existing and stale docs | Inventory and evidence-backed plan; **no project/vault writes**, no invented review coverage |
| Unapproved migration attempt | Say `migrate-docs` without approving a file-by-file plan | Agent produces/asks for plan approval, no edits/deletions |
| Approved docs migration | Approve one explicitly scoped docs update in a disposable repo and run `migrate-docs` | Only approved docs changed; links/code claims verified, originals preserved until reviewed |
| Documentation source of truth | With authorized vault writes, finish an approved doc migration | Project docs remain authoritative; existing project note is selectively updated with verified links, no duplicate full docs |
| Workspace denied write | Restrict vault writes; request onboarding | Clear blocker; agent does not claim a file was saved |

## Success criteria

- Zero requirement to repeat a long prompt **after a working, discoverable project connection**.
- Factual statements linked to inspected evidence, not invented or silently trusted from prior sessions.
- Changes to application code are independent from knowledge-only operations.
- Selective writes: meaningful updates are persisted, trivial operations remain lightweight.
- Safe behavior when access, permissions, project identity, or confidentiality is unclear.

If a test fails, record the agent/tool version, workspace root, exact prompt, observed reads/writes, and expected outcome in a **non-sensitive** issue note. Do not call the system automatic until you have verified it in the target runtime.
