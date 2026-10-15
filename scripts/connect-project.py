#!/usr/bin/env python3
"""Preview or maintain a small, optional AGENTS.md bridge to developer-second-brain."""
from __future__ import annotations

import argparse
import difflib
import os
from pathlib import Path
import sys

START = '<!-- developer-second-brain:begin -->'
END = '<!-- developer-second-brain:end -->'


def managed_block(relative: str) -> str:
    return f"""{START}
## Shared Developer Second Brain

Knowledge vault relative to this `AGENTS.md`: `{relative}/`

For **ordinary significant development tasks** (without needing to say `use developer-second-brain`):
1. Read `{relative}/workflows/development-lifecycle.md` and only relevant stored project context.
2. Verify important saved facts against current project docs/code; do not load the entire vault.
3. After material, verified changes, selectively update the relevant vault project note **only when permitted**; do not write for trivial changes, read-only tasks, or unapproved confidential material.

For explicit `use developer-second-brain`, `save-progress`, `resume-progress`, `sync-knowledge`, `brain-status`, `audit-docs`, and `migrate-docs`:
1. Read `{relative}/workflows/README.md` and the matching workflow.
2. Respect the project's own instructions, source of truth, user authorizations, and vault privacy restrictions.
3. Onboarding saves permitted project knowledge to the vault by default; `save-progress` creates a checkpoint; `brain-status` and the initial `audit-docs` / `migrate-docs` proposal are read-only.
4. Knowledge-only commands do not authorize app code changes, deployments, dependency updates, or Git commits/pushes.
5. Documentation migration implementation requires approval of a specific file-by-file plan. If the vault is inaccessible, report the actual limitation; do not claim a note was saved.
{END}"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True, help='Existing application or workspace directory')
    parser.add_argument('--apply', action='store_true', help='Write only selected AGENTS.md (otherwise preview)')
    parser.add_argument('--refresh', action='store_true', help='Replace existing marked block, preserving surrounding text')
    parser.add_argument('--full-template', action='store_true', help='Preview/install full project engineering template ONLY when AGENTS.md does not exist')
    args = parser.parse_args()

    vault = Path(__file__).resolve().parent.parent
    project = args.project.expanduser().resolve()
    if not project.is_dir() or project == vault or vault in project.parents:
        print('ERROR: Select an existing project outside the vault.', file=sys.stderr)
        return 2
    if not (vault/'workflows'/'development-lifecycle.md').is_file():
        print('ERROR: Missing expected development workflow in vault.', file=sys.stderr)
        return 2
    try:
        relative = os.path.relpath(vault, project).replace(os.sep, '/')
    except ValueError:
        print('ERROR: Different drives; use manual integration with an accessible path.', file=sys.stderr)
        return 2
    target = project/'AGENTS.md'
    if target.is_symlink():
        print('ERROR: Refusing to modify a symlinked AGENTS.md; review the real target manually.', file=sys.stderr)
        return 2
    if args.full_template:
        if args.refresh:
            print('ERROR: --full-template cannot be combined with --refresh.', file=sys.stderr)
            return 2
        if target.exists() or target.is_symlink():
            print('ERROR: Existing AGENTS.md must be preserved. Use bridge preview or obtain approval for manual integration.', file=sys.stderr)
            return 2
        template_path = vault/'templates'/'project-agents.template.md'
        try:
            template = template_path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            print(f'ERROR: Cannot read project template: {exc}', file=sys.stderr)
            return 2
        placeholder = '{{SECOND_BRAIN_RELATIVE_PATH}}'
        if template.count(placeholder) != 1:
            print('ERROR: Template must have exactly one vault-path placeholder.', file=sys.stderr)
            return 2
        proposal = template.replace(placeholder, relative)
        print(f'Target: {target}')
        print(f'Vault relative path: {relative}/')
        print('Action: create full engineering instructions (AGENTS.md absent)')
        print('--- proposed unified diff ---')
        sys.stdout.writelines(difflib.unified_diff([], proposal.splitlines(keepends=True),
                                fromfile='AGENTS.md (absent)', tofile='AGENTS.md (proposed)'))
        if not args.apply:
            print('\nPREVIEW ONLY — no files changed. Add --apply to create after review.')
            return 0
        try:
            with target.open('xb') as stream:
                stream.write(proposal.encode('utf-8'))
        except OSError as exc:
            print(f'ERROR: Cannot safely create AGENTS.md: {exc}', file=sys.stderr)
            return 2
        if target.read_text(encoding='utf-8') != proposal:
            print('ERROR: Write verification failed.', file=sys.stderr)
            return 2
        print(f'INSTALLED: New engineering AGENTS.md at {target}')
        return 0
    try:
        original_bytes = target.read_bytes() if target.exists() else b''
        current = original_bytes.decode('utf-8-sig')
    except (OSError, UnicodeError) as exc:
        print(f'ERROR: Cannot read AGENTS.md safely: {exc}',file=sys.stderr)
        return 2
    bom = b'\xef\xbb\xbf' if original_bytes.startswith(b'\xef\xbb\xbf') else b''
    newline = '\r\n' if b'\r\n' in original_bytes else '\n'
    block = managed_block(relative)
    occurrences = (current.count(START), current.count(END))
    if occurrences not in [(0,0), (1,1)]:
        print('ERROR: Malformed or duplicate markers; manual review required.',file=sys.stderr)
        return 2
    if occurrences == (1,1):
        start = current.index(START)
        end = current.index(END)
        if end < start:
            print('ERROR: Reversed markers; manual review required.',file=sys.stderr)
            return 2
        end += len(END)
        old_block = current[start:end].replace('\r\n','\n')
        if old_block == block:
            print(f'ALREADY CURRENT (no changes): {target}')
            return 0
        if not args.refresh:
            print(f'EXISTING CONNECTION FOUND: {target}')
            print('Run again with --refresh to preview an update to the managed block; no files changed.')
            return 0
        proposed = current[:start] + block.replace('\n',newline) + current[end:]
        mode = 'refresh marked instructions'
    else:
        separator = '' if not current.strip() else ('\n' if current.endswith(('\n','\r')) else '\n\n')
        proposed = current + (separator + block + '\n').replace('\n',newline)
        mode = 'create bridge' if not original_bytes else 'append bridge'
    print(f'Target: {target}')
    print(f'Vault relative path: {relative}/')
    print(f'Action: {mode}')
    print('--- proposed unified diff ---')
    diff = difflib.unified_diff(current.splitlines(keepends=True), proposed.splitlines(keepends=True),
                                fromfile='AGENTS.md current', tofile='AGENTS.md proposed')
    sys.stdout.writelines(diff)
    if not args.apply:
        print('\nPREVIEW ONLY — no files changed. Add --apply to write after review.')
        return 0
    if target.exists() and target.read_bytes() != original_bytes:
        print('ERROR: AGENTS.md changed after preview; retry.', file=sys.stderr)
        return 2
    content = bom + proposed.encode('utf-8')
    try:
        # Exclusive creation for nonexistent files; otherwise refuse silently changing a replaced file.
        if original_bytes or target.exists():
            if not target.is_file():
                print('ERROR: AGENTS.md is not a regular file.',file=sys.stderr)
                return 2
            # Note: verify metadata/content immediately prior to replace; no unrelated text altered.
            target.write_bytes(content)
        else:
            with target.open('xb') as stream:
                stream.write(content)
    except OSError as exc:
        print(f'ERROR: Failed to write AGENTS.md: {exc}',file=sys.stderr)
        return 2
    if target.read_bytes() != content:
        print('ERROR: Write verification failed.',file=sys.stderr)
        return 2
    print(f'CONNECTED: Updated only {target}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
