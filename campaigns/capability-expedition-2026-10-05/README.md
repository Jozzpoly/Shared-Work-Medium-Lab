# Capability expedition — 2026-10-05

Working handle: [Issue #7](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7).

This is a first exploratory loop of real collaboration through existing affordances. It is not an architecture proposal or a replacement for the rich project sources.

The question is whether a useful unfinished workpiece, its sources, and independent participant records help another participant recognize and choose a justified next action without Owner context transfer. Useful choices include verification, a different use, disagreement, or informed no-change. Surprise is optional; silence is not rejection.

## First workpiece

[Browser workpiece 01](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7#issuecomment-5985511668) chose the exchange-window fidelity edge. Browser authored that public note. Codex captured it, added optional view labels, selected a check, and left separate records. The comment is mutable; the local hashed capture fixes this copy, not the service's full edit history.

The historical exchange window remains the subject and one of the actual working surfaces. It is not relabelled as a live agent feed. The new passive workpiece is a separate lens through an existing Open Substrate adapter.

The two participants converged on these **working hypotheses**:

- An artifact can offer useful choices without assigning the consumer a task.
- A projection can enable work; it need not remain a passive viewer.
- Source preservation, wrapper identity, projection method, projected bytes, and semantic fidelity answer different questions.
- These distinctions are useful for this edge; they are not new mandatory Medium primitives.

This campaign intentionally solicits use. It does not establish spontaneous adoption or broad emergent capability.

## Sources and selected donor

- Research base: public main [d190d17](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/tree/d190d17db8edb5e6e41f8e5777fe2dc0894280d1), including the structural research program.
- Historical window and Quiet Presence renderer: public [44c5aaa](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/tree/44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487/campaigns/quiet-presence-2026-10-04).
- Passive adapter donor: [open_render.py at 1ec19fa](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/1ec19fa5064b4a731b471ad9485070770398d9a1/campaigns/open-substrate-2026-10-04/open_render.py). The copy in `apparatus/` is byte-identical; see [adapter-donor.json](evidence/adapter-donor.json).
- Public Browser workpiece: Issue #7 comment `5985511668`.

The donor was selected for this specimen because it already preserves a passive Markdown body, raw evidence, and separate participant-owned records with explicit local associations. It was not extended. Reuse here does not adopt it as project architecture.

**Known donor limitation:** its landing page and manifest still name Open Substrate / 2026-10-04. The actual specimen is this capability expedition. That inherited label is disclosed rather than silently rebranded.

## What Codex actually did

An initial comparison found different wrapper bytes. The pinned Quiet Presence method normalizes newlines while reading the wrapper and rewrites its return-door prefix. Reproducing that specific method produces the actually observed local wrapper hash.

The Browser workpiece sharpened the scope: Codex had already inspected the wrapper and four data files, then selected the complete `originalFilesSha256` set. All **seven declared originals** match both their recorded source hashes and their actually observed local preview bytes.

[window-check.json](evidence/window-check.json) binds that observation. It does not authenticate the original ChatGPT exports, establish full semantic fidelity, or turn an archival window into current activity. Wrapper byte inequality is expected here; it is not evidence that the preserved originals were damaged.

[interpretation.json](packages/codex-observation/interpretation.json) keeps the participant's before/after account separate from mechanical evidence. It is a self-report, not an independently established causal effect of Medium.

The small [source-bound probe](reproduce_window_check.py) reads ten exact public Git blobs in **one native batch process**, then optionally reads the actual local preview. It processes large source bytes in the tool and returns measured checks. Machine-processed bytes are not model tokens. Clone/fetch and previous orientation costs are excluded.

## Working surfaces and files

- [Generated optional entry](site/index.html)
- [Workpiece view](site/object-window-fidelity-edge-2026-10-05-eeaa1e8fc6.html)
- [Technical view](site/object-window-fidelity-edge-2026-10-05-eeaa1e8fc6-technical.html)
- Browser-owned text and public capture: [packages/browser-piece](packages/browser-piece)
- Codex's independent results and interpretation: [packages/codex-observation](packages/codex-observation)
- Evidence records: [evidence](evidence)
- Baseline reader: [baseline-reader.json](evidence/baseline-reader.json)

The generated files are an optional view. Raw packages, exact historical sources, and Issue #7 remain independently usable. External provenance links are not automatically fetched or verified by the passive adapter.

## Reproduce the bounded source check

Use a checkout containing public commit `44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487`; a shallow main-only clone may need that public branch fetched first.

```powershell
python -X utf8 reproduce_window_check.py --repo C:/path/to/Shared-Work-Medium-Lab
```

Without `--served-base`, this checks declared source integrity and calculates an expected wrapper only. **It makes no runtime observation.**

To bind an actual separately running Quiet Presence preview:

```powershell
python -X utf8 reproduce_window_check.py --repo C:/path/to/Shared-Work-Medium-Lab --served-base http://127.0.0.1:8792 --out evidence/new-local-observation.json
```

A new run has its own time and observation scope. It does not retroactively attest a different server or render. This apparatus reproduces one inspected pinned method, not a general projection verifier.

## Reproduce the optional Medium view

From this campaign directory:

```powershell
python -X utf8 apparatus/open_render.py --package packages/browser-piece --package packages/codex-observation --out site
python -m http.server 8793 --bind 127.0.0.1 --directory site
```

The unmodified donor replaces its output directory. Use the named campaign `site` directory, not a source/package/root directory.

[relay-verification.json](evidence/relay-verification.json) records this local specimen's raw-copy and navigation checks. Desktop 1280×900, mobile 390×844, and the no-JavaScript path were checked. These are scoped UI observations, not product-level Owner approval or a public deployment.

## Fresh-reader comparison and continuation

The first fresh reader started from public main / START_HERE and ordinary repo/GitHub/raw sources and completed its report. A second reader was given this task-sized view, the same natural reference question, free choice of route, and the same twelve-acquisition ceiling, without the baseline report. Its delegated turn ended with a usage-limit error and no completed report. See [projection-reader-attempt.json](evidence/projection-reader-attempt.json). The comparison is therefore **not evaluated**. No reduction in reading burden is established.

This is **not a controlled ablation**. Entries differ, the new workpiece adds analysis/results, orientation requirements can differ, and there is only one reader per condition. Acquisition characters, bytes, source counts, and source timing need separate interpretation. Do not infer a percentage token saving or a general Medium effect from these cases.

The next useful continuation is a consumer-selected use or critique of this exact workpiece, followed by recovering that consumer's actual output. Browser Medium can perform that real next use, but is already familiar with the workpiece and cannot replace the fresh-reader condition. Record failures and non-action as carefully as successful transforms. A broader repertoire is earned by useful independent choices, not by adding a platform or counting features.

Issue #7 is the live agent-maintained handle. No recurring/background automation is created by this artifact.
