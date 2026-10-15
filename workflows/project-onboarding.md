# Workflow: Project Knowledge Onboarding

**Trigger:** `use developer-second-brain`, `scan using developer-second-brain`, or `onboard <project> into developer-second-brain`.

**Success condition:** A verified, traceable, non-sensitive project note **exists on disk** in the vault, or a clear access/confidentiality blocker is reported. A scan with only a chat summary is **not complete** when persistence is authorized.

## 1. Establish scope

- Identify one or more explicitly named project roots or the unambiguous current application repository. Never assume every sibling directory is in scope.
- Detect the actual language, frameworks, conventions, layout, and project identity from the inspected repository. Never infer them from reusable examples or another project's note.
- Read applicable project `AGENTS.md` files, existing `docs/` indices, README, manifest/build configurations, and active plans **before** sampling relevant implementation files and tests.
- Inspect only enough code to support important claims. Note skipped parts and lack of test execution.
- Read `10-projects/<slug>.md` first if it already exists, and retain historical context.

## 2. Extract and verify

Capture the actual purpose, stack (from manifests), high-level modules, important user-visible functionality, major dependencies, known constraints, key cross-module boundaries, open issues, and source-document links. Separate:

- **Verified (source/test evidence):** directly supported by inspected file paths or executed checks.
- **Documented only:** described in existing docs but not confirmed in code.
- **Proposed/unknown:** tentative behavior or open question; don't promote to fact.

Treat an existing README as evidence of intended behavior, not proof that production works.

## 3. Privacy and classification

- Do not replicate large docs, proprietary code, secrets, keys, customer data, or internal operational information.
- If the vault's sharing policy does not clearly permit sensitive project summaries, ask for authorization **before** copying them; a non-sensitive note with local references may be acceptable if it reveals no restricted details.
- Do not make external requests to upload project context without explicit authorization.

## 4. Persist

- Choose a stable, lowercase `kebab-case` project slug. Store `10-projects/<slug>.md` using [the project-note template](../playbook/templates/project-note.template.md) as a guide; fill only supported fields.
- Create the note if absent. If present, read and merge verified updates without replacing unrelated notes or other work.
- Use relative links **from the note's own directory** to actual project docs and code where accessible. Prefer the project's existing authoritative docs; no duplicated multi-page specs.
- Do not create `progress` notes unless current active work merits a checkpoint or the user asks.
- If this is the first integration, explain that **future ordinary tasks will not automatically load this sibling vault** until a supported project instruction reference is discoverable. Consult [Safe Project Instruction Bootstrap](project-bootstrap.md):
  - A request for *knowledge onboarding only* authorizes vault project notes, **not** application-instruction edits.
  - If the user **explicitly asks for first-time installation** and no project `AGENTS.md` exists, install the [full general-purpose project template](../templates/project-agents.template.md), after verifying path, permissions and scope.
  - If project `AGENTS.md` **already exists**, preserve it and present an additive integration proposal. **Ask for approval before editing it.**
  - Check `CLAUDE.md` / other agent instructions as applicable, and disclose any discovery blockers. Never hide a missing connection.

## 5. Verify and report

- Reopen the saved note; check references/links where practical. Record unsupported or unexamined areas.
- Report exact paths saved, evidence inspected, confidence/coverage, unverified claims, and blockers.
- If `read-only` was requested, perform the analysis but create/update **nothing**.

**Do not:** rewrite application documentation (use [documentation modernization](documentation-modernization.md) as a separate audited and approved workflow), modify source/tests, install an instruction file without an explicit setup request, overwrite existing instructions, install packages, stage files, commit, push, or call an incomplete scan a complete architecture audit. For ordinary future tasks, follow [the development lifecycle](development-lifecycle.md) only when its instructions can actually be loaded.
