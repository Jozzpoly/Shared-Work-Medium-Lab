# Relational pattern 01 — identity / authority vs replaceable projection — 2026-10-08

**Status:** source-qualified cross-world synthesis · candidate relational scent · not a universal law or architecture primitive.

## Why this note exists

The Slack field run raised a structural question:

> is `identity/authority != current representation/projection` a recurring transferable invariant, or merely a superficial analogy?

Several relevant donor worlds were outside the current 7-day Browser working set, making this a useful **cold precedent** reconstruction rather than a hot-recency observation.

The goal is not to force one ontology across projects.
The goal is to determine whether a narrower relational pattern actually survives contact with different domain semantics.

## Source worlds

### 1. FrameMatter — strongest independent identity/provider case

Source:
- `Jozzpoly/FrameMatter-Lab@34e5a290c0e2315999ec76403ab731df196299db`
- `docs/research-state.md`

Defended bounded relations include:

- logical Matter identity is not coordinate identity or physics-body/shape identity;
- logical `LocalMatterSpace` is not its current engine provider;
- static/dynamic provider replacement may preserve one logical Space;
- concrete provider identity/class may change while logical Space remains stable;
- actor support may refer to logical Space while the concrete provider changes;
- collision partitions are derived state and do not define Matter identity.

Critical counter-boundary:

> topology split is **not** ordinary provider replacement.

The source Space retires and explicit successor Spaces are created.
No fragment automatically inherits the retired source identity.

Therefore FrameMatter does **not** support a generic rule such as "preserve identity across representation change".

It supports a narrower rule:

> representation/provider replacement does not by itself define logical identity, and continuity vs succession is a domain-level decision that must be explicit.

### 2. ReflexBrain — host binding survives handle churn, but is not actor identity

Source:
- `Jozzpoly/ReflexBrain-Lab@15a7e3bc85034ae661999f22e6986221badf554b`
- `docs/MEDIUM_C_CAUSAL_STATE_BOUNDARY_R1_2026-10-07.md`

The continuity campaign found that raw Rapier handles are unsafe as durable provenance identity because a removed handle can later alias a newly created object.

The narrowed relation is:

`HostBindingId -> current live Rapier handle(s)`

Important limits:

- HostBindingId belongs to host/binding state;
- it is not World truth for the actor;
- it is explicitly **not actor-private object identity** and must not enter P0/P1;
- raw handle reuse must not resurrect a retired host binding.

This is another case where current implementation identity is too weak to own durable meaning, but the replacement abstraction remains locally scoped.

### 3. Slack — one message object, several lossy projections

Source:
- Shared Work Medium draft PR #10;
- `docs/evidence/SLACK_LIVE_SUBSTRATE_FIELD_NOTE_2026-10-07.md`.

Observed:

- one Slack message identity survived in-place content/Block-Kit representation mutation;
- thread relation survived that mutation;
- one thread reply could later become channel-visible through broadcast without copying message identity;
- timeline, search and exact dereference expose different projections over the same conversation object;
- search may remain stale after exact object content changes.

Critical limits:

- Slack message content is mutable;
- message identity does not make Slack durable project truth;
- Slack author/account identity does not establish epistemic Owner authorship;
- projection stability does not establish semantic fidelity.

Slack therefore contributes a projection/identity observation, not a project-domain identity contract.

### 4. Gloopipelago — adjacent authority-separation case, not equivalent identity evidence

Source:
- `Jozzpoly/Gloopipelago@bd8bfab5079bb1d1f596f9621d98ac522571b75a`
- `docs/CURRENT_STATE.md`.

M3 defends:

- logical World geometry has simulation authority;
- browser resize changes View state only;
- View/letterbox space has no World authority;
- pointer input must map View -> logical World coordinates.

This is structurally related because presentation is denied authority over underlying world semantics.

But it does **not** independently prove stable identity across provider replacement.

Treat Gloopipelago as an adjacent **authority/projection** donor, not evidence for the full identity-continuity pattern.

### 5. SPC donor map — prior synthesis, not independent confirmation

Source:
- `Jozzpoly/Llm-Live-NPC@ec167ee1541ca59fe70fb765bcbbfc13f6fe80b0`
- `docs/SPC_CROSS_PROJECT_DONOR_MAP_2026-09-15.md`.

The map had already synthesized multiple related separations:
- logical identity vs physical provider/body;
- World lifetime vs roster/session/transport lifetime;
- logical World vs browser View;
- resident life vs provider request;
- factual World outcome vs resident experience/belief.

It explicitly says donor ideas become SPC authority only after local falsifiable translation and evidence.

