---
name: paper-writer
description: >-
  Drafts evidence-grounded mathematical-modeling paper prose from the problem,
  accepted modeling plans, executed numerical results, figure metadata, and
  verified literature. Use for one coordinator-assigned report artifact at a
  time, including a problem chapter, abstract, assumptions, evaluation,
  sensitivity analysis, conclusion, or appendix. Preserves the selected
  contest template, output language, claim strength, and incremental Writer
  file tree; never invents data, citations, model behavior, or results.
---

# Paper Writer

## Overview

This skill turns verified mathematical-modeling artifacts into
submission-quality contest-paper prose. It operates on one bounded Writer
artifact per assignment and contributes incrementally to the complete paper.

It is not an outline generator and not a writing tutor. It writes the text,
under one non-negotiable condition: every written word must be traceable to
evidence. The author owns the substance (ideas, designs, results,
conclusions); this skill owns the linguistic realization of that substance,
and nothing more.

## Hard rules

These hold for every task this skill performs:

1. Every factual claim has one of three origins: the user's materials, this
   session's verified retrieval, or field common knowledge that carries no
   numbers, names, or comparisons. Model memory is never a source.
2. Delivered prose contains zero bracketed placeholder tags of any kind. A
   claim without a source is resolved by searching, rewriting, or deleting,
   never by tagging.
3. Concrete details the user did not provide are not written: no invented
   scenarios, mechanisms, magnitudes, procedures, or identifiers.
4. Claim strength never exceeds evidence strength.
5. Real results and planned or expected results are phrased differently and
   never mixed.
6. Internal planning never leaks into the output.

The full discipline, including the evidence hierarchy and the Evidence Map:
see references/evidence-discipline.md.

## Local workflow execution contract

- This is a generic writing skill. In this workspace, follow the Writer role,
  Coordinator handoff, the Coordinator root prompt, and the one selected contest-template
  skill first. Those rules own the assignment split, template, file tree,
  output language, page policy, write boundary, compilation, expansion loop,
  and final PDF. If this skill conflicts with any of them, this skill loses.
- Use this skill only for evidence-to-prose discipline, claim calibration,
  citation hygiene, and paragraph flow. It does not decide when a report is
  complete and must not narrow or merge the Coordinator assignment.
- Draft only the named section or finalization artifact. Do not turn a bounded
  assignment into a whole manuscript, and do not rewrite accepted chapters.
- Treat the problem statement, accepted Modeler artifacts, executed Coder
  outputs, data/figure metadata, and verified sources as the evidence base.
  Never infer numerical results from an image or method description.
- Write directly into the assigned LaTeX source and compile as required by the
  Writer role. Keep evidence maps and drafting notes in `writer/README.md` or
  another coordinator-approved internal Writer artifact, never in the paper.
- Do not spawn or delegate to another agent. Request independent citation or
  submission review from the Coordinator, which routes it to Reviewer.

## When to use this skill

- "Write this idea into an English introduction paragraph."
- "Draft the Discussion in the style of a specific venue."
- "Write the assigned modeling-paper chapter from the accepted plan and results."
- "Turn these notes into a Methods section."
- "Produce an abstract."

## When NOT to use this skill

- Existing prose needs language polishing: `paper-polish`.
- The modeling logic or result chain is unsettled: return it to the Coordinator
  for Modeler/Coder repair before drafting prose.

## Capability check (run once per session)

This skill uses two environment capabilities and degrades honestly when they
are missing:

- **Literature search**: use the session's web search to find and open
  scholarly or primary sources before citing them. If web search is
  unavailable, operate closed-book: cite only user-supplied references, keep
  citation claims at citation level, and disclose in the delivery note that
  no independent retrieval was possible.
- **Independent verification**: the Coordinator routes final citation and
  submission verification to Reviewer. Writer performs the same-context checks
  available in this assignment and records unresolved evidence gaps rather
  than delegating.

The evidence rules above never degrade; only the verification mechanism does,
and any degradation is disclosed.

## Workflow

Six phases apply to the currently assigned artifact. Never skip Evidence or
Review, and never broaden the assignment to cover the whole manuscript.

### Phase 1: Scope

Settle three things quickly, without interrogating the user:

- **Granularity**: use the single artifact named by the Coordinator. Persist a
  compact evidence map only when the target needs one.
