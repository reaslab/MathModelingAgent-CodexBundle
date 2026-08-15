---
name: problem-analysis
description: Use when a mathematical or technical problem is still being clarified and the agent must separate stated facts from assumptions before choosing a direction.
---

## Use when

Use this skill when the problem statement is open-ended, underspecified, easy to over-interpret, or likely to tempt the agent into inventing structure too early.

Typical signals:

- The task mixes explicit givens with implied context.
- The objective is not yet precise enough to model, solve, or simulate safely.
- Multiple interpretations are plausible and the right framing matters.
- The agent is about to introduce hidden assumptions, equations, or domain structure not stated by the user.

## Inputs

- The original problem statement, prompt, or research question.
- Any user-provided facts, definitions, constraints, examples, and prior work.
- Any uncertainty about scope, missing data, or ambiguous terminology.

## Outputs

- A short problem restatement in plain language.
- A separated list of knowns, unknowns, and unresolved ambiguities.
- A clear distinction between user-provided facts and agent-added assumptions.
- Success criteria describing what would count as a satisfactory answer or next step.
- A short set of candidate directions, each labeled with why it may fit.

## Hard rules

- Separate given facts from agent-added assumptions explicitly.
- Do not silently invent variables, equations, structure, objectives, or data.
- Mark every assumption as an assumption, not a fact.
- If a key detail is missing, say it is missing instead of filling it in without notice.
- Do not jump to modeling, proof, simulation, or computation before the problem frame is clear enough.
- If multiple interpretations are plausible, surface them instead of pretending one is certain.

## Process

1. Restate the problem in simpler words without changing its meaning.
2. Extract explicit givens into a `Given facts` section.
3. List `Unknowns and ambiguities` that still block confident progress.
4. Add an `Assumptions introduced by the agent` section. If none are needed yet, say `None`.
5. Define `Success criteria` so the next stage has a clear target.
6. Produce a short ranked set of `Candidate directions` for the next stage.

## Red flags

- Treating common domain conventions as if the user already stated them.
- Converting a word problem into equations before naming the interpretation.
- Smuggling in units, boundary conditions, optimization goals, or probability models.
- Acting as if missing definitions are obvious when they materially change the task.

## Handoff guidance

- Move to `mathematical-modeling` only after the facts, assumptions, and success criteria are explicit enough to support a defensible model.
- If the problem is still too ambiguous, keep working in analysis instead of forcing a model.
