#!/usr/bin/env python3
"""Validate the local HMML data and search tool."""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[4]
HMML_ROOT = PROJECT_ROOT / "hmml"
SKILLS_ROOT = PROJECT_ROOT / ".agents" / "skills"
DATA = HMML_ROOT / "HMML.json"
SEMANTIC_SEARCH = SKILLS_ROOT / "hmml-method-search" / "scripts" / "search_hmml_semantic.py"


def count_methods(node: object) -> int:
    if isinstance(node, list):
        return sum(count_methods(item) for item in node)
    if isinstance(node, dict):
        return int(isinstance(node.get("method"), str)) + count_methods(node.get("children", []))
    return 0


def validate_scored_result(output: str) -> tuple[str, float]:
    results = json.loads(output)
    first = results[0]
    method_name = first["method_name"]
    similarity_score = first["similarity_score"]
    if not isinstance(method_name, str) or not method_name.strip():
        raise ValueError("empty method_name")
    if isinstance(similarity_score, bool) or not isinstance(similarity_score, (int, float)):
        raise ValueError("similarity_score is not numeric")
    score = float(similarity_score)
    if not math.isfinite(score):
        raise ValueError("similarity_score is not a finite value")
    return method_name, score


def main() -> int:
    missing = [
        str(path.relative_to(PROJECT_ROOT))
        for path in (DATA, SEMANTIC_SEARCH)
        if not path.is_file()
    ]
    if missing:
        print("Missing HMML paths:", ", ".join(missing), file=sys.stderr)
        return 2
    try:
        data = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid HMML JSON: {exc}", file=sys.stderr)
        return 2
    method_count = count_methods(data)
    if method_count == 0:
        print("HMML JSON contains no method entries", file=sys.stderr)
        return 2
    command = [sys.executable, str(SEMANTIC_SEARCH), "--query", "predict future values from historical time series data", "--top-k", "1", "--format", "json"]
    completed = subprocess.run(command, cwd=PROJECT_ROOT, capture_output=True, text=True, check=False)
    if completed.returncode != 0:
        print(completed.stderr.strip() or "HMML smoke query failed", file=sys.stderr)
        return completed.returncode
    try:
        method_name, similarity_score = validate_scored_result(completed.stdout)
    except (IndexError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"HMML scored-search smoke query failed: {exc}", file=sys.stderr)
        return 2
    print(
        f"HMML scored search OK: {method_count} methods; data={DATA.stat().st_size} bytes; "
        f"backend=semantic; model=all-MiniLM-L6-v2; top_method={method_name}; "
        f"similarity_score={similarity_score:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
