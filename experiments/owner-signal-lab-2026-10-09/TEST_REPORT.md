# Owner Signal Lab R1 — bounded verification

Date: 2026-10-09

## Owner smoke evidence

The Owner performed a fast real-browser smoke test of R0 with two arbitrary videos and exported both structured JSON and Markdown handoff. That established the basic capture/export loop as usable enough to justify one hardening pass. The private smoke artifacts are intentionally not included in this public archive.

## Automated/runtime checks performed during R1 hardening

PASS:

- inline JavaScript syntax check with Node;
- exact R0 session migration into R1;
- legacy A/B source-name recovery;
- millisecond regression: `3.082` remains `00:03.082`;
- edit existing signal;
- WORKING ↔ PRIORITY/STAGED toggle;
- untrusted annotation text rendered as text rather than executable markup;
- GENERAL signals export without fake timestamps;
- invalid/unsupported import does not destroy current session;
- R1 JSON export/import round-trip;
- New Session clears in-memory state even when localStorage is unavailable;
- real-browser decoding of two local MP4 files through file inputs;
- source-specific “Now” uses B time when B is selected;
- manual A/B alignment stores an offset and BOTH annotations export paired A/B ranges;
- handoff includes a source-availability caveat rather than pretending an agent can inspect unavailable footage.

## Not established

- frame-accurate stepping;
- semantic/content-based A/B alignment;
- cross-browser localStorage behaviour under every privacy policy;
- long-session performance at very large annotation counts;
- product value beyond the Owner's initial smoke test;
- superiority over ordinary text feedback where direct temporal pointing adds no value.

These remain explicit limits rather than implied PASSes.
