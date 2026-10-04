# Open Substrate — live campaign state

**Updated:** 2026-10-04  
**Branch:** `campaign/open-substrate-2026-10-04`  
**Base specimen:** Quiet Presence `fbfe3d6bdc224ee5517f6def85a85626681364b3`  
**Current durable checkpoint includes:** Phase 4 + Interaction Walk 02 Owner-ready boundary  
**Latest fully verified implementation run:** `37225383453` on `588f00c567d635362177f7136ef33953cdf33b28`  
**Exact Owner preview snapshot:** `2807bd2843167ecde3dabcc190ca82c6b961b206`

## Campaign status

Phases 0–4 have produced scoped mechanical/architectural evidence.

The campaign remains an **isolated controlled implementation/falsification line**.

It is not a replacement for Quiet Presence ecological incubation, does not alter PR #5/#6, and does not count its artificial specimens as ecological adoption.

## Phase 0 — baseline and invariant audit: PASS / complete

Durable evidence:

- `baseline_probe.py`
- `baseline.json`
- `PHASE0_AUDIT.md`
- Actions run `37219836032`

Demonstrated legacy closure:

- unknown standalone family can be silently invisible;
- unknown local/participant target kinds are rejected;
- unknown metadata may survive raw JSON while disappearing from derived views;
- the current Quiet Presence surface is English-first.

The audit separated:

### Candidate substrate invariants

- stable identity and resolvable intentional references;
- reachable source/provenance;
- participant/local interpretation must not silently become shared truth;
- local adoption should not require mutating shared object identity;
- declared revision/integrity claims should be verifiable;
- generated navigation should not silently break;
- package/body paths need explicit boundaries;
- representation openness must remain separate from executable capability.

### Quiet Presence laws, not universal Medium laws

- quiet place-only root;
- no global attention/relevance ranking;
- deep trace not leaking into the root;
- no notification/unread pressure.

### Ontology closure challenged by this campaign

- closed semantic target kinds;
- fixed object-family discovery;
- specialized renderer required for existence;
- fixed page-count assumptions;
- one view/language for both Owner and agents.

## Phase 1 — generic passive shared object: PASS

Specimen:

`fixtures/specimen-001/`

Shared identity:

`browser-field-knot-001`

Unknown descriptive kind:

`browser/field-knot`

Evidence:

- `specimen1-current.json` preserves the pre-change closure;
- `PHASE1_DESIGN.md`;
- `open_render.py`;
- `open_verify.py`;
- `open-verification-phase1.json`;
- `PHASE1_RESULT.md`;
- PASS run `37221160585` after one syntax-only repair.

Demonstrated:

- unknown `kind` does not need a bespoke renderer branch;
- exact raw object survives;
- unfamiliar nested metadata survives into technical/raw inspection;
- passive Markdown body survives;
- exact English source survives and SHA is verified;
- Owner generic view is Polish-first;
- technical/raw view may be English-first;
- known Quiet Presence remains a separate green regression oracle;
- no script/active capability was introduced.

Scoped warning:

Only one materially unknown **shared-object shape** has been exercised so far.

## Phase 2 — independently owned record packages: PASS

Specimen:

`fixtures/specimen-002/`

This specimen has no `object.json`.

It is a Reflex-owned local trace:

`reflex-local-trace-001`

pointing to the already existing shared identity:

`browser-field-knot-001`

Historical closure was frozen by:

- `specimen2_probe.py`
- `specimen2-current-frozen.json`
- run `37221478502`

The old adapter rejected it only because the package had no `object.json`.

The Phase-2 adapter then separated:

- **object packages** — contribute shared identity;
- **record-only packages** — contribute independently owned records.

Evidence:

- `open_verify_records.py`
- `record-verification-phase2.json`
- `PHASE2_RESULT.md`
- PASS run `37221783971`

Demonstrated:

- Reflex can own a trace outside the target object's package;
- raw trace stays under the owning package;
- target shared object remains byte-identical;
- derived target view may show the local trace without moving it;
- unknown relation semantics survive.

Phase-2 problem discovered:

The first implementation inferred Medium references by recursively treating every arbitrary JSON field named `object_id` as semantic.

That was too aggressive.

## Phase 3 — explicit reference boundary: PASS

Specimen #3:

`fixtures/specimen-003/`

It contains:

- one intentional Medium reference:
  `browser-field-knot-001`;
- one unrelated foreign payload field:
  `external-debug-object-77`.

Historical semantic false-positive is frozen in:

