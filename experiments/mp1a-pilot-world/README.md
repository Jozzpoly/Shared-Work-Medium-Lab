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
