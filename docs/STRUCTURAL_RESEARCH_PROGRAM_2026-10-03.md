# Structural Research Program — after semantic-medium-v0 reconnaissance

**Date:** 2026-10-03  
**Status:** active research program; no architecture freeze

## Why this phase exists

The first semantic-medium experiments were intentionally fast. They succeeded as reconnaissance because they produced concrete evidence and concrete failure.

They must now stop being allowed to determine the architecture merely because code exists.

The next phase is not "v0.2". It is a clean re-evaluation of the problem at a more serious structural level.

## Owner-confirmed target

The project is searching for an environment that:

- increases the real perception, action, continuity, and emergent capability of intelligent participants;
- reduces Owner routing, handoff, context-repair, setup, and babysitting burden;
- remains useful to a human while exposing rich machine-legible structure;
- maintains its own observation/state projection rather than requiring manual Owner upkeep;
- preserves source truth, provenance, uncertainty, and independent interpretations;
- allows new workflows to emerge from composable environmental affordances instead of encoding every workflow in advance;
- remains replaceable at the infrastructure/provider layer;
- is investigated deeply enough that temporary convenience choices do not become long-term constraints.

The founding Shinden specimen remains the reference phenomenon:

> a useful workflow emerged because the environment was legible and composable enough for the agent to invent the workflow itself.

## What reconnaissance established

### Material evidence

The current specimens support these scoped claims:

- native semantic HTML is highly useful to an accessibility-tree browser agent;
- the accessibility tree is deliberately lossy and must not be mistaken for a universal DOM/API representation;
- the same page has different effective affordances for different agent bodies;
- semantic topology can reduce observation/context acquisition before model reasoning;
- links can carry useful identity, source, dependency, and information-scent signals;
- source validators can bind later reasoning to an exact observed representation;
- small observer cursors plus a change log can recover unseen environmental traces without a handoff;
- authored project interpretation can be treated as a derived view whose dependencies can become stale;
- naive per-tab source polling failed under live GitHub rate limits;
- Cloudflare-like shared observation transport may reduce source fan-out and create common observation epochs.

### Still unproven

The reconnaissance did **not** prove:

- that GitHub is the right long-term project substrate;
- that Cloudflare is the right long-term runtime;
- that one observation identifier is sufficient for heterogeneous/cross-source reality;
- that WebMCP is the right universal action interface;
- that accessibility semantics are sufficient for rich agent perception;
- that a centralized event receiver is required;
- that emergent capability improves in a controlled comparison;
- that Owner burden is materially lower over repeated real work;
- that multiple heterogeneous agents can safely inhabit the same medium;
- that the system behaves well under missed, duplicated, reordered, stale, private, or conflicting evidence.

## Anti-lock-in boundary

The following current mechanisms are **donor hypotheses only**:

- GitHub Issues/PRs/commits as the object model;
- Markdown `RESEARCH_STATE.md` as the interpretation layer;
- Browser ChatGPT as the central mind;
- Opera accessibility tree as the canonical sensor;
- Cloudflare Workers/KV/Durable Objects/Queues/Workflows as mandatory infrastructure;
- the current HTML/JSON representations;
- polling intervals;
- the current `observation_id` hash;
- current event-envelope fields.

The next architecture-bearing specimen must select mechanisms again from evidence.

## Research workstreams

### A. Primary-source genealogy

Current source-bounded audit: [docs/PRIMARY_SOURCE_GENEALOGY_PARTIAL_2026-10-03.md](./PRIMARY_SOURCE_GENEALOGY_PARTIAL_2026-10-03.md)

Complete the originating conversation audit before architecture freeze.

Recover:

- the problem before implementation vocabulary appeared;
- Owner-confirmed needs and anti-goals;
- assistant-generated hypotheses that later became accidentally canonical;
- decisions produced by evidence versus decisions produced by convenience;
- where Shinden-like emergence was preserved and where the campaign drifted into workflow scripting.

Output: a compact invariant/decision ledger, not a giant transcript summary.

### B. Cloudflare substrate audit

Cloudflare now deserves a deep audit because live evidence created a concrete need for a shared observation layer.

Investigate current primitives as separable capabilities rather than choosing a stack:

