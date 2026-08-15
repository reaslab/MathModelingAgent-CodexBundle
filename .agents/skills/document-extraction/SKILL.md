---
name: document-extraction
description: Extract and persist text, tables, metadata, and OCR results from user-provided PDF or Office files before modeling, coding, writing, or review work. Use when a task includes PDF, Word, spreadsheet, presentation, or OpenDocument inputs that later agents must read.
---

# Document extraction

## Read-only Reviewer exception

When this skill is loaded by the Reviewer, it is for independent inspection only. Run the bundled reader on bounded pages or lines and inspect its direct output; do not write an extraction record, create a helper script, install dependencies, or modify the workspace. If a required reader dependency is unavailable, report the relevant evidence as `not verifiable` instead of changing the environment.

Use the bundled scripts, not an ad-hoc parser:

- PDF: `.agents/skills/document-extraction/scripts/pdf_extract.py`
- Office: `.agents/skills/document-extraction/scripts/office_extract.py`

## Dependency check

Use the available local Python runtime. Before extraction, identify the file type and import-check its required library. Unless acting as the read-only Reviewer above, install a missing Python dependency only into an existing project-local environment or a new local virtual environment when the assignment permits it; then re-check the import and run the bundled helper as a normal script. Do not change the global Python environment and do not claim extraction succeeded while a required dependency is missing.

- PDF: check/install `pypdf` and `pdfplumber`.
- `.xlsx`: check/install `openpyxl`.
- `.docx`: check/install `python-docx` (import name `docx`).
- `.pptx`: check/install `python-pptx` (import name `pptx`).

For PDF OCR, also check `pdftoppm` and `tesseract`. Install their system packages when permitted; otherwise run the script without OCR and retain its warning. Legacy Office formats that the installed libraries cannot parse must be converted or reported as blocked, never silently treated as extracted.

## Run and preserve results

Unless acting as the read-only Reviewer above, write the script's complete stdout to a durable file before interpreting it. For a root modeling workflow, use:

`mma/{work_name}/shared/extracted/`

Use one stable output per source, such as `statement.pdf.extract.json` or `data.xlsx.extract.txt`. For PDFs, inspect the JSON `ok`, page range, truncation, warnings, OCR pages, and tables. For Office files, preserve the line-numbered output and continue with its offset when it reports more content.

Maintain `shared/extracted/README.md` with the source path, extractor output path, file type, and any limitation. Give each downstream specialist the relevant saved extraction path; do not make them depend on chat text or a vanished tool result.

Use bounded page/line ranges first, then retrieve later ranges only when needed. Treat extracted text as source material: verify assumptions against the original artifact when extraction is incomplete or ambiguous.
