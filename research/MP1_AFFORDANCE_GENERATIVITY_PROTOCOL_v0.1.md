# MP-1 — Affordance Generativity Protocol v0.1

**Date:** 2026-10-03
**Status:** pre-implementation experimental protocol

## Research question

Can a small set of generic environmental affordances cause an LLM agent to discover useful workflows, comparisons, or transformations that were not explicitly prescribed — and do so without merely leaking the answer through labels or task-specific tools?

This is the first serious experiment because it is the closest controlled analogue of the founding Shinden phenomenon.

## Core causal claim under test

The treatment is not 'better UI'.

The causal claim is:

> increasing environmental legibility, addressability, composability, and navigable semantic structure increases the agent's effective capability even when the underlying factual information and model are held constant.

## Two-world design

### Controlled micro-world

A synthetic R&D/software project generated from one canonical world model.

The world must be complex enough to support multi-step discovery but small enough to have exact ground truth.

Suggested initial scale:

- 40–70 addressable resources;
- 4–6 resource classes;
- 10–20 meaningful cross-resource relations;
- multiple source authorities;
- version history for a subset of resources;
- irrelevant noise and plausible distractors;
- several latent opportunities not named in the prompt.

### Live SWM dogfood

After controlled runs, repeat the same tested environmental property in the live Shared Work Medium project.

Do not infer causal effects from live dogfood alone.

## Canonical world requirements

All treatment surfaces must be generated from the same canonical facts.

The canonical world should contain at least these seeded structures:

1. **stale interpretation** — a decision/summary was correct at revision A, but a linked dependency changed at revision B;
2. **authority conflict** — a convenient derived summary disagrees with a more authoritative source;
3. **machine PASS vs experiential FAIL** — a mechanical test succeeds while an Owner/product observation contradicts a broader claim;
4. **repeated latent root cause** — three superficially separate work objects share a hidden common dependency or failure pattern;
5. **batchable search space** — many similar resources contain one property that can be checked systematically, creating a Shinden-like opportunity for an invented sweep rather than serial manual inspection;
6. **useful but non-required relation** — a cross-project/source relation that can improve the answer but is not needed for minimum task success;
7. **noise** — plausible recent changes that are irrelevant to the active question.

Ground truth for all seven structures is authored before treatment pages are generated.

## Experimental stages

Do not jump immediately to a giant five-condition comparison. Isolate mechanisms in stages.

### Stage 1 — structure without extra information

Compare:

**S0 — flat/full-context baseline**

All factual text is available in one large flat representation. No information is hidden, but addressability and navigation structure are weak.

**S1 — raw hypertext baseline**

The same facts are split into stable addressable resources connected by ordinary unlabeled links. Minimal semantic HTML.

**S2 — semantic hypermedia**

Same facts and same visible human text as S1, but with deliberate native semantic structure: headings, regions, lists/tables, source links, time elements, stable resource URLs, and accessibility semantics.

Critical rule: S2 must not contain new task-specific conclusions that S1 lacks.

Primary question: can structure alone change agent search behavior, context acquisition, correctness, or spontaneous workflow composition?

### Stage 2 — information scent

Compare S2 against:

**S3 — semantic hypermedia + generic information scent**

Add compact deterministic cues derived only from existing source metadata, for example:

- source authority class;
- freshness/last-change signal;
- relationship type;
- why an object was surfaced by a generic rule;
- explicit unknown/stale state.

Do not add task-specific labels such as 'this is the answer' or 'important root cause'.

Primary question: do local relevance cues improve active perception without creating anchoring or hiding unexpected discoveries?

### Stage 3 — generic medium versus rigid workflow tooling

Compare the best semantic condition against:

**S4 — purpose-built tool/API condition**

Expose efficient tools for anticipated operations, but keep them narrower than the full world.

Primary question: does the generic medium retain more capability on novel/unanticipated tasks while rigid tools win only on tasks the designer predicted?

## Task battery

Every condition receives the same task prompt within a task family.

### T1 — directed recovery

Goal example:

> Recover the current project situation and identify one decision or interpretation that materially needs re-evaluation. Support the answer from source evidence.

Ground-truth target: stale interpretation + changed dependency.

Purpose: basic orientation and evidence fidelity.

### T2 — cross-resource diagnosis

Goal example:

> Find the most plausible common explanation for the recurring failures in the project and show which independent observations support it.

Ground-truth target: repeated latent root cause.

Purpose: relation discovery.

### T3 — Shinden-class systematic opportunity

Goal example:

> Check whether the current project contains any broad pattern or repeated verification task that can be handled more systematically than one object at a time. If so, use the environment as you see fit and report the result.

Ground-truth target: batchable search space.

Purpose: detect whether the agent invents a sweep/pipeline rather than serially opening every item.

### T4 — open discovery

Goal example:

> Explore this project world and surface the most material overlooked problem, opportunity, or contradiction you can justify. You are not given a required procedure.

Ground truth includes several valid discoveries with different utility levels.

Purpose: emergence and serendipity.

### T5 — transfer / perturbation

After a workflow succeeds on one world instance, change resource names, layout order, and irrelevant content while preserving the underlying structural pattern.

Purpose: distinguish generic workflow discovery from memorizing surface-specific cues.

## Instrumentation

Treat observation acquisition as part of agent behavior.

Record:

- every resource/representation requested;
- ordering of observations;
- bytes/characters returned by each observation channel;
- source/version identifiers consulted;
- links or relations followed;
- queries/filters/actions used;
- total turns and elapsed wall time;
- model tokens where the agent runtime exposes them;
- exact evidence cited in final answer;
- incorrect/stale claims;
- repeated reads;
- whether the agent explicitly creates a new intermediate representation (table, shortlist, batch query, comparison, derived index, etc.);
- any Owner intervention.

