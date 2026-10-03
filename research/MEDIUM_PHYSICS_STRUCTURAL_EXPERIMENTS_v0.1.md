# Medium Physics — Structural Experiment Design v0.1

**Date:** 2026-10-03
**Status:** research design; no implementation authorization

## Why this campaign exists

The first semantic-medium specimens mixed several effects at once: project orientation, semantic HTML, GitHub live state, cursors, event streams, cache behavior and agent-body limitations.

They were excellent reconnaissance but weak causal experiments.

The next campaign should isolate the deeper question:

> Which environmental properties actually amplify an intelligent participant's capability, continuity and self-directed behavior?

The campaign deliberately separates **generativity**, **continuity**, and **action** instead of forcing one giant system to answer all three at once.

## Two-lab method

Every structural property should be tested in two environments:

### Controlled micro-world

A small synthetic but realistic project world with seeded structure, hidden relationships, irrelevant noise, source changes and known ground truth.

Purpose: repeatability, causal comparison, failure injection, contamination control.

### Real dogfood world

The live Shared Work Medium project.

Purpose: ecological validity, Owner experience, real tool friction, unexpected behavior.

Neither is sufficient alone.

A synthetic benchmark can be gamed by its design. Live dogfood cannot easily distinguish causal effects.

## Campaign MP-1 — Affordance Generativity

### Core question

Does a small set of composable environmental affordances cause agents to discover useful workflows that were not explicitly prescribed?

### Experimental treatments

Present the same underlying micro-world through multiple surfaces:

**A — raw source baseline**
Plain resource list / files / minimally organized pages.

**B — human-dashboard baseline**
Useful visual organization but weak explicit semantic relations and limited machine-oriented affordances.

**C — semantic hypermedia medium**
Native semantic structure, stable URLs, source links, information scent, version/freshness cues, discoverable relations, no task-specific workflow scripting.

**D — rigid tool/workflow API**
Purpose-built operations that make intended tasks easy but constrain interaction to designer-predicted workflows.

### Task design

Agents receive broad goals, not instructions about the surface.

Seed tasks that can be solved directly, but also include cross-resource opportunities the experiment designer does not name in the prompt.

Examples:

- find one materially stale interpretation among many current ones;
- detect a repeated failure pattern across otherwise unrelated work objects;
- identify that two sources disagree and recover which authority should dominate;
- discover that a batch transformation is cheaper than opening resources one by one;
- derive a useful new comparison or index that was never exposed as a dedicated feature.

### Primary outcomes

- correct task result;
- source fidelity;
- context/source cost;
- navigation/actions used;
- number and quality of self-invented useful transformations;
- whether the workflow survives a changed task without a new dedicated feature;
- Owner judgement of whether the behavior feels genuinely capability-expanding rather than scripted.

### Falsification

The semantic medium hypothesis weakens if:

- it does no better than raw sources after controlling for information quantity;
- gains come only from task-specific labels that leak the solution;
- rigid tools consistently dominate on novel tasks without materially higher integration cost;
- agents require explicit instructions explaining the medium;
- extra semantics reduce exploration or create systematic anchoring errors.

## Campaign MP-2 — Continuity and Active Perception

### Core question

Can an observer leave and return to a changing project world, recover only the relevant delta, and continue correctly without giant handoffs or full-world rereads?

### Compared conditions

**A — full reconstruction baseline**
Fresh observer rereads all designated project sources.

**B — authored summary/handoff baseline**
Fresh observer receives a maintained project summary, then verifies sources as needed.

**C — snapshot observation**
Fresh observer receives a versioned observation manifest plus selective source links.

**D — event/cursor continuation**
Observer receives unseen change traces since its last cursor.

**E — adaptive hybrid**
Cheap change cues and information scent route attention; snapshot or exact source detail is acquired only when useful.

### Critical design correction

Do not assume one global total event order.

Preserve source-local versions, per-resource order and explicit causal/dependency relations. Treat transport sequence as transport sequence, not automatically project chronology.

### Failure injection

- duplicate event;
- delayed event;
- missing webhook followed by reconciliation;
- source unavailable;
- source rate-limited;
- stale cached projection;
- source changes during reasoning;
- interpretation dependency changes while unrelated sources also change;
- observer cursor falls behind a compacted change log;
- two observers have different permissions / visible source sets;
- two independent changes are concurrent and have no meaningful mutual order.

### Primary outcomes

