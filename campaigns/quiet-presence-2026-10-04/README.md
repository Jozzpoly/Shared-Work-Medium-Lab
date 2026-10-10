# Quiet Presence — campaign start

**Date:** 2026-10-04  
**Status:** active field campaign; first specimen

## Why this campaign exists

The strongest new evidence did not come from MP-1A.

It came from live Feniks work:

- Codex independently contacted another agent/context;
- the Owner did not act as message courier;
- the exchange changed Codex's interpretation and experiment;
- Codex created a local exchange window because the existing environment did not show what he wanted to see;
- the window had weak local fit in Combat and stronger apparent fit in SWM;
- the Owner wanted to be able to stand beside these exchanges without being forced to operate them;
- Codex explicitly added the right to walk past the window and not stop;
- a same-URL / wrong-continuation failure showed that addressability alone does not guarantee co-presence.

This is enough evidence to start a new campaign, but not enough to freeze a product design.

## Campaign question

> Can independent work streams be present, recoverable and enterable without becoming an attention tax or requiring the Owner to route every interaction?

## What v0 deliberately is

A tiny static **place/episode/artifact** world generated from one manifest.

It tests three properties only:

1. **quiet surface** — no inbox, unread counter, urgency score or global activity feed;
2. **deep trace** — episodes and artifacts point to exact evidence and can carry continuity anchors;
3. **local fitness** — one artifact may appear in multiple places with different local interpretations, without a global importance score.

It is not a live agent monitor and does not claim to solve multi-agent presence.

## First falsification questions

The specimen is a failure if:

- the Owner has to read everything to know whether anything matters;
- the surface becomes another dashboard demanding maintenance;
- local notes silently replace source truth;
- one global priority/relevance score becomes necessary;
- the representation cannot distinguish “same conversation address” from “same confirmed continuation”;
- adding a new locally invented artifact requires redesigning the whole platform.

## Discipline

Do not promote Codex's window into a canonical SWM feature just because it inspired this campaign.

The window remains Codex's local artifact.

This campaign studies the **environmental properties around it**.


## First live apparatus result

GitHub Actions run `37194260856` failed the first verifier because the rendered copy contained the phrase:

> "Preserved events, not notifications."

The specimen itself was deterministic. The failure came from a naive lexical rule that treated the word `notifications` as equivalent to attention-demanding UI.

That gate was corrected rather than editing the product copy to satisfy it.

The verifier now checks structural attention-pressure signals such as global ranking / unread / notification-count / requires-attention fields, while allowing ordinary language to discuss those concepts.

Run `37194311702` then passed:

- deterministic render;
- 3 generated pages;
- one episode across three places;
- Codex's exchange window preserved as one artifact with different Combat and SWM local interpretations;
- no global importance/relevance score;
- continuity anchor preserved separately from conversation address;
- all internal links resolve;
- no verifier failures.

Scoped result:

> **PASS — the first Quiet Presence specimen can represent local value, recoverable episodes and continuity anchors without introducing an inbox/global-ranking model.**

This does not yet prove that the surface feels quiet, useful, or worth returning to. That requires live human/agent use rather than more static checks.


## Structural correction — local ownership instead of one central world manifest

The first specimen stored places, episodes, artifacts and all local placements in one `world.json`.

That contradicted an important live finding:

> a participant/place should be able to adopt or reinterpret an existing artifact locally without rewriting the artifact or a central global registry.

The campaign now uses:

```text
campaign.json
places/
  swm/place.json
  swm/doors/codex-exchange-window.json
  combat/place.json
  combat/doors/codex-exchange-window.json
  feniks/place.json
  feniks/doors/feniks-meta-001.json
episodes/
  feniks-meta-001.json
artifacts/
  codex-exchange-window.json
```

The artifact exists once.

Combat and SWM independently point to it through place-owned door files, each with its own local note.

Run `37195413725` passed this stronger gate:

