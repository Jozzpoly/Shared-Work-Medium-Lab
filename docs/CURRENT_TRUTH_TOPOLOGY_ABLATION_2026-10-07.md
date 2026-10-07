# Medium dogfood — current-truth topology ablation — 2026-10-07

**Status:** EXPERIMENTAL TEST FIXTURE · DRAFT-BRANCH ONLY · NOT PROJECT AUTHORITY

## Research question

Does explicit separation of **accepted baseline / public draft frontier / volatile live state** improve fresh-agent orientation when no task-specific frontier names are supplied?

This fixture exists because the first PR #9 treatment bundles two changes:
1. authority-topology framing;
2. a curated list of relevant PR numbers.

A behavioral improvement under that bundle would not identify which change helped.

## Treatment T-topology-only

A fresh participant receives the same project goal/task it would otherwise receive, plus this neutral routing rule:

> The default branch contains the accepted public baseline. Newer public evidence may exist on draft branches or pull requests and is not automatically accepted truth. Still-newer private/live work may exist outside the public repository and must not be invented. Start from the actual question you need to answer, then inspect only the minimum source plane needed to support that claim.

Routing discipline:

### Accepted public intent / guardrails

Use the default-branch entrypoints and accepted documents.

Do **not** infer from their existence that no newer public draft evidence exists.

### Newer public evidence

Discover relevant open draft work from the repository itself.

No draft PR number is supplied by this treatment.

A draft is evidence/frontier material, not automatically accepted project truth.

### Volatile claim

When the answer depends on the current head, status, deployment, CI or latest experiment, verify the live source rather than trusting a dated prose snapshot.

### Insufficient public evidence

If the requested claim depends on private/live context unavailable from the public repository, say so. Do not fill the gap by inference.

## What is deliberately absent

This treatment does **not** name:
- Capability Expedition;
- Quiet Presence;
- MP-1;
- any current PR number;
- any expected answer;
- ReflexBrain or another donor project.

It therefore tests orientation topology more cleanly than the first PR #9 bundle.

## Suggested comparison

### T0 — accepted-main route

Start from:

`main@d190d17db8edb5e6e41f8e5777fe2dc0894280d1`

and its ordinary `START_HERE.md`.

### T1 — topology-only route

Use the same exact task and source access, but prepend only the neutral routing rule above.

### T2 — current PR #9 bundled route

Use the draft branch's current `START_HERE.md` + current-truth topology document, which also exposes public frontier landmarks.

T2 is useful operationally but is **not** a clean topology-only causal treatment.

## Candidate tasks

Use real questions whose correct answer lives on different planes.

Examples of task classes:
- accepted project North Star / guardrail;
- newest public Capability Expedition evidence;
- newest public Quiet Presence evidence;
- current status of an exact draft PR;
- a claim that cannot be supported from public sources alone.

Do not give the actor the source name it is meant to discover.

## Measures

Record at minimum:
- correct authority plane chosen;
- whether the agent lands on a source that can support the claim;
- false promotion of draft evidence to accepted truth;
- false assumption that accepted baseline is the newest frontier;
- number of source hops/reads before landing;
- unnecessary broad retrieval;
- honest `unknown / public evidence insufficient` when appropriate.

Token/latency measurement is optional and secondary.

## Falsifiers

Topology-only routing is not justified if:
- T1 does not improve decisions over T0;
- T1 creates extra reading without better authority selection;
- ordinary repository-native discovery already solves the task reliably;
- actors become overly conservative and refuse useful draft evidence;
- the treatment encourages one universal truth schema across heterogeneous projects.

## Interpretation ceiling

Even a T1 advantage would support only:

> explicit truth-plane separation can improve orientation in this Medium repository under the tested tasks.

It would **not** establish:
- a universal project schema;
- a need for central Medium state;
- lower Owner burden in general;
- ecological adoption;
- cross-project capability routing;
- the broader `medium between media` hypothesis.

