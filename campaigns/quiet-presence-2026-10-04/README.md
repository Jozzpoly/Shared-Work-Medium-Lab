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
