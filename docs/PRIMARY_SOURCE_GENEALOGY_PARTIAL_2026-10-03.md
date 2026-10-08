# Primary-Source Genealogy — partial, source-bounded

**Date:** 2026-10-03
**Status:** partial audit; explicitly incomplete

## Coverage boundary

This document intentionally records only project genealogy that has been recovered from primary/live sources during the current campaign.

Recovered directly:

- the founding Shinden/Opera conversation segment, including the original all-season upload sweep, the agent-created browser-native batch pipeline, the Owner reaction, and the follow-up sweep;
- the later Shared Work Medium conversation segment covering semantic-medium-v0, affordances, continuity probes, Cloudflare discussion, and the Owner's explicit warning against long-term lock-in from quick prototypes;
- live repository history, issues, draft PR #3, canonical docs, and experimental branches.

Not fully recovered:

- the middle portion of the originating SWM conversation between the founding Shinden segment and the later currently loaded section.

The ChatGPT UI currently stops that recovery with `Wczytywanie starszych wiadomości…` in the accessible conversation surface.

Therefore this document is **not** a complete conversation summary and must not be used to claim that the missing middle contains no additional Owner intent or corrections.

## Recovered exact founding mechanics

A direct reread of the founding Shinden branch recovered the concrete mechanics that triggered the project:

- the season page exposed **94 titles** in the first sweep;
- instead of human-style clicking, the agent extracted the repeated `/episodes` structure;
- one working browser tab became a reusable probe;
- each title page was reduced to the episode table and specifically the **`Wersja Online`** column;
- the search was transformed into a pipeline:
  `season list → episode endpoints → table rows → online marker`;
- a later sweep over **95 titles** made the process more deterministic, used multiple work tabs, and explicitly separated “has an episode table” from “has an online upload”;
- two broken resources were reported as unresolved rather than silently classified.

The Owner's positive reaction focused not only on task completion but specifically on the agent's self-chosen optimization and planning.

This sharpens the founding phenomenon:

> The important event was not that semantic HTML was easier to parse. It was that a broad real task + a legible, repeated, addressable environment let the agent **invent a better computational strategy** than the human-style procedure implied by the request.

That distinction matters for later experiment design.

## Founding phenomenon — directly recovered

The Owner asked the agent to use Opera to inspect every anime in a new Shinden season, enter episode lists, and determine which already had online uploads.

The useful behavior that emerged was not human-like clicking.

The agent discovered the repeated site structure, extracted the season's episode endpoints, reused one working browser tab as a probe, and reduced the task to a systematic browser-native pipeline over the `Wersja Online` column.

The Owner's reaction emphasized the surprising capability gain and the cleanliness/optimization of the agent's self-chosen plan.

The agent itself recognized the key property:

> the value came from systematically exploiting the structure of the live web environment rather than merely imitating human interaction.

A later sweep became more deterministic and parallel while preserving the same basic environmental leverage.

### Source-bounded implication

The founding evidence supports a strong invariant candidate:

> **The project is fundamentally interested in capability emerging from legible, composable environment structure — not merely in memory, handoff, or project organization.**

This is a candidate invariant because it is directly aligned with both the recovered founding behavior and the Owner's explicit reaction.

## Owner-confirmed intent recovered later

The later conversation directly confirms:

- the medium should maintain/update its own projection of project state rather than requiring manual Owner maintenance;
- a human-useful web surface that behaves almost like a rich API for agents is a high-value research direction;
- research time/effort should not be prematurely minimized when discovering the medium's deeper possibilities;
- unusual compositions of existing tools are explicitly desirable;
- quick first specimens are bridges, not architecture;
- Cloudflare deserves deep investigation because hidden useful primitives are likely present;
- subsequent experiments must be dramatically more serious, structural, and fundamental;
- temporary simplifications must not bind the long-term horizon.

These are Owner-confirmed constraints, not assistant hypotheses.

## Major drift episode — Browser ↔ Codex

The project temporarily narrowed around a Browser↔Codex continuity experiment.

That path produced useful evidence but also a strong negative result:

- the Owner had to route tools manually;
- local Codex setup/workspace friction exceeded the experimental value;
- the Owner explicitly stopped the path for the day because the setup burden was larger than the work value.

The resulting correction was not 'Codex is bad'.

It was:

> a medium that requires the Owner to provision, route, debug, or babysit agent bodies violates a central success criterion.

Browser↔Codex remains a specimen, not architecture.

## Second drift risk — semantic-medium-v0 becoming architecture

The semantic web specimen recovered the founding direction better than the Browser↔Codex path and produced real evidence:

- AXTree semantic legibility;
- declared vs observed state distinction;
- freshness/caching failure;
- observer cursors and event traces;
- information scent;
- source-budget failure;
- Cloudflare donor hypotheses.

But the Owner explicitly corrected the trajectory again:

> the quick probes were only a bridge; later experiments must be structurally serious and temporary simplifications must not constrain the long-term design.

Therefore semantic-medium-v0 is reconnaissance evidence only.

