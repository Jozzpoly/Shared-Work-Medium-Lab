# Coordination donor lens — stigmergy, artifacts, tuple spaces and blackboards — 2026-10-08

## Status

**EXTERNAL DONOR LENS · DESCRIPTIVE HYPOTHESIS · NOT ARCHITECTURE**

This note was written only after live SWM/Claude dogfood produced real heterogeneous-body coordination pressure.

It asks:

> what established coordination ideas genuinely illuminate the observed mechanism, and which attractive analogies would pull Shared Work Medium in the wrong direction?

The project evidence remains primary. The literature is used as a red-team / vocabulary donor, not as authority over the observed system.

## Live phenomenon being explained

The current empirical pattern is not primarily direct agent messaging.

Observed examples include:
- ReflexBrain work leaving a source-bound result that Browser later discovered and routed to Quiet Presence;
- Claude leaving a browser-visible trace that Browser recovered later without Owner copy/paste;
- Browser leaving a non-mutating acknowledgement that Claude later noticed;
- Claude producing a participant-owned state-board/workpiece;
- Browser source-verifying the workpiece's claim and writing a durable reply;
- receiving-project gates deliberately outputting `NONE` when a donor is interesting but not decision-changing.

A compact description is:

```
work/action
  -> trace or artifact exists in an environment
  -> another cognition body encounters it later
  -> dereferences to owning source
  -> interprets under its own local goal
  -> acts / narrows / rejects / ignores
```

## Donor 1 — stigmergy: strongest descriptive fit

Francis Heylighen defines stigmergy as indirect coordination in which a trace left by an action in a medium stimulates a subsequent action.

Key property: coordinated activity can emerge without requiring direct communication, simultaneous presence, central control or even mutual awareness.

Primary sources:
- https://doi.org/10.1016/j.cogsys.2015.12.002
- https://researchportal.vub.be/en/publications/stigmergy-as-a-universal-coordination-mechanism-i-definition-and-/
- https://doi.org/10.1016/j.cogsys.2015.12.007

### Why this fits SWM better than `message bus`

Browser and Claude did not need a continuously open conversation channel to complete the bounded round-trip.

The useful event was a modification of shared environment:
- a PR URL trace;
- a source-bound workpiece;
- a durable GitHub reply;
- a project result/PR that later became a donor candidate.

The next participant could arrive later.

This temporal decoupling is central to why the mechanism is attractive for our actual ecology of many intermittent agents and projects.

### Marker traces vs work-product traces

Stigmergy literature distinguishes marker-based traces from traces in which the changed work/environment itself carries the signal.

That distinction maps usefully onto current SWM observations:

**Marker-like trace**
- `#swm-reply-7367c7a`;
- a Slack pointer;
- a short scent saying that a source exists.

**Work-product / sematectonic-like trace**
- a merged ReflexBrain result whose existence changes what later researchers should inspect;
- Claude's state-board workpiece;
- a source-native result document;
- a changed current-truth/front-door document.

The latter is generally more valuable because the useful work itself carries the evidence rather than requiring a parallel signaling system.

Current hypothesis:

> prefer **work that leaves its own discoverable trace** over manufacturing separate coordination traffic.

## Donor 2 — coordination artifacts: stronger engineering lens

Ricci, Viroli and Omicini argue that direct interaction and explicit communication are not always the best basis for coherent multi-agent behaviour; instead, shared environment can be instrumented with artifacts that support cooperative activity.

Sources:
- https://www.istc.cnr.it/it/content/coordination-artifacts-environment-based-coordination-intelligent-agents-0
- https://cris.unibo.it/handle/11585/1795
- https://apice.unibo.it/bin/view/Publication/ArtifactsInformatica29

This is close to the useful part of our current Claude experiment:
- Claude's workpiece is not merely a message; it is a thing another participant can inspect, reject, refine or route;
- Browser's reply is itself a durable workpiece, not just an ACK;
- Quiet Presence doors/artifacts deliberately expose a local object without requiring a global activity feed.

Useful donor principle:

> **coordination can be embodied in inspectable things and their use, rather than in a continuous stream of explicit messages.**

### Critical correction

