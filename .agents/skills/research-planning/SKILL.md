---
name: research-planning
description: Use when numerical, empirical, or experiment-driven mathematical work needs a stated research objective and an explicit execution plan before running computations.
---

## Use when

Use this skill when the next stage involves simulations, parameter studies, numerical experiments, computational searches, or empirical checks that should be planned before execution.

Typical signals:

- The user wants to run experiments, sweeps, or simulations.
- Multiple parameter choices, methods, or baselines could change the conclusion.
- The work needs stopping conditions, fallback branches, or a decision rule before computation starts.
- There is a risk of running numerical work without a clearly stated research question.

## Inputs

- The current claim, hypothesis, or phenomenon under investigation.
- The model, assumptions, available methods, and computational constraints.
- Any prior results, candidate baselines, and target metrics already known.

## Outputs

- A research objective that states what claim or phenomenon each planned experiment supports or refutes.
- An experiment plan with parameter sweeps, baselines, metrics, and execution order.
- Stop rules describing when to halt, refine, or branch.
- Fallback branches for inconclusive, unstable, or contradictory outcomes.

## Hard rules

- State the claim or phenomenon that each experiment is meant to support or refute.
- Define parameter sweeps, baselines, metrics, stop rules, and fallback branches before numerical work begins.
- Do not start numerical work with no stated research objective.
- Keep exploratory experiments tied to a question, not just to available tooling.
- Distinguish confirmatory checks from exploratory searches.
- Record what outcome would count as support, refutation, or inconclusive evidence.

## Planning process

1. Write the research objective in one or two sentences.
2. Map each planned experiment to the claim or phenomenon it addresses.
3. Define the baseline method, baseline parameter setting, or comparison case.
4. Specify parameter sweeps, sampled ranges, and any fixed controls.
5. Choose metrics that determine success, failure, sensitivity, or instability.
6. Add stop rules for convergence, budget exhaustion, instability, or repeated null findings.
7. Add fallback branches for failed runs, ambiguous results, or invalid model assumptions.

## Required plan sections

- `Research objective`
- `Experiments and linked claims`
- `Baselines`
- `Parameter sweeps`
- `Metrics`
- `Stop rules`
- `Fallback branches`

## Metric and baseline guidance

- Use baselines that make the main claim interpretable, not just easy to run.
- Include at least one metric that can reveal failure modes, not only headline performance.
- If qualitative behavior matters, say what observable pattern counts as confirmation or contradiction.
- If uncertainty matters, note whether repeated runs, seeds, or sensitivity checks are required.

## Handoff guidance

- Move to execution only after every planned experiment has a stated objective, comparison point, and decision rule.
- If no research objective can be stated, return to `problem-analysis` or `mathematical-modeling` instead of starting computation.