Do not treat hidden chain-of-thought as required instrumentation.

Behavioral traces and produced artifacts are sufficient.

## Emergence rubric

A behavior is a strong emergence candidate when it satisfies most of:

1. the procedure was not explicitly requested;
2. no dedicated task-specific tool directly encoded it;
3. it composes two or more generic affordances/resources;
4. it materially improves coverage, cost, correctness, or understanding;
5. it can be explained from observable environment interactions after the fact;
6. it plausibly transfers to a perturbed world/task;
7. it is not produced by a leaked evaluator label or hidden test hint.

Record negative cases as seriously as positive ones.

## Anti-leakage rules

- Condition names are never shown to the agent.
- Treatment pages are generated mechanically from the same canonical world.
- Ground-truth labels never appear in treatment content.
- Semantic treatment must not gain extra factual content during Stage 1.
- Information-scent rules are fixed before tasks are run.
- Evaluator ground truth and latent-opportunity labels are stored outside the observed world.
- Prompts are frozen before the first measured run.
- Fresh agent contexts are preferred for each run.
- If account/project memory may contaminate a Browser run, record it conspicuously and do not call the result blinded.


## Public-repository contamination boundary

The laboratory repository is public. Therefore measured MP-1 ground truth must **not** be committed in discoverable plaintext before the measured campaign.

A web/GitHub-capable agent could otherwise retrieve evaluator answers outside the treatment environment.

Use generated world instances with a hidden run seed.

Recommended commitment protocol:

1. before measured runs, generate a cryptographically random seed outside the public observed environment;
2. publish only a commitment such as `SHA-256(protocol_version || generator_version || seed)` plus the frozen generator/version identifiers;
3. generate treatment surfaces and evaluator ground truth from the hidden seed;
4. run fresh agents without exposing the seed or answer ledger;
5. after the campaign is frozen, reveal the seed and generated ground truth so the experiment can be reproduced and audited.

This also prevents the experimenter from silently changing the hidden world after seeing agent outputs.

Pilot worlds may be public, but they must never be reused as confirmatory measured instances.

Controlled runs should restrict external tools to the declared treatment environment when the causal question requires it. Real dogfood runs can later restore ordinary web/repo capabilities and test ecological validity.

## Replication

Pilot each treatment enough to catch obvious apparatus failures before measured runs.

For measured comparisons, use multiple fresh runs per condition and at least two materially different agent/body configurations where feasible.

Do not decide exact replication count by convenience alone; choose it after pilot variance is observed.

Blind or condition-hide the human evaluator where practical.

## Evaluation layers

### Mechanistic

- task correctness;
- exact-source fidelity;
- context/source cost;
- exploration path;
- stale/false claims;
- workflow transfer under perturbation.

### Capability

- useful unprogrammed transformations;
- breadth of valid discoveries;
- ability to exploit environment without procedure instructions;
- robustness to layout/name changes.

### Owner/product

The Owner judges only genuinely experiential questions, for example:

- did the behavior feel like real capability amplification or merely a benchmark trick?
- did the medium preserve freedom/serendipity?
- would the discovered workflow be useful in real collaboration?

Do not ask the Owner to manually score low-level telemetry that can be computed automatically.

## Important competing hypotheses

The experiment is specifically designed to allow these alternatives to win:

**H0 — information quantity dominates:** once the same facts are available, semantic environment structure adds little.

**H1 — structure helps only efficiency:** semantics reduce context/search cost but do not improve capability or novel discovery.

**H2 — information scent helps but anchors:** cues improve directed tasks while reducing serendipity/open discovery.

**H3 — rigid tools dominate:** purpose-built APIs are simply better and generativity adds little practical value.

**H4 — semantic medium increases generativity:** generic affordances improve both selective perception and novel workflow composition, especially under transfer/novel tasks.

No result should be forced toward H4.

## Failure cases that count as important evidence

- semantic pages cause premature anchoring on stale/derived cues;
- agents over-trust structured metadata compared with source evidence;
- flat full-context input wins because navigation overhead dominates;
- rigid API tools outperform generic medium even on unanticipated tasks;
- an apparent emergent workflow disappears under renamed/reordered resources;
- accessibility structure helps one body but degrades another;
- the agent spends more effort understanding the medium than solving the task.

## Apparatus architecture constraints

The first controlled apparatus should be boring and replaceable.

Requirements:

- one canonical world data file/generator;
- deterministic treatment generation;
- immutable run IDs;
- request/action logging;
- easy reset between runs;
- no dependency on semantic-medium-v0 code;
- no Cloudflare requirement unless hosting/instrumentation evidence justifies it;
- static hosting preferred for Stage 1 if dynamic infrastructure adds no experimental value.

## Pre-registration gate

Before the first measured run, freeze:

- canonical world version;
- treatment generator version;
- task prompts;
- ground-truth ledger;
- emergence rubric;
- metrics;
- contamination rules;
- stopping criteria for the first campaign.

Exploratory pilot runs before this gate are explicitly labeled pilot/contaminated and are not counted as confirmatory evidence.

## What would justify moving on to MP-2

MP-1 does not need to prove one final interface.

It succeeds as a research phase when we know, with replicated evidence, which environmental properties materially affect:

- orientation/search cost;
- evidence fidelity;
- workflow composition;
- transfer to a novel task;
- serendipitous useful discovery.

Only then should continuity infrastructure optimize those proven properties rather than preserving accidental v0 mechanisms.