---
name: numerical-experimentation
description: Use when mathematical or model-based work needs reproducible numerical experiments, retained anomalies, and report-ready evidence rather than a single illustrative run.
---

## Use when

Use this skill when the next stage is to run simulations, solvers, parameter sweeps, numerical approximations, or computational studies that should produce evidence robust enough for later reporting and validation.

Typical signals:

- A claim depends on behavior observed across parameter ranges, seeds, tolerances, or initial conditions.
- One successful run is not enough to justify the conclusion.
- The work needs tables, plots, or summary metrics that will feed a later report or validation stage.
- Failures, instabilities, or surprising outputs might be informative and should not be discarded.

## Inputs

- The research objective, claim, or hypothesis the experiments are meant to inform.
- The model, governing equations, algorithms, assumptions, and computational constraints.
- Candidate parameters, ranges, seeds, baselines, solver settings, and target metrics.
- Any known anomalies, prior failed runs, or domain-specific edge cases already identified.

## Outputs

- A reproducible experiment record with parameters, seeds where applicable, software or method settings, and run identifiers.
- A body of evidence covering representative runs, sweeps, repeats, and failures rather than one cherry-picked outcome.
- Tables, plots, and summary metrics prepared so they can feed a later report or result-validation stage.
- A retained anomaly log covering failed runs, unstable cases, and unexpected qualitative behavior for later follow-up.

## Hard rules

- Record the exact parameter settings, seeds where applicable, tolerances, and method choices for every reported run.
- Do not present one cherry-picked run as the main evidentiary basis when richer evidence is available or required.
- Retain anomalies, failed runs, and unstable outputs for later validation instead of deleting them from the record.
- Distinguish exploratory runs from confirmatory runs.
- Keep outputs structured so tables, plots, and summary metrics can be reused by later reporting and validation steps.
- If randomness is involved, state whether seeds were fixed, varied, or sampled and why.

## Experiment record requirements

- `Objective`: what question this run or batch addresses.
- `Model and method`: model version, numerical method, solver, or approximation used.
- `Parameters`: all primary parameter values, ranges, and fixed controls.
- `Seed policy`: fixed seed, repeated seed set, or deterministic claim that no seed applies.
- `Run outcomes`: success, failure, instability, timeout, divergence, or other terminal state.
- `Artifacts`: tables, plots, traces, logs, and summary metrics produced.

## Evidence guidance

- Prefer parameter sweeps, repeated runs, or comparative batches over single examples.
- Report both headline metrics and failure-oriented diagnostics such as residuals, instability counts, or convergence warnings when they matter.
- Keep representative examples, but place them inside a broader evidence set that shows how typical they are.
- If some runs fail or behave anomalously, record them alongside successful runs and note possible causes without prematurely filtering them away.

## Reporting handoff guidance

- Prepare tables that make comparisons across parameter settings, baselines, or repeated runs easy to inspect.
- Prepare plots that show trends, regimes, sensitivities, or breakdown points rather than only best-case trajectories.
- Produce summary metrics that aggregate across runs when aggregation is justified, and keep the raw run context available.
- Label which artifacts are suitable for narrative reporting and which exist mainly for audit or debugging support.

## Exit criteria

- Another reviewer can reproduce the reported evidence from the recorded parameters and seeds where applicable.
- The evidence set includes successes, failures, and anomalies relevant to the claim.
- The produced artifacts are organized well enough to feed `result-validation` without rerunning experiments just to reconstruct context.