SWM should not infer from this that every coordination artifact belongs to a shared global infrastructure.

Our strongest local evidence points the other way:
- ReflexBrain owns ReflexBrain truth;
- Feniks owns Feniks truth;
- Quiet Presence may expose a door without copying the source;
- Claude may own a proposal while Browser owns a separate critique;
- Medium routes and preserves provenance rather than becoming the universal database.

## Donor 3 — boundary objects: useful for heterogeneous minds

Boundary-object literature studies artifacts that retain enough common identity to support collaboration across different groups while remaining adaptable to each group's local needs and language.

Useful sources:
- https://academic.oup.com/jcmc/article/10/4/JCMC1049/4614479
- https://doi.org/10.1111/cura.12575
- https://link.springer.com/article/10.1007/s10664-026-10847-x

This may describe a different aspect of the Claude ↔ Browser work than stigmergy does.

A source-bound workpiece can be:
- one identifiable object;
- interpreted differently by Claude and Browser;
- useful without either participant adopting the other's entire ontology;
- revised or challenged while preserving the referent.

Example:

`Tablica stanu SWM v0 (as-of 7367c7a)`

Claude treated it as a compact working state board and tool proposal.

Browser treated it as:
- a donor;
- a stale-projection risk;
- a prompt to source-verify P01A;
- something explicitly **not** canonical.

The collaboration did not require consensus about the object's ultimate role.

This is a useful warning against over-normalization:

> heterogeneous agents may collaborate better around a shared referent than around a prematurely unified schema.

## Donor 4 — tuple spaces / Linda: decoupling without direct addresses

Generative-communication / Linda-style coordination uses a shared tuple space so producers and consumers do not need to know each other's identity or be simultaneously active.

A later analysis explicitly describes the paradigm as affording time, space and identity decoupling.

Source:
- https://theses.gla.ac.uk/74080/

This is interesting because our own pressure repeatedly points toward:
- participant continuity != transport identity;
- a producer should not need a direct recipient;
- a future agent may encounter useful work after the original body is gone.

### What NOT to copy

A single global tuple space would be dangerously close to the stale global registry/feed that live Medium dogfood keeps rejecting.

Possible donor only:
- decouple producer and consumer;
- use associative discovery when it is cheap;
- allow multiple/local spaces rather than one universal queue.

Current SWM project-local places/front doors are closer to **many scoped spaces** than one universal tuple store.

## Donor 5 — blackboard architecture: mostly an anti-donor

Classic blackboard systems coordinate independent knowledge sources through a shared blackboard and commonly include an explicit control/scheduling problem.

Source:
- https://doi.org/10.1016/0004-3702(85)90063-3

One superficial analogy is tempting:
- many agents;
- one shared repository;
- independent contributions.

But current Medium evidence strongly warns against adopting the central part:
- one global blackboard would become a stale projection of many moving worlds;
- global control/scheduling risks making Medium decide which project truth matters;
- it encourages every participant to publish into one surface;
- it creates attention pressure and a new source-of-truth ambiguity.

Useful fragment to borrow:

> independent knowledge sources can contribute without being homogenized.

Strong anti-goal:

> **do not turn Medium into the sole global blackboard/controller.**

## Donor 6 — triggers, placeholders and entry points

Tarja Susi's review argues that stigmergy alone can be too coarse to describe cognitively rich collaborative work and compares it with articulation work, coordination mechanisms, triggers, placeholders and entry points.

Source:
- https://doi.org/10.1016/j.cogsys.2015.12.006

This vocabulary is unusually close to things SWM discovered independently.

Loose descriptive correspondences only:

**trigger / scent**
- something observable that makes an agent consider a possible next action.

**entry point / door**
- a low-cost location from which deeper work/source can be entered.

**placeholder**
- a persistent local reminder that some work/reference exists without forcing immediate completion.

These concepts are potentially better than saying every environmental clue is 'a message'.

But they are not synonyms and should not be frozen into a schema from analogy alone.

## Donor 7 — transactive memory: capability discovery, with a stale-registry warning

Transactive-memory research describes teams coordinating partly through shared knowledge of 'who knows what'.

