#!/usr/bin/env python3
# Bundled helper for the document-extraction skill.
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any


MIN_TEXT_CHARS_FOR_NO_OCR = 80


def compact(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def effective_len(text: str) -> int:
    return len(re.sub(r"\s+", "", text or ""))


def table_to_markdown(table: list[list[Any]]) -> str:
    rows: list[list[str]] = []
    width = 0
    for row in table:
        normalized = ["" if cell is None else compact(str(cell)).replace("\n", " ") for cell in row]
        rows.append(normalized)
        width = max(width, len(normalized))
    if not rows or width == 0:
        return ""
    rows = [row + [""] * (width - len(row)) for row in rows]
    header = rows[0]
    body = rows[1:] or [[""] * width]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def page_count_with_pypdf(filepath: str) -> int:
    from pypdf import PdfReader

    return len(PdfReader(filepath).pages)


def extract_with_pypdf(filepath: str, start_page: int, end_page: int) -> dict[int, str]:
    from pypdf import PdfReader

    reader = PdfReader(filepath)
    out: dict[int, str] = {}
    for index in range(start_page - 1, min(end_page, len(reader.pages))):
        try:
            out[index + 1] = compact(reader.pages[index].extract_text() or "")
        except Exception as exc:
            out[index + 1] = ""
            print(f"warning: pypdf page {index + 1} extraction failed: {exc}", file=sys.stderr)
    return out


def extract_with_pdfplumber(filepath: str, start_page: int, end_page: int) -> tuple[int, dict[int, str], dict[int, list[str]]]:
    import pdfplumber

    texts: dict[int, str] = {}
    tables: dict[int, list[str]] = {}
    with pdfplumber.open(filepath) as pdf:
        total_pages = len(pdf.pages)
        for page_no in range(start_page, min(end_page, total_pages) + 1):
            page = pdf.pages[page_no - 1]
            texts[page_no] = compact(page.extract_text(x_tolerance=1, y_tolerance=3) or "")
            page_tables: list[str] = []
            try:
                for table in page.extract_tables() or []:
                    md = table_to_markdown(table)
                    if md:
                        page_tables.append(md)
            except Exception as exc:
                print(f"warning: pdfplumber page {page_no} table extraction failed: {exc}", file=sys.stderr)
            tables[page_no] = page_tables
    return total_pages, texts, tables


def render_page(filepath: str, page_no: int, tmpdir: str, dpi: int) -> str:
    prefix = os.path.join(tmpdir, f"page-{page_no}")
    cmd = [
        "pdftoppm",
        "-f",
        str(page_no),
        "-l",
        str(page_no),
        "-r",
        str(dpi),
        "-png",
        "-singlefile",
        filepath,
        prefix,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=90)
    return prefix + ".png"


def ocr_image(image_path: str, languages: str) -> str:
    base_cmd = ["tesseract", image_path, "stdout", "-l", languages, "--psm", "6"]
    try:
        result = subprocess.run(base_cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
        return compact(result.stdout)
    except subprocess.CalledProcessError:
        if languages != "eng":
            result = subprocess.run(
                ["tesseract", image_path, "stdout", "-l", "eng", "--psm", "6"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=120,
            )
            return compact(result.stdout)
        raise


def append_limited(chunks: list[str], text: str, max_chars: int) -> tuple[bool, bool]:
    current = sum(len(chunk) for chunk in chunks)
    if current >= max_chars:
        return False, True
    remaining = max_chars - current
    if len(text) <= remaining:
        chunks.append(text)
        return True, False
    chunks.append(text[:remaining])
    return True, True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("--page-offset", type=int, default=1)
    parser.add_argument("--page-limit", type=int, default=30)
    parser.add_argument("--max-chars", type=int, default=60000)
    parser.add_argument("--ocr-dpi", type=int, default=220)
    parser.add_argument("--ocr-lang", default="eng+chi_sim")
    args = parser.parse_args()

    warnings: list[str] = []
    ocr_pages: list[int] = []
    table_count = 0
    filepath = os.path.abspath(args.filepath)

    try:
        total_pages = page_count_with_pypdf(filepath)
    except Exception as exc:
        print(
            json.dumps({"ok": False, "reason": f"Cannot open PDF: {exc}"}, ensure_ascii=False),
            flush=True,
        )
        return 0

    start_page = max(1, args.page_offset)
    end_page = min(total_pages, start_page + max(1, args.page_limit) - 1)
    if start_page > total_pages:
        print(
            json.dumps(
                {
                    "ok": False,
                    "reason": f"Page offset {start_page} is out of range for this PDF ({total_pages} pages)",
                    "pages": total_pages,
                },
                ensure_ascii=False,
            ),
            flush=True,
        )
        return 0

    texts: dict[int, str] = {}
    tables: dict[int, list[str]] = {}
    try:
        total_pages, texts, tables = extract_with_pdfplumber(filepath, start_page, end_page)
    except Exception as exc:
        warnings.append(f"pdfplumber unavailable or failed: {exc}; fell back to pypdf text extraction")
        texts = extract_with_pypdf(filepath, start_page, end_page)
        tables = {page_no: [] for page_no in range(start_page, end_page + 1)}

    can_ocr = shutil.which("pdftoppm") is not None and shutil.which("tesseract") is not None
    if not can_ocr:
        warnings.append("OCR skipped: pdftoppm or tesseract is not installed")

    with tempfile.TemporaryDirectory(prefix="pdf-ocr-") as tmpdir:
        for page_no in range(start_page, end_page + 1):
            text = texts.get(page_no, "")
            if effective_len(text) >= MIN_TEXT_CHARS_FOR_NO_OCR:
                continue
            if not can_ocr:
                continue
            try:
                image_path = render_page(filepath, page_no, tmpdir, args.ocr_dpi)
                ocr_text = ocr_image(image_path, args.ocr_lang)
                if effective_len(ocr_text) > effective_len(text):
                    texts[page_no] = ocr_text
                    ocr_pages.append(page_no)
            except Exception as exc:
                warnings.append(f"OCR failed on page {page_no}: {exc}")

    chunks: list[str] = []
    truncated = end_page < total_pages
    for page_no in range(start_page, end_page + 1):
        page_chunks = [f"[Page {page_no}]"]
        text = texts.get(page_no, "")
        if text:
            page_chunks.append(text)
        else:
            page_chunks.append("(No extractable text found on this page.)")
        for table_index, table_md in enumerate(tables.get(page_no, []), 1):
            table_count += 1
            page_chunks.append(f"[Table {page_no}.{table_index}]")
            page_chunks.append(table_md)
        added, char_truncated = append_limited(chunks, "\n".join(page_chunks) + "\n\n", args.max_chars)
        if char_truncated:
            truncated = True
            break
        if not added:
            truncated = True
            break

    content = compact("".join(chunks))
    if not content:
        content = "(No extractable text found in the selected PDF pages.)"

    print(
        json.dumps(
            {
                "ok": True,
                "pages": total_pages,
                "start_page": start_page,
                "end_page": end_page,
                "processed_pages": end_page - start_page + 1,
                "truncated": truncated,
                "ocr_pages": ocr_pages,
                "table_count": table_count,
                "warnings": warnings,
                "content": content,
                "preview": content[:500],
            },
            ensure_ascii=False,
        ),
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
