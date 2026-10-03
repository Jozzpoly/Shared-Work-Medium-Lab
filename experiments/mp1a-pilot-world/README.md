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
