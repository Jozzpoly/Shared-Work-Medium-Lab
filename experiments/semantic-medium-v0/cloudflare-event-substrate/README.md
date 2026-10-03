# Cloudflare event substrate v0

## Research question

Can one tiny push-driven observation service turn source changes into a durable shared event cursor so that many agents can resume from deltas instead of independently polling GitHub?

This is the push-side complement to the cached observation gateway. It is intentionally narrow.

## Shape

```text
GitHub webhook
    ↓  signed delivery
Cloudflare Worker
    ↓  verify + normalize
one Durable Object per project
    ↓  ordered SQLite event log
GET /events?after=<cursor>
    ↓
many human/agent observers
```

## Why Durable Object for this probe

Workers KV is attractive for read-heavy cached snapshots, but its reads are eventually consistent across locations. The event-cursor experiment specifically cares about ordered, non-duplicated traces and exact resume positions.

A single SQLite-backed Durable Object gives the project one serialized coordination point and strongly consistent storage while still being available on the Workers Free plan.

This is not a claim that every SWM project needs a Durable Object. It is a bounded fit for the exact property being tested: ordered shared change traces.

## What gets persisted

Only a small normalized envelope:

- monotonic local sequence number;
- GitHub delivery id for deduplication;
- GitHub event type and action;
- receive time;
- target URL when one can be recovered;
- actor login;
- SHA-256 digest of the original payload.

The full webhook payload is deliberately not stored by v0. Rich evidence remains at the source URL when possible.

## Cursor contract

`GET /events?after=42&limit=50` means:

> give me traces with local sequence numbers greater than 42.

The response includes `next_cursor`, which is simply the highest returned sequence. A new agent does not need the old model context; it needs the durable cursor plus enough environmental traces to decide what to inspect.

## Security boundary

Webhook deliveries must carry a valid GitHub HMAC signature generated from a secret stored only as a Cloudflare secret.

The service rejects unsigned/invalid deliveries and deduplicates GitHub delivery ids.

## Not yet proven

- no live Cloudflare deployment exists yet;
- no GitHub webhook has been connected;
- no delivery/retry/redelivery behavior has been measured;
- no cross-source events exist;
- no semantic relevance routing exists beyond the normalized target URL.

Do not promote this to architecture before deployment evidence.
