---
name: mcm-writing
description: >
  MCM/ICM paper writing guide built on the bundled template_en.
  Activate only when the coordinator has identified an English MCM/ICM report.
  Provides file-by-file instructions tied to the LaTeX template structure.
  Enforces English output and forbids fallback from CUMCM/template_zh failures.
description_zh: >
  美赛论文写作指南，基于内置 template_en 模板。
  仅在 Coordinator 已识别为英文 MCM/ICM 论文时激活。
  提供与 LaTeX 模板结构逐文件对应的使用说明。
  强制英文输出，禁止作为 CUMCM/template_zh 失败后的兜底。
---

# MCM/ICM Paper Writing Guide

This skill is built on the `assets/latex-templates/template_en/` template and provides file-by-file template usage instructions. MCM/ICM papers are written in English. The paper is the sole deliverable -- judges evaluate your modeling process, communication clarity, and analytical depth entirely through the written report.

---

## 0. Purpose and Runtime Boundaries

This skill writes English MCM/ICM papers. It is not a contest classifier and must not be used as a fallback when the Chinese CUMCM template or xelatex compilation fails.

Within this local workflow, this skill owns the English MCM/ICM template, section contract,
language, figure/equation conventions, and contest-specific content guidance.
The Coordinator and native Writer role own scheduling, assignment granularity,
global page policy, final acceptance, and rework routing. If a generic writing
skill conflicts with this contract, follow this skill and the Coordinator. If
the report is short, expand with verified derivation, experiments, baselines,
validation, sensitivity/robustness, and limitations; do not stop merely because
the prose is concise or the PDF compiles.

Hard boundaries:

- Use this skill only after Coordinator has identified an English MCM/ICM contest/report.
- Output language must be English, including headings, captions, body text, summary sheet, and status replies to Coordinator.
- The template must come from `assets/latex-templates/template_en/`; copy the entire directory into the active case `writer/` folder before editing.
- `writer/README.md` must record `Template source: assets/latex-templates/template_en/`, `Copied entrypoint: main.tex`, `Template family evidence: article + natbib/bibliography pairing`, `Output language: English`, and `Language evidence: ...`.
- The final article body and PDF must not expose local file addresses, workspace paths, template source paths, code/data filenames, tool artifact paths, or agent handoff wording; keep path evidence only in `writer/README.md` / Paper Status and use semantic figure/table captions, labels, and code descriptions in the paper.
- If the template directory is missing, `xelatex` is unavailable, or compilation returns a fatal LaTeX error, report the blocker. Do not switch to `template_zh`, Chinese output, or an ad-hoc template.

---

## 1. Template Overview

The template is located at `assets/latex-templates/template_en/`, based on the `article` document class with standard LaTeX packages.

`main.tex` includes the following files via `\input{}`:

```
\input{abstract}           -> abstract.tex          Summary Sheet
\input{01-introduction}    -> 01-introduction.tex   Introduction + problem reformulation
\input{02-assumptions}     -> 02-assumptions.tex    Assumptions + Notation
\input{03-q1}              -> 03-q1.tex             Problem 1 (Model -> Solution -> Results)
                              (04-q2.tex, ...)      Problems 2, 3, ... (Writer creates as needed)
\input{sensitivity}        -> sensitivity.tex       Sensitivity Analysis
\input{strengths}          -> strengths.tex         Strengths and Weaknesses
\input{conclusions}        -> conclusions.tex       Conclusions
\bibliography{references}  -> references.bib        References
\input{appendix}           -> appendix.tex          Appendix
```

Copy the entire template directory to `writer/` before editing. From the active case directory, compile locally with `latexmk -xelatex -interaction=nonstopmode -halt-on-error writer/main.tex`. If `latexmk` is unavailable, run the full `xelatex -> bibtex -> xelatex -> xelatex` sequence from the `writer/` directory and retain its logs.

