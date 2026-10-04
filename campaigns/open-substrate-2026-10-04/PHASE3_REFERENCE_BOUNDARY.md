# Phase 3 design decision — explicit reference boundary

**Evidence:** Specimen #3, run `37221964353`  
**Status:** experimental design choice for the next implementation slice

## Finding

Recursive discovery of every field named `object_id` is too aggressive.

It assigned Medium semantics to an unrelated external payload and rejected otherwise valid content.

This is a direct violation of the campaign principle:

> **Validate invariants, not imagination.**

## Rejected responses

### Whitelist JSON paths

For example:

- `$.to.object_id`
- `$.about.object_id`
- `$.relation.to.object_id`

Rejected because this merely replaces a closed type enum with a closed semantic-path enum.

### Guess from nearby keys

For example treating `relation` as meaningful but `foreign_payload` as opaque.

Rejected because the substrate would still infer semantics from names it does not own.

### Ignore unresolved inferred ids

Rejected because it would make broken intended references indistinguishable from unrelated payload fields.

## Candidate: package-local explicit reference sidecar

For the next experiment, a package may contain:

`medium.refs.json`

Minimal shape:

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

The sidecar does **not** define:

- relation semantics;
- participant meaning;
- importance;
- direction beyond record → target identity;
- ranking;
- display behavior.

Those remain in raw records/views.

The sidecar only declares an intentional Medium association that the substrate is allowed to validate.

## Why sidecar instead of embedded metadata

A sidecar lets arbitrary or imported content remain byte-identical.

That matters because future agents may want to preserve:

- tool logs;
- external JSON;
- source snapshots;
- foreign schemas;
- exact recovered records.

The Medium wrapper can declare relationships without editing those bodies.

Native future records may eventually choose an embedded namespaced envelope, but this campaign does not need to decide that now.

## Risks

This candidate creates a new convention and can itself become over-centralized if expanded carelessly.

Specific risks to test:

- sidecar points to a nonexistent record;
- sidecar points outside package boundary;
- sidecar target identity does not exist;
- duplicate/conflicting declarations;
- stale sidecar after record changes;
- sidecar starts accumulating semantic fields and becomes a hidden ontology.

Therefore Phase 3 must keep it deliberately narrow.

## Migration of current fixtures

Do **not** alter the existing raw records.

Add only `medium.refs.json` sidecars:

- Specimen #1 declares its relation and participant perspective as pointing to its object;
- Specimen #2 declares its Reflex trace as pointing to Specimen #1;
- Specimen #3 declares only its intended Medium target.

The unrelated `foreign_payload.snapshot.object_id` remains untouched and must stay visible in raw data while no longer being interpreted as a Medium link.

## Acceptance target

After the change:

- all three specimen raw records remain byte-identical;
- the recursive `object_id` scanner is removed from active routing;
- only explicit sidecar links participate in identity resolution;
- Specimen #3 renders successfully;
- `external-debug-object-77` remains present in raw content but absent from Medium reference manifests;
- missing sidecar targets still fail;
- legacy Quiet Presence remains green;
- Specimen #1 and #2 guarantees remain green.

This is still a controlled apparatus result, not a final Medium protocol.
