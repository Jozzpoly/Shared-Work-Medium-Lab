# Two real Gloopipelago instrument instances — Medium research donor (2026-10-12)

This is a **single self-contained HTML file** embedding the unchanged maintained Gloopipelago browser build in *two* isolated iframe contexts. No Gloop source repository or current Jaskinia environment is edited. The host itself carries no external dependencies, login, writes, cookies or data broker.

## Exact source
- Repository: `Jozzpoly/Gloopipelago`, `main` at `bd8bfab5079bb1d1f596f9621d98ac522571b75a`.
- Build algorithm: upstream `tools/build-standalone.mjs` at the same revision: `prefix + core.trimEnd() + "\n\n" + app + tail`.
- Four exact Git blob IDs:
  - `src/browser/shell-prefix.html`: `6279a73b82438781b6e197da082f6517a7d1ccac`
  - `src/core/v1-mirror.mjs`: `6e48c92976d5339d2354add554091be6bd38483f`
  - `src/browser/app.mjs`: `1c1c2aed11d05f258dd5fc7c3bf784c7eb2b41a9`
  - `src/browser/shell-tail.html`: `6cf8732c62875b52aab986325260fe308bc0392a`
- The exact assembled UTF-8 donor source (20279 bytes) is embedded as base64 in `index.html`, decoded by the browser with TextDecoder. No content edits, module loader rewriting, source API addition or Gloop simulation changes.
- The reference Gloop repo is not an automatically acceptable design pattern for all other games. It is a maintained real simulation that had earlier Owner/browser evidence in its own project, not an Owner acceptance of this Medium host.

## Specific capability and gap
Original Gloop `src/browser/app.mjs` binds visual canvas width/height directly to `Simulation.setSize(W,H)`. Its native M3 design specifically flags viewport-induced ecology shifts. In a resizable host, merely dragging a window could change the simulation's world geometry.

Our host sets *constant inner iframe dimensions* **1210×700** (canvas **900×700** plus 310px sidebar) and scales the whole iframe **as presentation only** via CSS. Each iframe is opaque-origin sandboxed (`sandbox="allow-scripts"`; no `allow-same-origin`). Focus/hide never destroys iframe nodes; invisible simulation continues running. Its own Pause button remains the only honest pause.

What this allows: play two actual live independently evolving populations; alter one physically through its native `burst` button; rearrange observation view without altering its inner world geometry.

What it does **not** allow: deterministic matched-seed A/B, shared time or controls, remote agent command, actual inter-agent presence, persistent world save, real multiplayer, portable viewport semantics of the donor itself, or accepted Medium product UX. These must not be inferred from two iframes.

## Verification
`npm install --no-save --no-package-lock playwright@1.56.1`
`node experiments/real-gloop-world-portal-2026-10-12/browser-smoke.mjs`
The scoped CI uses **real Chromium / upstream unmodified donor code**, verifies two living canvases, isolated material food burst, stable intrinsic world sizes across host resize and focus switches, no parent DOM read of sandbox and no page errors. Any machine PASS is narrower than an Owner product verdict. No automatic deployment or PR merge.

## Adoption decision
Keep as an **isolated donor** unless a later human/agent uses it in genuine exploration or demonstrates a capability missing from native Gloop / Jaskinia. Do not automatically import it into Claude's Jaskinia or change Gloop M3.
## First real Chromium results (2026-10-12)

- Earlier transformed-iframe runs produced intermittent solid-color canvas in the **composited screenshot** while `canvas.getImageData` and computed CSS background reported transparent pixels/dark background. Do not attribute this to Gloop's biology or ignore as cosmetic. Direct iframe-transform variant is retained in branch history as a visual negative.
- An attempted `zoom` replacement changed the inner canvas from exact 900×700 to approximately 900.02×699.25, rejected because presentation must not alter world geometry.
- Fixed intrinsic iframe under an independently transformed outer mount at `67ea23b54214f6adccaa22962c27066389d552e7`: [Chromium CI #38197271086](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38197271086) **PASS**. Both canvases visibly show organisms/food in the downloaded screenshot. Fixed canvas 900×700 and iframe 1210×700 persisted across host resize/focus; both real buttons accepted physical coordinate-mapped pointer events; world A got +50 food while paused B remained unchanged; no page exceptions; host DOM access to sandboxed frame denied.
- Playwright's default inner-frame `.boundingBox()` / `.click()` initially ignored the parent's CSS scaling and misclassified visible buttons as outside viewport. The passing smoke deliberately translates genuine browser pointer coordinates via the outer iframe rectangle and in-frame element rectangle. This is a browser automation geometry gap, not proof that human click events were broken.
- External HTMLPreview and Owner human experience are **not yet proven**. CI runs the public-URL check as a separate non-gating diagnostic only; do not promote a local-file PASS to hosted-product PASS.

## Cold-start race discovery and correction (2026-10-12)

Earlier browser tests only checked CSS canvas rect (900×700), but intermittent neon fullscreen remained. Real Chromium demonstrated canvas **bitmap 1×1** on some starts, stretched by CSS to 900×700 in the color of the last painted organism. Earlier CI PASS was not visual reliability qualification.

Local repeated cold starts with the *same unchanged Gloop donor*:
- Old eager parent source injection: **3/24 FAIL** with tested software renderer.
- New injection after two host requestAnimationFrame layout commits: **0/24 FAIL** on the same environment.
- CI now asserts HTMLCanvasElement.width/height **and** CSS rect; an additional test checks 16 independent new pages (32 canvases).
- No guarantee of zero future failures or Owner acceptance is claimed. Only parent loading chronology changes; Gloop donor bytes and source repository remain untouched.

External HTMLPreview at preceding exact branch 3102c68f initialized both worlds but emitted an extra SyntaxError during HTMLPreview script appendChild; despite main workflow green, the diagnostic is **not CLEAN PASS**. Use the independent self-contained HTML as primary playable artifact; public preview remains unqualified.

## HTMLPreview parse-container separation (2026-10-12)

The public HTMLPreview diagnostic had two real Gloop worlds yet reported `SyntaxError: Failed to execute 'appendChild' on 'Node': Invalid or unexpected token`. One falsifiable possibility is that HTMLPreview reinserts and executes a large non-JavaScript `<script type="application/octet-stream">` data node. The unchanged encoded donor payload is now stored inside a hidden `<textarea>`, not a script element. A local Chromium `page.set_content` readout qualified both 900×700 real-world bitmaps and no page errors for the new container on two fresh documents. The **actual external HTMLPreview result must be rechecked** before claiming this hypothesis confirmed.