The template pairs `\usepackage[numbers]{natbib}` with `\bibliographystyle{plainnat}` -- do not modify this pairing.

Core design principle: each sub-problem gets its own file (`03-q1.tex`, `04-q2.tex`, ...),
each containing the full structure (analysis, model, solution, results).
Writer creates additional files as needed and adds `\input{}` lines to `main.tex`.

The template, language, and file tree are hard acceptance gates, not style suggestions. The final paper must retain template_en's `main.tex`, `abstract.tex`, `01-introduction.tex`, `02-assumptions.tex`, per-problem `03-q1.tex` / `04-q2.tex` / ..., `sensitivity.tex`, `strengths.tex`, `conclusions.tex`, optional `letter.tex` only when required, `appendix.tex`, `references.bib`, `figure/`, `main.pdf`, and `README.md`. `writer/main.pdf` is only the compiled artifact: after Reviewer PASS, place one final PDF in `mma/{work_name}/` with a concise filesystem-safe filename derived from the paper title or task topic, never `main.pdf`, `final.pdf`, or `{work_name}.pdf`.

---

## 2. File-by-File Usage Guide

### 2.1 abstract.tex -- Summary Sheet (the single most important page)

The Summary Sheet is a standalone one-page document. Many judges read it before (and sometimes instead of) the full paper. It determines first-round triage.

In one page: explain what you did, how you did it, and what you found. Open with 1-2 sentences on the problem context. Then for each sub-problem, name the specific model/method and report the key quantitative result. End with 2-3 sentences on model strengths and limitations, followed by keywords.

No figure/table references, no bibliography citations, no lengthy derivations.

The Summary Sheet should be written last, after all sub-problems are completed.

Length: exactly 1 page.

### 2.2 01-introduction.tex -- Introduction

Combines problem restatement, literature review, and approach overview in one section. Unlike CUMCM which has a separate restatement chapter, MCM integrates problem reformulation into the introduction narrative.

Start with real-world context (2-3 sentences), describe the specific contest challenge (2-3 sentences), provide a brief literature review (1 paragraph, 3-4 references), translate the problem into precise mathematical language (define decision variables, objective functions, constraints), and conclude with an overview of the approach for each sub-problem.

This file does not depend on Modeler/Coder outputs and can be written first.

Develop the introduction until it fully states the problem, motivation, and approach; do not compress required context to meet a fixed length.

### 2.3 02-assumptions.tex -- Assumptions and Notation

Two sections: Assumptions and Notation.

Assumptions: MCM judges expect each assumption to be justified, not merely stated. For each, write a clear statement then 1-2 sentences explaining why it is reasonable and how it affects the model. Typically 5-8 assumptions, ordered from most fundamental to most technical. Can be incrementally expanded as new sub-problems introduce additional assumptions.

Notation: Three-line table format. Group by category: input variables, intermediate variables, model parameters. Define every symbol before it appears in the text.

Develop this section until every assumption is justified and every symbol is defined.

### 2.4 03-q1.tex, 04-q2.tex, ... -- Per-Problem Chapters (paper core)

The template provides `03-q1.tex` as a skeleton with four subsections:

```
\section{Problem 1: Modeling and Solution}
  \subsection{Problem Analysis}       -- Core challenge and approach strategy
  \subsection{Model Development}       -- Motivation -> math formulation -> notation
  \subsection{Model Solution}          -- Algorithm -> computation -> figures inline
  \subsection{Results and Discussion}  -- Quantitative results with analysis
```

Writer creates an independent file for each sub-problem, adds the `\input{}` line to `main.tex`.

Problem Analysis: Identify the key difficulty and the high-level strategy. 1-2 paragraphs.

Model Development: Start with motivation (why this method, what phenomena or data features led to the choice), then present the mathematical formulation. Complete derivations with text connecting equations. Use `\equation` or `\align` for key equations, reference with `\eqref{eq:xxx}`.

