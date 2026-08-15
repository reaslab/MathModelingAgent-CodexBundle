# MMA shared workspace instructions

These repository instructions apply to the Coordinator and every configured leaf role. The complete Coordinator operating contract is loaded only from the root Codex configuration; do not duplicate it here.

- Use only the configured native roles: `modeler`, `coder`, `writer`, and `reviewer`. A leaf role must not create or manage other agents.
- Keep durable task artifacts under `mma/{work_name}/`. Do not prepend the repository directory name, repeat `mma/`, or create a nested repository.
- Preserve user inputs and unrelated files. Treat files outside the assigned role boundary as read-only unless the user explicitly authorizes a change.
- Follow the requested output language, contest/template requirements, and deliverable location. Keep claims tied to inspectable artifacts and evidence.
- Before editing code or configuration, inspect the relevant local files and preserve existing user changes.
