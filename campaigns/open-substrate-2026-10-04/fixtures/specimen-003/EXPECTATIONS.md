# Specimen #3 — semantic false-positive pressure

This is a record-only package with two fields named `object_id` that mean different things.

## Intended Medium reference

`$.relation.to.object_id = browser-field-knot-001`

This is an intentional link to an existing Medium identity.

## Unrelated foreign data

`$.foreign_payload.snapshot.object_id = external-debug-object-77`

This value belongs to an external payload schema.

It is **not** a Medium identity reference.

## Why this matters

A substrate that claims to tolerate arbitrary/unknown content cannot safely infer:

> every field called `object_id` must be a Medium relation.

Doing that silently assigns semantics to data the platform does not understand.

## Frozen current-adapter expectation

Before a reference-boundary correction, the current recursive scanner is expected to:

- discover both `object_id` fields;
- resolve the real target successfully;
- misclassify `external-debug-object-77` as another Medium target;
- reject the package as containing an unresolved Medium identity.

That expected failure is the evidence sought by this specimen.

Do not solve it by special-casing `foreign_payload`, `external-simulator`, this trace id, or this external id.