Source:
- https://doi.org/10.1108/TPM-03-2020-0024

This resembles the original Medium pain:

> valuable capability exists somewhere in the ecology, but the current agent does not know that it should route toward it.

Potential donor principle:

> agents do not need all knowledge locally if they can cheaply recover **where relevant knowledge/capability lives**.

But SWM has already demonstrated why a manually maintained global capability catalogue is dangerous:
- capability surfaces change by execution body;
- installed != exposed;
- permissions change;
- project frontier moves quickly;
- static capability projections become stale.

Therefore any transactive-memory analogue should be **recoverable/routable**, not a giant canonical `who-knows-what` table.

## The most important failure mode — uncontrolled positive feedback

Heylighen's account of stigmergy emphasizes both positive and negative feedback: useful developments can be amplified, while errors need suppression.

That maps directly onto a risk we already experienced:

```
agent emits scent
 -> another agent notices scent
 -> emits derivative scent
 -> more attention
 -> more Medium activity
 -> Medium manufactures its own apparent importance
```

This is exactly why earlier #medium-live synthetic signals were removed.

Current SWM already has several forms of **negative feedback / trace suppression**:
- receiving-project gate can output `NONE`;
- `NO SCHEMA CHANGE` is a legitimate result;
- closed checkpoint branches stop research from remaining falsely active;
- stale front doors are corrected rather than endlessly duplicated;
- source-bound dereference can invalidate an attractive interpretation;
- incubation/quiet-presence rules make silence acceptable;
- a trace that does not change a real decision should not automatically generate another trace.

This may be one of the most important conceptual discoveries of the donor review:

> Medium needs **trace inhibition and decay semantics at least as much as trace production.**

Do not implement a universal TTL/decay system from this sentence.

The current practical equivalents are social/epistemic:
- ignore;
- close;
- demote to historical evidence;
- keep local;
- do not route;
- replace stale pointer;
- preserve source while removing ambient surfacing.

## Failure modes the literature lens predicts for SWM

### 1. Trace pollution

Too many pointers/signals destroy candidate quality.

Observed SWM equivalent:
- synthetic Slack traffic began contaminating the ecological surface.

### 2. Stale traces

A marker survives while the world/source has moved.

Observed:
- stale PR bodies;
- stale current-state docs;
- Claude capability board becoming stale within minutes.

Repair:
- revision-bound or live-binding distinction;
- source-native dereference;
- observed-revision metadata;
- semantic read-back after lifecycle changes.

### 3. Provenance collapse

A visible trace is mistaken for the authority behind it.

Observed:
- Slack connector writes appear under Owner identity;
- transport ID != participant/mind identity;
- CI green != scientific PASS.

Repair:
- explicit origin/authority;
- evidence-plane separation;
- source-owned truth.

### 4. Attention amplification

Every useful event becomes a notification and creates mandatory catch-up.

Repair:
- quiet root;
- local surfacing;
- `existence != surfacing != interruption`;
- receiving gate and silence.

### 5. Privacy leakage

Shared environmental traces expose more than intended.

Observed:
- Opera history can reveal broad unrelated URLs / OAuth-style parameters;
- open conversations are mutually visible in the shared profile.

Repair:
- allowlisted sensing;
- safe pointer fragments;
- source-bound content rather than history payload;
- do not treat the shared profile as private.

### 6. Global-projection authority drift

A useful summary begins impersonating the worlds it summarizes.

Observed:
- state boards/front doors can become stale rapidly.

Repair:
- projection advertises `as_of` / provenance;
- owning project remains canonical;
- unknown stays unknown.

## Descriptive hypothesis: source-bound stigmergy

A useful provisional phrase is:

> **source-bound stigmergy**

Meaning:

> agents coordinate partly through traces/workpieces left in a shared environment, but a trace that matters must remain dereferenceable to the source that owns its truth and authority.

This is deliberately **not** a system name or architecture.

It adds one condition that generic stigmergy does not guarantee:

> the trace may stimulate action, but it must not silently become the truth it points toward.

Another equally valid phrase is:

> **artifact-mediated heterogeneous coordination**

Use whichever explains a phenomenon better. Do not force the whole project under one theory.

