---
name: derivation-and-proof-checking
description: Use when a derivation, proof attempt, or mathematical argument must separate fully justified results from partial justification, heuristics, and conjecture.
---

## Use when

Use this skill when the task involves proving a statement, checking a proof, auditing a derivation, or deciding whether an argument is rigorous enough to support a claim.

Typical signals:

- A result is being presented as a theorem, proof, lemma, or formal derivation.
- Some steps are intuitive or skipped, and the confidence level is unclear.
- Numerical evidence, symbolic manipulation, and reasoning are being mixed together.
- The user needs to know whether the conclusion is proved, partially justified, heuristic, or still conjectural.

## Inputs

- The statement, identity, inequality, or claim under review.
- Any existing derivation, proof sketch, symbolic steps, computational evidence, or cited references.
- The assumptions, definitions, and dependencies that the argument relies on.

## Outputs

- A stepwise derivation or proof review with explicit justification labels.
- Named dependencies for each material step, such as definitions, lemmas, theorems, or assumptions.
- An explicit classification of the result as `proof`, `partially justified argument`, `heuristic reasoning`, or `conjecture`.
- A list of proof gaps, unsupported transitions, or unresolved obligations when full proof is not available.

## Hard rules

- Always distinguish `proof`, `partially justified argument`, `heuristic reasoning`, and `conjecture` explicitly.
- Never present numerical support, examples, simulations, or spot checks as proof.
- Surface proof gaps, missing lemmas, and unsupported transitions instead of hiding them.
- Use stepwise derivations for nontrivial arguments; do not compress multiple logical moves into an unexplained jump.
- Name the dependency behind each material step when possible.
- Classify the final output by evidentiary status before stating the main conclusion.

## Output classification

- `proof`: every material step is justified from stated assumptions, definitions, or cited results.
- `partially justified argument`: the main structure is plausible, but one or more material steps are incomplete or not fully established.
- `heuristic reasoning`: the argument gives intuition or likely direction, but it relies on informal approximations, pattern-matching, or unproved transitions.
- `conjecture`: the claim is not established and should be presented only as a proposed statement or hypothesis.

## Process

1. State the target claim and the assumptions that govern it.
2. Break the argument into stepwise derivation blocks.
3. For each material step, name the dependency or state that the dependency is missing.
4. Mark any unsupported transition as a proof gap immediately when it appears.
5. Separate exact reasoning from heuristic commentary and from numerical support.
6. End with an explicit output classification and a short note on what would be required to upgrade the result.

## Gap reporting guidance

- If a lemma is invoked but not established, say so directly.
- If a transformation depends on regularity, convergence, invertibility, or another hidden condition, name that condition.
- If the argument uses numerical evidence, put it in a separate support section and label it as non-proof evidence.
- If a claim cannot currently be proved from the available material, downgrade the classification instead of overstating confidence.

## Handoff guidance

- Move to `research-planning` when the next step is to gather counterexamples, numerical evidence, or experimental support for a conjecture.
- Stay in proof-checking until the current claim has a clear evidentiary classification and all major proof gaps are surfaced.
