# HMML Local Tool

HMML is the bundled local mathematical-modeling method index derived from
[HKUST USAIL/LLM-MM-Agent](https://github.com/usail-hkust/LLM-MM-Agent).
The local search tool compares a problem description with its method entries
to suggest candidates for Modeler to evaluate. It is not a solver, a code
generator, or a current literature database.

## Use

For a complete modeling workflow, HMML is enabled by default. Before Modeler
uses it, Coordinator creates or reuses the project-local environment, installs
the HMML requirements, and runs one semantic-search preflight. A passing check
must return a real candidate with a finite cosine `similarity_score` from
`all-MiniLM-L6-v2`; the presence of `HMML.json` alone is not enough.

When that check passes, Modeler uses `.agents/skills/hmml-method-search/` and
the local semantic search command:

```text
python .agents/skills/hmml-method-search/scripts/search_hmml_semantic.py \
  --query "optimize resource allocation under constraints" \
  --top-k 5 --format json
```

The command embeds the method corpus and query with `all-MiniLM-L6-v2`,
computes cosine similarity, and returns at most 10 candidates. Modeler compares
the candidates with the problem's assumptions, constraints, data, validation
needs, and implementation feasibility; a ranking is advisory, not a method
selection by itself.

An explicit request to disable HMML skips setup and uses ordinary method
comparison. If automatic setup previously failed, an explicit request to enable
HMML retries the same preflight; it does not bypass it.

A failed setup, model download, or semantic query disables HMML for the current
workflow without blocking ordinary modeling; no substitute retrieval score or
algorithm is used. The first model download for a primarily Chinese request
tries the mirror route first and then the official Hugging Face endpoint. The
Python environment remains project-local and no system Python packages are
modified.

## Setup and diagnostics

Python 3.12 is the preferred and tested version for the complete semantic
backend. Use an environment tool already available on the machine. Prefer uv,
then Conda, then an existing Python interpreter to create a local virtual
environment; do not require users to install uv only for HMML.

With uv:

```text
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

With Conda when uv is unavailable:

```text
conda create --prefix ./.venv python=3.12
conda activate ./.venv
python -m pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

With neither tool, create a local virtual environment from an existing Python
3.12 interpreter:

```text
python -m venv .venv
source .venv/bin/activate
python -m pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

On native Windows, activate `.venv` with `.venv\Scripts\activate`.

For automatic setup or an explicit HMML check/repair, use
`.agents/skills/hmml-local-setup/`:

```text
python .agents/skills/hmml-local-setup/scripts/check_hmml.py
```

The checker validates the JSON index and runs a local smoke query. Its first
semantic run may download the embedding model, but it does not start a network
service or install global dependencies.

## Provenance and license

The two data files were copied without modification from the upstream
[`MMAgent/HMML`](https://github.com/usail-hkust/LLM-MM-Agent/tree/main/MMAgent/HMML)
directory. They were compared byte-for-byte with the upstream `main` branch on
2026-08-12:

| File | Size | SHA-256 |
| --- | ---: | --- |
| `HMML.json` | 180,173 bytes | `b146fc917a8b93ce9607f8660b2a9d852b3900db2d3b82c29fad0c2c49c441b9` |
| `HMML.md` | 161,895 bytes | `b407823ab7d96ef517ad7f67dc64d5a5c5a18656a296fbe982bd15429abb28db` |

These upstream files are not covered by this project's MIT relicensing. At the
time of verification, the upstream repository's root `LICENSE` contained
GPL-3.0 while its README described the source code as CC BY-NC 4.0; neither HMML
file included a file-specific license notice. Preserve this attribution and
consult the upstream project's current terms or maintainers before
redistributing the HMML data.
