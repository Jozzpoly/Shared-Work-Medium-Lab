# Phase 4 result — second shared-object falsifier PASS without substrate change

**Evidence run:** `37222682719`  
**Head:** `373a7d62776ed68fbcc232ec057bd63f8e9808c6`  
**Result:** PASS  
**Important:** `open_render.py` was **not changed** for Specimen #4.

## Falsifier

Specimen #4 intentionally removed almost every convenience provided by Specimen #1.

Present:

- stable `id`;
- unfamiliar nested metadata.

Absent:

- `kind`;
- Owner view metadata;
- agent view metadata;
- body;
- provenance;
- local/participant records;
- `medium.refs.json`.

## Result

The existing generic adapter accepted Specimen #4 unchanged.

The generated environment contained two shared objects:

1. the richer `browser-field-knot-001`;
2. the minimal `minimal-shared-identity-004`.

For Specimen #4:

- `kind` remained `null`;
- Owner entry remained Polish-first;
- stable identity was used as the safe fallback title;
- no source/provenance was invented;
- no body was invented;
- raw `object.json` remained byte-identical;
- unfamiliar nested metadata remained visible in technical/raw inspection;
- no specimen-specific literal was added to the renderer;
- Specimen #1 continued to coexist.

## Why this matters

This falsifier **did not expose another shared-object closure**.

That is stronger evidence than another implementation patch.

The current passive shared-object thin waist is therefore smaller than Specimen #1 initially suggested.

At the level demonstrated so far, the substrate does not require:

- a known semantic type;
- a human-authored display view;
- a body;
- provenance;
- attached local meaning.

A stable identity plus exact preserved metadata is enough for existence and generic inspection.

## Scoped conclusion

We now have evidence across two materially different shared-object shapes.

That still does **not** prove a universal object model.

But it removes the immediate justification for further shared-object refactoring.

## Stop condition reached

Do not mechanically create Specimen #5.

The representation/reference campaign has reached a useful review boundary:

- Phase 0 characterized closure;
- Phase 1 opened passive unknown shared objects;
- Phase 2 separated local records from target ownership;
- Phase 3 replaced inferred semantics with explicit identity references;
- Phase 4 failed to break the generic shared-object fallback.

Before further implementation, reassess the evidence and choose the next research pressure deliberately.

The next move may be a real Owner/browser walk, stale-reference pressure, passive body diversity, independent Codex attack, or eventually capability sandbox work — but none is automatically selected by this result.
