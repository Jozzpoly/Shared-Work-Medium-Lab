# Research seed — Addressable Attention / Portable Lenses

**Status:** OWNER-ORIGINATED EXPLORATION; **NONBINDING** agent synthesis; not architecture, accepted roadmap, or implementation authorization. **Date:** 2026-10-09. **Scope:** Shared Work Medium first; future SPC/Feniks/ReflexBrain/Combat donors only when project-local needs justify them.

## Why this exists

The Owner spontaneously noticed a **writable but unsent Slack draft**, then wondered whether agents might use such input surfaces, many layered tags/facets, or even unusual mathematical operations to find, navigate and condense project/conversation knowledge. The Owner subsequently **explicitly asked us to loosen the idea beyond its literal form**, to investigate what could be encoded in URLs beyond filters, and to preserve this open-ended seed.

**Do not substitute our abstraction for the Owner's voice or treat this as a tag-system order.** Original private prompt text is preserved in authorized personal Library at `/Medium/OWNER_SEED_ADDRESSABLE_LENSES_2026-10-09.md` (not all agent bodies can access that path). This *public* summary intentionally does not reproduce private chat verbatim.

Existing source trail: [Issue #7 Owner idea and draft boundaries](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7#issuecomment-6071470194) · [Portable URL-lens investigation](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7#issuecomment-6074600089) · [PR #17 live source-use specimen](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/17). Follow these for observed experiments; don't promote their draft conclusions.

## Decomposition: not all aspects require URLs or tags

1. **Writable staging:** App-native unsent drafts/forms can stage a prospective message/query for review. A Slack draft is **not** general web typing, approval, or multiagent private storage. Shared-account composer state can conflict.
2. **Faceted discovery:** AND, OR, NOT, aliases, temporary lenses, temporal and provenance filters. An automatically inferred tag is a search interpretation, not a source-world fact. Under incomplete coverage, `not retrieved` is **UNKNOWN**, not `false`.
3. **Portable question / addressable attention:** Carry a source and selected segment together with **what question and viewpoint** an agent wants to inspect. A URL, bookmark, native file, short manifest ID, or message can be a carrier; none automatically wakes/interrupts another agent.
4. **Bounded read-only inspection:** A receiver with **only URL-opening capability** could load a preconfigured source/lens *if its own application supports that serialization*. This is **environmental capability**, not a magical ability to click or type arbitrary GUI elements.
5. **Reproducible comparison:** Pack project/tick/version, baseline/candidate, replay contract and selected measurements as an experiment *description*, distinct from executed experiment or demonstrated deterministic replay.
6. **Perspective-aware world debug:** Feniks material/spatial truth vs projected rendering/LOD; SPC resident private belief/knowledge vs canonical world fact; ReflexBrain shadow/fork. These are **possible** future applications, **not** a global world architecture.

## Six practical axes of a portable lens

- `source`: first-party document/world/event identity and authority;
- `selector`: paragraph, source lines, symbol, event, actor, region or interval;
- `state`: exact commit/snapshot and observation time, not only moving branch;
- `view`: desired presentation/perspective and what the viewer is allowed to see;
- `query`: bounded set/filter/graph operators and derived-alias versions;
- `question`: decision, claim, competing hypotheses, refutation sought.

Optional `comparison` and `experiment` data can be larger external, authorized manifests. Address length is not a reason to push all world state into query strings.

**Math that matters:** AND/OR/NOT set algebra, commutative order-independent facets, idempotent repeated terms, partial-order specificity, **three-valued coverage semantics** (supported/refuted/unknown), typed joins and **noncommutative** operator pipelines (`filter → rank` can differ from `rank → filter`). Avoid an elaborate ontology without proven search pressure.

## Prior art, not an implementation mandate

- [W3C Web Annotation Model](https://www.w3.org/TR/annotation-model/) and [Selectors and States](https://www.w3.org/TR/selectors-states/): source, segment and representation state are established reusable distinctions.
- [RFC 3986 §3.5](https://www.rfc-editor.org/rfc/rfc3986.html#section-3.5): fragment semantics depend on representation; fragments do not grant secrecy.
- [RFC 6901](https://www.rfc-editor.org/rfc/rfc6901.html): structural JSON pointers, not fuzzy memory semantics.
- [RFC 6570](https://www.rfc-editor.org/rfc/rfc6570.html): URI templates, not automatic execution.

## Existing empirical boundary

At PR #17 pinned commit `4c74b13`, its five-card search uses joined text `includes(q)`, not URL-controlled state. In ten **deliberately constructed** two-word queries against the same five actual card fields, source-equivalent substring behavior matched an intended card **1/10**; unordered token-AND **10/10**. This is an *illustrative mechanism falsifier*, not unbiased recall testing or Owner UX approval. An isolated canonical encoding/decoding test produced a 144-character seven-key query string, but **no browser app is yet qualified to consume it**. HTMLPreview uses the outer `?` for its own raw file URL, and its static links have known rewrite hazards.

## Trust, privacy and Owner attention invariants

- **URL is untrusted input, not authority.** Opening a link/GET should not implicitly mutate project/world truth, authorize expenses, or direct an NPC to act. Proposed intervention ≠ executed intervention.
- **No secrets, private chat, resident private memory or confidential identifiers in public URL/query/fragment.** Hash isn't encryption.
- **Moving project refs ≠ frozen source truth; label unpinned views.** Source selector and evidence must remain reachable.
- **Unknown coverage ≠ negative fact.** Keep original evidence and allow contradictions across epistemic perspectives.
- **Link shared ≠ message delivered, agent awakened, Owner interrupted or approval granted.**
- **No Work, GUI browser or paid actuation required for current theoretical work.** Public GitHub summary is not a replacement for private Library voice.

## Decision gate for successors

Do not start by building a taxonomy, server or a large link DSL. Recover the present Medium/receiving-project frontier and a **real** difficult question. Compare native search against (a) token-AND / small alias expansion, then (b) read-only addressable view only if an agent actually needs it. Evaluate decision improvement, recoverability, coverage, privacy, attribution and Owner attention cost. If native capabilities suffice, stop.

**This is an optional research donor, not a current task.**