- Workers Caching: tiered cache, request collapsing, `Vary`, purge/invalidation, failure behavior;
- Workers KV: global read-heavy cache, eventual-consistency semantics, propagation windows;
- SQLite Durable Objects: strong local consistency, ordered event state, alarms, PITR, WebSocket hibernation;
- Queues: at-least-once delivery, retry/dead-letter behavior, idempotency;
- Workflows: durable re-evaluation jobs, waiting for events, retries, and the risk of accidentally introducing a central orchestrator;
- Service Bindings/RPC: capability modularity without public network plumbing;
- Workers/Pages static assets: cheap human surface independent of dynamic observation;
- observability/tracing: measure source calls, cache behavior, event latency, failures, and cost rather than infer them;
- secrets/auth/Access boundaries;
- failure, pricing, quota, and regional-consistency behavior.

For every primitive record:

1. property it gives the medium;
2. property it does **not** give;
3. consistency/failure semantics;
4. agent/human affordance implications;
5. replaceability;
6. cost/Owner setup;
7. test needed before adoption.

### C. Body × projection matrix

Test the same underlying project reality through heterogeneous bodies.

Initial body classes:

| Body | Likely perception | Likely action | Important limitation to test |
| --- | --- | --- | --- |
| Human browser | rendered UI | native controls | cognition/attention cost |
| Opera Browser agent | accessibility tree + navigation | limited connector actions | lossy semantics / actuator gaps |
| DOM/source-aware browser agent | DOM/structured metadata | browser actions | availability varies by adapter |
| WebMCP-capable ChatGPT browser | page + structured site tools | typed page-local tools | page-open/session/tool support constraints |
| Repo-native agent | files/history/issues via repository tools | code/repo writes | weaker human/web context |
| Structured client | JSON/HTTP | protocol actions | loses human gestalt unless deliberately exposed |

Do not require all bodies to receive the same serialization.

Require them to be able to establish what source reality/version they are observing and where their capability boundary lies.

### D. Observation, time, and interpretation model

Research the minimum primitives for:

- resource identity;
- immutable source versions;
- observation epochs;
- change events;
- observer cursors;
- dependency/invalidation;
- independent interpretation;
- provenance;
- uncertainty / unknown / stale;
- source disagreement.

Avoid prematurely creating a universal ontology.

Prefer source-addressable facts and small composable envelopes.

### E. Trust and action

Before consequential writes, design tests for:

- source authority;
- prompt/tool injection boundaries;
- read-only vs consequential affordances;
- stale-world preconditions (ETag / conditional writes where possible);
- idempotency and duplicate delivery;
- human confirmation only where consequences justify it;
- machine PASS vs Owner experiential PASS.

### F. Serious experiment design

The next structural experiment should be designed before implementation.

Working candidate:

> **Shared Observation Plane v1:** can heterogeneous observers recover a common live project world and only the relevant deltas, with explicit freshness/provenance and lower Owner/source/context cost than direct independent observation, while preserving freedom for unprogrammed agent workflows?

This is a candidate question, not yet an architecture.

## Candidate experiment structure

### Compared conditions

**A — direct baseline**  
Each observer independently reconstructs the project from source systems.

**B — shared snapshot**  
Observers consume a shared versioned observation projection.

**C — event + cursor**  
Observers resume from a durable cursor and selectively acquire affected evidence.

**D — adaptive hybrid**  
Events provide wake-up/information scent; snapshots and exact source reads are acquired only when needed.

Cloudflare may implement B–D for one experimental run, but the properties are the experimental variables, not the vendor.

### Scenario battery

At minimum test:

- clean orientation from no prior model context;
- one meaningful change while observer is absent;
- many irrelevant changes plus one frontier-relevant change;
- duplicate event;
- delayed event;
- missed event / reconciliation;
- stale cache;
- source API unavailable / rate-limited;
- conflicting declared interpretation and observed source facts;
- source changes during agent reasoning;
- agent body unable to use one advertised affordance;
- multiple observers consuming the same sampled reality.

### Measurement

Record at least:

- Owner interventions / manual routing steps;
- source requests and external API budget;
- bytes/characters/tokens acquired before useful action;
- time to correct orientation;
- stale/incorrect claims;
- exact source verifications performed;
- event-to-observer latency;
- cache hit/miss behavior;
- recovery completeness after absence;
- action failures caused by capability mismatch;
- whether the agent invents a useful transformation/workflow not explicitly encoded by the experiment.

The final metric is deliberately qualitative but central: **emergent capability** must remain a first-class result, not be displaced by infrastructure metrics.

## Experimental method correction — controlled world + live dogfood

The next serious experiments should use two complementary environments.

### Controlled micro-world

Use a small synthetic but realistic project world with known ground truth, seeded irrelevant noise, hidden relationships, versioned changes, and deliberate failure cases.