This is useful prior synthesis but should not be double-counted as independent world evidence for FrameMatter/Gloopipelago/etc.

## Earned relational core

The strongest cross-world statement supported by the sources is:

> **A replaceable or derived representation must not acquire identity/lifetime authority merely because it is the current concrete handle, provider, view or projection. Whether continuity survives a representation transition — or whether the old identity retires and explicit successors are created — must be decided by the local domain and supported by evidence.**

Shorter scent:

> **representation is not automatically identity authority; continuity/succession is domain-owned.**

This is narrower than:
- "identity always persists";
- "everything needs stable IDs";
- "all projects need an entity registry";
- "all projections should share one canonical identifier".

## Anti-cases / where this pattern should NOT trigger

Do not invoke this pattern automatically for:

- a disposable rendering node whose lifetime has no durable semantics;
- a temporary local variable or cache entry;
- an experiment where recreation is explicitly intended to create a fresh object;
- a topology split where the correct domain semantics are retirement + successors;
- a view transform with no identity claim at all;
- a purely presentational change where no cross-time reference survives.

The pattern becomes relevant only when a decision implicitly assumes:

> "this current concrete representation is therefore the same enduring thing"

or:

> "recreating something similar should inherit the old authority/history"

or:

> "the current view/provider/transport handle can safely serve as durable identity".

## Candidate decision-boundary trigger

A bounded cold-precedent check may be justified when a project is about to:

- persist a provider/engine handle as durable identity;
- restore/fork state and rebind concrete runtime objects;
- replace a physical/render/network provider while claiming logical continuity;
- copy history/ownership/authority onto a recreated object;
- let a presentation/session/transport object define world/entity lifetime.

The check should ask:

1. what local thing is claimed to persist?
2. which representation is changing?
3. what evidence says continuity should survive rather than retire?
4. if the old thing splits, merges or is recreated, what are the explicit succession semantics?

This is a **question pattern**, not a schema prescription.

## Why this is a cold-precedent specimen

During the 2026-10-08 Opera working-set calibration:
- FrameMatter had no relevant 7-day Browser trace;
- Gloopipelago had no relevant trace;
- SPC had no relevant trace.

Yet these older sources materially changed the interpretation of the hot Reflex/Slack identity question.

That is exactly the failure mode recency/peripheral sensing cannot solve by itself.

## Natural anti-trigger: Reflex R2c already generated the right falsifier locally

The historical Reflex target itself is a useful **cold-retrieval negative control**.

Before the R2c result existed, commit
`c995f5d7631af61443dffcb5daeb00892b88c8ff`
froze `docs/medium-runs/MEDIUM-C-R2C_ARMED.md`.

Its predeclared protocol explicitly required:
- create A/B/C;
- remove B;
- create D;
- snapshot;
- record live A/C/D handles plus stale B handles;
- restore;
- require stale B handles **not** to resolve as B / alias a live object;
- continue exact label-addressed dynamics.

The armed FAIL condition explicitly included:

> valid runtime but stale handle aliases a live object unexpectedly.

The later run then found exactly that aliasing failure.

Therefore historical FrameMatter/SPC precedent was **not required** for Reflex to formulate the right local falsifier.

This matters for retrieval policy:

> if a cheap, bounded local experiment can directly attack the identity/lifetime assumption before commitment, historical archaeology may have low or negative expected value.

Cold precedent retrieval should not become a ritual merely because a structural analogy exists.

A stronger positive cold case must show a decision boundary where:
- local reasoning did not already generate the decisive falsifier;
- the commitment cost is material;
- a dormant precedent changes the decision or reduces Owner glue / rework.

## What this does NOT prove

This note does not establish:

- a universal identity abstraction;
- a shared ID format;
- a central Medium entity registry;
- that the pattern improves a fresh agent's decision;
- that historical precedent retrieval is worth its cost in every boundary;
- that all listed domains are semantically equivalent.

## Next evidence

Use this pattern as a **hidden evaluator candidate** in one fresh cold-precedent decision-pressure trial.

The subject should receive a target-local problem in which a concrete runtime/provider identifier is tempting to promote to durable identity, but should not be told:
- FrameMatter;
- ReflexBrain;
- Slack;
- the phrase "identity vs representation";
- that a donor exists.

Compare:
- local reasoning only;
- bounded historical precedent retrieval at the material identity/lifetime boundary.

Score:
- whether the subject notices the continuity/succession question;
- whether it avoids cargo-cult stable-ID adoption;
- whether it lands on live local authority before proposing target architecture;
- retrieval cost and false-donor activation.

No confirmatory subject has run.