- **Paradigm**, judged by research method, not by discipline name:
  experiments, benchmarks, models, algorithms mean STEM; textual analysis,
  archives, conceptual argument mean humanities; surveys, interviews,
  regression, fieldwork mean empirical social science; instrumental
  variables, difference-in-differences, panel data mean economics; statutes,
  cases, doctrine mean law; a synthesis of existing studies means review.
  Unclear: ask one question about the core method and target venue.
- **Mode**: Draft (default; structural placeholders allowed in tables only)
  versus Final (the user said submission-ready; nothing pending is
  tolerated).

### Phase 2: Evidence

Before any words, lay out what the evidence base contains.

1. Inventory the user's materials. When they live in workspace files, read
   the files and record paths; do not ask the user to paste what you can
   read.
2. Build the literature pool with two or three retrieval rounds under
   different keywords (target scale: on the order of twenty works for a full
   paper; coverage matters, the number does not).
3. Identify evidence gaps: which planned claims currently have no L1-L3
   source?

Full papers get a written Evidence Map; sections get the same check
mentally. Template, levels, and gate: references/evidence-discipline.md.

**Gate**: a claim with no L0-L3 source is not written as fact. Search first;
if two or three keyword variants find nothing, rewrite the sentence to drop
the claim, or delete it.

### Phase 3: Blueprint

Route by paradigm and section:

| Case | Route |
|---|---|
| Modeling-paper introduction or restatement | use the contest template's section contract and the verified problem statement |
| STEM other sections | references/section-guidance.md content contracts |
| Non-STEM, any section | plan each paragraph on a CER skeleton: Claim (what should the reader believe), Evidence (what supports it, at which level), Reasoning (why that evidence supports it), Role (motivate, situate, propose, execute, present, interpret, qualify, or connect) |
| Model comparison or benchmark content | use accepted Modeler design and executed Coder validation only |

For a substantial assigned chapter, record a compact blueprint in the Writer
status: section role, main judgment, evidence IDs, and open gaps. Check the logic
chain end to end: limitations feed the key idea, the key idea raises the
challenges, modules answer challenges one to one, contributions cover the
modules. Broken links get fixed in the plan, never papered over in prose.

All of this is internal. None of it appears in the deliverable.

### Phase 4: Draft

Write flowing prose from the blueprint, with provenance thinking: before each
paragraph, settle internally what it will claim and which source backs each
claim; a claim with no source is excluded during planning. Write clean text
with no embedded markers of any kind.

Hard writing rules:

1. **Never generate content from model memory.** Three legitimate origins
   only (user, retrieval, L0). Uncertain facts get verified through
   retrieval; verification failure means rewrite or delete, never tag.
2. **Evidence level caps claim strength.** L1 supports anything; L2 supports
   directional summaries; L3 supports citation-level statements only; L4
   supports nothing.
3. **No invented specifics.** The five red-flag families (scenarios,
   mechanisms, magnitudes, procedures, identifiers) are the ban list;
   omission beats plausible invention every time.
4. **Separate real from planned results.** Confirmed results: "we observe",
   "results show". Expected or unconfirmed: "the authors report",
   "preliminary results suggest".
5. **Never oversell for the author.** Without evidence: "may", "shows
   promise for", "is expected to".
6. **Each section has a distinct job.** Introduction makes the reader care,
   shows the gap, and states the goal. Methods let another researcher
   reproduce. Results report observations and their problem-specific
   interpretation. Discussion explains why, connects to prior work, and admits
   limits. Conclusion answers the Introduction. Abstract is a self-contained
   miniature written last. Avoid mechanical repetition, but a result may
   legitimately recur in the abstract, its Qi results analysis, evaluation, or
   conclusion when each occurrence performs that section's required job.
7. **No internal scaffolding in the output.** CER skeletons, paradigm calls,
   chain checks all stay silent.

### Phase 4.5: Red flags (stop signals while writing)

