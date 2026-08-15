#!/usr/bin/env python3
"""Run local HMML semantic search."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[4]
HMML_PATH = PROJECT_ROOT / "hmml" / "HMML.json"

_hmml_data: Optional[list] = None
_all_methods: Optional[list] = None
_method_embeddings: Optional[np.ndarray] = None
_model = None


def _load_hmml() -> list:
    global _hmml_data
    if _hmml_data is not None:
        return _hmml_data
    if not HMML_PATH.exists():
        raise FileNotFoundError(f"HMML.json not found at {HMML_PATH}")
    with HMML_PATH.open(encoding="utf-8") as handle:
        _hmml_data = json.load(handle)
    return _hmml_data


def _flatten_methods(data, parent_path: str = "") -> list:
    methods = []
    if isinstance(data, list):
        for item in data:
            methods.extend(_flatten_methods(item, parent_path))
    elif isinstance(data, dict):
        if "method" in data:
            desc = data.get("description", "")
            methods.append(
                {
                    "method_name": data["method"],
                    "category": parent_path,
                    "description": desc,
                    "full_path": (
                        f"{parent_path} > {data['method']}"
                        if parent_path
                        else data["method"]
                    ),
                }
            )
        elif "method_class" in data:
            class_name = data["method_class"].rstrip(":")
            current_path = (
                f"{parent_path} > {class_name}" if parent_path else class_name
            )
            if "children" in data:
                methods.extend(_flatten_methods(data["children"], current_path))
    return methods


def _get_model():
    global _model
    if _model is None:
        from sentence_transformers import SentenceTransformer

        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model


def _get_methods_and_embeddings() -> tuple[list, np.ndarray]:
    global _all_methods, _method_embeddings
    if _all_methods is not None and _method_embeddings is not None:
        return _all_methods, _method_embeddings

    data = _load_hmml()
    _all_methods = _flatten_methods(data)
    if not _all_methods:
        return [], np.array([])

    model = _get_model()
    texts = [
        f"{method['method_name']}: {method['category']}. {method['description']}"
        for method in _all_methods
    ]
    _method_embeddings = model.encode(texts, convert_to_numpy=True)
    return _all_methods, _method_embeddings


def hmml_search(query: str, top_k: int = 3) -> list[dict]:
    """Return the local HMML search result schema."""
    top_k = min(top_k, 10)
    all_methods, embeddings = _get_methods_and_embeddings()
    if not all_methods:
        return [{"error": "HMML data not found or empty"}]

    model = _get_model()
    query_embedding = model.encode(query, convert_to_numpy=True)

    norms = np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    similarities = np.dot(embeddings, query_embedding) / np.where(
        norms == 0, 1e-10, norms
    )
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    return [
        {
            "method_name": all_methods[index]["method_name"],
            "category": all_methods[index]["category"],
            "description": (
                all_methods[index]["description"][:500]
                if all_methods[index]["description"]
                else ""
            ),
            "similarity_score": round(float(similarities[index]), 4),
        }
        for index in top_indices
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    if args.top_k < 1:
        parser.error("--top-k must be at least 1")

    try:
        results = hmml_search(args.query, args.top_k)
    except Exception as exc:
        print(f"HMML search failed: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for index, item in enumerate(results, 1):
            if "error" in item:
                print(item["error"])
                continue
            print(f"{index}. {item['method_name']} [{item['similarity_score']:.4f}]")
            print(f"   Category: {item['category']}")
            print(f"   {item['description']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
