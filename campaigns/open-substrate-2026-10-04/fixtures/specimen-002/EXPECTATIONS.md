# Specimen #2 — relation-only local trace

This fixture is intentionally structurally different from Specimen #1.

It contains **no `object.json`**.

## What it represents

A locally owned trace in Reflex points to an existing identity created elsewhere:

`browser-field-knot-001`

The trace does not own, copy, move or rewrite that target.

Its declared semantic relation is intentionally unknown to the adapter:

`borrowed-as-debugging-lens`

## Why this matters

A real ecological event may produce:

- a local project interpretation of someone else's thing;
- a negative or positive trail;
- a reason to return;
- a donor-use note;
- a pointer to another participant's work.

Forcing every such trace into the target object's package blurs ownership.

Forcing every trace to become another shared global object may over-objectify the medium.

This fixture tests whether independently owned records can exist *between* identities/scopes.

## Frozen current-adapter expectation

Before Phase 2 substrate changes:

- Specimen #1 still renders successfully by itself;
- passing Specimen #2 as another explicit package root fails because it has no `object.json`;
- the error is specifically a package-shape closure, not a source mutation or target-identity failure;
- Specimen #1 fixture bytes remain unchanged.

This expected failure is evidence, not an accidental red CI.

## Future acceptance target

Do not freeze the implementation yet.

A later mechanism must at minimum allow the trace to be preserved, attributed to Reflex, and associated with the existing target identity without:

- moving or editing Specimen #1;
- inventing a `reflex/borrowed-lens` core type;
- inventing a core branch for `borrowed-as-debugging-lens`;
- requiring the trace to masquerade as another shared object;
- centralizing all local meanings into the target object.

Owner-facing explanation should remain Polish-first; technical/raw inspection may remain English-first.
