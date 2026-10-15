# Optional Integration Helper

**No script is required** to use the Second Brain in an AI session with a known, accessible path. For future sessions to load the vault automatically, however, your coding agent needs a small persistent instruction bridge. You can ask the agent to *propose* the bridge and approve its creation, or [add it manually](../docs/project-integration.md#manual-integration-no-script).

`scripts/connect-project.py` is a Python 3 **standard-library-only** opt-in convenience utility for safely creating the full project engineering template on a **new project** or managing a short marked bridge in a project that already has instructions. It is not a project scanner or documentation migrator and never modifies project code, dependencies, Git state or vault notes. New bridges also point to the `audit-docs` / `migrate-docs` safety workflow, but neither command runs automatically.

If no project `AGENTS.md` exists and you want the **full general-purpose engineering template**, preview it, then explicitly apply:

```powershell
py -3 .\scripts\connect-project.py --project ..\sample-app --full-template
py -3 .\scripts\connect-project.py --project ..\sample-app --full-template --apply
```

For a small bridge (including existing project instructions), use the original behavior:

```powershell
# From developer-second-brain/; previews ONLY
py -3 .\scripts\connect-project.py --project ..\sample-app

# Apply to create a new bridge, or append it to AGENTS.md
py -3 .\scripts\connect-project.py --project ..\sample-app --apply

# Already connected to V1.1? Preview an update of the marked block
py -3 .\scripts\connect-project.py --project ..\sample-app --refresh

# Apply ONLY after reviewing the diff (preserves content outside marked block)
py -3 .\scripts\connect-project.py --project ..\sample-app --refresh --apply
```

**Safety:** Default preview-only. `--full-template` refuses existing `AGENTS.md` files rather than overwriting them. `--refresh` is necessary to update an existing marked bridge and does not write unless `--apply` is also present. The helper refuses malformed or duplicate markers, protects unrelated `AGENTS.md` content, and only attempts an update in the selected target project. Always review diffs and respect company repository permission rules. For paths on different drives, use a manually verified accessible path.
