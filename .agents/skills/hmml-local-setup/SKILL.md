---
name: hmml-local-setup
description: Set up, check, diagnose, or update the bundled local HMML method-search tool and data. Use it automatically before complete modeling workflows unless the user disables HMML; keep dependencies in a project-local environment.
---

# HMML Local Setup

Keep HMML as a local, optional project tool. This skill checks availability but does not choose a mathematical method.

## Automatic availability setup

Before a complete modeling workflow, unless the user explicitly disables HMML,
create or reuse a project-local environment, install the bundled requirements,
then run the checker. A model download is allowed when required for semantic
search. Do not install globally, alter an unrelated environment, update HMML
data, or block the modeling workflow if setup fails.

- Exit 0: resolve `HMML status: enabled`.
- Setup/check failure or no usable Python: resolve `HMML status: disabled-unavailable`,
  retain the concise reason, and continue with ordinary method comparison.
- Explicit user disablement: do not check; resolve `HMML status: disabled-by-user`.

The checker runs the local semantic search and accepts the tool only when
`all-MiniLM-L6-v2` produces a nonempty method candidate with a finite numeric
cosine `similarity_score`. Merely finding `HMML.json` or other package files is
not an availability result.

## Chinese-user model download route

When the latest user request is primarily Chinese, use the same Hugging Face
fallback route as the product Dockerfile for a needed first model download:
try `https://hf-mirror.com` first, then retry once with
`https://huggingface.co`. Set `HF_ENDPOINT` only on the setup/check command;
do not persist it in shell profiles, project configuration, or global package
configuration. This applies to the embedding-model download only, not to an
already cached local model or ordinary Python package installation. If both
endpoints fail, resolve `HMML status: disabled-unavailable` and continue the
workflow.

## Check workflow

1. Prefer Python 3.12 for HMML setup and semantic-backend diagnostics. Detect
   available tooling and use it in this order: uv, Conda, then an existing
   `python` or `python3` interpreter to create `.venv`. Do not require or
   install uv when it is absent. Read `references/semantic-backend.md` before
   creating or changing the Python environment.
2. Confirm the repository root and scoring paths:
   - `hmml/HMML.json`
   - `.agents/skills/hmml-method-search/scripts/search_hmml_semantic.py`
3. Create or reuse `.venv` (with uv, Conda, or `python -m venv`), activate it,
   install `.agents/skills/hmml-local-setup/requirements.txt`, then run the
   bundled checker with that environment's Python. For a primarily Chinese user
   when a model download is needed, use the mirror-first fallback above:

   ```text
   HF_ENDPOINT=https://hf-mirror.com python .agents/skills/hmml-local-setup/scripts/check_hmml.py
   # If the model download/load fails, retry once:
   HF_ENDPOINT=https://huggingface.co python .agents/skills/hmml-local-setup/scripts/check_hmml.py
   ```

4. If the checker passes, report the local data size, method count, semantic model, top method, cosine score, and Python command used.
5. If it fails, identify the missing or malformed path, report the concise
   reason, and disable HMML for this workflow. Do not silently modify global
   packages.

## Update and repair

Only update the HMML data when the user explicitly asks. Preserve the current files until the replacement has been validated as JSON and produces a successful smoke query. Record the source, date, and any transformation in the local handoff. Do not silently replace the local index with a hosted service.

## Relationship to method search

`hmml-method-search` is the separate method-selection skill. Use it only after
this check resolves `HMML status: enabled`.
