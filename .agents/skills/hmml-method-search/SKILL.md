---
name: hmml-method-search
description: >
  Search the bundled local Hierarchical Mathematical Modeling Library (HMML)
  for candidate mathematical modeling methods. Use during Modeler method
  selection only when the Coordinator reports that the complete local HMML
  availability check passed and sets HMML status to enabled.
---

# HMML Method Search

Use the bundled HMML reference as a local method-discovery aid before selecting a modeling method. It is advisory: compare its candidates against the problem's data, assumptions, constraints, validation needs, and available implementation tools. Never treat a match as proof that a method is appropriate.

## Enablement

- Use this skill only for a Coordinator-resolved `HMML status: enabled`, which requires a successful local semantic scored-search check. File presence alone is insufficient.
- For `HMML status: disabled-by-user` or `disabled-unavailable`, skip this skill and use ordinary method comparison.
- An explicit request to enable HMML does not bypass a failed semantic scored-search check.
- Do not install, repair, download dependencies, or substitute another retrieval algorithm during method selection.

## Search workflow

1. Confirm the resolved setting and the problem scope.
2. Read `hmml/HMML.json` only through the bundled script unless a direct inspection is needed for debugging.
3. Run the complete HMML searcher from the repository root:

   ```text
   python .agents/skills/hmml-method-search/scripts/search_hmml_semantic.py \
     --query "describe the modeling problem in English" --top-k 5 --format json
   ```

   This is the local semantic search adapter:
   `all-MiniLM-L6-v2`, corpus/query embeddings, cosine similarity, and at most
   10 returned methods. Use an available local Python command.
4. Compare two or three returned candidates. For each candidate, state the matching problem structure, assumptions, advantages, limitations, and what evidence would be needed to reject or accept it.
5. Select a method based on the problem, not on the ranking alone. Record the query, returned candidates, selected method, rejected alternatives, and `HMML status` in `modeler/README.md` or the assigned modeling artifact.

## Search limitations

- The bundled data is a reference index, not a current literature database and not a solver.
- Semantic matching requires the embedding model and may require a first-run
  model download. For a primarily Chinese user, if this exceptional first
  download is still needed, set `HF_ENDPOINT=https://hf-mirror.com` for the
  search command and retry once with `HF_ENDPOINT=https://huggingface.co` on
  download/load failure; do not persist that setting. If it is unavailable,
  HMML is unavailable; do not fabricate a substitute score. Try a second
  English query when valid results are weak.
- Do not invent details that are absent from the result or problem materials. Use authoritative external sources separately when current domain facts or literature claims matter.
- If a path becomes missing or data becomes malformed after preflight, report `HMML status: disabled-unavailable` and continue with ordinary method comparison. Do not block the complete modeling workflow solely because HMML became unavailable.

## Script contract

`.agents/skills/hmml-method-search/scripts/search_hmml_semantic.py` accepts a
query, `--top-k` (capped at 10), and `--format text|json`.
It exits nonzero for missing dependencies/model, missing/malformed data, or
invalid arguments. Keep output in the current context unless the assignment
requests a durable search record.