Purpose: causal comparison, repeatability, contamination control, and reliable falsification.

### Live SWM dogfood

Run the same properties against the real Shared Work Medium project.

Purpose: ecological validity, real Owner burden, real adapter/tool friction, and unexpected behavior.

Neither environment is sufficient alone.

A synthetic benchmark can reward its own design. Live dogfood can produce impressive anecdotes without isolating why they happened.

The current leading experimental decomposition is:

- **affordance generativity** — does environmental structure cause useful unprogrammed workflow composition?
- **continuity / active perception** — can observers resume from selective deltas instead of giant context reconstruction?
- **action ecology** — can heterogeneous bodies discover and safely use available actions without Owner routing?

These should be separable campaigns rather than one monolithic v1.

## Preferred experiment ordering

Unless new evidence changes the order, the first serious implementation should target **affordance generativity**, not infrastructure continuity.

Reason:

The founding Shinden result was capability emergence from a legible environment. Continuity, cursors, caching, and event transport are important supporting problems, but they can easily become an infrastructure gravity well and recreate the earlier Browser↔Codex drift.

Preferred sequence:

1. **Affordance generativity** — isolate whether environmental structure itself produces new useful agent behavior.
2. **Continuity / active perception** — test selective delta recovery, observation manifests, and source/event economics.
3. **Action ecology** — test discoverable actions, capability boundaries, trust, and consequential writes across heterogeneous bodies.

Cloudflare research continues in parallel because it may become an excellent substrate for steps 2–3, but Cloudflare deployment is not a prerequisite for step 1.

## Current MP-1 design artifacts

The clean research branch `research/medium-physics-experiment-design` now contains:

- `research/MP1_AFFORDANCE_GENERATIVITY_PROTOCOL_v0.1.md`
- `research/MP1_CONTROLLED_MICROWORLD_GENERATOR_SPEC_v0.1.md`
- `research/MP1_APPARATUS_CAUSAL_ISOLATION_SPEC_v0.1.md`
- `research/BODY_PROJECTION_CALIBRATION_PROTOCOL_v0.1.md`
- `research/MP1_CONTAMINATION_ISOLATION_PREREG_PROTOCOL_v0.1.md`

The leading Stage-1 causal test is now a **pixel-equivalent semantic ablation**: same human-visible facts, links, layout, and near-identical pixels; different machine-legible semantic structure.

The current Browser ChatGPT/Owner collaboration context is considered **contaminated by design** for confirmatory MP-1 because it helped design the motifs and protocol. It remains valuable for apparatus design and later ecological dogfood, but clean confirmatory runs require a stateless/isolated subject runtime.

## Experiment-harness donor candidate

The MP-1 design branch now includes `research/WEB_AGENT_EXPERIMENT_HARNESS_DONOR_AUDIT_v0.1.md`.

BrowserGym / AgentLab / WebArena-Verified are being treated as **apparatus donors**, not project architecture.

Their relevant properties include explicit browser observation/action spaces, custom/resettable tasks, AXTree/DOM/screenshot capture, reusable experiment execution, and deterministic/network-trace-based evaluation.

The current preference is to reuse mature browser-lifecycle/evaluation plumbing if a small donor spike confirms it preserves MP-1's causal controls. The hidden-seed world generator, semantic ablation compiler, parity verifier, contamination controls, and generativity scoring remain custom research apparatus.

## Replication discipline

One successful agent run is evidence, not validation.

The next serious experiment should:

- repeat conditions across more than one fresh run;
- use at least two materially different agent/body configurations where practical;
- keep contamination visible;
- preserve failed runs;
- distinguish mechanistic PASS from Owner/product PASS;
- treat unexpected useful behavior as evidence worth isolating and reproducing.

## Clean-slate implementation rule

Do not grow the next architecture-bearing experiment directly out of `semantic-medium-v0`.

When the research gate is satisfied:

1. branch from current `main`;
2. define hypotheses and instrumentation first;
3. import only donor mechanisms that remain justified;
4. keep reconnaissance artifacts unchanged for comparison.

## Gate to implementation

A serious v1 implementation begins only when we can answer:

- what exact property is being tested;
- what baseline it must beat;
- what evidence would falsify it;
- which current mechanism choices are incidental;
- which agent bodies will test it;
- how Owner burden is measured;
- how source/provenance truth is verified;
- how the experiment preserves room for unplanned behavior.

Until then, research is the implementation.