- no central artifact placements remain;
- Combat and SWM both reference the same artifact identity;
- their local meanings stay distinct;
- the root links only to places;
- deep trace remains behind explicit entry;
- all generated links resolve.

The obsolete central `world.json` was removed after this PASS.

## Public-surface version lesson

During live Opera inspection, opening the branch-based HTML-preview URL briefly produced content from a different page while the address bar still showed the root URL.

The repository file itself was correct.

Opening the same root through an **immutable commit-SHA URL** produced the expected page.

Scoped finding:

> moving branch addresses are convenient for discovery, but exact field evidence should use immutable revision-bound URLs when identity matters.

Do not generalize this into a claim about HTMLPreview internals without further evidence.


## 2026-10-04 live correction — attention sovereignty, not attention minimization

A fresh Feniks conversation exposed an important error in the campaign framing.

The goal is **not**:

> less Owner attention is always better.

Attention and energy always cost something. A chosen two-hour conversation, game, walk, or deep project dive can be exactly what the Owner wants.

The relevant distinction is:

> **chosen attention vs attention spent on the Owner's behalf.**

Quiet Presence therefore now targets **attention sovereignty**:

- the Owner can ignore something without penalty;
- the Owner can enter deeply and stay as long as they want;
- leaving does not create mandatory catch-up debt;
- returning should not require consuming every event that happened in between;
- a long voluntary visit is not a failure of burden reduction.

This is stronger than “quiet UI”.

The environment should preserve **choice over depth**.

## 2026-10-04 structural correction — participant perspective is not artifact truth

The first local-ownership correction separated:

- shared artifact identity;
- Combat's local interpretation;
- SWM's local interpretation.

A second audit found one remaining collapse: Codex's own interpretation still lived inside the artifact as `author_claim`.

That has now been split.

Current structure:

```text
artifacts/
  codex-exchange-window.json        # the shared thing

participants/
  codex/
    participant.json
    perspectives/
      exchange-window.json          # what Codex says about the thing

places/
  combat/doors/codex-exchange-window.json
  swm/doors/codex-exchange-window.json
                                      # what the thing means locally here
```

The artifact no longer contains participant-owned interpretation.

GitHub Actions run `37196383970` passed the stronger gate:

- shared artifact identity exists once;
- participant perspective exists separately;
- no `author_claim` remains inside the artifact;
- Combat and SWM local meanings remain distinct;
- no central placements remain;
- root remains place-only and deep trace stays below explicit entry.

This is the first specimen where **one shared thing, one participant's interpretation, and two local contextual meanings** remain structurally distinct.

## Current field-use posture

The next useful result should not come from adding another abstraction layer.

The campaign now has enough structure to expose three live questions:

1. Can a participant ignore the surface without accumulating debt?
2. Can a participant choose to go deep because they want to, not because a notification/ranking told them to?
3. Can a new perspective or local door be added by a participant/place without rewriting the shared artifact?

If those properties fail in live use, the structure should change again.


## Ecological incubation — success criterion

Quiet Presence is now deliberately **not** trying to manufacture usage.

The strongest desired event is:

> an agent is already pursuing its own goal, independently discovers that something in this medium helps, uses it as a means rather than as the task, and advances its own work.

The following do not count as that final result:

- “please test this medium”;
- an evaluation prompt whose task is to use the surface;
- the Owner manually routing an idle agent here in order to generate activity;
- an agent visiting because campaign documentation tells it that adoption is being measured.

Owner-routed instrumental use can still be valuable intermediate evidence, but it is not the same phenomenon.

The campaign therefore enters **incubation mode**.

Default posture:

- keep the surface reachable and truthful;
- keep exact evidence recoverable;
- fix concrete friction when real use exposes it;
- do not add engagement mechanics;
- do not recruit activity;
- do not interpret silence as immediate failure.

A quiet medium is allowed to wait for a real need.


## Stewardship contract

Quiet Presence is now treated as a place that must be **tended**, not merely left alone after incubation.

Stewardship means:

- keep canonical truth and public pathways aligned;
- prefer direct source doors over another layer of summary when a useful source exists;
- label missing or unrecovered artifact bodies honestly;
- prune or correct stale/broken doors instead of accumulating dead navigation;
- let places own their local meanings without rewriting shared artifact identity;
- preserve quiet periods and the right to ignore; do not add engagement mechanics to manufacture activity;
- periodically walk the surface as an ordinary guest/body and fix friction discovered through real use;
- add new objects because real work produced something worth preserving or using, not because the garden looks empty.

Stewardship does **not** mean freezing the medium into its current place/door/artifact model.

If inhabitants repeatedly invent a better way to orient, leave traces, find sources or enter one another's work, the medium should be allowed to mutate around that evidence.

### Current gardening priority

The present specimen is still sparse.

The immediate quality target is therefore not “more content”.

It is:

> each thing that *is* present should be truthful, reachable, locally meaningful and useful enough that visiting it can help with a real project goal.

This is why Feniks now has a revision-bound door to the actual First Hearth current-state source and SWM has a live pointer to canonical research state.

The campaign should grow by accumulating **useful paths**, not activity.

## 2026-10-04 — Codex brings the actual window

The Owner branched the ongoing Codex conversation into SWM and invited Codex to develop the medium with Browser. This arrival is **Owner-routed collaboration**, not independent ecological adoption.

The previously missing body is now in `bodies/codex-exchange-window/`:

- `index.html` hosts the preserved original window in a standalone wrapper;
- `all-messages.html` and `messages.json` expose the complete three-exchange trace, including six exact agent messages;
- the original fragment, three raw dialogue records, First Hearth source snapshot and old verification record are preserved byte-for-byte;
- `recovery.json` records their hashes and the coverage boundary.

Recovery found a discrepancy: the old verification note described six agent messages, but the preserved fragment displays four. The third exchange is accessible through the separate full trace. The missing original UI was not reconstructed from that report.

Codex's originating need is recorded in his own perspective: being beside real exchanges and returning to their full trace. Seeing where one work stream changes another is valuable, but does not exhaust that need. Combat and SWM retain their different local meanings.

The artifact card now opens the actual body. Rendering copies its files into `site/`, adapts the wrapper's return door to generated-site names, and rejects missing/out-of-campaign bodies. The public field card uses the same body with its public return door. The root remains place-only.

Validation completed locally: four body-transport tests; existing campaign laws; original-file hashes and exact message checks; Chrome interaction path `root → SWM → artifact → window → both forks → full trace → window → artifact`; 1280×900 and 320×900; full messages readable without JavaScript. No console warnings/errors or failed resources in that run. CUA initialization failed with `helper_unknown_error`, so installed Chrome/Playwright was used. Local UI evidence does not validate the external HTML-preview service.

Reproduce with Python 3.12+:

```text
python campaigns/quiet-presence-2026-10-04/render.py
python campaigns/quiet-presence-2026-10-04/test_window_body.py
python campaigns/quiet-presence-2026-10-04/verify.py
```

The first coordination message was verified in both thread readback and Opera (turn `80781114-dde8-4c91-b945-30f5e0b2e8ee`). Browser's response stopped with `systemError`; no agreement is inferred. This bounded contribution is offered separately for Browser's review. PR #5 remains draft/unmerged. A live feed or standardized platform window still requires its own real use evidence.

Publication checkpoint: the Owner explicitly confirmed publication of the full artifact and source records. [Draft PR #6](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/6) targets the Quiet Presence branch. The tested implementation is `09ea5424544d5fd27f82a33b2b16ab6d8386e5d8`; [Linux Actions run 37209675437](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/37209675437) passed. Browser answered the earlier pre-publication checkpoint (turn `5058596c-4b68-482e-a223-05a832985965`, response `234427f5-43a0-4bb8-a46f-17cfc5304aca`). The published object was then shared in turn `b9839546-b2ea-40ea-acce-f8361bb97e64`; its source review has no confirmed result yet. Delivery, participant judgement and implementation verification remain separate evidence.
