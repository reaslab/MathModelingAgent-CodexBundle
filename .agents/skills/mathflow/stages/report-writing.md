# report-writing

## Use when

Use this skill when analysis, modeling, derivation, experimentation, and validation stages have produced material that now needs to be turned into a final writeup for a reviewer, collaborator, or decision-maker.

Typical signals:

- The work already has real outputs such as derivations, tables, plots, parameter sweeps, validation notes, or anomaly logs.
- The next step is a report, memo, technical summary, or results section rather than another round of execution.
- The main risk is overstating confidence, hiding caveats, or writing a smooth narrative that is not supported by the recorded evidence.
- The writeup needs to separate proved results, validated findings, exploratory observations, and unresolved limitations.

## Inputs

- The original problem statement, scope, and success criteria.
- The modeling assumptions, variable definitions, equations, and derivation artifacts used in the work.
- Experiment records, tables, plots, solver settings, anomaly logs, and validation outputs from prior stages.
- The current claim-strength assessment, caveats, limitations, and unresolved questions.
- The target audience and expected report format if already known.

## Outputs

- A report structure that covers problem definition, modeling assumptions, derivations, experiments, validation, limitations, and conclusions.
- A final writeup whose claims are tied to actual prior outputs rather than reconstructed from memory.
- Explicit wording that distinguishes proved claims, validated claims, experimental observations, and open questions.
- A limitations section that states what was not established, not tested, or not resolved.

## Hard rules

- Cite actual outputs from previous stages such as derivations, experiment logs, plots, tables, and validation records; do not fabricate confidence or narrative certainty.
- Distinguish proven claims from experimental observations and from tentative interpretations in the final writeup.
- Do not describe a result as established if it was only observed experimentally or only supported in a restricted regime.
- Keep assumptions, parameter regimes, numerical settings, and validation boundaries attached to the claims they support.
- Report important anomalies, failed runs, contradictory checks, and unresolved caveats when they affect interpretation.
- If evidence is incomplete or mixed, weaken the conclusion explicitly instead of smoothing the narrative.

## Problem definition

- State the exact question, task, or phenomenon the work addressed.
- Record the scope, constraints, and success criteria that framed the work.
- Clarify what the report covers and what remains out of scope.

## Modeling assumptions

- List the variables, definitions, assumptions, and chosen model structure used in the analysis.
- State which assumptions are structural, which are approximations, and which were only adopted for tractability.
- Note any assumption changes that occurred during the work and how they affect interpretation.

## Derivations

- Summarize the derivation path, main identities, and key intermediate results that support analytical claims.
- Mark which statements were proved, which were argued heuristically, and which remain conjectural.
- Reference the actual derivation outputs rather than rewriting them with stronger certainty than the original work justified.

## Experiments

- Summarize the experiment objective, setup, parameter ranges, baselines, seeds where applicable, and artifacts produced.
- Report representative outcomes together with the broader evidence set, not only the best-looking run.
- Keep anomalies, failed runs, and unstable cases visible when they materially affect the story.

## Validation

- State what checks were performed, including special cases, limit cases, sensitivity checks, and consistency checks.
- Separate evidence that survived validation from evidence that remained exploratory or mixed.
- Link each major conclusion to the validation record that supports or weakens it.

## Limitations

- State the domain of validity, tested regime, unverified assumptions, and any missing counterexamples.
- Note where evidence depends on numerical settings, restricted parameter ranges, or incomplete validation.
- Make unresolved issues easy for a reviewer to find.

## Conclusions

- Present conclusions in decreasing order of strength: proved results, well-supported validated claims, experimental observations, then open questions.
- Say explicitly when a conclusion is limited to a tested regime, model assumption set, or numerical setup.
- End with the strongest defensible statement, not the most impressive possible statement.

## Claim-framing guidance

- Use language such as `proved`, `derived`, or `follows from` only for claims supported by actual derivation outputs.
- Use language such as `validated within the tested regime` for claims that passed the recorded validation checks.
- Use language such as `observed experimentally`, `appears consistent with`, or `suggests` for empirical patterns that are not proved.
- Use language such as `remains unresolved` or `requires further study` when the evidence is incomplete, contradictory, or highly sensitive.

## Assembly process

1. Collect the actual outputs from each prior stage before drafting the narrative.
2. Build the report structure around the evidence categories, not around a desired conclusion.
3. Draft each section with explicit source grounding for the claims it contains.
4. Review every major statement and label it as proved, validated, observed, tentative, or unresolved.
5. Tighten the conclusion until every sentence matches the available evidence strength.
