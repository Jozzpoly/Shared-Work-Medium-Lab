# Phase 1 result — generic passive object PASS, new closure found

**Evidence run:** `37221160585`  
**Head:** `f9bc183bcb884d4d42009bf76a417505ffede711`  
**Result:** PASS after one syntax-only repair

## Demonstrated

Without modifying the legacy Quiet Presence renderer/verifier:

- Quiet Presence regression still passes;
- the historical closure probes still reproduce the old closed behavior;
- Specimen #1 remains byte/source-integrity valid;
- an explicit foreign package with unknown `kind` can be rendered by a parallel generic adapter;
- behavior is not dispatched from that `kind`;
- the raw object JSON is preserved byte-for-byte;
- unknown nested metadata survives into technical/raw inspection;
- passive Markdown body is preserved and enterable;
- local source hash is verified and preserved;
- local and participant records remain separate raw JSON records;
- Owner generic view is Polish-first;
- technical/raw view is English-first;
- no scripts are introduced;
- `open_render.py` contains none of the fixture's object id, kind or relation-kind literals.

This is **mechanical/architectural evidence for one passive foreign object**, not ecological evidence and not yet proof of broad generality.

## Failure encountered

The first strict run failed before rendering because of a Python quoting syntax error in one passive-body fallback string.

The repair commit changed only that string syntax. The full pipeline then passed.

This failure is retained as implementation history; it did not falsify the substrate hypothesis.

## Important newly discovered closure

The Phase-1 adapter still makes a strong structural assumption:

> each explicit package root has exactly one `object.json`, and attached local/participant records may reference only that package object's identity.

This was useful to keep Specimen #1 bounded, but it is **not obviously compatible with the ecological behavior we actually care about**.

A future real event may look like:

- Reflex owns a local trace;
- that trace points to an object created elsewhere by Codex/Browser/Feniks;
- Reflex must not rewrite or move the target object;
- the trace may not itself deserve to become another globally shared "object".

Forcing that local trace to live inside the target object's package would blur ownership.

Forcing it to become another object may over-objectify the ecology.

Therefore the next falsifier should attack the one-object-per-package assumption rather than polishing rendering.

## Next falsifier

**Specimen #2: relation-only / local-trace package**

Requirements:

- no `object.json`;
- locally owned by a different place/scope;
- points to Specimen #1 by stable identity;
- carries unknown relation semantics;
- carries a Polish Owner explanation and technical/raw record;
- does not mutate Specimen #1 files;
- remains passive;
- source/provenance is optional but, if present, must stay exact.

Expected current result:

> the Phase-1 adapter rejects it because a package has no `object.json`.

That FAIL would be useful evidence.

The next implementation question then becomes:

> what is the smallest way to let independently owned records/traces reference existing identities without turning every trace into a new universal object type or central placement registry?

Do not answer that in advance.
