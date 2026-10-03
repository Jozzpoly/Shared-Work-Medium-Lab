# MP-1A generated pilot world

This branch validates the **world-generator seam**, not an LLM capability hypothesis.

A deterministic public pilot seed produces:

- one canonical project world;
- evaluator-only motif ledger;
- P0 visual-equivalent non-semantic treatment;
- P1 visual-equivalent semantic treatment;
- manifest with content hashes.

GitHub Actions then:

1. generates the same world twice and requires byte-identical output;
2. validates resource IDs and relations;
3. scans for evaluator motif-label leakage;
4. opens P0/P1 through BrowserGym;
5. requires normalized visible text parity;
6. requires raw link label/target parity;
7. requires near-exact screenshot parity;
8. requires intended AXTree semantic divergence;
9. uploads evidence artifacts.

## Scope

This is a **public pilot**. The seed and evaluator ledger are intentionally not secret.

No measured/confirmatory run may reuse this pilot world.

No LLM subject is invoked here.

The next gate after a clean generator PASS is a small pilot subject run whose only purpose is to validate the scoring/logging seam. Confirmatory hidden-seed worlds remain blocked until that works.


## Live generator result — 2026-10-03

GitHub Actions run `37146692319` completed successfully.

Generated world:

- **25 resources**;
- deterministic public seed commitment `f4e1d79e6d513b709cd0c914dfb4ae656d4a4012841d2cfa85aed81fed1e4f72`;
- two independent generation passes produced byte-identical outputs;
- all resource IDs unique;
- all declared relation targets resolve;
- no evaluator motif labels leaked into P0/P1.

P0/P1 parity:

| Check | Result |
| --- | --- |
| normalized visible text | **identical** |
| raw link labels/targets | **identical** |
| screenshot mismatch | **0.0%** |
| mean pixel delta | **0.0** |
| P0 AXTree chars | 7211 |
| P1 AXTree chars | 11718 |
| P0 heading/article/listitem | 0 / 0 / 0 |
| P1 heading/article/listitem | 29 / 25 / 25 |
| link count in both | 41 |

Scoped judgement:

> **PASS — one deterministic canonical project world can mechanically compile into pixel-identical P0/P1 treatments with materially different machine-legible semantic topology.**

Still unproven:

- no model subject has been exposed to either treatment;
- no correctness/search-cost/capability effect has been measured;
- no scoring pipeline has yet been exercised on a real or synthetic action trace.

## Next gate

Validate the evaluator/logging contract using deterministic synthetic traces with known outcomes.

This prevents the first real model run from simultaneously testing:
- the medium;
- the subject adapter;
- the logging layer;
- and the evaluator.

A real isolated LLM subject remains a later explicit step and must not require silently using the Owner's API credentials.


## Synthetic scoring seam — PASS

GitHub Actions run `37146844616` exercised the evaluator on deterministic synthetic behavioral traces.

Verified distinctions:

- T1 correct stale-dependency judgement → **exact task success**;
- same T1 target/source with an unjustified `proven_false` judgement → **scope failure**;
- T2 common-cause case → correct cause + three independent supporting resources + inference remains scoped as plausible;
- T3 serial inspection → correct exceptions but **systematic_workflow = 0**, 4800 observation bytes, 8 resource reads;
- T3 generic batch strategy → same correct exceptions but **systematic_workflow = 1**, 1900 observation bytes, 2 exact-source reads.

Scoped judgement:

> **PASS — the current evaluator can keep correctness, epistemic scope, acquisition cost, and systematic-workflow behavior on separate axes.**

This is still synthetic validation. It does not establish that a real LLM will produce traces that are always unambiguous to score.

## Current boundary

The next materially new evidence requires a **real isolated LLM subject** driving the BrowserGym treatment.

That step needs an explicit subject runtime/model connection.

This branch deliberately contains no API key lookup, no Owner credential access, and no hidden dependency on the user's normal ChatGPT account.

Before a real subject run, the experiment must choose a credentialed/stateless runner explicitly and record that choice as part of the contamination boundary.


## Navigable acquisition + interaction-loop gate — PASS

GitHub Actions run `37148886330` validated the corrected multi-page pilot and the BrowserGym interaction loop.

### Navigable world

Each treatment now contains **29 pages**:

- 1 resource index;
- 25 resource evidence pages;
- 3 collection pages.

The acquisition boundary is explicit:

- full resource bodies do **not** appear on the index;
- the release collection lists candidate resources but does **not** expose smoke/contract/Owner-visible check results;
- a subject must navigate to evidence pages to acquire those facts.

Across all 29 corresponding P0/P1 pages:

- visible text equality: **PASS**;
- link equality: **PASS**;
- overall screenshot mismatch: **0.0%**;
- semantic enrichment present on **29/29** pages;
- evaluator labels: no leakage;
- resource/collection references: fully resolved.

### Scripted BrowserGym interaction loop

A deterministic plumbing subject was then run through both treatments using only:

- flattened AXTree observations;
- BrowserGym high-level `click(...)` and `go_back()` actions.

Both treatments followed the same logical route:

```text
index
→ Release records
→ Fir release candidate
→ back to Release records
→ Harbor release candidate
→ final
```

Observed:

- 4 BrowserGym actions per treatment;
- zero action errors;
- complete per-step URL / AXTree hash / observation-byte trace;
- P0 total AXTree payload on this fixed route: **7632 bytes**;
- P1 total AXTree payload on this fixed route: **12308 bytes**.

The byte difference is a **treatment mechanic**, not model-performance evidence. P1 carries richer semantic topology and therefore may expose a larger serialized AXTree. Real evaluation must keep acquisition cost separate from correctness and action efficiency.

Scoped judgement:

> **PASS — the apparatus now measures actual information acquisition and real browser actions rather than pretending one all-visible page is a browsing task.**

## Remaining boundary before a real model

The next step is to isolate the subject interface itself.

The model process must receive only:

- the frozen task;
- the current observation packet;
- the generic action contract;
- prior interaction history required by the chosen subject protocol.

It must not receive:

- evaluator ground truth;
- motif labels;
- hidden seeds;
- scoring implementation;
- the experiment-design repository as context.

A provider/model adapter belongs outside the world/evaluator core.
