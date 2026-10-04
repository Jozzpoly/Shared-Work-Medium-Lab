# Phase 2 result — independent local records can target shared identity

**Evidence run:** `37221783971`  
**Head:** `96c6f8708e04c738da701171632e813ce4741288`  
**Result:** PASS

## Demonstrated

The experimental adapter now accepts two distinct package roles without introducing a core semantic type for either specimen:

1. an **object package** contributes a stable shared identity;
2. a **record-only package** contributes independently owned records that may point at existing identities.

For Specimen #2:

- there is no `object.json`;
- the trace remains owned by Reflex;
- its raw JSON is stored outside Specimen #1's raw package;
- it points to `browser-field-knot-001`;
- the target object's exact bytes remain unchanged;
- the target Owner page derives the Reflex trace beside the object;
- the raw trace remains directly inspectable;
- the unknown relation kind survives;
- the renderer contains no Specimen-#2 id, kind, relation-kind or `reflex` literal;
- legacy Quiet Presence and Specimen #1 regressions remain green.

This is evidence that **local meaning does not need to reside in the target object's package**.

It is not yet proof that the relation mechanism is sufficiently open.

## New problem exposed by the fix

To avoid a closed relation-kind enum, the adapter currently discovers references by recursively scanning arbitrary JSON for any field named:

`object_id`

That is deliberately simple, but it is epistemically dangerous.

The adapter may now confuse:

> arbitrary foreign data that happens to contain a field called `object_id`

with:

> an intentional Medium identity reference.

This would make the substrate infer semantics from data it does not actually understand.

That conflicts with the campaign's central rule:

> **Validate invariants, not imagination.**

## Next falsifier

Create **Specimen #3** containing both:

- one genuine intended link to an existing Medium identity;
- one unrelated foreign payload that also contains an `object_id` field whose value is not a Medium identity.

Expected current behavior:

> the recursive scanner treats both as Medium references and rejects the package because the unrelated payload points to an unresolved identity.

That failure would demonstrate a false-positive semantic inference.

Do not choose the final reference protocol before the failure exists.

Possible later answers include an explicit reference envelope, sidecar, namespaced metadata, or another mechanism, but none is canonical yet.
