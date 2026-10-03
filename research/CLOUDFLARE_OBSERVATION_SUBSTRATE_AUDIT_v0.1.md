# Cloudflare Observation-Substrate Audit v0.1

**Date:** 2026-10-03
**Status:** research notes; no architecture selection

## Research question

Cloudflare entered the campaign because semantic-medium-v0 produced a real failure: independent browser surfaces exhausted the public GitHub REST budget.

The question is not which Cloudflare products SWM should use. The question is which environmental properties Cloudflare can supply cleanly, and which properties actually help create fresh, shared, selective perception without centralizing intelligence.

## Capability map

| Property | Candidate primitive | Semantic caveat |
| --- | --- | --- |
| shared cached projection | Workers Caching | cache, not durable truth |
| globally readable derived snapshot | Workers KV | eventual consistency |
| ordered project-local coordination | SQLite Durable Object | serialized coordination point |
| reliable async fan-out | Queues | at-least-once, duplicates normal |
| durable maintenance process | Workflows | easy to over-centralize orchestration |
| internal capability composition | Service Bindings / RPC | account-local coupling |
| connected wake-up channel | DO WebSocket Hibernation | body must support persistent channel |
| cheap human/semantic shell | Static Assets / Pages | dynamic routes still invoke Workers |
| measurement | Logs / Tracing / Analytics Engine | quotas, retention, sampling |

## Workers Caching

Current Workers Caching can serve cache hits before Worker code runs. It is tiered by default: a lower edge tier consults an upper tier before the Worker executes. It also performs request collapsing for simultaneous misses on the same cache key.

For SWM this means one observation can be generated once and consumed by many bodies without each body executing a Worker or reading GitHub.

Important trap: the programmatic Cache API has different semantics. Its entries are local to a data center and cache.put does not participate in tiered caching. It must not be mistaken for a globally coherent observation cache.

Vary supports multiple cached representations under one URL, but header values are keyed verbatim. Representation negotiation should therefore use a very small normalized vocabulary.

## Workers KV

KV is useful as a globally readable, read-heavy derived-state cache. It is eventually consistent. Concurrent writes to the same key can overwrite each other, and writes may take time to become visible in other locations.

Good candidates: recent projections, indexes, information scent, non-authoritative caches.

Bad candidates: exact event ordering, authoritative observer cursors, strong coordination truth.

## SQLite Durable Objects

SQLite-backed Durable Objects provide transactional strongly consistent storage, SQL, alarms, PITR, WebSockets and RPC. Cloudflare recommends SQLite for new Durable Object namespaces.

A project-keyed Durable Object is therefore a plausible small strong-consistency island for sequence, deduplication, cursors and invalidation.

The risk is architectural gravity: strong consistency makes it tempting to move the whole Project World into the object. The audit rejects that inference.

## WebSocket Hibernation

Durable Objects can keep WebSocket clients connected while hibernating when idle. This may later support a cheap wake-up channel from environmental events to connected surfaces.

But three capabilities must stay separate: a page can update live; an agent can observe the update when invoked; an agent can be autonomously awakened. Current browser bodies do not automatically imply all three.

## Queues

Cloudflare Queues is at-least-once. Duplicate delivery is therefore a normal system condition, not an exception. Idempotency/deduplication must be designed in.

This aligns naturally with GitHub X-GitHub-Delivery identifiers. A future queue can decouple fast webhook acknowledgement from slower normalization or enrichment, but only if direct webhook-to-event-log processing proves insufficient.

## Workflows

Workflows can execute durably, retry, sleep and wait for events. This is attractive for environmental maintenance such as reconciliation or interpretation invalidation.

It is also the easiest route to reintroduce a central workflow engine that scripts intelligent participants. Use it only for maintenance processes whose state machine genuinely belongs to the environment.

## Service Bindings / RPC

Service Bindings allow Workers and Durable Objects to call one another without public URLs and with low platform overhead. They are useful for separating real semantic/failure boundaries, not as an excuse for microservice proliferation.

## Static assets