Model Solution: Algorithm description, computational process. Cite standard algorithms. Place figures at the point of first reference using `[H]` float option. Each figure/table followed by analysis text.

Results and Discussion: Every conclusion supported by specific numbers. Error analysis, comparisons in tabular form. Use `Figure~\ref{fig:xxx}` and `Equation~\eqref{eq:xxx}` with non-breaking spaces.

When referencing figures, read the corresponding `.png.metadata` file for Coder's computed statistical insights (Autonomous Insights). All statements about figure/chart characteristics must come from metadata -- you cannot see the image content.

A strong MCM paper contains 10-15 figures total across all sections.

Each Qi file can be written as soon as its Modeler plan and Coder results are ready, without waiting for other problems.

The depth of each Qi chapter follows its verified model, results, and discussion; do not pre-allocate fixed page counts.

### 2.5 sensitivity.tex -- Sensitivity Analysis

Almost mandatory for competitive MCM papers. Select 2-4 key parameters, vary each while holding others constant. Present as line plots. Address which parameters are most influential, whether the model is robust, and where it breaks down.

This file requires results from at least some sub-problems.

Include the analyses needed to establish sensitivity, stability, and limits of the reported conclusions.

### 2.6 strengths.tex -- Strengths and Weaknesses

Two subsections. Discuss in paragraph form (not bullet lists). Each strength/weakness supported by evidence from results. Pair each weakness with a mitigation strategy or future direction. This balanced evaluation often distinguishes Outstanding from Meritorious papers.

This file should be written after all sub-problems are complete.

Explain substantive strengths, weaknesses, and appropriate improvement directions.

### 2.7 conclusions.tex -- Conclusions

Concisely restate key findings with quantitative results. Highlight the most novel aspect. End with broader implications or future extensions. Do not introduce new results.

State the validated conclusions and their scope without omitting material implications.

### 2.8 appendix.tex -- Appendix

Three subsections: Core Code, Supplementary Figures, Detailed Derivations.

Core Code: Include it only if Coordinator explicitly marks `Code appendix: required` for a 高教社杯 task. Then use `\lstinputlisting` to include Coder's actual code files; do not use `\begin{lstlisting}` to manually type code. Path from `writer/` uses the `../coder/` prefix. Each code segment is preceded by a brief description. For every other task, omit code listings and retain reproducibility evidence in Coder's scripts and README.

Example:
```tex
The following implements the prediction model for Problem 1:
\lstinputlisting[language=Python, caption={Problem 1: Prediction Model},
  firstline=30, lastline=85]{../coder/solve_q1.py}
```

### 2.9 Letter or Memo (if required by the problem)

Some MCM/ICM problems require a one-page letter/memo to a non-technical audience. Create a new file `letter.tex` and add `\input{letter}` to `main.tex`.

Write in clear, accessible language without jargon. Use concrete numbers and actionable recommendations. Structure: context (1 paragraph) -> key findings (2-3 paragraphs) -> recommendation (1 paragraph). No equations.

---

## 3. References (references.bib)

MCM papers should include references from diverse sources: foundational method papers, related work, algorithm/software documentation, domain background. The number of references should match actual citation needs — there is no hard minimum.

When adding or validating references, use the session's available web search in multiple directions: model methodology, application domain, and evaluation methodology. Open sources to verify metadata and ensure citation diversity.

Every `.bib` entry must include `author`, `title`, `year`. Use descriptive keys like `smith2023wildfire`. Never fabricate references from memory.

Cite whenever using others' methods, data, or conclusions.

---

## 4. LaTeX Conventions and Evidence Coverage

Equations: Introduce every equation with a text lead-in. After a block equation, provide interpretation. Never present consecutive equations without connecting text. Inline math: `$...$`, display math: `\begin{equation}...\end{equation}`.

Figures: Resolution 300 dpi minimum. Use `\includegraphics[width=0.8\textwidth]{figure/xxx.png}`. Tables use `booktabs` three-line format. Bold best results in comparison tables. Column headers include units.

