# Phase 0 audit — ontology checks vs candidate invariants

**Campaign:** Open Substrate  
**Date:** 2026-10-04  
**Status:** working audit; conclusions are scoped to the current implementation

## Dla Ownera — skrót

Obecne Quiet Presence ma kilka bardzo dobrych zabezpieczeń, ale są one wymieszane z założeniami typu „wiemy z góry, czym jest artefakt, epizod i źródło”.

Nie chcemy po prostu „poluzować walidacji”.

Chcemy zachować zabezpieczenia dotyczące prawdy, źródeł, własności i spójności, a usunąć tylko te miejsca, które mówią:

> „nowa rzecz jest niedozwolona, bo jeszcze nie wymyśliliśmy dla niej typu”.

## Evidence baseline

Actions run `37219836032` at head `89131cfa2689c5ba3a71cb11bb02d26c842a8662` completed successfully.

The preserved `baseline.json` demonstrates:

- known Quiet Presence still renders and verifies;
- an unknown standalone object family is silently undiscovered;
- a local door to an unknown target kind is rejected;
- a participant perspective to an unknown target kind is rejected;
- an unknown field on a known object survives in source JSON but is absent from the generated view;
- the current root is explicitly English-first (`lang=en`, `Enter this place`).

## Classification method

Each current rule is classified as one of:

- **candidate invariant** — protects truth, integrity, ownership, addressability or safety and may deserve a general form;
- **campaign law** — valid for Quiet Presence but should not automatically become a universal Medium law;
- **ontology closure** — assumes today's object taxonomy or rendering model;
- **mixed** — contains a useful invariant encoded through a type-specific mechanism.

The classifications below are hypotheses for implementation pressure, not final doctrine.

## Renderer audit

### Fixed discovery directories

Current loader discovers:

- `places/*/place.json`
- `episodes/*.json`
- `artifacts/*.json`
- `sources/*.json`
- `participants/*/participant.json`

**Classification:** ontology closure.

Useful property underneath: objects need stable discovery/addressability.

Problem: a new family placed beside these directories can exist in Git while being semantically invisible to the generated environment.

### Door target dispatch

Current doors branch on `episode`, `artifact`, `source`; unknown target kinds terminate rendering.

**Classification:** mixed.

Useful invariant:
- a local relation must resolve to a real target.

Ontology closure:
- target resolution is coupled to a closed list of target families;
- display/action labels are coupled to target family.

Desired pressure:
- resolution should be identity-based;
- unknown relation semantics should not require a new core branch;
- specialized known views may remain.

### Participant perspective target dispatch

Perspectives currently resolve only to `artifact` or `episode`.

**Classification:** mixed.

Useful invariant:
- a participant-owned statement should identify its target and remain participant-owned.

Ontology closure:
- only two target families may receive perspectives.

The ownership invariant should survive even if target families change.

### Artifact body handling

Known artifacts may declare a `body_href`; renderer checks that it is inside `bodies/<artifact>/`, exists, and copies it into generated output.

**Classification:** mixed, with strong candidate invariants.

Useful properties:
- body path cannot escape the campaign body root;
- declared body must exist;
- preserved body is not silently synthesized;
- byte-preserved source files can be separately verified.

Type-specific assumption:
- arbitrary bodies are currently coupled to the `artifact` family.

Open question:
- what is the general body/capability contract for an unknown form?

### Specialized page generation

The renderer generates one page per known place/episode/artifact and assumes known field shapes.

**Classification:** ontology closure plus useful enhancement.

Specialized rendering is valuable; requiring it for existence is the problem.

Candidate direction:
- specialized renderer if known;
- generic envelope/view if unknown.

### Root place-only navigation

**Classification:** Quiet Presence campaign law.

It protects this field experiment from becoming a feed.

It should remain a regression law for Quiet Presence, but must not automatically define every future Medium surface.

## Verifier audit

### Forbidden global ranking / attention fields

`priority`, `importance`, `global_rank`, `relevance_score`, unread/notification fields, etc.

**Classification:** Quiet Presence campaign law with a broader design warning.

Do not generalize the exact forbidden field-name list into the substrate constitution.

The deeper property is that Quiet Presence should not create global attention pressure/ranking.

### Reject central artifact placements

**Classification:** mixed.

The exact `placements` field check is campaign-specific.

The deeper candidate invariant is:
- local adoption/meaning should be able to exist without mutating shared object identity.

### Reject `author_claim` inside artifact

**Classification:** mixed.

The exact field name is historical.

The deeper candidate invariant is:
- participant-owned interpretation must not silently become shared object truth.

### Source href / revision check

If a source declares a revision, the current verifier requires the revision token to appear in its href.

**Classification:** candidate provenance invariant, though current string matching is only one implementation.

The principle worth preserving:
- a claim of revision-bound identity should resolve to revision-bound evidence.

### Known target resolution

Unknown target kinds fail.

**Classification:** mixed / ontology closure.

Preserve target existence checking; remove dependence on a closed semantic type list.

### Fixed expected page count

`1 + places + episodes + artifacts`.

**Classification:** ontology closure.

Useful deeper property:
- every surfaced object/view expected by the renderer should be internally reachable and deterministic.

The count formula itself should not survive generalization.

### Internal link resolution

**Classification:** strong candidate invariant for generated static views.

Broken local navigation is real friction regardless of object taxonomy.

### Deep trace must not leak into root

**Classification:** Quiet Presence campaign law.

Important for attention sovereignty in this specimen; not a universal rule for all Medium views.

### Original recovered-window hashes / exact messages

**Classification:** artifact-specific verification implementing a broader integrity principle.

Keep exact recovery evidence local to that body. General substrate should provide a way for objects to carry their own verification, not hard-code every object's domain checks into one global verifier.

## Current capability-boundary finding

The repository code has **no general explicit sandbox/capability model** for arbitrary active bodies.

The known body mechanism copies declared body files into the generated site and links directly to them.

This does not by itself prove a concrete exploit in every hosting environment, but it means:

> representation of an arbitrary HTML body and execution privileges of that HTML are not yet explicitly separated by the Medium substrate.

Therefore Phase 1 should stay passive.

Active-body pressure belongs to a later dedicated phase with browser/runtime tests.

## Provisional invariant set for the first specimen

Do not freeze a universal schema yet.

For specimen #1, require only enough structure to test these properties:

1. **stable identity** — another local object can refer to it;
2. **discoverable existence** — it is not silently erased because its family is unknown;
3. **attributed ownership/scope** — local/participant additions remain attributable;
4. **source/provenance** — exact evidence can remain reachable;
5. **body preservation** — content can be entered without a bespoke core type;
6. **unknown metadata retention** — new metadata is not silently destroyed;
7. **generic view** — unknown kind remains inspectable;
8. **known-view compatibility** — existing specialized Quiet Presence pages still work;
9. **no new executable privilege** — specimen #1 remains passive;
10. **view separation** — Polish Owner explanation and technical agent metadata can coexist without replacing source truth.

## Important design constraint

The first specimen must **not** become the implicit universal schema.

Its shape is adversarial input.

The substrate change should be justified in terms of the candidate invariants above, and Phase 5 must challenge it with a materially different second form.

## Remaining Phase 0 work

Before production behavior changes:

- define specimen #1 as a fixture outside Quiet Presence live ecology;
- define exact PASS/FAIL observations for the specimen;
- add an assertion layer that can fail when the substrate still exhibits the specific closure being targeted;
- keep the observational baseline probe unchanged enough to show historical behavior;
- decide where generic object discovery lives in the experiment without pre-designing a universal ontology.

Only then begin Phase 1 implementation.
