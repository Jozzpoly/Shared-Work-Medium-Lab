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