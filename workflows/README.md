# Command Router and Default Workflow

Commands below are **natural-language triggers** for agents that have loaded the appropriate instructions. They do not function as standalone CLI executables or background automation.

| Trigger | Procedure | Write scope |
| --- | --- | --- |
| `use developer-second-brain`, `scan using developer-second-brain`, `onboard ...` | [Project onboarding](project-onboarding.md) | Permitted project knowledge note(s) |
| `bootstrap project instructions`, `set up ...` | [Project instruction bootstrap](project-bootstrap.md) | New project `AGENTS.md` only when explicitly requested; existing instructions need specific approval |
| `save-progress`, `checkpoint` | [Save progress](save-progress.md) | Project progress checkpoint |
| `resume-progress`, `continue from checkpoint` | [Resume progress](resume-progress.md) | Read/verify; only user-authorized continuation |
| `sync-knowledge`, `refresh second-brain` | [Sync knowledge](sync-knowledge.md) | Permitted knowledge notes |
| `brain-status`, `show brain status` | [Brain status](brain-status.md) | Read-only |
| `audit-docs`, `review project documentation` | [Documentation audit/modernization](documentation-modernization.md) | **Read-only inventory, evidence, and migration proposal** |
| `migrate-docs`, `documentation modernization` | [Documentation audit/modernization](documentation-modernization.md) | Read-only proposal **until explicit file-level approval**; scoped documentation changes after approval |

**No keyword needed for routine coding:** When a project has a loaded bridge, follow [Everyday context and selective maintenance](development-lifecycle.md). It retrieves relevant project knowledge before meaningful work and may save **material, verified, authorized** changes afterward. It does not scan the entire repository or save a checkpoint on every turn.

## Scope, privacy, and precedence

1. Explicit **`read-only`, `audit only`, `do not save`** or a denial of vault writes overrides every persistence default.
2. `audit-docs` and an initial `migrate-docs` request are **read-only** unless a concrete file-by-file plan has been explicitly approved. Do not remove or reorganize project docs on the basis of a generic request. Follow [documentation modernization](documentation-modernization.md).
3. A `use developer-second-brain` **knowledge onboarding** request authorizes permitted vault notes, not application source changes, documentation reorganization, deployment, or Git state. An **explicit project instruction setup request** authorizes creation from the project template **if no `AGENTS.md` exists**; changes to existing instruction files require specific approval. Follow [project bootstrap](project-bootstrap.md).
4. Normal development requests authorize only their requested code/document changes under project rules; implicit knowledge updates require existing project-level permission to store that information in the vault. Ask when unclear.
5. If project scope is not clear within a multi-project workspace, ask rather than scan every sibling project.
6. Read project-local instructions. Project-owned code, tests, requirements and approved decisions define the actual product; vault instructions define memory handling. Higher-priority instructions always apply.
7. Avoid naming collisions: check existing project identity/path before creating or merging `10-projects/<slug>.md`.
8. Prefer stable, verifiable links. Distinguish documented goals from observed code behavior and record scan limitations.
9. If the vault cannot be read or written due to sandbox restrictions, report it; don't bypass controls or claim successful persistence.

See [knowledge conventions](../docs/knowledge-conventions.md), [project integration](../docs/project-integration.md), and [acceptance tests](../docs/acceptance-tests.md).
