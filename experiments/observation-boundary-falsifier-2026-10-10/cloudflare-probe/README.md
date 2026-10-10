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

## Actual Owner Cloudflare interface — corrected 2026-10-10

The Owner's video **directly shows** that `swm-medium-observation-probe` already exists and is connected to `Jozzpoly/Shared-Work-Medium-Lab`. The Builds panel has **Root directory `/`**, build command `None`, deploy command `npx wrangler deploy`. The experiment branch is visible as the selected Production branch, but the screen also displays **Unsaved changes** throughout the capture; this recording alone does not prove that the branch was saved. The latest Cloudflare build in the capture had **failed**, with no exact build logs inspected.

**Engineering resolution:** add `wrangler.jsonc` at **repository root on the isolated experiment branch only**. It names the existing Worker `swm-medium-observation-probe` and points `main` to `experiments/observation-boundary-falsifier-2026-10-10/cloudflare-probe/src/index.mjs`. Its other settings match the nested experimental config. No Cloudflare Root directory change, new Worker, new repository, or new project name is needed. `main` has no new root config and must remain unmodified.

**Exact existing settings accommodated:**

| Cloudflare setting | Existing value / requirement |
| --- | --- |
| Worker | `swm-medium-observation-probe` — already exists |
| Git repository | `Jozzpoly/Shared-Work-Medium-Lab` — connected |
| Branch | `experiment/observation-boundary-falsifier-2026-10-10` — selected on screen; save status unverified |
| Root directory | `/` — **keep unchanged** |
| Build command | `None` — **keep unchanged** |
| Deploy command | `npx wrangler deploy` — **keep unchanged** |
| Code entry | root `wrangler.jsonc` on the experiment branch, pointing into the probe folder |
| Approved pinned source | `cff9839c1ac33189c23d93a399f17b44e8f219a0` |

**Verification:** CI must run `node --test` and `npx wrangler deploy --dry-run` from the **repository root**, not `--config` in the nested folder. [Run #38017731891](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38017731891) proved 27/27 tests and a successful root dry-run at commit `642f03cb678775771b0ceaee4e878bd252a58413`. This is not proof of real Cloudflare deployment.

**Important restraint:** no further Owner navigation through speculative settings. If the UI still says `Unsaved changes` for the already chosen production branch, the only potentially needed manual action is **Save** in that existing Builds screen. Do not press Deploy in the old repository-import wizard or change the root directory. An account-side build/deploy must be verified from its actual run logs and the real generated Worker URL, which are not accessible from these GitHub-only tests.

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
