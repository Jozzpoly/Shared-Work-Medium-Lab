# Cloudflare observation probe — live research state

**Status (2026-10-10):** deployed read-only experimental Worker. This is **not** an accepted Medium product or a general shared-agent service. [Draft PR #22](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/22) remains unmerged; canonical Medium **Owner FAIL / not accepted** remains authoritative.

**Live service:** https://swm-medium-observation-probe.jozzpoly.workers.dev/

## What the Worker actually provides

| Route | Contract |
| --- | --- |
| `GET /health` | Runtime-only, NOT GitHub source health |
| `GET /project` | Simple semantic HTML navigation for observed document headings |
| `GET /project.json` | Same navigational model in JSON |
| `GET /project[.json]?ref=cff9839c1ac33189c23d93a399f17b44e8f219a0` | **One allowlisted immutable commit** with SHA-256 checked against pinned expected bytes |

The default, moving `main` view reads `docs/RESEARCH_STATE.md` through GitHub Raw and supplies a **content SHA-256 + sampled-at time**, but **no asserted Git commit or blob SHA**. This is intentional: unauthenticated Cloudflare-origin GitHub REST reads returned a real **HTTP 403** during the first live test. Raw GitHub avoids that particular REST budget dependency. The moving source can still be delayed by GitHub CDN or Cloudflare cache; `main` is **not** a globally atomic revision.

The pinned view uses the immutable GitHub Raw URL and an independently recorded expected SHA-256; mismatching bytes fail closed. It is a reproducible historical sample, not the current project. Every other arbitrary `ref`, duplicated or unknown query parameter is rejected before source access.

A moving source's heading line numbers are sampled positions, **not guaranteed stable deep links** when GitHub changes. HTML explicitly warns about that. Product claims are never inferred from navigation; `claims_about_current_product` stays empty.

## Verified live evidence

- **[GitHub Actions #38018785019](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38018785019)**: 29/29 source/mechanism tests, real pinned Cloudflare HTTP/source-integrity **PASS**, `CF-Cache-Status` sequence **MISS → HIT → MISS** (JSON twice, HTML once). Snapshot digest: `c12c04a6fc23b47caf750beae97ae7dad139bf021f2deca17997ee411ce6573e`.
- **[GitHub Actions #38019221203](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38019221203)**: 34/34 tests, real moving `main` observation `HTTP 200`, epistemic contract **PASS**, separate GitHub Raw comparison **SAME_BYTES** (both SHA-256 `59df42c314d2018d1ab0d31b6d503dd3b04baee90da318fcdbd595874383c7b4` at the sampled time). Pinned cache `HIT` also reconfirmed.
- **Cloudflare dashboard:** production branch `experiment/observation-boundary-falsifier-2026-10-10`, root directory `/`, deploy command `npx wrangler deploy`. The dashboard directly confirmed upload/deployment from this branch; e.g. version ID `72f3e61a-9f91-4bec-b6f0-e80e5a7d0560` at the preceding moving-main code commit. Further head deployments should be checked by their own build record.
- The current tests run from repository root via `node --test` and `wrangler deploy --dry-run`. CI diagnostic PASS is narrower than actual Cloudflare HTTP PASS; both are narrower than Owner/product PASS.

## Deployment and safety boundaries

The existing Cloudflare Worker was configured by the Owner before this line. No new Cloudflare account, Worker, database, credentials, write endpoint, queue, MCP server or private-data surface was created. A **root `wrangler.jsonc` exists only on the isolated experimental branch**, pointing at `cloudflare-probe/src/index.mjs`; do not copy it to `main` by momentum.

Workers Caching uses HTTP `Cache-Control` and `cache.enabled` (not programmatic `caches.default`):
- moving main: **300 seconds** max-age;
- immutable pinned sample: **3600 seconds**;
- failure and health: `no-store`.

Separate HTML and JSON requests on unpinned `main` can legitimately sample different revisions. Across deployment changes an already cached representation can continue serving its earlier source sample until expiry. Observed timestamp and digest are required to interpret freshness; one cache HIT does not prove global consistency or reduced Owner burden.

## Decision boundary / next run

**Mechanism demonstrated:** bounded public Cloudflare source projection, cache HIT and moving-source read without GitHub REST. **Not demonstrated:** differential agent capability over native GitHub/Actions/Pages, lower Owner cost, long-term freshness/reconciliation, private-source access, or satisfying human World / For me UX.

Next, test an **instrumental receiving-agent task** against A (native GitHub/source) and B (Worker projection), including genuine source changes and uncertainty. If no measured advantage over A emerges, park the Cloudflare line as a proven donor. Do **not** generalize the infrastructure or merge PR #22 based on 34/34 machine PASS.

Resume by reading [Medium canonical Research State](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md) and PR #22 HEAD; do not re-open unrelated Cloudflare configuration quests.