- `specimen3_probe.py`
- `specimen3-current-frozen.json`
- run `37221964353`

The recursive scanner incorrectly rejected the record because it invented Medium semantics for the foreign payload id.

### Phase-3 correction

The active adapter no longer recursively scans arbitrary `object_id` fields.

Intentional Medium associations are declared by a deliberately narrow package-local sidecar:

`medium.refs.json`

Current experimental shape:

```json
{
  "version": 1,
  "links": [
    {
      "record": "trace.json",
      "object_id": "some-stable-object-id"
    }
  ]
}
```

The sidecar is **not** treated as a relation ontology.

It only gives the substrate permission to validate:

> this specific local record intentionally associates with this stable Medium identity.

Raw record semantics remain opaque.

### Exact PASS evidence

Run:

`37222293851`

Head:

`7a67e150d9b633aa215ef50a87b0b3d1fef95d93`

Durable files:

- `PHASE3_REFERENCE_BOUNDARY.md`
- `reference-verification-phase3.json`
- `reference-negative-phase3.json`
- `PHASE3_RESULT.md`
- `open_verify_refs.py`
- `reference_boundary_probe.py`

Demonstrated:

- Specimen #3 raw trace remains byte-identical;
- `external-debug-object-77` remains present in raw content;
- it does **not** appear in Medium reference routing;
- the generated reference set for that record is exactly:
  `browser-field-knot-001`;
- the sidecar is preserved separately and byte-identically;
- Owner view derives the Combat-local record beside the target;
- invalid explicit sidecars are rejected.

Negative boundaries proven:

1. unresolved target identity → rejected;
2. record path escaping package → rejected;
3. missing referenced record → rejected.

Legacy Quiet Presence, Specimen #1, and Specimen #2 remained green in the same pipeline.

### Scoped Phase-3 principle

Current evidence supports this candidate invariant:

> **arbitrary participant/tool/source content stays semantically opaque unless it explicitly opts into Medium-level identity relationships.**

The particular `medium.refs.json` carrier remains experimental.

Do not freeze it as the final protocol.

## Current implementation shape

The Open Substrate adapter is still an experimental parallel layer.

It does **not** replace `campaigns/quiet-presence-2026-10-04/render.py`.

Current discovery is explicit through CLI package roots.

This is intentional.

Repository-wide discovery, semantic search, feeds or recommendation have not been designed.

## Current Owner / agent view posture

For Open Substrate campaign views:

- Owner-facing wrapper defaults to Polish;
- technical/raw inspection may use English;
- original source language remains untouched;
- translation/gloss remains a derived view;
- raw evidence stays reachable behind voluntary depth.

This is still mostly mechanically verified.

A real Owner interaction walk is a later evidence class and can veto a machine PASS.

## Capability boundary

All current specimens remain passive.

No current PASS demonstrates a safe arbitrary active-body model.

Representation openness is **not** execution permission.

Do not add active HTML/JS privileges incidentally while working on representation.

## Active campaign vetoes

Do not:

- modify Quiet Presence to manufacture campaign progress/adoption;
- modify Codex PR #6/body in parallel;
- count artificial specimens as ecological evidence;
- build semantic search/recommendation before scale pressure exists;
- turn `medium.refs.json` into a growing hidden ontology;
- special-case specimen ids, kinds, projects or relation kinds;
- assume every local record must become a shared global object;
- trade Owner clarity for machine elegance;
- infer semantics from arbitrary raw payloads;
- move into active execution before passive representation/reference foundations survive broader pressure.

## Phase 4 — second shared-object falsifier: PASS without adapter change

Specimen:

`fixtures/specimen-004/`

Stable identity:

`minimal-shared-identity-004`

Specimen #4 deliberately omits:

- `kind`;
- Owner/agent view metadata;
- body;
- provenance;
- local/participant records;
- `medium.refs.json`.

Evidence:

- `specimen4_probe.py`;
- `specimen4-phase4.json`;
- `PHASE4_RESULT.md`;
- PASS run `37222682719`.

The existing adapter passed **without any change to `open_render.py`**.

Demonstrated:

- two materially different shared-object shapes coexist;
- a shared object does not need a known `kind`;
- missing kind remains `null`, not synthesized;
- stable id is sufficient for the Polish generic fallback title;
- no provenance/body is invented when absent;
- exact raw JSON remains byte-preserved;
- unfamiliar nested metadata remains inspectable;
- no specimen-specific renderer branch was required.

### Interpretation

