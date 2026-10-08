# Negative control: repository capability search can silently under-cover the estate

**Observed:** 2026-10-08, authenticated GitHub connector. **Scope:** connected repository list / this search body's index and default-branch behavior; not a statement about all GitHub search modalities, live deployments or repository function.

## Trigger

While exploring source-backed reusable capabilities for Medium, code search for `DurableObject` and `WebSocketPair` returned **zero results**. The negative answer conflicted with known Cloudflare multiplayer source.

## Source-grounded checks

1. `mcp__GitHub__list_repositories({page_size:100,owner:"Jozzpoly",include_search_index_status:true})` returned **26 accessible repositories**, of which **2** had `is_code_search_indexed: true` (`Simply_game_experiment` and `voxel-aeronautics-workshop`); **24** were marked false. This is a live connector observation on this date, not a permanent GitHub-wide fact.
2. Connector code search, explicitly scoped to `Jozzpoly/cloudflare-multiplayer-lab`, reported **zero** matching results for each of `DurableObject`, `WebSocketPair`, `SharedYardV0` and `World V0`.
3. Direct `fetch_file` on [`src/index.ts`](https://github.com/Jozzpoly/cloudflare-multiplayer-lab/blob/main/src/index.ts) returned `import { DurableObject } from "cloudflare:workers";` (line 1), `new WebSocketPair()` (lines 169 and 241), and `export class World extends DurableObject` (line 195). Direct `fetch_file` on [`src/world-v0-shared-yard.ts`](https://github.com/Jozzpoly/cloudflare-multiplayer-lab/blob/main/src/world-v0-shared-yard.ts) returned `export class SharedYardV0 extends DurableObject` (line 200). [`wrangler.jsonc`](https://github.com/Jozzpoly/cloudflare-multiplayer-lab/blob/main/wrangler.jsonc) declares the Cloudflare Durable Object bindings and staging environments.
4. Direct allowed Git tree API `/repos/Jozzpoly/cloudflare-multiplayer-lab/git/trees/main?recursive=1` returned **273** entries, `truncated: false`. Directory and exact-file reads remained possible despite indexed code search returning zero. Direct REST `/search/code?q=DurableObject%20repo%3AJozzpoly%2Fcloudflare-multiplayer-lab` returned zero with **`incomplete_results:true`**. A zero here is explicitly not exhaustive.
5. A separate scope hazard: `/repos/Jozzpoly/ReflexBrain-Lab/git/trees/main?recursive=1` returned **1** entry, while `.../git/trees/research/pre-o0-foundations-campaign?recursive=1` returned **178** entries, including `src/medium-spatial-interaction.ts` and `probes/medium-d-r3c-shadow-fork.html`. Both tree responses reported `truncated:false`. The active research branch's source cannot be inferred absent merely because the default branch is sparse.

## Defended finding

> **Search returned zero** is a sensor observation about a *query + index coverage + branch scope + access body*, not a repository-wide evidence-of-absence claim.

The same source can be visible through repository enumeration, branch discovery, Git trees and exact file reads while absent from code search. This is a real, observed instance of the Medium problem: agents can forget or misjudge existing capabilities even though the accessible source contains them.

This does **not** prove that the Cloudflare deployment is currently healthy/available, that another provider's search is incomplete, or that an automatic estate-wide index is needed.

## Immediate composable recovery procedure

When a negative search result would materially determine a project decision:

1. Inspect that body's repository index metadata / search coverage when exposed; if not available, treat coverage as unknown.
2. Recover the owning project's **live branch/frontier** from its native state, not from default-branch search assumptions.
3. If code search is unqualified, use source-native directory or Git-tree listing and fetch likely exact files; cite the exact ref/branch and observed bytes.
4. If candidates cannot be located within a bounded source-native investigation, report **not established / search insufficient**, not `does not exist`.

This is an **agent behavior correction**, not a request for a global registry, crawler, schema, CI machinery or SWM backend.

## Falsifiers / replay caveat

- Search/index readiness can change. Repeat index-coverage observation for a future run before using any ratio.
- This result does not measure recall over all capabilities, model intelligence, time savings or Owner productivity.
- The path-based fallback was easy here because source-native structures exposed plausible filenames. That need not generalize to enormous trees or deliberately obscure code.
