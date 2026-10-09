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
- `state`: exact commit/snapshot and observation time, not only moving branch; **do not collapse when something happened, when a source recorded it, and when an actor learned it into one `asof` timestamp**;
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
- [W3C PROV-O](https://www.w3.org/TR/prov-o/): distinguish entities, activities, agents, derivation, revision and attribution. This is valuable for link receipts but **not** automatically authenticated authorship.
- [RFC 7089 Memento](https://www.rfc-editor.org/rfc/rfc7089.html): a possible temporal web-resource/version-selection donor, not a universal time-travel ability.

## Existing empirical boundary

At PR #17 pinned commit `4c74b13`, its five-card search uses joined text `includes(q)`, not URL-controlled state. In ten **deliberately constructed** two-word queries against the same five actual card fields, source-equivalent substring behavior matched an intended card **1/10**; unordered token-AND **10/10**. This is an *illustrative mechanism falsifier*, not unbiased recall testing or Owner UX approval. An isolated canonical encoding/decoding test produced a 144-character seven-key query string, but **no browser app is yet qualified to consume it**. HTMLPreview uses the outer `?` for its own raw file URL, and its static links have known rewrite hazards.


**New falsifier — multiple clocks:** Consider an SPC event at tick 400, Mira learning of it at tick 900, and our test recording the observation at wall-clock time T. `world_at=400`, `actor_knows_at=900`, and `source_checked_at=T` answer **different questions** even when the URL contains exactly the same actor/event reference. In Medium the same issue appears when an old quote, a later GitHub correction, and the current project frontier differ. A single label `asof=...` hides that disagreement. This is a conceptual counterexample, **not an R6 runtime fact**.

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

---

## Further donor research — IIIF and CQL2 (Agent_Slack, 2026-10-09)

**Type:** agent-derived outside-source research, appended to existing Owner-originated seed without changing the original text or treating it as an Owner requirement. Browser/Opera is disconnected for this run; the evidence below is standards text and GitHub source inspection, **not a live Medium UI qualification**.

### Discovery 1: a link can be a *pure view constructor* rather than an object locator or form

The [IIIF Image API 3.0](https://iiif.io/api/image/3.0/) is a deployed standardized example: a request URI has the form `/{identifier}/{region}/{size}/{rotation}/{quality}.{format}`. With a capable service, opening a link **requests a specified transformation of existing image content** without opening a GUI and moving crop/resize/rotate controls by hand. Its normative *operation order* is `region → size → rotation → quality → format`, and its canonical URI guidance improves reuse and caching. No claim is made that Medium currently runs IIIF.

Important distinction that a tag-only vision misses:

- **Unordered predicates** such as `has(contact) AND has(failure)` are commonly commutative/idempotent (after defining a fixed corpus and truth semantics).
- **Ordered transformations** are not: crop→rotate need not equal rotate→crop; filter→rank need not equal rank→filter. Some "math magic" requires a *typed pipeline*, not a bag of tags.
- **An observing lens** changes a requested representation, not canonical spatial truth, actor knowledge, or source evidence. In Feniks, a URL for camera/LOD/occlusion must not be treated as a URL that changes the world.

A closely related donor is [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/): image/document "Canvas" identity, spatial region `#xywh=`, temporal `#t=`, and annotations can refer to parts of a view. This is relevant to visual source annotation or world-inspection thinking, not proof that physics/actor topology fits IIIF's model.

### Discovery 2: the environment can *advertise a query language* rather than demand prior agent training

The [OGC API — Features Part 3: Filtering](https://docs.ogc.org/is/19-079r2/19-079r2.html) specifies URL parameters `filter`, `filter-lang` and optional `filter-crs`. The query may use [CQL2](https://www.ogc.org/standards/cql2/) (text or JSON grammar), covering richer predicates than flat labels. Crucially, a service can publish **queryable fields and their schemas** through a `/collections/{collectionId}/queryables` resource.

Research implication for Medium: perhaps the high-value primitive is not a permanently authored global tag ontology but a **discoverable local affordance contract**: the particular project/source advertises which entities, dimensions and read-only operations are actually supported *now*. An agent with only URL-construction and navigation could discover those affordances and choose its own observation question; another project need not conform to identical facets.

Do not make the analogy too strong: CQL2 evaluates expressions as `true/false/null` over a dataset, whereas **unknown because the Medium source/branch was never indexed** is a separate *coverage epistemic* condition. Never silently equate a `null` predicate result with a global absence of evidence. Maintain scope/coverage and source provenance alongside the result.

### Discovery 3: a link can *stage* an intended operation without executing it

The [VS Code URL protocol documentation](https://code.visualstudio.com/docs/configure/command-line#_prepare-a-new-agent-session-draft) supports `vscode://agents/new?prompt=...&workspace=...`: opening such a link prepares a new agent-session **draft** with prompt/workspace ready for review, **not submitted**. This is source documentation only, not runtime qualification on the Owner's machine. The original Slack unsent composer discovery is in this broad family. App-native URL protocols and UI drafts are **different carriers with different authorization and collision semantics**; neither implies universal ability to type into arbitrary websites.

Do not conflate three classes:

1. **Read-only observation links**: open a prepared source/view/query; no mutation expected.
2. **Preparation links**: compose editable pending text or an experiment setup; require explicit send/approval and must not overwrite existing drafts.
3. **Authorized action calls**: actual mutation or spending through a separate verified actuator; do **not** smuggle them into GET navigation. [RFC 9110 §9.2.1](https://www.rfc-editor.org/rfc/rfc9110.html#section-9.2.1) requires unsafe operations not to be activated by safe-method retrieval.

### A stronger general hypothesis: *addressable affordances, not one URL DSL*

`source + question + lens + scope/coverage + exact evidence + optional recipient` can travel as an URL, a small immutable manifest, a source-native permalink, a CLI command, or a staged app draft. Whether it becomes a useful capability depends on the recipient's actual parser/renderer/permissions. The carrier does not wake a model, authenticate an Owner message or substitute for receiving-project authority.

A plausible minimal *read-only* flow, without any new backend mandate:

1. Recover current project/source-native boundaries and its declared or discoverable queryable dimensions.
2. Compile the requested view into a **bounded, versioned and explicitly parseable** lens, or reject unsupported operators.
3. Open a result with exact first-party source receipts; distinguish *pinned* from moving data and *not indexed* from negative evidence.
4. Permit alternate perspectives on the same source without overwriting truth. A downstream agent may choose whether to inspect the link; posting it is not delivery/attention.
5. Measure real reduction in Owner copy/paste, search steps and incorrect decisions against the native-tools baseline. If no improvement, use the native search and stop.

**Questions to revisit only under actual pressure:** Who controls field schemas and synonyms without maintenance debt? Can a receiving system preserve unknown coverage and multiple clocks? Does preparing a draft violate shared composer ownership? Does a new URL view bypass private actor knowledge restrictions? How does the Owner resume after an interrupted conversation when no reply was actually delivered? A durable link can make context recoverable **but cannot guarantee that a response ran or arrived**.

### What is not claimed

No new live site, browser click, text field actuator, CQL2 implementation, IIIF instance, URL-based world simulator, approved tagging schema, automatic Slack interruption or periodic job was created. These are comparative external donors and research hypotheses. Public summary links intentionally avoid copying private Owner chat words; authoritative verbatim phrasing remains in authorized Library.
