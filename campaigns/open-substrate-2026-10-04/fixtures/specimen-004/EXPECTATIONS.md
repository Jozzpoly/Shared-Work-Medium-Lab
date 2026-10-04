# Specimen #4 — minimal second shared object

This fixture is deliberately unlike Specimen #1.

It contributes a shared identity with almost no platform-facing conveniences.

## Present

- stable `id`;
- unfamiliar nested metadata.

## Intentionally absent

- `kind`;
- Owner view metadata;
- agent view metadata;
- body;
- provenance;
- local records;
- participant perspectives;
- `medium.refs.json`.

## Question

Can the current generic shared-object fallback accept this package **without any renderer change**?

A useful PASS means:

1. the object is present in the generated object index;
2. the Polish Owner fallback uses the stable id as a safe title;
3. the Owner fallback does not invent semantics or fake provenance;
4. the technical/raw view exposes the exact unfamiliar metadata;
5. exact `object.json` bytes are preserved;
6. absence of `kind` is tolerated rather than synthesized into a canonical type;
7. Specimen #1 can coexist with this object in the same generated environment;
8. the renderer contains no specimen-specific literal.

A FAIL is also useful evidence if it reveals a hidden requirement that was only satisfied by Specimen #1.

Do not add fields to the fixture merely to satisfy current code.
