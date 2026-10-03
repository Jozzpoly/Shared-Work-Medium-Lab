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