Static asset requests are currently free/unlimited. A serious specimen should test a resilient split: the human/semantic shell remains available while dynamic live observation can explicitly degrade to unknown.

## Observability

Workers Tracing automatically instruments outbound fetches, bindings, RPC and handler lifecycles. Traces now propagate across Worker-to-Worker and Worker-to-Durable-Object calls. Custom spans and Analytics Engine can capture experiment-specific metrics.

This is highly valuable for the next phase because source calls, cache behavior, latency, event processing and failure paths can be measured rather than inferred.

Instrumentation itself has quotas, retention and sampling semantics and must be treated as another resource budget.

## GitHub webhook constraints

GitHub recommends subscribing only to needed events, using a webhook secret, responding within 10 seconds, checking event type/action, and using X-GitHub-Delivery as a unique delivery id.

Critically, failed webhooks are not automatically guaranteed to be redelivered. An event-driven observation plane therefore needs reconciliation. Webhooks are a fast change signal, not infallible source truth.

## Observation identity needs a more serious model

The v0 gateway used one observation_id derived from GitHub state. The underlying goal is good: participants should be able to establish whether they reasoned from the same sampled reality.

But a single global id may fail once multiple sources have different observation times, permissions and consistency guarantees.

A more serious experiment should consider an observation manifest containing per-source version/cursor/observed-at/permission/unknown information. This is a hypothesis, not a final schema.

## Structural hypothesis

The strongest Cloudflare-shaped idea is a sensory ganglion, not a backend brain.

It would concentrate transport, cache, wake-up, ordering and observation health while leaving source authority and interpretation distributed.

Source systems -> observation plane -> events/cursors/snapshots/health -> multiple human and agent projections.

The plane should know what was observed, when, through which sensor, at what cost and with what uncertainty. It should not decide what every participant must believe.

## Candidate serious experiment

Compare four sensing conditions over the same controlled source world:

A. Direct polling baseline: every observer reconstructs independently.
B. Shared snapshot: Workers Cache serves one versioned observation.
C. Event plus cursor: webhook changes enter an ordered durable event trace.
D. Adaptive hybrid: events provide wake-up/information scent, shared snapshots provide orientation, exact source reads provide high-resolution evidence.

Required failure injections include duplicate webhook, dropped webhook plus reconciliation, delayed event, stale snapshot, rate limit, Durable Object restart/failure, KV staleness versus event cursor, source change during reasoning, and different observer permissions.

Measure source calls, cache hits, event latency, missed/recovered events, context acquired before useful action, time to correct frontier, stale claims, Owner interventions, provenance recovery and unprogrammed useful workflow behavior.

## Current judgement

Cloudflare is more interesting after deeper inspection, but not because it is a convenient hosting stack. It exposes several separable environmental laws with different consistency/failure semantics, and it now has enough observability to test them seriously.

The strongest danger is equally clear: Cloudflare makes it easy to build a sophisticated central system before proving that sophistication increases agent capability.

Use Cloudflare as a laboratory of environmental primitives, not as an architecture template.
## Correction: do not invent one global event chronology

OSLC Tracked Resource Set and classic distributed-systems work both expose an important flaw in the v0 monotonic global cursor idea.

TRS explicitly notes that event ordering can be meaningful for changes to one tracked resource while having no semantic meaning across unrelated resources. Lamport's classic result makes the broader point: distributed events naturally form a partial order; a total order can be imposed for implementation reasons, but that imposed order is not automatically the same thing as causal truth.

For SWM this means a single Durable Object sequence such as 41, 42, 43 can be a useful delivery/cursor mechanism without becoming the semantic chronology of the project.

A more honest model may need to distinguish:

- delivery order in one transport;
- source-local version/order;
- per-resource causal order;
- observation time;
- explicit dependency/causal relation;
- concurrency/unknown ordering.

This becomes critical when GitHub, conversations, files, external web sources and human judgements enter the same medium.

Design implication:

> preserve partial order where reality only gives partial order; total ordering is an implementation convenience that must not silently become epistemic truth.

