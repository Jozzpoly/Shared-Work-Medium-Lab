# Open Substrate — live campaign state

**Updated:** 2026-10-04  
**Branch:** `campaign/open-substrate-2026-10-04`  
**Base specimen:** Quiet Presence `fbfe3d6bdc224ee5517f6def85a85626681364b3`  
**Current durable head:** `b97927539723baf8904c1f372ce1efd6bb36296a`  
**Latest fully verified implementation run:** `37222293851` on `7a67e150d9b633aa215ef50a87b0b3d1fef95d93`

## Campaign status

Phases 0–3 have produced scoped mechanical/architectural evidence.

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

## Current frontier — second shared-object falsifier

The strongest unresolved generality question is now:

> **have we demonstrated a generic shared-object fallback, or only one convenient object shape plus flexible records around it?**

Only Specimen #1 has exercised an unknown shared object.

The next controlled specimen should therefore be a **materially different second shared object**.

It should intentionally omit conveniences that Specimen #1 provided.

Pressure candidates:

- stable `id` remains, because cross-object identity is the property under test;
- no `kind`, or a missing/empty descriptive kind;
- no Owner-specific view metadata;
- no agent-specific view metadata;
- no body;
- no local/participant records;
- no local source file;
- unfamiliar nested metadata;
- optionally one external provenance URL or no provenance at all.

The test question is not whether the page looks rich.

It is:

> can a minimally described shared identity still exist, be entered through a Polish generic fallback, expose exact raw metadata, and coexist with the richer Specimen #1 without adding a type-specific branch?

Before changing the adapter again:

1. freeze Specimen #4;
2. define exact fallback expectations;
3. run the current adapter unchanged;
4. only modify substrate if the specimen exposes a real closure.

If the current adapter already passes, preserve that as useful generality evidence rather than inventing a change.

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

**Immediate next move:** materialize and test the second radically different shared-object specimen before changing `open_render.py`.
