# HMML semantic search

The standalone backend searches the bundled `hmml/HMML.json` with
`sentence-transformers/all-MiniLM-L6-v2` and cosine similarity.

Python 3.12 is the preferred and tested runtime for the complete semantic
backend. Use the first available option below. Do not install uv solely for
this setup.

## uv

```text
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

On native Windows, activate with `.venv\Scripts\activate` instead. Let uv use
its normal shared cache; do not create a project-specific cache unless the
user requests one.

## Conda

Use Conda when uv is unavailable:

```text
conda create --prefix ./.venv python=3.12
conda activate ./.venv
python -m pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

## Existing Python

When neither uv nor Conda is available, select an existing Python interpreter,
prefer version 3.12, and use it to create a local virtual environment:

```text
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install -r .agents/skills/hmml-local-setup/requirements.txt
```

The exact executable may be `python3`, `python3.12`, or `py -3.12` depending on
the platform. On native Windows, activate with `.venv\Scripts\activate`.
Report the selected version. Do not install the requirements into a
system-managed interpreter or require elevated privileges.

Run the local semantic search:

```text
python .agents/skills/hmml-method-search/scripts/search_hmml_semantic.py \
  --query "predict future values from historical time series data" \
  --top-k 5 --format json
```

The retrieval algorithm uses embeddings from
`all-MiniLM-L6-v2` followed by cosine similarity. The first run may download the
model from Hugging Face; pre-cache it for an offline environment. For a
primarily Chinese user, set `HF_ENDPOINT=https://hf-mirror.com` only for the
first model-loading command, then retry once with
`HF_ENDPOINT=https://huggingface.co` if that download/load fails. This matches
the Dockerfile's mirror-first fallback; never persist the endpoint or replace
the retrieval algorithm. If the model cannot load from either endpoint, HMML is
unavailable and no alternate score is returned.

The result schema is `method_name`, `category`, `description`, and
`similarity_score`. Scores are retrieval signals only; the Modeler must still
check assumptions, constraints, data, validation, and implementation feasibility.
