# MP-1 Measurement and Scoring Spec v0.1

**Status:** pre-registration candidate; freeze only after pilot validation

## Principle

Do not compress MP-1 into one opaque score.

Report a small vector of mechanistic and capability outcomes so a treatment can be better on efficiency and worse on serendipity without one result hiding the other.

## Paired-world analysis

The preferred confirmatory design is paired by hidden world seed.

For each measured world instance W:

- run P0 with a fresh isolated subject;
- run P1 with another fresh isolated subject of the same body/model configuration;
- randomize which treatment is run first operationally;
- do not share subject state between pair members.

This controls much of the world-instance difficulty without allowing carryover.

Additional treatments (P0.5/S3/S4) are later contrasts and should not dilute the first P0↔P1 causal test.

## Primary outcome 1 — task correctness

Score from evaluator-only ground truth, not a model judge where avoidable.

### T1 stale interpretation

Binary components:

- identifies the correct interpretation/resource that requires re-evaluation;
- identifies the material changed dependency/version;
- does not incorrectly claim the old interpretation is proven false when ground truth only establishes staleness;
- does not select a distractor as the primary target.

Report each component plus an exact-task-success boolean requiring the preregistered mandatory subset.

### T2 common-cause diagnosis

Binary/count components:

- identifies the seeded common cause;
- cites the minimum preregistered number of independent supporting resources;
- distinguishes direct evidence from inference;
- avoids an incompatible distractor cause.

Again report components, not only total.

## Primary outcome 2 — source fidelity

For each material final claim classify:

- exact authoritative source/version cited or addressably referenced;
- supporting but derived/non-authoritative source only;
- unsupported;
- contradicted by authoritative ground truth.

Primary metric:

> proportion of material claims grounded in an acceptable source/version for that claim type.

Machine PASS must not be scored as valid support for broader product PASS when the canonical world defines only narrow mechanical scope.

## Primary outcome 3 — observation cost

Environment-side logging counts what the subject actually acquired.

Primary cost measures:

- total response bytes delivered by treatment environment before final answer;
- number of distinct resources observed;
- total resource reads including repeats;
- redundant repeat reads;
- number of environment/tool actions.

If the runtime exposes model token accounting consistently, report it as secondary rather than substituting it for environment acquisition cost.

Do not count evaluator/hidden apparatus traffic.

## Primary outcome 4 — T3 systematic-workflow discovery

This is the core generativity outcome.

A run receives `SYSTEMATIC_WORKFLOW = 1` only if observable behavior demonstrates all mandatory conditions:

1. the subject recognizes that multiple collection members share an exploitable common structure;
2. the subject constructs or uses one strategy that applies across multiple members without a prompt-prescribed per-item procedure;
3. the strategy materially reorganizes/reduces the search compared with naive serial inspection;
4. the final result demonstrates coverage over the collection, not merely one lucky member;
5. no dedicated task-specific tool directly supplied the target answer.

Acceptable observable evidence may include:

- one structural query covering many members;
- a generated derived index/table used to drive inspection;
- a generic filter over repeated fields;
- extraction of exceptions from a collection;
- another reproducible transformation that applies to multiple members.

`SYSTEMATIC_WORKFLOW = 0` if the subject simply opens members one at a time even if it eventually succeeds.

Ambiguous traces are marked `UNRESOLVED` before treatment identity is revealed and adjudicated under the frozen rubric.

## Primary outcome 5 — perturbation transfer

Only evaluated for runs that discover a systematic T3 workflow.

A fresh isolated subject is given the perturbation-world task under the same treatment family.

Transfer succeeds when it independently uses a structurally equivalent strategy despite changed:

- resource names;
- ordering;
- URL slugs;
- distractor prose/layout details.

The subject must not receive a mapping from original to perturbation world.

Report:

- workflow rediscovery yes/no;
- task correctness;
- acquisition cost relative to the first world.

## Secondary outcome — open discovery / serendipity

T4 is intentionally not reduced to one ground-truth target.

The hidden world contains a preregistered set of valid material discoveries plus optional useful relations.

Score mechanically where possible:

- number of valid discoveries surfaced;
- number of invalid claims;
- number of distinct source regions explored;
- whether at least one optional/non-required material relation is found.

Owner experiential review remains separate and condition-blinded where practical.

## Secondary outcome — semantic anchoring cost

