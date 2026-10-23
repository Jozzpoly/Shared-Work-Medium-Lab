# Medium: one source geometry, two meanings — counterexample (23 Oct 2026)

**Research workpiece, agent-authored, NOT Owner experience or Studio design.** Isolated branch: no main/Opus/Astra/JURE code edits or deployment.

## Source of truth

Two exact, original existing Medium PR #27 HTML instruments, at `419b9c9dbf49301ed9fb9bf65e39de33d35f17bb`:

- [PRZESMYK — playable hydraulic topology](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/419b9c9dbf49301ed9fb9bf65e39de33d35f17bb/experiments/received-workpieces/przesmyk-kowal-2026-10-18/playable-authored-breach-gpt6.html), Git blob SHA-1 `46f1e640d4e4f5643d7f830f795d040a64ed1f15`.
- [ŚLAD — alternate sound/pathfinding interpretation and Jaskinia instrument](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/419b9c9dbf49301ed9fb9bf65e39de33d35f17bb/experiments/received-workpieces/przesmyk-kowal-2026-10-18/second-life-signal-instrument-gpt6.html), Git blob SHA-1 `e846b8c9d4c96a0d60973b22ca3693ab50a60fb9`.

The published donor files were **not modified**. The [test runner](roundtrip.cjs) extracts and executes their original JavaScript in a minimal mock DOM (no browser rendering, no iframe or user gestures). Only the hydraulic solver's simulation function is temporarily exposed **in memory** for synchronized fixed-step qualification.

Run from a local checkout of the two exact donor HTML files:

`node roundtrip.cjs /path/to/playable-authored-breach-gpt6.html /path/to/second-life-signal-instrument-gpt6.html`

Optional third argument is a file prefix to emit both JSONs again. No npm dependencies.

## Authored workpiece and observation

1. Start with the donor's existing 11-cell dam breach, schema `medium.przesmyk.variant.v1`.
2. An independent test agent opens one additional stone at grid index **4872** (x=56, y=43), giving **12 changes**. It assigns the ŚLAD receiver at **(82,40)**, previously unoccupied, using that donor's own supported optional metadata.
3. ŚLAD imports and exports [with-lens.json](with-lens.json): same geometry, explicit authored receiver; its route solver reports **reach=true**, travel cost **79.5269088745** in source grid units.
4. PRZESMYK imports that JSON through its actual `importCapsule`, exports [through-legacy.json](through-legacy.json): **12/12 topology edits, source, drain and feeding remain equal**, but its export **does not include the mediumSignal receiver**.
5. A fresh independent ŚLAD runtime imports the second file. With no receiver in the document, it uses **(62,52)**, not the author's earlier **(82,40)**. It has not preserved the complete interpretation.
6. Negative control: an invalid receiver at (0,0) is rejected by ŚLAD's validation **before applying any change**. The previous world is retained.
7. Stronger red-team: an independent hydraulic edit fills receiver cell **4562** (x=82, y=40), while a hypothetical unaware editor blindly forwards the old opaque receiver metadata. ŚLAD correctly **rejects** that stale interpretation without changing its world. Therefore merely echoing unknown fields can prevent data loss but cannot guarantee their continued validity.
8. With the unchanged PRZESMYK solver at exactly 240 direct test-only steps: original 11-cell version gives right-side water mass **69.66**, 12-cell variant **69.68** (small effect, NOT evidence of a useful new fluid-mechanics interaction).

## Interpretation and boundaries

- **PASS:** two independent donor runtimes materially receive/operate on the same authored topology. This is a real data-semantic integration result without new simulation code or a new editor.
- **FAIL of full interpretation continuity:** a legacy reader intentionally ignores an optional extension, then emits a fresh object without it. This is a compatibility boundary, **not proof of a software bug** or a requirement that all legacy tools must understand future semantics.
- The initial new cell was **agent-authored**, not Owner-authored; no Owner PASS.
- A metadata-preserving envelope must also maintain an explicit validity/uncertainty boundary; passing an opaque extension through after material alteration does not certify its semantics.
- No actual browser file dialogs, WebGL, Jaskinia embedding, cross-origin persistence or user-visible interaction tested. A local Chromium network smoke was blocked by environment policy; don't claim otherwise.
- Different source-derived behaviour in two consumers is useful only if the author understands what survived; no "automatic always-lossless interpretation" claim.

This directly tests the larger F9/F10 Medium hypothesis of **multiple independent interpretations of one source**: a tool may operate correctly on a shared geometry and still silently discard meaning introduced by another instrument.

## Next useful decision

Before designing plugins or an overarching universal format, distinguish workpiece **core data**, **optional tool-specific interpretation**, and **forward-preserved but unrecognized information**. The smallest future test is to compare ordinary forward preservation versus deliberate explicit conversion with a real recipient, without secretly replacing the author's decision. Do not promote a new schema until a real task requires it.

For a later Jaskinia first-contact test, the existing ŚLAD variant is the less-privileged candidate (file input + Blob download, optional status handshake). JURE relies on File System Access pickers that Chromium disallows in a cross-origin iframe. Both observations are separately documented in [the adjacent field checkpoint](../nadwozie-identity-2026-10-23/RESULT.md). A standalone source/import success does not imply a full Jaskinia product PASS.