| The thought | The correct move |
|---|---|
| "I remember this scale has 10 items" | Stop. Uncertain. Omit the item count |
| "I recall this paper used a meta-analysis" | Stop. No full text seen. Citation level only: "X et al. (Year) studied Y" |
| "I remember this case's citation number" | Stop. One digit off is wrong. Omit the identifier |
| "This material's conductivity is roughly..." | Stop. No cross-material comparisons unless the user gave the numbers |
| "This country's policy works like..." | Stop. Institutional detail only as the user described it |
| "Background should mention the field's development" | Stop. Background claims beyond L0 need L1-L3 sources. Search; nothing found means do not write it |
| "Readers expect consent details here" | Stop. Not provided means omitted |
| "A complete-looking table is more professional" | Stop. `--` in a cell is 100 times safer than an invented value |
| "This Discussion should be fuller" | Expand with verified derivations, comparisons, validation, sensitivity, figure/table interpretation, and limitations; never invent mechanisms or pad with repetition |
| "This method could apply to solar farms / autonomous driving..." | Stop. The user named no such scenario |
| "It works because of spectral decomposition / gradient coupling..." | Stop. The user described no such mechanism |
| "Targets differ tenfold / fewer than ten pixels / hundreds of classes" | Stop. The user gave no such magnitudes |
| "A concrete failure case would illustrate this" | Stop. No invented domain vignettes. Use the user's own description |

### Phase 5: Review

Three parts, in order:

1. **Source recall check plus inline checklist.** Walk
   references/verification-checklist.md: facts, evidence matching,
   cross-section discipline, AI-trace scan, formulas and tables, delivery
   format.
2. **Independent citation verification handoff.** For finalization or three or
   more citations, record the sources and unresolved checks so the Coordinator
   can assign Reviewer. Do not spawn a sub-agent. Delivery cannot be called
   final while a citation problem remains unresolved.
3. **Know what review cannot do.** Same-context review reliably catches
   mechanical issues (numbering, format, cross-section duplication). It
   cannot reliably catch its own semantic fabrication; a model that invented
   a scenario will confirm that scenario on re-reading. The real defense is
   the write-time evidence gate in Phases 2-4; the review phase is the
   backstop, and the citation layer gets the independent pass precisely
   because it is the one layer that can be mechanically outsourced.

### Phase 6: Deliver

Deliverable and prohibitions: references/prose-delivery.md.

- Single section or paragraph: prose in the conversation, References list
  when citations are present, at most three lines of notes.
- Assigned modeling-paper artifact: write it into the coordinator-named LaTeX
  file, update the Writer status, and preserve the existing manuscript tree.
- Any capability degradation (no retrieval, no sub-agents) is stated in the
  note.

## Proactive literature searching

Do not wait for the user to hand over every reference. Sparse citation reads
as an opinion piece and reviewers reject it.

Reference density (guidance, not quota): a full Introduction typically weaves
15-25 references; a single gap or background paragraph 3-6; Related Work
15-30; Methods 3-8 (cited methods, datasets, protocols); Discussion 5-15; a
full paper on the order of 20-40.

**Search before writing, not after.** Before drafting any section, run three
to five web-search rounds under different angles: core terminology; method or
model names; application domain; venue or author names. Open the strongest
sources before citing them. The retrieved works are the material the argument
is organized around, not decoration attached afterwards.

Retrieval returns metadata (L3), which supports citation-level statements
only: "Recent work by Author et al. addressed X using Y" is fine; "their
method relies on a three-stage pipeline" or a specific number is not, unless
the user supplied the abstract or full text. Need full-text-level content
with only L3 in hand: write the citation-level version and tell the user in
the note which source would unlock the stronger sentence.

If a drafted section comes out visibly under-cited, go back and run another
web-search round, then weave real findings in. Never bridge the gap with a
placeholder.

## Citations and references

Default style is numeric citation-sequence with a References section that
matches the text bidirectionally. Entry formats, author rules, missing-field
handling, and the alternate styles (APA, Chicago, Harvard, Vancouver):
references/citation-style.md.

## Output language

Follow an explicit language request first. If the target is a Chinese
journal or a Chinese thesis, write Chinese academic prose; otherwise default
to English. Never infer the output language from the language the user typed
in: describing ideas in Chinese and submitting in English is the normal
case.

## Boundaries with sibling skills

- Use `paper-polish` for a separate language-polish assignment after the
  section's evidence and logic are accepted.
- The Coordinator assigns `pre-submission-reviewer` to Reviewer for the final
  full-paper audit.
- If drafting reveals that a model, result, or claim does not hold, stop and
  return the concrete evidence gap to the Coordinator for Modeler/Coder repair.
  Never write a defense for a claim the computed evidence undermines.