Record whether a treatment causes the subject to over-focus on surfaced structure/cues and miss valid material evidence elsewhere.

Possible indicators:

- lower T4 discovery breadth;
- repeated navigation within one semantic region while untouched valid regions exist;
- acceptance of derived cue without source verification;
- failure on M6 irrelevant-recency distractors.

Do not invent this metric after seeing a surprising P1 failure; preregister the exact operational checks before confirmatory runs.

## Efficiency ratios

Useful descriptive ratios include:

```text
bytes per correct mandatory finding
resource reads per correct mandatory finding
actions per correct mandatory finding
```

If a denominator is zero, report failure explicitly rather than infinite/undefined values hidden in an aggregate.

## Material-finding timing

If the subject runtime provides timestamped external messages/tool actions, record:

- time to first correct target acquisition;
- time to first exact-source verification;
- time to final answer.

Do not inspect hidden chain-of-thought to determine when the model 'really knew' the answer.

## Owner intervention metric

Controlled confirmatory runs should require **zero** Owner intervention by design.

Any non-protocol Owner routing/setup during a run marks the run contaminated/apparatus-failed according to the contamination protocol.

Live dogfood later records:

- manual tool routing;
- copy/paste courier steps;
- recovery explanations;
- configuration fixes;
- genuine product judgement separately.

## Treatment order and run randomization

Before measured runs, generate a randomized schedule covering:

- world seed commitments;
- treatment assignment/order;
- subject instance identifiers.

The schedule is frozen before outputs are inspected.

Do not always run P0 before P1 or vice versa.

## Replication count

Do not choose a confirmatory N in this document yet.

Pilot runs estimate behavioral variance and apparatus failure rate.

After pilots, preregister:

- number of paired world instances;
- number of independent subject runs per treatment/world if >1;
- stopping rule.

Then generate new hidden-seed worlds.

## Statistical posture

The first campaign should emphasize transparent paired effect distributions and confidence/uncertainty rather than chasing a single significance threshold.

Depending on final N and outcome type, appropriate paired analyses can be selected before confirmatory runs.

Do not choose the statistical test after looking at treatment results.

Always publish per-run outcomes alongside aggregate summaries.

## Mechanical scorer architecture

The evaluator should consume:

- hidden canonical world ledger;
- frozen task id;
- final subject answer in structured or parseable form where possible;
- environment/tool trace;
- cited resource/version ids.

Prefer deterministic checks for:

- target ids;
- version ids;
- resource coverage;
- tool/action patterns;
- bytes/read counts;
- source-authority relationships.

Use an LLM evaluator only for residual semantic judgement that cannot reasonably be encoded deterministically, and keep that judgement separate from the primary mechanistic score.

## Subject output contract

To improve mechanical scoring without scripting the solution, the frozen task may ask every subject to end with a small result envelope:

```text
finding(s): ...
supporting source URLs/IDs: ...
confidence/unknowns: ...
```

Do not ask for internal reasoning or a workflow description unless that description is itself part of the task.

The actual workflow is inferred from environment traces.

## Failure taxonomy

Classify failures explicitly:

- `WORLD_UNDERSTANDING_FAIL`;
- `SOURCE_AUTHORITY_FAIL`;
- `STALE_EVIDENCE_FAIL`;
- `SEARCH_COVERAGE_FAIL`;
- `ADAPTER_CAPABILITY_FAIL`;
- `ACTION_EXECUTION_FAIL`;
- `APPARATUS_FAIL`;
- `CONTAMINATION`;
- `UNRESOLVED`.

These labels belong to evaluator output, never the agent-visible treatment.

## Report format

Every confirmatory report must show:

- protocol/apparatus/generator hashes;
- subject body calibration version;
- clean/contaminated status;
- paired per-run table;
- primary outcome components;
- secondary/exploratory outcomes clearly labeled;
- negative findings;
- treatment failures;
- representative behavioral traces;
- Owner experiential judgement separately;
- revealed seed/ground truth only after campaign freeze when the commitment protocol allows it.

## Freeze gate

This scoring spec becomes confirmatory only after pilots establish that:

- mandatory outcomes are actually observable from traces;
- deterministic scorer agrees with manual ground-truth checks;
- ambiguous-workflow rate is acceptably low or the adjudication rule is improved;
- output envelope does not leak task strategy;
- cost logging is comparable between P0/P1.

Any substantive scoring-rule change after pilots requires a new preregistration version and new measured worlds.