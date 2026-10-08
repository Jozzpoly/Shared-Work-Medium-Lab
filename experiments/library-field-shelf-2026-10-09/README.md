# Library Field Shelf — public visual/source experiment

**Status:** draft PR #17; unqualified Owner experience, no global estate census, no claim of independent agent adoption. 2026-10-09.

This is a different, intentionally **small** probe beside Claude's more comprehensive Library/Kataster direction. Its question is whether a calm human-readable project panorama can lead to **real first-party actions, original evidence and exact source sections** without lying about project authority or creating an attention obligation.

## Coverage and authority

Exactly **four deliberately selected PUBLIC repositories**, not "4/26 of a correctly sampled inventory" and not the whole estate. The prototype embeds neither private repo metadata nor Claude's private-inclusive Kataster ZIP.

| Place | Actual entry source | Crucial boundary |
|---|---|---|
| Medium | [main research state](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/RESEARCH_STATE.md) and draft [QP PR #5](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/5) | main accepted routing ≠ incubating draft implementation |
| Combat | [main research state](https://github.com/Jozzpoly/Combat-Lab/blob/main/docs/RESEARCH_STATE.md), isolated contact-responsive branch, neutral Pages | no Owner-qualified combat/organism; live public Pages is **neutral smoke only** |
| ReflexBrain | Pre-O0 [CONTINUE_HERE](https://github.com/Jozzpoly/ReflexBrain-Lab/blob/research/pre-o0-foundations-campaign/docs/CONTINUE_HERE.md), [live unqualified owner Field Lab](https://jozzpoly.github.io/ReflexBrain-Lab/probes/owner-field-lab.html) | main = historical R0, Pre-O0 is **one of multiple research lanes**; O-CTRL/G5 PR #45 and other pressure branches coexist; playable does not mean scientifically qualified |
| JURE | [main/docs/STATUS.md](https://github.com/Jozzpoly/Jozz-Universal-Rig-Editor/blob/main/docs/STATUS.md), local [run instructions](https://github.com/Jozzpoly/Jozz-Universal-Rig-Editor#run) | main is accepted foundation, BIND-00 is provisional and the workbench runs locally |

Feniks/Studio and private/local workspaces are **not** included; not indexed does **not** mean nonexistent or dormant. Card prose is **agent-authored provisional interpretation**, not Owner-ratified project direction. Source documents and their own boundaries prevail.

## Instrumental surfaces

- Two reversible presentations: editorial cards and compact list. Both keep the project-native status cautions; no global ranking, urgency count, activity score or "unread" debt.
- Source/action doors link to project-owned repositories, a QP draft World visit, a real ReflexBrain field, a carefully **labeled neutral** Combat smoke, or local JURE start instructions.
- A source-inspection disclosure is **opt-in**. It does not issue network requests in the background during ordinary entry.
- On request it first attempts public GitHub branch metadata; a successful HEAD yields an immutable commit SHA and a second fetch of that exact raw document. It offers a GitHub source receipt at SHA + original line number. Source Markdown is inserted via `textContent`, never executable HTML.
- If the unauthenticated GitHub REST API is rate-limited/unavailable, it still attempts **the same public document at the moving branch path**, marks it `NIEPRZYPIĘTE`, keeps SHA receipt **hidden**, and preserves the first-party source fallback. If the raw source itself is unavailable, it reports failure without inventing a document. No new credential or provider is required.
- From whichever document text is actually obtained, section navigation is derived directly from literal original Markdown headings (up to level 3). It is not an LLM-generated summary, project plan or authority claim. Search indexes only fixed curator-authored card copy; fetching a source cannot silently alter search results.
- Accessible section controls, keyboard-scrollable source text, compact live status messages instead of announcing several thousand source characters, and a responsive single-column narrow layout.

## Actual browser qualification — evidence boundary

The connected Opera browser ran **source-fetch and actual interactive JavaScript** using the test page below. This is different from merely viewing an AXTree or executing a mocked unit.

- [`network-proof.html`](network-proof.html): HTMLPreview-origin GitHub API `200` → exact-sha raw source `200`; exact first source text was visible in AXTree. Independently repeated by Agent_Slack in [PR #17 evidence comment](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/17#issuecomment-6070770230).
- [`browser-e2e.html`](browser-e2e.html): one explicit testing page opens actual served candidate HTML in a same-origin `srcdoc` frame and performs DOM interactions. Verified four project cards, ten source/action links, reading all four original public documents, deep heading navigation (including ReflexBrain's non-introductory `Current next move`), changing source links to line-specific SHA receipts when possible, five deterministic search transitions, reversible compact view, narrow 390px layout without horizontal overflow, limited screen-reader announcement, keyboard focus, and a deliberately nonexistent-repo control without fake receipts.
- **Before rate exhaustion:** real Opera run showed **4/4 exact-SHA source receipts**; each had real API and raw-source responses.
- **After repeat runs exhausted the unauthenticated GitHub limit:** Opera's `api.github.com/rate_limit` returned core `0/60`; API returned an explicit rate-limit error. With the bounded fallback implementation, actual browser E2E then showed **4/4 original documents readable, 0 pinned / 4 explicitly unpinned**, source section navigation retained, and the deliberately unavailable repository correctly rejected.
- E2E test orchestration no longer consumes GitHub REST API quota just to load its own candidate. It hashes actual served moving-ref HTML with browser SHA-256 and states explicitly that this **content hash is not a Git commit HEAD receipt**. The test source itself is in git and can be inspected/repeated. Moving previews, HTMLPreview caching and provider-specific limits remain possible.

The earlier reviewer independently found an overclaim that labeled the selected Pre-O0 source as ReflexBrain's entire active frontier. [Source-bound reviewer note](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/17#issuecomment-6070702230) informed the correction: one lane among several.

## Qualification deliberately missing

Neither a developer's screenshots nor automated PASSes prove that the Owner wants to stay here, finds the art direction satisfying, learns independently, or gains a new workflow. A later **reader other than the maker** is required for external-use evidence; a controlled no-Library comparator is required before claiming incremental agent discovery/capability.

No watcher, backend, event bus, whole-estate generator, access token, private corpus release, Work invocation, unconditional QP adoption or merge to `main` has been introduced. Keep this as a **replaceable draft specimen**, not a new canonical Medium ontology.
