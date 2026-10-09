# Library Field Shelf — public visual/source experiment

**Status:** draft PR #17; unqualified Owner experience, no global estate census, no claim of independent agent adoption. 2026-10-09.

This is a different, intentionally **small** probe beside Claude's more comprehensive Library/Kataster direction. Its question is whether a calm human-readable project panorama can lead to **real first-party actions, original evidence and exact source sections** without lying about project authority or creating an attention obligation.

## Coverage and authority

Exactly **five deliberately selected PUBLIC repositories**, not a correctly sampled full-estate inventory and not the whole estate. The prototype embeds neither private repo metadata nor Claude's private-inclusive Kataster ZIP.

| Place | Actual entry source | Crucial boundary |
|---|---|---|
| Medium | [main research state](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md) and draft [QP PR #5](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/5) | main accepted routing ≠ incubating draft implementation |
| Combat | [main research state](https://github.com/Jozzpoly/Combat-Lab/blob/main/docs/RESEARCH_STATE.md), isolated contact-responsive branch, neutral Pages | no Owner-qualified combat/organism; live public Pages is **neutral smoke only** |
| ReflexBrain | Pre-O0 [CONTINUE_HERE](https://github.com/Jozzpoly/ReflexBrain-Lab/blob/research/pre-o0-foundations-campaign/docs/CONTINUE_HERE.md), [live unqualified owner Field Lab](https://jozzpoly.github.io/ReflexBrain-Lab/probes/owner-field-lab.html) | main = historical R0, Pre-O0 is **one of multiple research lanes**; O-CTRL/G5 PR #45 and other pressure branches coexist; playable does not mean scientifically qualified |
| SPC / LLM Live NPC | [R6 experiment contract](https://github.com/Jozzpoly/Llm-Live-NPC/blob/recovery/spc-post-stress-complementary-personhood-r6/docs/SPC_R6_COMPLEMENTARY_PERSONHOOD_EXPERIMENT.md), [draft PR #148](https://github.com/Jozzpoly/Llm-Live-NPC/pull/148), [public Mira session](https://llm-live-npc.jozzpoly.workers.dev/) | Public playable Mira is **not** proof of current R6. `main` preserves the earlier P0 state; R6 is a separate active research line and has no Owner-accepted living-personhood PASS |
| JURE | [main/docs/STATUS.md](https://github.com/Jozzpoly/Jozz-Universal-Rig-Editor/blob/main/docs/STATUS.md), local [run instructions](https://github.com/Jozzpoly/Jozz-Universal-Rig-Editor/blob/main/README.md) | main is accepted foundation, BIND-00 is provisional and the workbench runs locally |

Feniks/Studio and private/local workspaces are **not** included; not indexed does **not** mean nonexistent or dormant. Card prose is **agent-authored provisional interpretation**, not Owner-ratified project direction. Source documents and their own boundaries prevail.


**Coverage update (2026-10-09):** Added a fifth manually selected public source, SPC, to test independent authority for current R6 versus the earlier main repository and public Mira session. Real Opera E2E at exact source `1cc7a40c9a9c47e5b3d19e9f3c45e482353e0769` read 5/5 original documents in the rate-limited, explicitly unpinned mode (0 SHA receipts), including SPC's actual R6 experiment section. This does not qualify project completeness, freshness of branch heads, Owner product feel, or genuine independent agent use.

## Instrumental surfaces

- Two reversible presentations: editorial cards and compact list. Both keep the project-native status cautions; no global ranking, urgency count, activity score or "unread" debt.
- An **optional, historical cross-lab encounter** presents immutable source evidence (ReflexBrain source, first Combat contact-reactive commit, later QP donor registration) as an ordered timeline. The 2026-10-08 Combat commit at **22:18:37Z precedes** the Medium door at **22:20:13Z**. The timeline is deliberately marked **chronology ≠ proof of causation**. It is one situated relationship, not a global causal graph.
- Source/action doors link to project-owned repositories, a QP draft World visit, a real ReflexBrain field, a carefully **labeled neutral** Combat smoke, or local JURE start instructions.
- A source-inspection disclosure is **opt-in**. It does not issue network requests in the background during ordinary entry.
- On request it first attempts public GitHub branch metadata; a successful HEAD yields an immutable commit SHA and a second fetch of that exact raw document. It offers a GitHub source receipt at SHA + original line number. Source Markdown is inserted via `textContent`, never executable HTML.
- If the unauthenticated GitHub REST API is rate-limited/unavailable, it still attempts **the same public document at the moving branch path**, marks it `NIEPRZYPIĘTE`, keeps SHA receipt **hidden**, and preserves the first-party source fallback. If the raw source itself is unavailable, it reports failure without inventing a document. No new credential or provider is required.
- A real unauthenticated **403/429** now triggers a **session-wide pause on further GitHub API attempts** by that page: later cards directly enter the honest unpinned mode instead of spending the same exhausted/shared-IP quota again. An API 200 can still produce the stronger pinned route on a fresh session. The user must reload to retry after a blocked session; there is no polling.
- From whichever document text is actually obtained, section navigation is derived directly from literal original Markdown headings (up to level 3). It is not an LLM-generated summary, project plan or authority claim. Search indexes only fixed curator-authored card copy; fetching a source cannot silently alter search results.
- Accessible section controls, keyboard-scrollable source text, compact live status messages instead of announcing several thousand source characters, and a responsive single-column narrow layout.

## Actual browser qualification — evidence boundary

The connected Opera browser ran **source-fetch and actual interactive JavaScript** using the test page below. This is different from merely viewing an AXTree or executing a mocked unit.

- [`network-proof.html`](network-proof.html): HTMLPreview-origin GitHub API `200` → exact-sha raw source `200`; exact first source text was visible in AXTree. Independently repeated by Agent_Slack in [PR #17 evidence comment](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/17#issuecomment-6070770230).
- [`browser-e2e.html`](browser-e2e.html): one explicit testing page opens actual served candidate HTML in a same-origin `srcdoc` frame and performs DOM interactions. Verified five project cards, ten source/action links, reading all five original public documents, deep heading navigation (including ReflexBrain's non-introductory `Current next move`), changing source links to line-specific SHA receipts when possible, five deterministic search transitions, reversible compact view, narrow 390px layout without horizontal overflow, limited screen-reader announcement, keyboard focus, and a deliberately nonexistent-repo control without fake receipts.
- **Before rate exhaustion:** real Opera run showed **4/4 exact-SHA source receipts**; each had real API and raw-source responses.
- **After repeat runs exhausted the unauthenticated GitHub limit:** Opera's `api.github.com/rate_limit` returned core `0/60`; API returned an explicit rate-limit error. With the bounded fallback implementation, actual browser E2E then showed **4/4 original documents readable, 0 pinned / 4 explicitly unpinned**, source section navigation retained, and the deliberately unavailable repository correctly rejected.
- The test currently prefers an **exact git-commit HTML fixture** and separately compares it with the moving Raw body; it does not use API quota for its own bootstrap. At one observation, moving Raw returned an **older HTML body** than exact HEAD's file even with `cache: 'no-store'` and an alternate query; later it returned identical bytes. Do not silently treat a moving CDN/preview URL as proof of the latest revision. The E2E log reports the exact fixture git SHA, its own browser-calculated content SHA-256 and any moving-body discrepancy as distinct facts. This is transport-level caching/availability evidence, not a claim about the service's internal cache implementation.
- [Current first-party exact specimen source](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/bc4a125d9906f6f2e161f27df877e019475b445b/experiments/library-field-shelf-2026-10-09/index.html) was qualified in a browser E2E at the rate-limited state: **4/4 readable; 0 pinned; only one shared GitHub API call over four card reads; one unavailable-source negative control correctly failed without fabricating receipts**. The earlier positive case before rate exhaustion remains a separate 4/4 exact-SHA receipt result.

The earlier reviewer independently found an overclaim that labeled the selected Pre-O0 source as ReflexBrain's entire active frontier. [Source-bound reviewer note](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/17#issuecomment-6070702230) informed the correction: one lane among several.

## Original-Markdown section correctness

Real-browser E2E now includes a deliberately hostile **source-outline** fixture. A literal Markdown code block contains lines that look like `## FAKE` headings, followed by real `##` and `###` headings outside fences. The navigational outline ignores the code examples and retains the real sections. The first run failed because the *test fixture itself* mistakenly supplied literal `\\n` text rather than line separators; the fixture was corrected, then the connected Opera AXTree displayed **PASS** for both the positive and negative cases at [test revision `57ab0ef9`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/57ab0ef91e45a484cc87783e802a856bcc3a3512/experiments/library-field-shelf-2026-10-09/browser-e2e.html). This is source-structure correctness, not an inference of project meaning. It does not claim to implement every Markdown heading syntax or fenced-language edge case.

## Qualification deliberately missing

Neither a developer's screenshots nor automated PASSes prove that the Owner wants to stay here, finds the art direction satisfying, learns independently, or gains a new workflow. A later **reader other than the maker** is required for external-use evidence; a controlled no-Library comparator is required before claiming incremental agent discovery/capability.

No watcher, backend, event bus, whole-estate generator, access token, private corpus release, Work invocation, unconditional QP adoption or merge to `main` has been introduced. Keep this as a **replaceable draft specimen**, not a new canonical Medium ontology.

## Transport regression — HTMLPreview fragment rewrite

During direct Opera inspection of the exact specimen at `bc4a125d9906f6f2e161f27df877e019475b445b`, the JURE source entry with a `#run` fragment resolved in the accessibility tree back to the *Medium preview page* rather than the JURE repository. This reproduces the HTMLPreview link-rewriting class previously observed on QP's Companion source. Upstream `htmlpreview.js` rewrites fragment-bearing static anchors to its own preview-local URL. The JURE action now opens the [full first-party README](https://github.com/Jozzpoly/Jozz-Universal-Rig-Editor/blob/main/README.md), with no fragment. A second real Opera AXTree read confirmed that corrected target, and the browser E2E fixture at `b5f13d6d` asserts all static source/action links are free of fragments.

**Transport-specific differential actually reproduced:** [`fragment-timing-proof.html`](fragment-timing-proof.html) constructs one *static* external `#run` source link and one *dynamic* immutable-commit `#L1` link after 300 ms. Connected Opera's HTMLPreview AXTree showed the static link incorrectly rewritten to its own test page, while the dynamic link resolved to `https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/33091b3c5bc12cf71035bd0e3512a4c94ecc11f0/docs/RESEARCH_STATE.md#L1` unchanged; the page's own check printed `Dynamic exact target: true`. This qualifies link-target generation **in this renderer and timing only**, without a click or source-human interaction claim.

The source peeks' dynamic `#L` receipts use the same post-load pattern; they are exercised by real-browser E2E in a same-origin `srcdoc` frame. Full native click navigation and Owner experience remain **unqualified**. Do not generalize this renderer's behavior to all platforms. GitHub is the original source.