- time to correct orientation;
- source requests;
- observation/context size;
- missed material changes;
- false relevance alarms;
- stale claims;
- recovery completeness;
- Owner interventions;
- ability to identify exactly which source versions support the current judgement.

## Campaign MP-3 — Action Ecology

### Core question

Can heterogeneous agents discover and safely use actions embedded in the same human-useful environment without the Owner acting as router?

### Candidate action layers

- ordinary native human controls;
- accessibility-exposed controls;
- declarative WebMCP forms;
- imperative WebMCP tools;
- HTTP actions with explicit preconditions;
- repo-native actions;
- richer server-side capabilities exposed only to compatible bodies.

### Test properties

- discoverability;
- accurate action semantics;
- body/adapter capability detection;
- read-only vs consequential distinction;
- stale-world preconditions;
- idempotency;
- provenance of effects;
- explicit unknown/failure state;
- human confirmation only when consequences justify it.

### Failure injection

- control visible but actuator absent;
- action becomes unavailable mid-run;
- target changes after observation;
- duplicate action delivery;
- malicious/untrusted page content attempts to influence action choice;
- permission mismatch;
- action mechanically succeeds but Owner product judgement is FAIL.

## Body matrix

The same source reality should be tested through materially different bodies rather than assuming equivalence.

| Body | Observation channel | Action channel | Expected blind spot |
| --- | --- | --- | --- |
| Human browser | rendered UI | native UI | time/attention cost |
| Opera Browser agent | AXTree + URL navigation | connector-limited | lossy DOM + actuator gaps |
| DOM/source-aware browser | DOM + metadata | browser controls | adapter-dependent availability |
| WebMCP-capable ChatGPT browser | page + structured site tools | typed page tools | page-open/model/account constraints |
| Repo-native agent | files/history/issues | repository operations | weaker web/human gestalt |
| Structured HTTP client | JSON/links/events | explicit protocol actions | can miss human semantic context |

Each run should record the participant's actual sensor/action capability before interpreting failure.

## Experimental instrumentation

The next implementation should emit structured experiment traces from the beginning.

Minimum trace events:

- observation requested;
- representation/body used;
- source read;
- cache hit/miss;
- event consumed;
- cursor advanced;
- source version verified;
- interpretation produced;
- action attempted;
- action effect verified;
- failure/unknown;
- Owner intervention;
- unplanned useful workflow detected.

Keep product truth separate from machine telemetry.

## Emergence rubric

Emergent capability must not become a hand-wavy success label.

A candidate emergent behavior should satisfy most of:

1. not explicitly requested as a procedure;
2. not directly encoded as a dedicated task-specific tool;
3. uses two or more generic affordances compositionally;
4. materially improves the result, cost, coverage or understanding;
5. is understandable after the fact from the environment and reasoning;
6. can plausibly transfer to another task/world configuration;
7. does not merely exploit accidental leakage of hidden test labels.

Record both positive and negative cases.

## Owner-burden accounting

Every experiment must count Owner work as a first-class cost.

Record:

- setup steps;
- copy/paste or courier actions;
- manual tool routing;
- recovery explanations;
- permission/configuration interventions;
- product-judgement decisions that genuinely require Owner input.

Do not count legitimate Owner vision/product judgement as avoidable burden.

## Architecture hygiene

The experiment should optimize for **replaceable laws**, not replaceable syntax.

Examples:

- property: versioned observation; implementation may be Cloudflare cache, Git, another service;
- property: ordered per-resource change history; implementation may be Durable Object, source-native log, another store;
- property: discoverable action; implementation may be WebMCP, HTML form, MCP, repo operation;
- property: information scent; implementation may be accessible description, link metadata, structured index.

If removing a vendor forces redesign of the conceptual model, the abstraction boundary is probably wrong.

## Gate before MP-1 implementation

Do not build MP-1 until:

- the founding conversation genealogy has been audited enough to recover Owner-confirmed invariants;
- Cloudflare and major web/agent prior art have been mapped far enough to avoid obvious reinvention;
- the controlled micro-world ground truth and task battery are defined before treatments;
- treatment pages/interfaces are generated from the same underlying world data so information content can be controlled;
- evaluation and contamination rules are written before first agent run;
- at least two agent/body configurations are available or a clear reason for one-body pilot is recorded.

## Current judgement

The next serious move should not be 'build better semantic-medium-v0'.

It should be: build an experimental apparatus capable of telling us which **laws of the medium** actually matter.

Until that apparatus exists, the best work is research design, source recovery, substrate audit and falsification planning.