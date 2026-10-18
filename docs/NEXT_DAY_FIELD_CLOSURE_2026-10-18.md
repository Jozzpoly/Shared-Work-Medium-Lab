# Medium · next-day field closure · 18 October 2026

> **Historical snapshot, superseded for live routing on 18 Oct 2026.** Read [START_HERE.md](../START_HERE.md#current-repository-lifecycle--18-oct-2026-verify-live-github-before-acting) before acting. Since this note: Jaskinia public PR #4 v6/v6.1 appeared (the previous "no public v6" is outdated); Medium PR #27 **fixed** its inherited R/Space editor regression in commit [9570e852](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/commit/9570e85202d12d2040675515c973f5fd73217755); Medium PRs #5, #17, #23, #24, #25 and #28 were closed **unmerged**, Issues #1/#2 closed, and Jaskinia GPT PR #3 closed unmerged. Their preserved historical details below remain useful but **are no longer open work orders**. No other findings are implicitly resolved. This document is not a reason to ask the Owner to repeat old tests.

**Agent bootstrap, not an Owner-facing status dashboard.** Captures the end of the October 16–18 Medium/Jaskinia/Feniks cross-agent campaign. Check live sources before acting; no background run or pending deployment is implied. All source links below are public unless explicitly described as private.

## Mission regained

Medium is **not** principally a catalog, persistence library, agent message bus, PR review service or common 3D editor. Its [North Star](NORTH_STAR.md) is to increase independent human/agent **perception, action, orientation, continuity and the invention of unscripted workflows**, while reducing Owner routing, administration and forced context transfer, without extinguishing spontaneous play.

The founding Shinden discovery concerned a participant inventing a workflow from an environment's *own navigability and visible signals*. Its historical full causal trace is not independently replayed; [recheck](evidence/SHINDEN_FOUNDING_SENSOR_RECHECK_2026-10-08.md) also shows that observers produce browser-history **scent** and that different bodies see different signals. Do not confuse a researcher-planted path with independent discovery.

Owner's lived Jaskinia incident (older imperfect Lab spontaneously used on a phone for play with a niece) is **one valid experiential positive case**, not blanket approval of Jaskinia. The existing Medium human-facing World/Library had a direct **Owner FAIL**. Do not transfer that FAIL to Jaskinia or replace either verdict with machine CI.

## Verified live objects at closure

| Object | Grounded position | Important limit |
| --- | --- | --- |
| [Jaskinia PR #2](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/2) | v5 instruments, publicly visible source head `96c2a1c`; Opus resumed private work on 3D materials and shared Studio seams with Astra | Working conversation ≠ unpublished code, no public v6 branch at checkpoint |
| [Jaskinia PR #3](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/3) | Separate two-world/live A/B experiment, head `2aa5d21`, prior Chromium CI PASS | Not merged, not Owner acceptance, not the same session through two cameras |
| Feniks Studio | Public `main` at `f650d24`; Astra's real private work may exceed this snapshot | Do not equate absent public commits with absent work |
| [Medium PR #26](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/26) | Kowal's original HTML plus independently recovered editable derivative and exported dam-world; fixed editing-input reset, source and hosted-browser checks | Draft, not automatic unsaved work recovery, no Owner-play verdict |
| [Medium PR #27](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27) | Independent, easier **one-click playable authored world** stacked on #26; first-contact UX improvement | Draft **currently contains an older global keyboard handler**; see below |
| [Medium PR #28](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/28) | Small origin-scoped IndexedDB return probe, confirmed across new HTTPS tabs, URL paths and closed-tab reopen in one browser profile | **No** file:// move/rename, full-browser restart, cross-origin asset library or real Jaskinia scene roundtrip tested |

Additional existing Medium drafts #5, #17, #22–25 remain **unmerged evidence**, not accepted product layers. Private D21 corpus exists in Owner's Medium Library (last verified v10); it is deep retrieval material, **not** a required read or a main-branch document. GitHub source files need not duplicate its ~80 kB.

## Two critical open correctness findings

1. **Fix propagation across independently moving descendants.** PR #27 branched from an early PR #26 state: compare current heads `aa7a4a7` vs `9d26ca1` => **diverged**. #27's `playable-authored-breach-gpt6.html` still has global `R -> initial()` and Space interception even when the JSON textarea is active. #26 fixed this at [`a15ced2`](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/commit/a15ced2d93195e1539777876c9d46945ce2cf361). Exact source-level warning was delivered to [PR #27 author](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27#issuecomment-6245430343). **Open until recipient fixes or consciously rejects.** Do not overwrite the other agent's branch or count message delivery as resolution. If choosing to act later, prove on exact #27 playable file that editing `R`/Space preserves authored world and normal world shortcuts still work.

2. **Artifact identity ≠ dependency closure ≠ accessible storage ≠ recoverable authoring state.** Opus/Astra's proposed glTF material SHA of only root JSON may omit separate `.bin`/texture bytes; real VAW Blockbench glTF sample has such dependencies. [Source-bound objection](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/2#issuecomment-6245014655). IndexedDB is origin-scoped; identical HTML on HTTPS versus `file://` does not automatically share materials. [Bounded probe](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/2#issuecomment-6245228635). **Neither is yet a reproduced v6 product bug**; test against the real published source when available, without inventing new architecture or stopping Opus.

## Own-footprint / environmental costs

- The PR #26/27/28 automated Cloudflare Preview comments currently contain **10 + 2 + 4 failed build status entries**, respectively. These are *reported failed deployment previews*, **not proven monetary billing** or proof of the root cause. Do not generate one commit per paragraph to test the same already-qualified function; first verify whether the external preview is actually needed and who owns the failure. GitHub commit success ≠ hosting success.
- Cloudflare Dashboard build-details link for last PR #28 failure was opened read-only in Opera, but resolved to **Cloudflare sign-in**; the underlying error log is **not accessible** from this session. Keep cause and cost **UNKNOWN** rather than assigning a diagnosis or asking Owner to troubleshoot. Do not rerun deployments for curiosity.
- HTMLPreview executes at `htmlpreview.github.io`, a **shared third-party origin**. It was adequate for disposable public demo/probe bytes, **not** a trusted place to upload personal models, secrets, saves or recordings. Same-origin storage tests there say little about native `jozzpoly.github.io` or `file://`.
- Browser reads/navigation and GitHub comments can contaminate later apparent spontaneous discovery. Distinguish *participant's self-found cue* from *researcher-created cue*.
- In separate Library maintenance, Owner's storage budget was saturated earlier; archival staff later reported temporary relief, but original private recordings must not be destructively purged merely because similar branches/exports exist. That work has its own owner/context. Avoid new redundant snapshots and giant agent reports.

## Authority, roles, and the next substantial test

- **Direct later Owner judgments override historical agent-authored recommendations**, especially prior generic no-public-hosting notes. The later Owner rejection of dumping hundreds of indistinguishable Okazy builds is a **product-quality correction**, not a publication veto. Respect local author/project sovereignty.
- Opus is building Jaskinia's materials, coherent presentation and immersive walking; Astra handles authored places, editing, undo, export/import and recovery. These are their own lines. Do **not** start a competing Studio, universal catalog, main merge or global agent control plane.
- Medium's own useful next question is **differential capability**. Compare an *authentic* independent participant goal using ordinary GitHub/browser/tools versus the same goal aided by a Medium affordance. Track actual new action/aftereffect, missed consequential errors, Owner routing cost and surprise, not token counts or how many green tests are generated. Do not prompt the receiver to fake “spontaneous adoption”.
- The strongest future field event would be: **Owner or independent agent unexpectedly discovers a runnable workpiece, reshapes its world, leaves, and later genuinely returns to the same recoverable meaningful work**, potentially across clients/views. A synthetic artifact import or controlled physical comparison is useful but does not establish the full phenomenon.
- Preserve the broader [D21 aspiration](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/main/docs/NORTH_STAR.md) of **one world with multiple distinct perspectives/instruments**. Two iframe programs and a transferred JSON are not that world. No requirement to implement multiplayer now.

## Next session: a short decision, not a mandatory checklist

**Recover live truth first** (Jaskinia/Studio latest heads, Owner judgments, PR #27 repair status, Medium issue #7). Then choose at most one next action with a material open consequence. Strong candidates: verify a *real* first exported/reopened 3D authored place, or independently inspect a new workpiece's usefulness against a native-tool baseline, or qualify the PR #27 repair if unresolved and materially blocking. **Skip** more PRZESMYK solver microtests, a fourth persistence test, a new mass-branch Okazy filter, a fresh D21 rewrite and automatic Cloudflare deployment work absent genuine pressure.

**End of campaign:** No artifacts or other agent branches deleted; no Medium drafts merged; no permanent automation created. All confirmations above are scoped. This note is a restart **reference**, not a design freeze or an instruction to manufacture work.
