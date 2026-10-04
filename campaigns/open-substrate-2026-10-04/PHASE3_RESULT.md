# Phase 3 result — explicit reference boundary PASS

**Evidence run:** `37222293851`  
**Head:** `7a67e150d9b633aa215ef50a87b0b3d1fef95d93`  
**Result:** PASS

## What changed

The Open Substrate adapter no longer infers Medium references by recursively scanning arbitrary JSON for fields named `object_id`.

An explicit package-local sidecar, `medium.refs.json`, now declares only the records that intentionally associate with a stable Medium identity.

Raw records remain byte-preserved and may contain arbitrary foreign schemas.

## Positive evidence

Specimen #3 contains:

- one intentional Medium target: `browser-field-knot-001`;
- one unrelated foreign payload id: `external-debug-object-77`.

The final generated reference manifest contains exactly one reference:

`trace.json -> browser-field-knot-001`

The foreign id remains present in exact raw content but is absent from Medium references.

This is the desired separation:

> **raw content may say anything; the substrate only validates Medium semantics that were explicitly declared to it.**

The Owner view still derives the Combat-local interpretation beside the target, and the raw trace + sidecar remain separately inspectable.

## Negative boundary evidence

The same run also proves that explicitness did not mean abandoning integrity checks.

The adapter rejects:

1. a sidecar targeting an unknown identity;
2. a sidecar record path escaping the package boundary;
3. a sidecar pointing to a missing local record.

Each negative case failed at the intended boundary.

## Regression evidence

The same pipeline preserved:

- legacy Quiet Presence PASS;
- historical closed-behavior probes;
- Specimen #1 generic passive object PASS;
- Specimen #2 independent record-package PASS;
- source/provenance and raw-byte integrity checks.

## Scoped conclusion

Phase 3 supports a stronger candidate thin-waist rule:

> **Medium identity relationships should be explicit substrate metadata, while arbitrary participant/tool/source content remains opaque unless it explicitly opts into Medium semantics.**

This is still not a final reference protocol.

The current sidecar format is an experimental carrier for that property.

## What is not demonstrated

Phase 3 does not establish:

- repository-wide discovery;
- semantic search;
- active-body capability safety;
- a complete ownership model;
- how stale declarations should be handled;
- whether every local record must point to a shared object;
- whether `object.json` is the right long-term shared-object envelope;
- ecological adoption.

## Next frontier

Do **not** immediately add fields to the sidecar.

The strongest remaining representation question is now broader:

> have we actually demonstrated a generic shared-object fallback, or merely one object shape plus increasingly flexible records around it?

Only Specimen #1 has exercised an unknown shared object.

The next adversarial test should therefore use a **materially different second shared object**, with fewer of Specimen #1's conveniences:

- no `kind` requirement if possible;
- no Owner-specific view;
- no body;
- no attached participant/local records;
- a different provenance shape (preferably external or absent);
- unfamiliar metadata.

The generic fallback should still provide a minimal inspectable Owner entry and exact technical/raw identity without adding a type-specific branch.

This tests the shared-object thin waist itself before moving to active execution or richer discovery.