## Base + change log is stronger prior art than the v0 cursor

OSLC TRS models a tracked set as a Base plus an ordered Change Log and a cutoff linking them. It also allows log truncation/rebasing while retaining enough overlap for clients to catch up.

This suggests a more serious continuity experiment than an endless event table:

1. a client obtains a bounded base observation;
2. it records the cutoff/cursor associated with that base;
3. later it consumes only newer change traces;
4. when the log is compacted, a new base is published with overlap sufficient for lagging clients;
5. duplicate traces remain recognizable by stable event identity.

TRS also warns that a base/change log can be eventually corrected and still may not represent an exact global point-in-time state. That warning is highly relevant to our observation-epoch concept.

The lesson is not to adopt RDF/TRS wholesale. The lesson is to separate base snapshot, incremental change stream, event identity, cutoff, and completeness guarantees explicitly.
## Cloudflare Agents SDK: powerful donor, dangerous center of gravity

Cloudflare now has a substantial Agents runtime built on Durable Objects. It provides durable identity, embedded SQL state, WebSockets, scheduling, recovery, channels and tool integrations.

This is highly relevant but should not become SWM's center by convenience.

Potential donor properties:

- durable body/session identity;
- persistent local SQL state;
- real-time synchronized client state;
- schedulable work that survives restarts;
- WebSocket communication;
- recoverable execution;
- MCP client/server integration;
- Browser/Sandbox/other capability attachment;
- built-in observability.

Architectural risk:

The product is explicitly optimized around hosting an Agent instance whose state is durable and synchronized. SWM is trying to preserve a different separation: shared external reality plus potentially many independent minds/bodies.

Therefore Cloudflare Agents should initially be treated as a possible **agent body runtime**, not the Project World and not the mandatory orchestrator.

## Important MCP finding: rich agent projections need not be stateful

Cloudflare's current Agents SDK supports the newer stateless MCP path through createMcpHandler and MCP 2026-07-28-style discovery, while the older stateful McpAgent route is deprecated/frozen for migration.

This strengthens the progressive-projection hypothesis.

The same observation substrate could eventually expose:

- ordinary semantic HTML for humans / weak browser bodies;
- JSON or hypermedia for structured clients;
- a stateless MCP resources/tools projection for compatible agents;
- WebMCP tools inside the human page;

without forcing the shared medium itself to become one long-lived agent session.

That separation is strategically attractive: richer bodies can gain richer interfaces without making them prerequisites for the underlying project reality.

## Another identity warning: agent identity is not observer identity

Cloudflare Agent instances have durable identities and synchronized state. That is useful for a body that needs persistence.

But SWM should distinguish at least:

- identity of a project/world resource;
- identity of an observation/observation manifest;
- identity of an agent body/session;
- identity of an interpretation/claim;
- identity of an Owner/human actor where materially needed.

Collapsing these into one Durable Object or session key would create subtle long-term coupling.
## Browser Rendering: potentially a projection compiler, not merely a scraper

Cloudflare Browser Rendering is materially more relevant than a generic headless-browser service.

The current REST API can derive several representations from the same rendered page:

- raw/rendered HTML content;
- links;
- selected element scrape output;
- Markdown;
- JSON extraction with a prompt/schema;
- accessibility tree;
- screenshot;
- a combined Snapshot response containing accessibility tree + HTML + Markdown + screenshot;
- multi-URL Crawl jobs that can return HTML/JSON/Markdown records.

This creates an unusually useful research primitive for SWM:

> one dynamic web source can be sampled once through a real browser and projected into multiple observer channels.

That directly supports the Body × Projection program.

A serious experiment could compare:

- screenshot/human visual channel;
- accessibility-tree weak-agent channel;
- Markdown/text channel;
- full DOM/HTML channel;
- structured extraction channel;

against the **same rendered source state**.

Important epistemic distinction:

- HTML / accessibility tree / links / screenshot are browser-derived observation channels;
- the JSON endpoint can use a prompt or schema to extract structure, so it should be treated as a **derived interpretation/extraction**, not automatically as source truth.

