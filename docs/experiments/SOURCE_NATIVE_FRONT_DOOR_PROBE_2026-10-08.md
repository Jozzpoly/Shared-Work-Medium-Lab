# Source-Native Front Door Probe — 2026-10-08

**Status:** LIVE BOUNDED DOGFOOD · DRAFT-BRANCH ONLY · NOT ARCHITECTURE

## Question

Before building a shared event feed or central capability registry:

> can ordinary project repositories already expose enough current-truth structure for a Browser agent to orient, reject stale/cross-project temptation, and decide whether deeper traversal is justified?

This probe samples existing labs. It does not require every project to adopt one schema.

## Sampled project front doors

Observed live repository surfaces:

| Project | Source-native current door |
|---|---|
| Combat Lab | `docs/RESEARCH_STATE.md` |
| Companion Brain Lab | `docs/CURRENT.md` |
| LLM Live NPC | `docs/PROJECT_STATE.md` |
| FrameMatter Lab | `docs/research-state.md` |
| Nextgen JV | `docs/NEXTGEN_JV_CURRENT_STATE.md` |
| Planet Matter Lab | `AI_PROJECT_MEMORY.md` |
| ReflexBrain | root README redirects away from historical `main` to active branch + mutable current-state authority |

The names are heterogeneous. The useful commonality is semantic, not syntactic:

> each project can tell a newcomer where current authority lives and what must not be inferred from stale/history/projection surfaces.

## ReflexBrain front-door traversal

Root README states:
- `main` is historical R0 baseline;
- active branch is `research/pre-o0-foundations-campaign`;
- continuity PR is #6;
- recover first through `docs/CONTINUE_HERE.md`;
- mutable current-state authority is `docs/PRE_O0_CAMPAIGN_CURRENT_STATE_2026-10-06.md`;
- status/HEAD are deliberately not copied into README and must be checked live.

Live verification:
- PR #6 is open/draft;
- branch: `research/pre-o0-foundations-campaign`;
- PR head observed: `742c0a6f40063f614b656b6053b94ec6293e30ee`;
- PR updated 2026-10-07T23:24:16Z.

Current-state file says:
- foundational campaign converged;
- O-CTRL contract frozen;
- atomic execution in progress;
- no run currently active;
- historical PR #5 is specimen evidence, not implementation authority.

**Finding:** the repo front door encodes not just state, but a *freshness protocol*: source identity first, then mutable current authority. A generic feed duplicating one status line would lose this.

## Combat -> Companion negative transfer check

Candidate-generation pressure:
- Combat current frontier is embodied/material agency beyond transit;
- Combat intends to discover useful body/world phenomena.

Potential superficial relation:
- Companion is embodied and has movement/collision/world concerns.

Receiving local truth:
- Companion `docs/CURRENT.md` says movement substrate is **closed-enough for current research**, explicitly not a product PASS;
- movement should be reopened only when a **new concrete failure in richer teammate gameplay** shows the substrate blocks the active behavior question;
- the current strategic objective is recovery toward richer teammate behavior, command/autonomy/action, not another movement-only gate.

Sender local truth:
- Combat currently has **no active research specimen**;
- its current frontier is pre-implementation design;
- historical mechanisms have no inheritance rights.

Decision:

> **NONE / DO NOT ROUTE NOW.**

Combat has not yet produced new embodied evidence that would falsify Companion's scoped closure. A cross-project similarity is not enough.

This is a successful negative decision: current-truth doors prevent Medium from turning conceptual relatedness into attention debt.

## Combat -> ReflexBrain negative transfer check

Potential superficial relation:
- both projects currently care about bodies/world coupling and material consequences.

Receiving local truth:
- ReflexBrain Pre-O0 campaign has already selected a bounded first substrate;
- B1 oriented rigid body is primary candidate;
- B0 disc is mandatory control;
- O-CTRL and M0-Lite are already frozen as first research candidates;
- atomic execution is in progress.

Sender local truth:
- Combat has not yet built the new serious discovery specimen.

Decision:

> **NONE / WAIT FOR NEW EVIDENCE.**

Importing Combat's current design discussion into Reflex would add another unresolved design influence while Reflex is deliberately executing a frozen bounded substrate.

If Combat later produces evidence that directly falsifies B1/B0 assumptions or reveals a material phenomenon Reflex cannot represent, the relation can be re-evaluated.

## Stale-root counterexample — LLM Live NPC

The simple "find a CURRENT/PROJECT_STATE file" heuristic immediately failed under live pressure.

Observed:
- root `docs/PROJECT_STATE.md` says **Updated: 2026-09-05** and still describes P0 infrastructure;
- the repository has extensive later recovery/refoundation branches;
- latest active PR observed: **#148**, updated 2026-09-30;
- PR #148 points explicitly to branch `recovery/spc-post-stress-complementary-personhood-r6`;
- the PR body names `docs/SPC_POST_STRESS_RECOVERY_PROGRAM.md` as **Canonical execution authority**;
- that branch-local document identifies the post-stress recovery program and supersedes an earlier execution program;
- PR #148 itself carries the more current active frontier: single-current-plan autonomous reappraisal.

Therefore:

> a named root front door is a candidate authority, not self-validating current truth.

The source-native recovery chain here is:

`root state looks old`
-> `repository activity contradicts it`
-> `inspect latest active PRs`
-> `PR identifies live branch + canonical execution authority`
-> `read exact branch-local authority`.

This still avoids corpus-wide search.

### Front-door freshness test

Before trusting a front door when currentness matters, compare at least one cheap volatile source:

- repo `pushed_at` / active branch movement;
- latest active PR update;
- explicit branch/PR named by README;
- current HEAD/CI where project rules require it.

If a supposedly-current document is materially older than obvious live project activity, classify:

> **FRONT_DOOR_FRESHNESS_GAP**

Do not:
- declare the project stale;
- fall back immediately to global semantic search;
- copy a guessed replacement state into Medium.

Instead, traverse the project's own freshest active work surface and look for an explicit local authority pointer.

This is the first material falsifier of the naive current-file heuristic and strengthens the case for **source-native traversal + freshness contradiction handling**, not one universal naming convention.

## Implication for candidate generation

A useful peripheral mechanism needs at least two stages:

1. **candidate appearance**
   - memory;
   - open tabs/history;
   - repository activity;
   - explicit cross-project mention;
   - sparse external scent.

2. **local current-truth gate**
   - recover the receiving project's own current authority;
   - ask whether the candidate changes the current question;
   - respect explicit closures/frozen bounded experiments;
   - return NONE when no material edge exists.

This is cheaper and safer than a global relevance score.

## Front-door heuristic (candidate, not schema)

When a repository becomes relevant, use the smallest source-native traversal:

1. root README / repository entrypoint;
2. follow explicit `CURRENT`, `RESEARCH_STATE`, `PROJECT_STATE`, `CONTINUE_HERE`, project-memory or equivalent pointer;
3. verify volatile branch/PR/HEAD when the entrypoint says it matters;
4. only then open deeper corpus/evidence relevant to the local question.

Do **not**:
- scan the whole docs tree by default;
- infer current state from filename recency alone;
- force projects to share one filename/schema;
- copy mutable current state into Slack merely to make it discoverable;
- route cross-project evidence merely because the projects are thematically related.

## Falsifier

This pattern is weak if:
- front doors are routinely stale or misleading;
- projects lack a reliable current authority;
- agents cannot discover the front door cheaply;
- the relevant cross-project evidence routinely lives outside what current authority points toward;
- maintaining these doors costs more than the orientation they save.

Those cases should generate a specific missing-edge problem. They do not justify a central registry by default.

## Current result

**POSITIVE BOUNDED.**

Existing heterogeneous project front doors already provide meaningful local proprioception and can suppress bad cross-project routing.

The strongest current Medium role is therefore not to mirror their state. It is to help agents:
- notice a candidate project;
- find that project's own front door;
- verify reachability/freshness;
- let the receiving project's current truth decide whether to continue.

