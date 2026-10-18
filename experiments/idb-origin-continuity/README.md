# IndexedDB origin/return probe — Medium · 2026-10-18

**Isolated experimental donor. Not Jaskinia v6, not a hosting architecture, not a product verdict.**

This is a **single offline-capable HTML file** (`index.html`), with no dependencies, that writes only a random, disposable marker to IndexedDB when explicitly asked. It intentionally does not handle actual project documents, models or any personal files. No external requests occur in the JS.

## Why

Opus and Astra are currently co-designing native Jaskinia place authoring, imported material bundles and reference-by-ID. The planned material library uses IndexedDB, while standalone Jaskinia must also work as a downloaded `file://` HTML file. IndexedDB storage is origin scoped: an identical app under HTTPS and a downloaded local file does not automatically see the same library, and `file://` origin behavior is implementation dependent.

Material source content hash, place-document reference and **storage location/availability** are three separate truths. A place-document export that reopens but cannot resolve its materials is not an entirely recovered place.

## Open

- [Live HTTPS probe via HTMLPreview](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/6e47fa1484483bc4053a117d8c6f922e080d2153/experiments/idb-origin-continuity/index.html)
- [One-time sample creation in HTTPS](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/6e47fa1484483bc4053a117d8c6f922e080d2153/experiments/idb-origin-continuity/index.html#seed)
- Download `index.html` from this directory, open it as `file://`, select **Utwórz identyfikator, jeśli brak**, then close/reopen the browser or move an exact copy to a new path. Compare the displayed random token. To do an inspection-only open, choose **Odczytaj ponownie**; the probe's normal launch does not automatically populate the DB.

**Do not assume `HTMLPreview` and a locally downloaded file are the same origin.** HTMLPreview itself runs at `https://htmlpreview.github.io`: the probe writes only under that host during remote verification. Using the raw GitHub URL may download text rather than execute it.

## Independent empirical observations (Opera, 2026-10-18)

- On the live HTTPS page, IndexedDB operations completed and the probe displayed an existing disposable marker.
- A **new distinct Opera tab**, running the exact pinned source at the **same HTTPS origin** with `#read`, reported **ODZYSKANO ZAPIS** with the **same marker**. Environment: Windows desktop, Opera/Chromium build shown by the probe. This is browser UI/DOM-read evidence in the Owner-connected Opera, not an external-host database attestation.
- A **third new Opera tab** opened an exact **byte-identical HTML copy at a DIFFERENT URL PATH** within the same `htmlpreview.github.io` origin: [`identical-copy.html#read`](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/f7092211c32c22b4889d68d2c7dbdfb69f22d1e2/experiments/idb-origin-continuity/identical-copy.html#read). The independently fetched GitHub file had the **same blob SHA** as `index.html`, and the distinct-path page recovered the **same marker**. This is a real HTTP(S) same-origin path control, NOT a moved `file://` test.
- Reported `navigator.storage.persisted() === false`; this **does not mean that current data were lost**, only that durable-storage permission was not currently granted.
- **NOT tested**: complete browser exit and next-day return, a moved/renamed `file://` file, another browser profile, private/incognito mode, quota eviction, database corruption and restoration of imported GLB dependencies.

## Interpretation, not rules

- PASS same origin + same profile means data were recoverable **at that checkpoint**.
- FAIL or empty read under a different origin does *not* imply the original origin's data are gone.
- The real acceptance question in native Jaskinia is whether an **authored place plus all material bytes needed to render/re-edit it** survives the Owner's actual save/move/download workflow. That is a separate test to run on the actual v6 implementation, not this dummy marker.

Relevant external standards/background:
- https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API/Using_IndexedDB
- https://developer.mozilla.org/en-US/docs/Glossary/Origin
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS/Errors/CORSRequestNotHttp

**Owner burden:** no Owner action is required for this research. Agents can independently reproduce the public HTTPS half. The local-file half remains open until an agent with a native local Chromium runtime can test it; this environment's container/Python sessions were returning infrastructure errors when attempted.

Agent-performed-by: GPT-6 Medium, source written via Owner's GitHub connector. No modifications to Opus's or Astra's repository.
