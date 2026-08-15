---
name: mathematical-modeling
description: Use when the problem frame is clear enough to introduce variables, assumptions, and candidate mathematical structures while documenting model tradeoffs and risks.
---

## Use when

Use this skill when the task has moved past basic clarification and now needs a mathematical representation that can support derivation, estimation, simulation, or proof planning.

Typical signals:

- Variables, symbols, states, or parameters need to be defined.
- Competing model families are possible and the tradeoffs matter.
- Assumptions must be made explicit before proceeding to calculations.
- The likely failure modes of a model need to be called out early.

## Inputs

- The analyzed problem statement and success criteria.
- Explicit givens, unresolved uncertainties, and any accepted assumptions.
- Available data, constraints, physical interpretation, and intended use of the model.

## Outputs

- A named candidate model or model family with justification.
- A variables and notation section with consistent symbols and meanings.
- A recorded assumptions section, including which assumptions are strong.
- A short tradeoff discussion covering why this model was chosen over alternatives.
- A `Likely failure regions` section describing where the model may break down.

## Hard rules

- Define variables and notation before using them in equations or prose.
- Record every modeling assumption explicitly.
- Mark strong assumptions as `strong assumption` where they appear.
- State the main tradeoff behind the selected model.
- Name at least one likely failure region or invalid operating regime.
- Do not present a convenient model as ground truth.

## Process

1. State the modeling goal: prediction, explanation, optimization, approximation, control, or another target.
2. Define variables, parameters, units, and notation with stable names.
3. Propose one primary model and, when useful, one alternative model family.
4. Record assumptions, distinguishing routine simplifications from strong assumptions.
5. Explain the model selection tradeoff: realism vs tractability, interpretability vs fidelity, deterministic vs stochastic, continuous vs discrete, or similar.
6. Mark likely failure regions, edge cases, and conditions where the model should not be trusted.

## Variable and notation guidance

- Reuse standard notation only when it helps clarity in the stated domain.
- Prefer one symbol per concept and one concept per symbol.
- Include units or dimensions when they matter.
- Avoid introducing notation that is not used by the selected model.

## Assumption recording rules

- Keep assumptions in their own section.
- If an assumption is convenient but weakly justified, say so directly.
- If an assumption materially narrows applicability, label it `strong assumption`.
- If the model depends on unavailable data or calibration, say what is missing.

## Model selection tradeoffs

- Favor the simplest model that can still answer the stated question.
- Prefer a richer model only when the extra complexity changes decisions or conclusions.
- If two models are viable, explain why one is the current default and what would trigger switching.

## Failure regions

- Nonlinear effects ignored by a linear approximation.
- Boundary regimes, sparse data, extrapolation, or scale changes.
- Sensitivity to parameters that are uncertain or unobserved.
- Violations of independence, stationarity, equilibrium, or homogeneity assumptions.

## Handoff guidance

- Move to planning or execution only after the notation, assumptions, and failure regions are explicit enough that downstream work can test the model instead of rediscovering it.