## Assistant-generated hypotheses — useful but not Owner invariants

The following ideas have been generated or substantially shaped by the assistant and must remain hypotheses until independently supported:

- `Project World` as a specific conceptual model;
- `thin shared epistemic spine` as architecture;
- Browser ChatGPT as primary/central project brain;
- one shared observation plane;
- one `observation_id` / observation epoch model;
- Cloudflare as a sensory ganglion;
- GitHub as primary long-term substrate;
- event-log + cursor as the central continuity mechanism;
- AXTree as canonical weak-agent representation;
- WebMCP as the primary action layer;
- Markdown `RESEARCH_STATE` as long-term interpretation storage;
- incremental-build/dependency invalidation as the final epistemic model.

Several are promising donor concepts. None is protected from falsification by having appeared repeatedly in the conversation.

## Strong invariant candidates

Subject to completion of the missing source audit, the currently strongest invariant candidates are:

1. **Capability amplification over organization.** The medium must increase what participants can actually do, not only make work tidier.
2. **Environment over prescribed workflow.** Prefer simple composable environmental laws from which intelligent participants can invent workflows.
3. **Owner burden must not scale with agent/tool count.** The Owner should spend attention on vision, judgement, feel, priorities, and consequential tradeoffs — not courier/setup/routing work.
4. **Shared reality, independent minds.** Participants should be able to ground themselves in the same addressable evidence without requiring one shared belief state.
5. **Source truth and provenance survive abstraction.** Projections/interpretations may help, but cannot erase where claims came from or silently upgrade uncertainty.
6. **Body heterogeneity is normal.** Different agents/humans perceive and act through different channels; the medium should not assume one universal adapter.
7. **Graceful degradation.** Unknown/stale/unavailable is preferable to fabricated continuity or silent stale state.
8. **Self-maintenance is part of the medium.** Manual Owner upkeep of duplicated state is not an acceptable steady-state design.
9. **Serendipity/freedom must survive optimization.** Better routing and structure must not turn the environment into a cage that only supports designer-predicted tasks.
10. **Temporary implementation choices are replaceable.** A quick successful specimen is evidence, not an architectural entitlement.

## Open questions that the missing middle may materially affect

- how early and how strongly the Owner endorsed/modified `shared reality, different minds`;
- whether additional anti-goals or privacy/public/private constraints were established before the current repo;
- whether the project had already identified other preferred first organisms before the Codex bridge;
- whether specific Cloudflare/web/MCP directions were considered and rejected earlier;
- whether the Owner made further corrections to project terminology or scope that are not visible in the recovered segments.

## Audit rule going forward

Until the missing middle is recovered or independently reconstructed from durable primary artifacts:

- do not present this genealogy as complete;
- do not fill gaps from conversational memory;
- do not freeze architecture on the assumption that the missing segment merely agrees with current direction;
- allow small reversible research specimens, but keep the structural research gate active.
## Current-direction critique after rereading the trajectory

The structural-research correction is necessary, but the project now has a new drift risk: **the apparatus itself can become the project**.

The current MP-1 work is scientifically stronger than the fast reconnaissance, but several pieces are narrower than the founding phenomenon.

### 1. Pixel-equivalent semantic ablation is a mechanism test, not the North Star experiment

A P0/P1 treatment that changes semantic HTML while preserving visible pixels can cleanly test whether machine-legible structure changes perception/search behavior.

That is valuable.

But the Shinden event depended on a richer bundle:

- repeated resource structure;
- stable addressability;
- real navigable collections;
- enough regularity to support a batch transformation;
- browser/tool access;
- broad task freedom;
- the model's ability to invent a strategy.

Therefore a positive P0/P1 result would support **semantic-legibility leverage**, not prove the wider medium hypothesis.

A null P0/P1 result would also not falsify the wider medium.

### 2. The current T3 wording is too revealing for a strong emergence claim

A task phrased as “find whether a broad repeated verification can be handled more systematically” already points the subject toward the desired Shinden-like strategy.

That can test execution of a generic systematic strategy, but not spontaneous discovery of one.

The serious generativity condition should state only the **world-level goal/outcome** and leave serial inspection versus batching entirely latent.

### 3. Controlled micro-world and live dogfood should form a loop, not a one-way ladder

The founding insight came from real work, not from a benchmark.

A healthier research cycle is:

```text
real ecological surprise
      ↓
extract candidate environmental law
      ↓
controlled causal isolation
      ↓
reintegrate into live work
      ↓
look for transfer / new surprise
```

Controlled worlds protect causal claims. Live dogfood protects relevance and serendipity.

Neither should become subordinate to the other.

### 4. Emergence cannot be reduced entirely to a predefined binary

Mechanical scoring is necessary for correctness, cost, coverage, and transfer.

But if every valuable emergent behavior must already fit a preregistered taxonomy, the experiment can become blind to the very category of useful surprise that motivated SWM.

The apparatus should therefore preserve a clearly separated **exploratory novelty ledger**:

- unexpected useful behavior is recorded verbatim from traces/artifacts;
- it does not retroactively change confirmatory primary outcomes;
- it can generate the next controlled hypothesis.

### 5. Research-document growth is now a real burden risk

The campaign has accumulated multiple protocols and audits quickly.

That rigor is useful only if each artifact changes an experiment boundary, exclusion rule, measurement, or implementation decision.

From this point forward:

> prefer executing/falsifying the frozen apparatus over adding another design document unless a concrete unresolved confound requires one.



## 2026-10-08 partial recovery note

Later prior-conversation recovery narrowed part of the previously inaccessible middle interval.

Two Owner-message anchors were recovered:
- 2026-10-02 19:49:44 UTC: capability amplification over mere organization, lower AI-management burden, shared reality with independent minds, agent reach extended through environment/tool senses and actuators, and preservation of freedom/serendipity.
- 2026-10-03 11:28:53 UTC: self-maintained project-state projection, deep critical exploration, and explicit resistance to long-term lock-in from temporary simplifications.

The full surrounding message sequence is still not recovered. Treat this as a narrowed coverage gap, not a complete transcript reconstruction.


## 2026-10-08 additional missing-middle anchors

A broader prior-conversation recovery found several more Owner-level anchors from the previously incomplete founding interval.

- **2026-10-01 21:24 UTC** — Owner accepted the direction that human/Browser/other agent bodies may refer to the same reality through different sensors and interfaces; Browser/Work/Codex was valued as a serious bridge for carrying project soul/history/context, not established as the final architecture.
- **2026-10-02 00:16 UTC** — Owner wanted the project to grow as a snowball while preserving freedom, serendipity and open-ended exploration, and warned against prematurely fixing architecture or future possibilities.
- **2026-10-03 00:11 UTC** — Owner bounded publicness: public lab/code/protocols/synthetic specimens were acceptable; private project reality and raw collaboration memory were not to become the public substrate by default.
- **2026-10-03 02:28 UTC** — Owner stopped the local Codex/Luna path because setup/workspace burden outweighed its current value; the operational burden itself violated the Medium goal.
- **2026-10-03 13:49 UTC** — Owner asked for much more serious structural/fundamental experiments, supported deep Cloudflare exploration, and explicitly rejected letting early simplifications bind the long-term horizon.

These anchors narrow several earlier open questions:
- privacy/publicness had an explicit Owner boundary during the founding period;
- Browser↔Codex was already being treated as a potentially useful bridge whose setup burden could disqualify the current path;
- shared-reality / heterogeneous-sensor thinking and anti-lock-in/open-endedness appeared before the later canonical documents;
- Cloudflare interest was Owner-supported as a research direction, not evidence that Cloudflare had been selected as architecture.

The complete adjacent transcript sequence is still not recovered. Do not infer missing wording, rejected alternatives, or stronger architectural commitments from these anchors.

## Evidence-class refinement for the strong invariant candidates

The 2026-10-08 missing-middle recovery changes how the ten existing invariant candidates should be read.

Several of their **wordings remain synthesized by the assistant**, but their underlying directions now have direct Owner-level support from the recovered founding interval.

### Directly Owner-supported direction

The recovered Owner anchors directly support the substance of:

1. **Capability amplification over organization** — capability gain and reduced AI-management burden were explicit.
2. **Environment over prescribed workflow** — the Owner explicitly returned to the Shinden premise of environments exposing unforeseen affordances/capabilities rather than pre-scripted workflow.
3. **Owner burden must not scale with agent/tool count** — the local Codex/Luna path was stopped when setup/workspace burden outweighed value.
4. **Shared reality, independent minds** — `shared reality, different minds` and same reality through different sensors/interfaces were explicitly endorsed.
5. **Source truth and provenance survive abstraction** — source/provenance and stale/unknown/conflicting states were explicitly protected over invented continuity.
6. **Body heterogeneity is normal** — the exact phrase is synthesized, but the Owner explicitly framed different agents/humans as looking at the same reality through different sensors/interfaces and wanted the medium to extend hands/eyes/ears.
7. **Graceful degradation** — unknown/stale/conflicting state was preferred to fabricated continuity.
8. **Self-maintenance is part of the medium** — self-updating project-state projection was explicit.
9. **Serendipity/freedom must survive optimization** — freedom, serendipity and open-ended exploration were explicit anti-drift requirements.
10. **Temporary implementation choices are replaceable** — early simplifications/prototypes were explicitly forbidden from binding the long-term direction.

### Important provenance caution

This does **not** mean the ten labels above are verbatim Owner quotations.

The evidence class is:

> **Owner-confirmed direction · assistant-synthesized compact wording**

That distinction matters. Future agents may challenge or rename the formulations while preserving the underlying Owner constraints.

The still-missing adjacent transcript sequence matters mainly for:
- chronology and causal development of the ideas;
- additional corrections or rejected alternatives;
- exact scope/boundary language;
- discovering whether other Owner constraints were present but remain unrecovered.

Do not use the improved confidence in these directions as permission to freeze an architecture.
