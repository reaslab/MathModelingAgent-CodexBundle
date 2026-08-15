# self-audit-loop

## Use when

Use this skill when a result appears supportable but still needs an adversarial review focused on where the current support fails, where the definitions drift, and where the claim may be stronger than the evidence warrants.

Typical signals:

- A derivation, model, or experiment summary looks coherent, but the current support has not been stress-tested against counterexamples or failure regions.
- The work mixes formal results, numerical evidence, and interpretation, and the conclusion may be outrunning the strongest available support.
- Assumptions, metrics, regimes, or success criteria may have shifted during the work.
- Negative or null results exist, but they have not been integrated honestly into the final judgment.

## Inputs

- The current claim, conclusion, or proposed takeaway.
- The derivation, proof status, model assumptions, experiment outputs, and supporting artifacts behind that claim.
- Any prior validation notes, anomalies, failed runs, contradictory examples, or unresolved caveats.
- The originally stated definitions, success criteria, domain of validity, and intended scope of the conclusion.

## Outputs

- A `Risk list` naming the main failure regions, counterexample candidates, and unsupported stretches.
- `Claim downgrades` whenever the current wording exceeds the available support.
- `Requested revisions` describing what must change in the analysis, wording, or evidence record.
- `Unresolved issues` that block stronger conclusions.
- A handoff recommendation to `mathematical-modeling`, `derivation-and-proof-checking`, `research-planning`, or `numerical-experimentation` when support is insufficient.

## Hard rules

- Treat this as a rigid adversarial audit, not as a supportive narrative review.
- Default to searching for counterexamples, failure regions, and claim-breaking regimes before looking for confirming interpretations.
- Check assumption drift explicitly against the original problem statement, model frame, and experiment plan.
- Check definition slippage explicitly for key terms, variables, metrics, regimes, and success criteria.
- Flag unjustified extrapolation whenever a conclusion extends beyond the proved conditions, validated regime, or tested parameter range.
- Flag insufficient evidence whenever the support is too thin, too selective, or too indirect for the current claim strength.
- Check weak negative-result handling explicitly; null findings, failed runs, and contradictions must affect the conclusion instead of being sidelined.
- Downgrade claims when support is mixed or incomplete; do not preserve stronger wording for convenience.
- If support is insufficient, hand the work back to the stage that can strengthen it instead of inventing certainty inside the audit.

## Audit procedure

1. State the exact claim under audit and the strongest support currently available for it.
2. Search first for counterexamples, contradictory cases, failure regions, and breakdown regimes.
3. Compare the final claim against the original assumptions, definitions, and scope to detect assumption drift and definition slippage.
4. Mark any conclusion that extends beyond proved, validated, or tested conditions as unjustified extrapolation.
5. Review the evidence record for selectivity, missing baselines, missing edge cases, or thin support and mark insufficient evidence where appropriate.
6. Review null findings, failed runs, anomalies, and contradictions to determine whether negative-result handling is weak or incomplete.
7. Produce explicit claim downgrades, requested revisions, unresolved issues, and the correct handoff if stronger support still requires more work.

## Required audit checks

- `Assumption drift`: Did the operative assumptions change from the original statement, model, or plan?
- `Definition slippage`: Did any key term, metric, variable, domain, or success criterion change meaning?
- `Unjustified extrapolation`: Is the conclusion being extended beyond what was proved, tested, or validated?
- `Insufficient evidence`: Is the evidence too narrow, too selective, or too indirect for the current wording?
- `Weak negative-result handling`: Were failed runs, null results, anomalies, or contradictions minimized instead of incorporated?

## Claim downgrade guidance

- Use `unsupported` when the evidence does not justify the claim at all.
- Use `overstated` when the direction may be plausible, but the wording is too strong for the support.
- Use `regime-limited` when the claim may hold only inside a narrower domain than currently stated.
- Use `evidence-incomplete` when more derivation, planning, or experiments are required before the claim can be strengthened.

## Handoff guidance

- Return to `mathematical-modeling` when the audit finds unstable assumptions, missing variables, or a model scope that no longer matches the claim.
- Return to `derivation-and-proof-checking` when the audit finds logical gaps, unsupported derivation steps, or proof-level overreach.
- Return to `research-planning` when the audit finds that the current experimental support lacks a clear objective, baseline, decision rule, or coverage plan.
- Return to `numerical-experimentation` when the audit finds missing counterexample searches, weak coverage, unreproduced anomalies, or insufficient negative-result evidence.
