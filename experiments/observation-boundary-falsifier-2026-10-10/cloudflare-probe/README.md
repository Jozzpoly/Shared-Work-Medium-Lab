# Cloudflare B candidate — read-only observation probe

**Status:** isolated experimental branch; not deployed, not accepted Medium product, not a globally coherent observer.

## What this does

Cloudflare Worker serves:
- `GET /health`: only runtime availability, explicitly NOT GitHub source health;
- `GET /project`: semantic HTML list of `docs/RESEARCH_STATE.md` headings;
- `GET /project.json`: same navigational model in JSON.

The Worker first identifies the current `main` Git commit using GitHub API, then fetches **this exact commit** of `docs/RESEARCH_STATE.md`. A response contains an immutable commit URL, Git blob SHA, SHA-256 of observed bytes and a sample time. It NEVER infers project status, accepted Owner verdict, active tasks or agent liveness. A failure is explicit `source-unknown` (503), with HTTP `no-store`.

Use `?ref=cff9839c1ac33189c23d93a399f17b44e8f219a0` on either representation to fetch the **one explicitly approved** exact commit without querying the moving `main` head. All other refs, unknown query parameters, or duplicate parameters are rejected before GitHub access. For two separate HTML/JSON requests **only pinned ref makes the source revision identical by contract**. Default moving-`main` responses are NOT atomic across requests.

## Why Workers Caching, not Cache API

The current Cloudflare Workers Caching (`cache.enabled` in Wrangler) can cache Worker outputs on `*.workers.dev` by normal HTTP response cache headers. It should be tested against actual Workers Builds; this repository only tests request/response semantics and bundling.

The programmatic `caches.default` Cache API is **not a trustworthy workers.dev experiment**: its documented behavior on workers.dev, dashboard previews and across data centers is different. Therefore this probe avoids `caches.default`.

- Current latest-source responses: `Cache-Control: public, max-age=300`.
- Exact-commit responses: `Cache-Control: public, max-age=3600`.
- Errors/health: `Cache-Control: no-store`.
- No custom cache hit flag is fabricated. Runtime/outside cache evidence requires live Cloudflare headers/metrics and repeat requests.
- Never interpret a cached snapshot as live current-state truth.

Docs: https://developers.cloudflare.com/workers/cache/ and https://developers.cloudflare.com/workers/cache/configuration/ .

## Exact Git-linked deployment parameters — NOT YET USER-APPROVED TO DEPLOY

On the user's screenshot, defaults select the **wrong root** (`Shared-Work-Medium-Lab/main` has no root Wrangler config). Clicking Deploy with the defaults can trigger Cloudflare autoconfiguration PR instead of deploying this probe.

When the experiment is actually authorized for live deployment:

| Setting | Required value |
| --- | --- |
| Repository | `Jozzpoly/Shared-Work-Medium-Lab` |
| Worker/project name | `swm-medium-observation-probe` (MUST match `wrangler.jsonc`) |
| Production branch | `experiment/observation-boundary-falsifier-2026-10-10` |
| Root directory | `experiments/observation-boundary-falsifier-2026-10-10/cloudflare-probe` |
| Build command | empty |
| Deploy command | `npx wrangler deploy` |
| Preview command | `npx wrangler preview` (default; branch-isolated Preview, unlike `versions upload`) |
| Runtime secrets | none required for public-scope initial test; optional `GITHUB_TOKEN` stays server-side |
| Public ref allowlist | `PINNED_SOURCE_COMMIT=cff9839c1ac33189c23d93a399f17b44e8f219a0` via tracked `wrangler.jsonc` vars |

In an existing Worker, Cloudflare docs locate branch selection at **Settings > Build > Branch control** and root directory at **Settings > Build > Build Configuration**. If the creation flow does NOT let the Owner select both **before creating/deploying**, STOP; use a separate, controlled repo or a connection workflow that allows both, rather than accepting autoconfiguration on `main`.

The screenshot's `shared-work-medium-lab` project name must not be reused for this Worker unless the configuration is consciously renamed consistently.

Useful docs: https://developers.cloudflare.com/workers/ci-cd/builds/configuration/ and https://developers.cloudflare.com/workers/ci-cd/builds/build-branches/.

## Boundaries and evidence

- Only one public source; no private conversations, personal data, API model calls or writes.
- GitHub unauthenticated public REST limit is shared and finite. Workers Caching should reduce duplicate source calls, but the actual rate, cache hits and costs **must** be observed on real deployment; may still fail with concurrent misses or edge variation.
- Tests simulate the GitHub source and validate pinned ref, failure transparency, HTML escaping and no invented product interpretation. CI also runs `wrangler deploy --dry-run`; neither simulates Cloudflare's actual Workers Cache network.
- No claim of MCP, cross-chat memory, autonomous agent wakeups, shared agent persistence or Cloudflare vendor selection.

## Deployment readiness checkpoint

**SOURCE-TEST PASS, LIVE DEPLOY NOT DONE.** The Worker is ready for a *controlled* read-only deployment after production branch and root directory are confirmed. The repository root selected in the Owner's initial screenshot is still not a valid target. Public route key-space is now bounded: no arbitrary `ref`, duplicated parameters or cache-busting `nonce` can trigger source I/O.

**After deployment:** run `node experiments/observation-boundary-falsifier-2026-10-10/cloudflare-probe/live-qualification.mjs https://swm-medium-observation-probe.<account-subdomain>.workers.dev/` from a checkout. This conducts **seven bounded HTTP GETs** and separates mechanical provenance PASS/FAIL from actual `Cf-Cache-Status: HIT` evidence. The command is for an agent or CI runner; the Owner need not execute it manually. It is NOT run automatically and cannot run until the real URL exists.

**Current evidence:** [21/21 security+mechanism PASS at run #38016748354](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38016748354); [25/25 including synthetic live-qualifier tests at run #38016892935](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38016892935). More recent commits must be requalified on their own GitHub Actions run. `wrangler deploy --dry-run` checks bundling, not cloud availability, real cache hits or Owner value.

## Real B qualification (after explicit deployment)

Compare A and B on the SAME pinned commit: get HTML + JSON and verify observation SHA; measure source requests and latency on repeated identical requests, force unavailable source where safe, check stale cache response behavior; compare orientation against actual source and Owner FAIL, then do a real agent-task comparison. If B has no material gain, stop and retire deployment. Never merge B by machine PASS alone.
