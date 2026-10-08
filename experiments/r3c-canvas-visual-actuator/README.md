# R3C remote visual-actuator boundary probe (2026-10-08)

**Isolated, one-purpose research branch · do not merge by CI momentum · no changes to ReflexBrain**

## Pressure

An actual TinyFish browser-automation run on the **public** ReflexBrain R3C page succeeded at MARK and FORK but failed to use a graphical cyan body's canvas-only pointer affordance. It falsely said that Compare A/B does not exist (the source includes the control inside a ribbon initially hidden until divergence).

- Live R3C target: https://jozzpoly.github.io/ReflexBrain-Lab/probes/medium-d-r3c-shadow-fork.html
- Failed bounded TinyFish gesture run: https://agent.tinyfish.ai/runs/9d33ef2a-0e0f-43f3-92a7-b49403f0c3c3
- Source reference used for script inspection: `Jozzpoly/ReflexBrain-Lab`, `probes/medium-d-r3c-shadow-fork.html`, PR #6 head `7367c7ab7fd27382fc1a01b51387ed21cc258de7`. **The live Pages deployment is not independently proved byte-identical to that branch source.**

## Single bounded hypothesis

Does another available execution body (stock Chromium + Playwright mouse, orchestrated from a GitHub Actions job) actually perform one rendered-pixel-grounded canvas gesture and reveal the source-defined A/B effect without reading hidden physics state or changing ReflexBrain source?

The program:
1. opens one public webpage, watches, MARKs and waits >2s;
2. FORKs and records A/B synchronization;
3. screenshots the **rendered canvas**, searches only for the visible `#72e4de` outline (no app internal state access);
4. issues native mouse `move / down / move / up` at the pixel centroid;
5. requires **visible** `RELEASE / IMPULSE`, a real divergence tick, an accessible Compare panel and a successful return to Habitat;
6. exports `result.json` and a few screenshots; closes the browser.

A single attempt. No retries, no application-state injection, no credentials, no user browser/history access, no GitHub/ReflexBrain writes. The only intentional effect is in an **ephemeral simulated browser World**.

### Distinct outcomes

- **PASS_SCOPED_REAL_VISUAL_GESTURE:** all source-visible effects and return to Habitat observed. This is **not** proof of an autonomous agent discovering the gesture, good user experience, cross-project donor adoption, or stable reliability.
- **FAIL_OR_INCONCLUSIVE:** browser cannot reach the page, identify the graphical object, emit an effective gesture, or observe a decisive transition. Preserve exact failure evidence; do not retrofit the test to obtain PASS without explicitly changing the hypothesis.

## Architectural implications (conditional, not a decision)

If PASS: there is an **actuator exposure gap**, not a universal canvas impossibility. An agent body able to make screenshot-grounded native pointer gestures could complement one that only exposes DOM/AX element actions. This does **not** license giving a game-world actor global debugger truth.

If FAIL: determine whether the failure belongs to network, browser automation, image-to-coordinate mapping, timing, target movement, in-page interaction contract or differing deployment revision before concluding anything about federation design.

No global schema, no agent bus, no new framework. Keep this experiment isolated and discard it if the real value is not repeatable or if maintenance costs outweigh insight.
