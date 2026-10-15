# Reusable Engineering Principles

**Status:** Foundational guidance  
**Scope:** Project-agnostic  
**Review:** Reassess when applying to an actual project.

## Understand before changing

- Read relevant code, requirements, tests, and configuration before editing.
- Identify expected behavior, affected boundaries, dependencies, and failure cases.
- Explain trade-offs for meaningful design changes; avoid speculative abstractions.

## Optimize for correctness and maintenance

- Prefer the smallest coherent solution that meets the requirement.
- Use conventions and dependencies already established by the project, unless there is a justified reason to change them.
- Separate concerns where doing so provides clarity; avoid layering for its own sake.
- Design external interfaces and state transitions explicitly.

## Defend system boundaries

- Validate untrusted input and enforce authorization at the correct boundary.
- Consider concurrency, retries, partial failures, idempotency, resource limits, and data integrity when relevant.
- Protect secrets and personal information; use synthetic test data by default.
- Make observability useful without exposing sensitive data.

## Verify and communicate

- Add meaningful tests for important or regression-prone behavior, using existing tools when possible.
- Execute relevant checks and report which ones passed, failed, or could not run.
- Preserve backward compatibility unless an approved change requires otherwise.
- Document significant decisions near the owning codebase and link to their rationale.
- Distinguish known facts, assumptions, and proposals.

## Respect ownership and approval

- A project repository owns its current behavior, requirements, deployment configuration, and architecture decisions.
- Reusable advice is guidance, not an instruction to override project requirements.
- Ask before destructive actions, broad migrations, public API breaking changes, or other high-impact operations.
- Do not commit or push without explicit authorization.