This falsifier did **not** expose another shared-object closure.

That is useful evidence.

There is no current evidence-based reason to continue refactoring the passive shared-object representation merely to make it more abstract.

## Current stop/review boundary

The most important current implementation work is complete enough to stop and reassess.

Do **not** mechanically create another specimen or feature.

Current evidence chain:

1. **Phase 0:** legacy closure characterized;
2. **Phase 1:** passive unknown shared object can exist through a generic fallback;
3. **Phase 2:** independently owned local records can reference shared identity without moving/mutating the target;
4. **Phase 3:** Medium relationships must be explicit; arbitrary raw payload remains semantically opaque;
5. **Phase 4:** a second radically simpler shared object passes without another substrate patch.

The campaign has therefore reached a natural decision boundary rather than an unfinished implementation seam.

Before further implementation, first review the combined evidence and deliberately choose the next pressure.

## Interaction evidence — Browser self-walk: PASS to Owner-ready boundary

Durable evidence:

- `RETURN_PREP_OWNER_WALK.md`
- `INTERACTION_WALK_01.md`
- `INTERACTION_WALK_02.md`
- `interaction_view_probe.py`
- exact preview snapshot at `2807bd2843167ecde3dabcc190ca82c6b961b206`

Walk 01 exposed real Owner-facing friction without finding a substrate-truth failure:

- technical `kind` surfaced too early;
- local/participant records were apparatus-heavy;
- English participant text interrupted Polish Owner flow;
- minimal object looked like an empty schema;
- independent technical records had ambiguous duplicate labels.

Only the derived renderer/view layer was changed.

The full regression + interaction-view pipeline then passed on run `37225383453`.

Walk 02 on the exact refreshed snapshot found no new material Browser-level interaction friction:

- root is Polish-first and quiet;
- rich object separates thing/source/local meanings while hiding semantic/raw detail behind voluntary depth;
- English participant original remains exact and is not silently translated;
- technical view remains English and distinguishes independent raw records without semantic inference;
- minimal object now states sparse identity honestly instead of rendering empty schema sections.

### Evidence limit

Opera in this session has no element-click action, so Browser did not physically toggle the `<details>` controls.

The accessibility tree shows them as collapsed disclosure controls, exact generated HTML contains the hidden content, and `interaction_view_probe.py` verifies the boundary mechanically.

Do not claim a stronger click interaction test.

### Current product-level status

**Browser interaction PASS / Owner experiential status unresolved.**

No further Browser-led UX refactor is justified before Owner judgement.

Owner judgement can veto this PASS.

### Immediate frontier

The next real evidence should be the Owner opening the exact snapshot normally and reacting freely.

Do not begin Codex critique, staleness machinery, capability sandboxing, search/discovery work or another specimen before Owner judgement unless an independent regression appears.

## Deferred frontiers

After the second shared-object falsifier, reassess rather than mechanically progressing.

Potential later pressure:

- whether reference sidecars need staleness/revision binding;
- whether record-only packages may exist locally before pointing to a shared identity;
- preservation vs surfacing/stale local trails;
- passive body variety;
- active-body/capability sandbox;
- real Owner browser walk;
- eventual Codex critique;
- ecological discoverability in real project work.

None of these are automatically the next feature.

## Coordination state

- Quiet Presence PR #5 remains draft/unmerged and outside this campaign.
- Codex PR #6 remains draft/unmerged and outside this campaign.
- Browser already left Codex the narrow 4-vs-6 seam.
- Do not contact Codex merely for theory approval.
- Return to Codex once this branch contains a sufficiently mature implementation seam that benefits from an independent collaborator trying to break it.

## Continue protocol

When Owner says `kontynuuj`:

1. recover live branch head and this file;
2. inspect CI/evidence newer than the checkpoint recorded here;
3. continue the current unresolved falsifier rather than restarting architecture design;
4. make the smallest reversible implementation move that produces evidence;
5. run the full regression/falsification pipeline;
6. preserve important historical FAIL/PASS evidence in the repository;
7. update this state before stopping at a meaningful boundary;
8. if a new result falsifies the plan, change the plan rather than defending continuity.

**Prepared return pressure:** fulfilled through Browser Walk 02.

**Immediate next move:** Owner walk of exact snapshot `2807bd2843167ecde3dabcc190ca82c6b961b206`.

Stop implementation until Owner judgement. If Owner reports a product/experiential FAIL, that becomes authoritative for the relevant surface even if CI and Browser checks remain green.