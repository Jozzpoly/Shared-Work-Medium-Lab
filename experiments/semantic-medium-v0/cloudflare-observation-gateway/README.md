# Cloudflare observation gateway v0

## Why this exists

The browser-only semantic-medium specimen falsified a simple steady-state design:

> every open surface polls every source independently.

During live use, the public browser-origin GitHub REST budget reached `60/60` requests/hour and the page degraded to HTTP 403.

This bounded probe asks a narrower question:

> Can a tiny shared Cloudflare Worker collapse many browser observations into one cached project observation, while preserving freshness, provenance, source-budget visibility, and multiple representations of the same underlying state?

This is **not** a production backend and does not replace the event-driven direction.

## What the Worker does

One public resource, `/project`, is generated from the same observation object and can be represented as:

- semantic HTML for humans / accessibility-tree agents;
- JSON for structured clients.

The response varies on `Accept` and is cacheable by Cloudflare Workers Caching.

On a cache miss the Worker currently reads five GitHub resources:

1. repository metadata;
2. `docs/RESEARCH_STATE.md`;
3. open Issues;
4. open pull requests;
5. recent commits.

It then exposes:

- source observation time;
- source rate-limit state;
- source validators / provenance where available;
- declared project state;
- directly observed repository objects;
- links back to source truth.

Repeated clients should consume the shared cached representation rather than each spending GitHub requests.

## Adaptive cache policy

The Worker deliberately makes freshness a function of the **observed source budget**.

Without a `GITHUB_TOKEN` secret, the default target TTL is conservative because GitHub's unauthenticated public REST limit is small. If the remaining source budget drops, the Worker lengthens its next cache lifetime instead of blindly continuing to sample.

If an optional authenticated token is later supplied as a Worker secret, the same code can use the larger authenticated GitHub budget without exposing that credential to browsers.

This is only a first approximation. The stronger long-term direction remains:

```text
webhook/change signal
      ↓
shared observation substrate
      ↓
cached semantic projections
      ↓
observer cursor / selective attention
```

rather than periodic full snapshots forever.

## Why Cloudflare is a plausible fit

Current Cloudflare primitives line up unusually well with the experiment:

- **Workers Caching** can serve cached GET/HEAD responses before Worker code runs and can collapse repeated identical reads;
- **Vary: Accept** lets one URL cache human HTML and structured JSON representations separately;
- **Workers KV** is a read-heavy globally distributed cache candidate if later evidence requires persistent shared observations (with explicit eventual-consistency caveats);
- **Durable Objects** remain an option if later evidence requires strongly consistent ordered coordination;
- **Pages/static assets** can host the human surface cheaply while Functions/Workers handle only dynamic observation paths.

None of those is selected as final architecture by this probe.

## Deployment boundary

No deployment is required to keep researching the current branch.

A real deployment would require one-time Cloudflare account setup. An authenticated GitHub path would also require storing a GitHub token or GitHub App credential as a Cloudflare secret.

Do not ask the Owner to perform that setup merely to make the repository look more complete. Deploy only when we have a concrete experiment that cannot be answered locally/staticly.

## Success criteria

A deployed version would need to show, with measurements:

- many browser reads collapse to far fewer GitHub reads;
- source rate-limit state remains visible;
- stale/degraded states are explicit;
- HTML and JSON are generated from one observation model;
- cache freshness is bounded and inspectable;
- no GitHub credential reaches the client;
- the system still degrades usefully when the dynamic gateway is unavailable.

## Non-goals

- no database;
- no accounts;
- no orchestration;
- no write actions;
- no attempt to mirror all project truth;
- no claim that periodic aggregation is the final sensing model.
