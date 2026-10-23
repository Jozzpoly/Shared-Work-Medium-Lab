# Medium — material identity and first-contact boundary (23 Oct 2026)

**Type:** isolated, reproducible research specimen. Not a Jaskinia release, Studio architecture, Owner-approved interface, working rebind algorithm, nor a request for a merge.

## Purpose and sources

This branch supports the Medium question: can an owner reinterpret existing, unprepared material without the original source tool and without silently losing their intent across source revisions?

Exact source asset: `Jozzpoly/Box3d_FunProject/assets/source/Nadwozie.gltf` from commit [959aefb78587ce60cf2b8eb03ff82797a4165142](https://github.com/Jozzpoly/Box3d_FunProject/blob/959aefb78587ce60cf2b8eb03ff82797a4165142/assets/source/Nadwozie.gltf). Git blob SHA-1: `a25cb0ef61d342ce476c9ef26a3b24188bace047`. glTF declares exporter Blockbench 5.1.4. A newer re-export has NOT been tested.

Run with Node (no dependencies):
`node experiments/nadwozie-identity-2026-10-23/probe.cjs /path/to/Nadwozie.gltf`

The script was fetched back from this branch and executed against the exact original asset via connected GitHub source in a V8 runtime. The test uses a Node-compatible mocked filesystem for the source read; no local native Node run against the original file was claimed. Its JS syntax, actual asset computations and test assertions ran successfully.

## Verified bounded result

- Original input: 3,264 vertices, 1,632 triangles, 11 joints with geometry. Rigid one-joint skin weights in this asset. At 1e-5 position tolerance, 121 separate per-joint geometric islands.
- Component triangles: 113 islands × 12 triangles, 5 × 24, 2 × 36, 1 × 84.
- Only axis-aligned box extents: 42 distinct size signatures; **116 of 121 islands** share their size signature with at least one other island.
- Relative vertex-shape signatures: 52 classes; **106 of 121 islands** belong to an ambiguous repeated-shape class (largest equivalence class: 12).
- Shape plus inherited joint **name**: 77 classes, still **72 ambiguous instances** (largest: 6). This is not a stable authored identity.
- Shape plus exact rest-position: 121 unique signatures **within this source revision only**. A synthetic uniform translation destroys all such exact keys while preserving all relative-shape signatures.
- 9 executed checks: exact source baseline, ambiguity counts, order-invariance under synthetic triangle reorder, source-translation and joint-rename negative controls.
- 3 additional fail-closed checks, using mutated source inputs: truncated embedded buffer, unsupported primitive mode and soft skin data each rejected. These are refusal tests, NOT safety assurance against arbitrary hostile input.

**Crucial distinction:** a geometric island, a Blockbench bone, a visually meaningful component, an authored mechanical part and a physics body are five different categories. Their relationship must be authored or explicitly adopted. No semantic segmentation, pivot/hinge authoring, physics, interactive Owner experience or revised real asset transfer was proven.

The benchmark deliberately uses *synthetic* reorder, translation and rename variants of the original bytes for falsification. It does NOT prove re-export/identity continuity for different actual Blockbench versions, edits, rotations, split/merge, UV/texture, nor near-symmetric parts. A position-based mapping can be a candidate locator, never automatic authority over saved author decisions.

## Parallel finding: independent delivery already partly exists

Checked current Jaskinia `v6-materialy` source, including [58-api.js](https://github.com/Jozzpoly/Jozz-Cave-Workbench/blob/85aaaaec7334428cbc85ce9379930e17b4f5d6cb/src/jaskinia/58-api.js), and [instrument contract](https://github.com/Jozzpoly/Jozz-Cave-Workbench/blob/85aaaaec7334428cbc85ce9379930e17b4f5d6cb/docs/przyrzad/KONTRAKT.md).

- `przyrzad` opens an independently hosted lab from a URL in a Jaskinia window, without adding a host-native window implementation. A minimal, optional postMessage instrument contract exists.
- `window.Jaskinia.ext.type(key, def)` registers native host window types, but the extension JavaScript needs a load/execution route inside the host. These two delivery levels must not be confused.
- Cross-origin host/instrument saves are not automatically shared, and origin/framing constraints matter; no proof of cross-tool authored material exchange.
- Read-only browser observation of the already-open live [Jaskinia](https://jozzpoly.github.io/Jozz-Cave-Workbench/) displayed **v6.4.1** while the text of PR #4 still mentioned a v6.3 public preview. The live observation is bounded to the sampled page and does not prove deployment synchrony to every client.

This **corrects** the earlier overly general claim that independent externally authored work cannot appear at all in the Jaskinia Dom without a new Jaskinia release. It can appear as an instrument; deeper native interoperability remains open.


## Cross-asset control (all six checked-in Box3D source glTFs)

The same narrow parser was run against the other five **real** `assets/source/*.gltf` files. This is a controlled sample from one exporter/project, not a claim about arbitrary glTF files.

| Asset | Islands | Shape-ambiguous instances | Shape+bone-name ambiguous | Shape+raw-position ambiguous |
|---|---:|---:|---:|---:|
| Nadwozie | 121 | 106 | 72 | 0 |
| OneSided_Steering_Suspension_Rig | 26 | 10 | 10 | 0 |
| Offroad_Big_Wheels | 51 | 33 | 31 | **2** |
| Cardan_shaft | 19 | 18 | 12 | 0 |
| One_Sided_wheel_mount | 19 | 14 | 10 | 0 |
| Asset_Dumper | 10 | 6 | 0 | 0 |
| **Total (within each model)** | **246** | **187** | **135** | **2** |

The wheel model is a stronger counterexample than Nadwozie alone: one 12-triangle box attributed to joint `Tire`, and one attributed to joint `group`, share an identical quantized raw-mesh POSITION shape and location. Bone provenance differentiates them in the current file, but a rename/regrouping might not. The inspected skin inverse bind matrices compensate their distinct joint translations in the source rest pose; do not confuse raw POSITION data with independent future world-space part identity.

This is a **static source geometry** result. It does not establish any of these models' intended components or reconstruct real authored rig topology. Each geometry input was fetched via GitHub, not a user local-file import.

## First-contact friction and safety caveat

A source check of Jaskinia `52-przyrzady.js` confirms a manually entered URL/recent-pages picker; `59-adresy.js` has no external `#przyrzad~URL` route. Thus the existing external lab bridge avoids *host code integration* but does not yet prove frictionless one-click installation, integrated asset sharing or restoration of a lab in a new origin/browser.

The iframe path is not a security boundary: instrument communication is optional, and the contract warns that storage is origin-sensitive, lab frames can share origin with Jaskinia on GitHub Pages, and the drop-in does not authenticate a framing parent. **Do not create an arbitrary external deep-link auto-loader without reviewing trust, permissions and origin isolation.** No such loader was implemented here.

## Continuation route — not a mandatory scheduler

1. Before creating another editor, inspect whether existing `Przyrząd` plus the existing JURE or JV authoring/runtime can support one genuine, reversible Owner action on a real asset. Distinguish 'reachable inside one Dom' from 'semantically interoperable'.
2. Re-evaluate interaction-spike candidates against the native JV Sandbox principle: topology freedom must improve, not merely hardpoint count. Compare geometry-first, component-first and connect-by-drag in one small context only if that could change the next decision.
3. Require an early Owner-facing, acquisition-checked experience before further substantial UX hardening. A machine pass cannot overturn the recorded Ruch Owner FAIL.
4. If a real *second source revision* is supplied/available, use it to falsify position/shape rebind; with no revision, do not claim migration solved and do not fabricate a 'real' test.
5. Preserve the wider Medium objective: environment-generated agency, lower Owner routing burden, durable cross-agent receiving and one Jaskinia Dom. Do not turn F11 semantics into the architecture of Medium.

**Boundary:** current work was confined to this separate Medium research branch. No writes to Jaskinia, JURE, JV, Opus/Astra branches or Medium main. No PR opened; branch is not a proposed product merge.