The current Browser Rendering Snapshot API is therefore interesting as a controlled observation multiplexer.

Current cost boundary: Browser Rendering has a small Free allowance (currently 10 browser minutes/day and up to 3 concurrent browsers); Paid includes a larger monthly allowance and charges by browser duration/concurrency after that. This makes it suitable for bounded experiments, not an excuse to continuously crawl the world.

Reference: https://developers.cloudflare.com/api/resources/browser_rendering/

## D1 Sessions and bookmarks: a surprisingly strong continuity donor

D1 read replication is asynchronous, so an arbitrary read replica may lag.

The Sessions API adds **sequential consistency**. A session carries a bookmark, and a later session can start from that bookmark to guarantee it observes a database version at least as up-to-date as the previous session.

Useful properties include:

- monotonic reads;
- read-your-own-writes;
- writes-follow-reads;
- carrying a compact bookmark from one observer session into a later one.

This is strikingly close to an important SWM continuity property:

> resume from a world that is at least as fresh as the world I previously observed.

The bookmark is not a source-world cursor and does not solve cross-source causality. It only applies to data that has already entered the D1-derived view.

That makes D1 potentially interesting for **derived observation projections / indexes**, not as the authority for GitHub/conversations/etc.

Research implication:

A future continuity experiment should compare at least three cursor semantics:

1. source-native cursor/version;
2. derived-view bookmark guaranteeing monotonic observation;
3. event-log cursor describing unseen traces.

They solve different problems and should not be collapsed into one integer.

Reference: https://developers.cloudflare.com/d1/best-practices/read-replication/

## Smart Placement: sensor execution can move toward the source

Workers can currently use Smart Placement or explicit region/host/hostname placement hints to execute closer to upstream infrastructure rather than automatically closest to the end user.

For an observation plane, this suggests another environmental degree of freedom:

> move sensing/aggregation toward expensive or latency-sensitive sources while keeping static/human projections edge-local.

This is probably an optimization, not a foundational law. It should only enter experiments if upstream round trips become material.

Reference: https://developers.cloudflare.com/workers/configuration/placement/

## R2 event notifications: stored artifacts can become eventful without polling

R2 can emit object-change notifications into Cloudflare Queues. The event includes object key, event time, size and ETag where applicable.

If SWM later stores immutable observation artifacts, reports, media or derived snapshots in R2, those artifacts can participate in the change substrate without another polling loop.

This is a donor mechanism, not a reason to put project truth into R2.

Reference: https://developers.cloudflare.com/r2/buckets/event-notifications/

## AI Gateway: potentially useful experimental instrumentation, not project cognition

AI Gateway can provide provider-agnostic request logging, token/cost/latency metadata, caching/rate limiting, and custom-provider routing.

Two properties matter for serious experiments:

- model-call cost/latency/error instrumentation can be centralized;
- payload logging can be disabled while retaining metadata, which is useful when prompts/responses are sensitive.

However Browser ChatGPT product interactions cannot simply be routed through our own AI Gateway, so this is mainly relevant to controlled API-based agent experiments.

Do not let AI Gateway become a new central LLM router unless the experiment actually needs one.

References:
- https://developers.cloudflare.com/ai-gateway/observability/logging/
- https://developers.cloudflare.com/ai-gateway/configuration/custom-providers/

## Revised Cloudflare donor classification

Cloudflare now appears to contain at least four distinct donor families:

1. **Observation acquisition** — Browser Rendering, fetch, source APIs;
2. **Observation transport/freshness** — Workers Caching, webhooks, Queues, R2 notifications;
3. **Consistency/continuity** — Durable Objects, D1 sessions/bookmarks, event cursors;
4. **Projection/capability surfaces** — Static Assets, HTML, stateless MCP, agent/browser bodies;
5. **Experiment instrumentation** — Traces, Logs, Analytics Engine, AI Gateway.

The useful research move is to select individual properties from these families, not to select a 'Cloudflare architecture'.