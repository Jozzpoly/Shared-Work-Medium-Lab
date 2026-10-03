# Semantic Medium v0 — first deliberate Shinden-style specimen

## Research question

Can one ordinary web surface be useful to a human while also exposing enough stable, semantic structure that a browser agent can treat it almost like a rich API — and can that surface keep its own state projection fresh without Owner maintenance?

This is not a dashboard project and not a commitment to a final SWM architecture.

The specimen exists to test whether **environmental legibility creates emergent capability**.

## Why web is a serious candidate

The founding Shinden experiment did not succeed because the agent had a purpose-built Shinden tool. It succeeded because ordinary web primitives composed unusually well:

- stable URLs;
- repeated semantic structure;
- links from collection to detail;
- tables with meaningful columns;
- browser-native navigation;
- enough regularity for the agent to invent a batch transformation on the fly.

Modern web standards already contain several underused ingredients for a dual human/machine surface:

- native semantic HTML and WAI-ARIA map meaningful page structure, controls, names, state, and live regions into browser accessibility APIs;
- JSON-LD can be embedded directly in HTML as machine-readable linked data;
- Web Linking gives typed relationships between resources;
- HTTP content negotiation allows multiple representations of one resource;
- HTTP validators such as ETag and Last-Modified provide explicit freshness/version semantics;
- server-sent events can push state changes to an open page;
- hypermedia systems such as Hydra explored machine-readable affordances and runtime-discoverable state transitions.

These are reference points, not dependencies. Hydra in particular is useful conceptually but is not a W3C standard and its Community Group closed in 2026.

## Emerging research axis: HTML itself may already be a small action protocol

Standards research after the first live readback suggests a stronger hypothesis than "semantic HTML is easy to read."

Ordinary HTML already bundles several useful layers:

- **native structural semantics** — headings, regions, lists, tables, articles and controls are mapped by browsers into accessibility APIs;
- **hyperlinks** — stable navigation plus typed relations can connect resources without copying them;
- **forms** — HTML forms expose a destination, method, named parameters, values, validation constraints, and a submit action. In other words, a normal human UI can also describe a bounded parameterized operation to an automated client;
- **embedded structured data** — JSON-LD can place a linked-data representation inside the same HTML document;
- **HTTP representation semantics** — one resource can later expose alternate representations without creating a second project world.

This suggests a possible progression:

```text
human-readable HTML
      +
browser accessibility semantics
      +
typed links / stable resource addresses
      +
native forms as discoverable actions
      +
optional structured representations
      ↓
a web surface that is simultaneously UI, observation surface, and partial action vocabulary
```

That is still a hypothesis. Do not add write forms merely to demonstrate it. First establish that read-only semantics produce useful agent behavior; then introduce one safe, reversible action and observe whether an agent discovers it naturally.

## First live findings

### Semantic readback

The specimen was opened through the existing Opera Browser Connector. Its accessibility tree exposed project state, issue objects, a draft pull request, source links, commit history, timestamps, and the refresh control as meaningful browser objects.

This matters because the browser agent did not need a custom SWM parser to recover those structures.

### Freshness

The first version read the declared research state through a raw-content URL. The preview path served stale state even while newer commits were visible.

Switching the state read to GitHub's Contents API fixed the bounded freshness test: a commit-specific frozen copy of the specimen recovered the newly updated canonical project status without editing the page's project-state content.

Scoped result:

- **PASS:** GitHub-backed projection freshness;
- **PASS:** observed live repository facts can be separated from authored interpretation;
- **not proven:** autonomous reconstruction of project meaning;
- **not proven:** cross-source state beyond public GitHub;
- **not proven:** Shinden-class emergent workflow discovery.

The caching failure is useful evidence: a medium must expose freshness and provenance explicitly rather than equating "request succeeded" with "state is current."

## v0 hypothesis

A small page backed directly by live GitHub state may already provide more useful agent affordance than another project summary.

The first page therefore:

1. fetches live public repository state on load;
2. refreshes itself periodically and when the tab becomes active after being stale;
3. exposes freshness and failures explicitly instead of silently showing old state;
4. uses native semantic HTML first — headings, sections, articles, lists, links, buttons, time elements, definition lists;
5. exposes exact source links rather than copying source truth;
6. mirrors a small live state graph into embedded JSON-LD for clients that inspect DOM/source;
7. stays read-only so the first test isolates perception/orientation rather than permissions and write semantics.

## What is intentionally absent

- no accounts;
- no custom backend;
- no database;
- no task schema;
- no orchestrator;
- no MCP server;
- no attempt to encode all project knowledge;
- no manual Owner-maintained status fields inside the page.

## Primary experiment

Give a fresh browser-capable agent the page URL and a broad instruction such as:

> Enter this project environment, orient yourself, and decide what is worth investigating or doing next.

Do **not** teach it the page structure.

Observe three levels:

- **orientation:** can it reconstruct what the project is and what changed?
- **self-directed navigation:** does it find the relevant sources and choose useful views/actions itself?
- **emergence:** does it invent a useful transformation, comparison, or workflow that the page did not explicitly prescribe?

The third level is the real Shinden-class signal.

## Anti-success conditions

Treat the experiment as weak or failed if:

- the page is only a prettier README;
- the Owner must manually keep it current;
- the agent needs a procedure explaining where to click;
- the page replaces source truth with stale summaries;
- success depends on hidden prompt-specific wording;
- adding structure reduces exploratory freedom more than it increases capability.

## Next layers only if evidence demands them

Potential later experiments include:

- same-resource JSON representation / content negotiation;
- richer typed links and action affordances;
- event-driven refresh from repository webhooks;
- SSE or another live change channel;
- write actions with explicit preconditions and provenance;
- MCP exposure generated from the same underlying state model;
- cross-source projections beyond GitHub.

Do not add these because they are technically attractive. Add them when v0 friction identifies a concrete missing sense or actuator.