Length and evidence coverage: unless the user explicitly specifies a page count, use 25 substantive body pages as an asymmetric scrutiny baseline. Count only the rendered PDF interval from `Problem Background` (or the contest-equivalent first body section) through the page immediately before `References`, excluding front matter, bibliography, and explicitly marked appendices/code listings. The baseline is neither a hard floor nor a completion cap. Fully develop verified derivations, data provenance, experiments, baseline comparisons, sensitivity analysis, robustness checks, and limitations; reaching the baseline never permits early finalization while valid evidence remains unexplained. Above the baseline, there is no length penalty when the paper remains coherent, relevant, and evidence-backed. Recompile and record the physical PDF body-page count. Below the baseline, the larger the deficit, the more concrete and evidence-backed the coverage-matrix rationale Reviewer must require; Writer may not claim the problem is simple or pad the paper. Only Reviewer may make the final determination.

Path control: the body, summary sheet, captions, tables, references, and rendered PDF outside appendix code listings must not contain `/tmp/`, `mma/`, `../coder/`, template source paths, or raw `.py` / `.csv` / `.json` / `.xlsx` / `.metadata` filenames.

---

## 5. Incremental Writing Rhythm

Papers are built incrementally as modeling and coding progress, not written all at once. Writer is dispatched multiple times by Coordinator, each time handling part of the report.

Typical rhythm:

First round (after problem is available, no Modeler/Coder dependency):
  Copy the complete template from assets/latex-templates/template_en/ to writer/.
  Record template source, copied entrypoint, template family evidence, output language, and language evidence in writer/README.md.
  Set \title{} in main.tex to a specific title based on the problem (not a placeholder).
  Write 01-introduction.tex.
  Use websearch + webfetch to build initial references.bib entries.
  Write initial assumption skeleton in 02-assumptions.tex.
  Compile to confirm framework builds.

When each sub-problem Qi's Modeler plan + Coder results arrive:
  Create the Qi file (e.g., 04-q2.tex) with full four-section structure.
  Add \input{} to main.tex.
  Supplement 02-assumptions.tex with Qi-specific assumptions.
  Use websearch + webfetch to find references relevant to this chapter's methods, append to references.bib.
  Compile PDF to confirm.

After all sub-problems are complete (finalization — this phase is MANDATORY):
  Update abstract.tex with specific quantitative results from all sub-problems.
  Write sensitivity.tex, strengths.tex, conclusions.tex.
  Finalize appendix.tex with \lstinputlisting for real code only when `Code appendix: required`; otherwise retain only applicable supplementary figures and derivations.
  Verify \title{} is a specific title (update if still placeholder).
  Supplement references.bib if needed via websearch + webfetch.
  Final compilation.

When updating incrementally, read existing .tex files first. Append new content; do not delete or rewrite completed sections.

---

## 6. Compilation Environment and Common Errors

| Item | Value |
|------|-------|
| Engine | XeTeX (xelatex), native Unicode |
| Document class | article with standard LaTeX packages |
| OS | Local system |
| Packages | A local TeX distribution with xelatex, bibtex, and required packages |

Common errors:

`natbib Error: Bibliography not compatible` -- .bib entry missing author or year. Check every entry.

`Citation 'x' undefined` -- \cite key does not match .bib key (case-sensitive), or bibtex did not run. Run the complete bibliography compilation sequence.

`File 'x.png' not found` -- Copy charts to writer/figure/ first, reference as figure/x.png. Compile from writer/, not the bundled template source.

`Overfull \hbox` -- Usually long equations or URLs. Split equations with \multline. Use \url{} for URLs. This is not an ignorable warning in finalization: inspect the final compiler output or `.log`, repair every `Overfull \hbox` / `Overfull \vbox`, recompile, and record a zero-warning result before final PASS.