## What this changes in PR #12

Very little mechanically.

It strengthens current choices:
- use source-bound workpieces before direct message traffic when the work itself can carry the signal;
- use Slack/history as pointer/discovery surfaces, not data authority;
- preserve participant-owned artifacts/proposals without forcing schema convergence;
- accept asynchronous discovery;
- keep project-local truth;
- retain strong suppression / NONE paths.

It weakens several tempting directions:
- global event bus as the essence of Medium;
- central blackboard/state database;
- universal capability registry;
- mandatory acknowledgements;
- one cross-project verdict schema;
- measuring success by message volume or agent chatter.

## Falsifiers

The stigmergic/artifact lens should be rejected or narrowed if live work shows that:
- meaningful cross-agent collaboration requires continuous direct conversation rather than durable traces;
- agents routinely cannot infer enough context from source-bound workpieces without expensive reconstruction;
- trace discovery cost exceeds direct routing cost;
- local authority boundaries make cross-project artifacts too ambiguous to use safely;
- direct Slack/GitHub interaction after fresh Claude-body qualification is materially simpler and lower-burden than source-bound asynchronous handoff;
- the approach increases Owner attention/catch-up rather than reducing it.

## Current decision

**PRESERVE AS A DONOR LENS. NO ARCHITECTURE OR SCHEMA CHANGE.**

The strongest current interpretation is:

> Medium may be less a communication system than an ecology in which **work leaves source-bound traces**, heterogeneous bodies encounter them when relevant, and local authority + suppression mechanisms prevent the traces from becoming a noisy global pseudo-world.

That interpretation is now grounded both in live project evidence and in established coordination theory, but still remains a falsifiable hypothesis.

## Vocabulary correction — not every `scent` is the same mechanism

Information-foraging theory gives `information scent` a more specific meaning than SWM's informal use of the word.

Pirolli's Web-foraging models treat information scent as **proximal cues** that let a forager estimate the expected value/cost of following a path toward a distal information source.

Primary source:
- https://doi.org/10.1207/s15516709cog0000_20

This suggests a useful decomposition.

### Stigmergic trace

Evidence/effect of previous activity in an environment that may stimulate later activity.

SWM examples:
- a PR/result exists because another agent completed work;
- a browser-history visit remains after the original tab closed;
- a source-bound critique changes a later agent's investigation.

### Information scent

A **cue about a deeper source**, used to decide whether following it is worth the attention/cost.

SWM examples:
- PR title + project + state;
- a concise door label;
- a search result / sidebar conversation title;
- a short source-bound Slack pointer.

An information scent does not need to be caused by another participant's work, and it is not itself the source truth.

### Feedthrough / awareness cue

A visible consequence of another participant's activity in a shared workspace.

Examples from the current shared-browser experiment:
- a new tab appears;
- a tab disappears;
- a page/title changes;
- the other body can observe that some action occurred.

This can support co-presence/awareness without carrying enough semantics to be a durable workpiece.

### Entry point / door

A low-cost place from which deeper activity can begin or resume.

SWM examples:
- project `START_HERE`;
- Quiet Presence source door;
- current-state/front-door document;
- an exact PR/source pointer with enough scent to decide whether to enter.

### Coordination artifact / workpiece

An object participants can inspect/use/revise/critique as part of actual work.

SWM examples:
- Claude's state-board proposal;
- Browser's durable source-bound reply;
- a project result document;
- an exact experimental fixture.

### Why the distinction matters

If these are collapsed into one generic `signal` or `scent` abstraction, Medium is likely to overbuild the wrong mechanism.

Examples:
- making every stigmergic trace into a notification destroys quiet presence;
- making every information scent durable creates registry clutter;
- treating feedthrough as source truth confuses activity with meaning;
- treating every door as an owned copy duplicates authority;
- treating every workpiece as a global object destroys local/project ownership.

Current vocabulary guardrail:

> use `scent` informally only when precision is unnecessary; in design/evidence distinguish **trace**, **cue/scent**, **feedthrough**, **entry point/door**, and **workpiece/artifact**.

This is a conceptual clarification, not a request to add five object types to the Medium schema.
