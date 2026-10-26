# E2e · od mechanicznego dowodu do bezpośredniego authoringu (25.10.2026)


> **OWNER VERDICT — 25.10.2026, supersedes all earlier “Owner experience unconfirmed” assessments: FAIL (authoring/control).**
> Owner independently built and exported his first non-scripted mechanism (6 bodies, 4 joints), but says creating it took a very long time because the controls and connections were extremely difficult to understand and use. He reports that placing two bodies on top of one another **did not let him reliably make the hinge work at their actual contact**, forcing a workaround with joint anchor positions outside the body's visible geometry. Earlier researcher speculation that these anchors might be intentional design choices was **explicitly corrected by Owner**: they resulted from the tool's limitations. Owner strongly approves the *ambition/direction* of this experiment, while judging execution, direct control and building experience very negatively. **No mechanical/browser PASS supersedes this experiential FAIL.**
>
> **Scope correction:** the project sample belongs to Owner and is NOT copied into this public repository. The causal code hypothesis is that `hinge` mode relies on topmost single-body hit testing and two near-spatial clicks (including cancellation when both target the same body), while E2h's occlusion-cycling control lives in `move` mode. This can make coincident/contacting parts hard to address, but the exact sequence the Owner used was not instrumented; do not present the hypothesis as a reproduced root cause.
>
> **Direction:** Do not improve E2e by inertia or ask the Owner to debug it. Freeze this as a bounded technical research donor, with the real Owner FAIL attached. Future authoring work must be judged against intuitive contact-grounded assembly and meaningful construction control, not merely a working solver or a scripted browser gesture. Medium's wider purpose remains discoverable capabilities and reduced Owner orchestration in one Jaskinia home.

>
> **Source-grounded cause qualification (later review):** `hitCandidates(q)` lists bodies from the last drawn (topmost), `preferredHit(q)` returns one body, and `hinge` mode takes `pending.id` from its first click, then cancels when the next click returns `id===pending.id`; another candidate under the same pixel is not exposed as a direct second-body choice. The `cyclePick` widget was accessible through `move`, but E2h's 15/15 witness tested a hidden body joined to the **world** (its second click hits empty canvas), **not two coincident bodies hinged to each other**. Thus this PASS never covered Owner's failing workflow. Exact user actions were not recorded; do not overclaim an exhaustively reproduced causal trace.
>
> **External design contrast, not a requested feature:** Autodesk Fusion's As-Built Joint explicitly selects both already-positioned components and then determines the joint origin/type; Onshape's Mate Connectors are geometry-referenced local frames, with implicit points on faces/edges and explicit adjustment. Official sources: [Fusion As-Built Joint](https://help.autodesk.com/view/fusion360/ENU/?contextId=ASM-CREATE-AS-BUILT-JOINT), [Onshape Mates](https://cad.onshape.com/help/Content/Assembly/mates.htm), [Onshape Mate Connector](https://cad.onshape.com/help/Content/Assembly/assembly_mate_connector.htm). Reference principle only: component identity, location/attachment and allowed degrees of freedom are distinct authoring decisions. Neither app is proof of the right future Studio UX. No code or architecture promotion.



**Status: ADEQUATE jako techniczny, izolowany falsyfikator; Owner EXPERIENCE i współautorstwo NIEPOTWIERDZONE.**
Nie jest docelowym Studiem/Jozz Vehicle/Jaskinią ani odpowiedzią na pytanie o wybór solvera.

## Dlaczego ten etap

W E2b autor mógł narysować punktową prowadnicę, ale nie otrzymywał materialnego kontaktu. E2c pokazał, że sam niepołączony punkt w grafie więzów nie reaguje na napędzany, bliski element. E2d pokazał natywne przeguby i kontakt w Planck, lecz był **zaprogramowanym mechanizmem**. E2e bada węższe, mocniejsze pytanie: czy da się tworzyć **własne ciała i przeguby z gestów**, uruchamiać je jako prawdziwą fizykę i zachować edytowalny projekt bez cichego przepisania go przez runtime.

**[Otwórz warsztat E2e](e2e-material-workshop.html)** · **[portable, edytowalny przykład JSON](e2e-authored-specimen.json)** · [browser rehearsal: autor→kontakt→transfer](e2e-browser-rehearsal.html) · [empty-world falsifier](e2e-empty-world-falsifier.html).

## Faktyczne wyniki, z granicą SHAs

- **20/20 real-browser** na plikach SHA **`156f9a54fb9d9cfa76325bbef437e2ff3f85a6aa`**: interfejs syntetycznymi PointerEvent utworzył world hinge, włączył motor, w realnym Planck uzyskał **4.7255 jednostki** przemieszczenia niezwiązanego cargo; bez motoru **0**, poza torem kontaktu **0**. Stop wrócił do authored, gest przesunął bryłę, undo, world rail, staged save/import, recovery drugiego runtime przeszły. **To nie jest sprawdzian swobodnej jakości UX ani prawdziwego urządzenia.**
- **22/22 real-browser** na plikach SHA **`fc89686d3cef92baf722c14abd335556a786f950`**: od pustego świata przez UI dodano trzy ciała, joint między dwoma ciałami, osobny world hinge i motor, prowadnicę do świata, zmianę kąta/rozmiaru, podgląd przeciągania, anulowanie gestu, undo, import i czasowo uruchamianą symulację. Kontrolowany brak złącza zmienił wynik po 720 krokach o **1.83779 jednostki**. To nie jest dowód, że człowiek sam odkrywa te możliwości bez instrukcji.
- Po tych dwóch PASS poprawiono w izolowanej gałęzi: **kontekstowy panel edycji** (mniej domyślnych przycisków), atomowe fizyczne staging przed zmianą dokumentu, widoczne uchwyty motoru, ciągły drag preview i jego rollback po anulowaniu, ochronę przed zbyt sprzecznymi world joints oraz świadome umieszczanie nakładających się części.
- **Historyczny blocker, już nieaktualny:** Opera była przejściowo rozłączona po zmianie UI. Po odzyskaniu połączenia w tej samej kampanii uruchomiono oba testy ponownie na kodzie SHA **`df677590e3024b49f4ffa544ed730bce4f6c8743`**: **20/20 i 22/22 PASS**. Dodatkowo nowy E2f: **18/18 PASS** przy testowym commit SHA **`e9c9440e40af22d290e84e76edf323150e7ebb6f`** (ten sam kod E2e co `df677590`). Zewnętrzna biblioteka `planck@1.5.1` nadal pochodzi z CDN bez twardej kontroli bajtów.

## E2f · pierwsza jawna semantyka przebudowy przegubów

- **Falsifier**: [E2f: ten sam zawias, dwie interpretacje przesunięcia](e2f-joint-intent-witness.html) — **6/6** rzeczywistych browser kontroli w Operze, źródło `956b8a087be62b9c7cc69600ab5dd52f809de982`. Przesunięcie belki o 2 jednostki z nieruchomym zawiasem zmienia lokalny punkt zaczepienia z `0` na `−2`; w rzeczywistym obrocie środek belki przemieszcza się o **3.990** jednostki. Przesunięcie belki wraz z zawiasem zachowuje lokalne zaczepienie `0` i brak translacji środka. Pierwszy red test wynikał z aliasowania mutowalnego wektora Planck w teście, naprawiono *pomiar*, nie fizykę.
- **Implementacja warunkowa**: w kontekstowym panelu wybranej bryły jest jawny przełącznik `Przesuń z połączeniami`. **WYŁ.** przesuwa tylko jedną bryłę i zostawia osie w świecie; **WŁ.** przesuwa całą spójną składową brył połączonych przegubami oraz zapisane punkty zawiasów/osi jako jeden sztywny wektor translacji. Graf jest identyfikowany po identyfikatorach części, bez automatycznego przenoszenia niezwiązanych elementów. Nie zmienia rotacji ani relacji lokalnych przy zmianie rozmiaru. Zmiana źródła pozostaje pojedynczą autorską operacją do undo. Czasowy podgląd jest rollbackowany po `pointercancel`.
- **Regresja**: [E2f: translacja połączonego grafu](e2f-connected-move-test.html) — **18/18 real Opera PASS** na kodzie aplikacji `df677590e3024b49f4ffa544ed730bce4f6c8743`. Test obejmuje body↔body hinge, world hinge, trzeci niezwiązany obiekt, preserve joint local offsets, drag preview, odrzucenie drugiego wskaźnika przez aktywny gest, cancel, undo, bounds, real Planck run.
- **Otwarte i ważne**: obrót i skalowanie brył względem osi, znaczenie świata przy mieszanym grafie przegubów, komfort wybierania nakładających się części, fizyczny dotyk, realny Owner feel, czytelność trybów i cold-agent transfer pozostają nieudowodnione. Sam jawny wybór dwóch translacji nie odpowiada na pytanie o finalny builder. Nie kodować arbitralnie analogicznego zachowania dla obrotów.


## E2g · geometria, mocowanie i jawność decyzji (25.10.2026)

**Rzeczywisty [kontrprzykład geometrii](e2g-geometry-intent-falsifier.html): 12/12 PASS w Operze** (źródło/plik testu `8c2d8c05074582e08772058511899aea62302173`). Przy jednej belce i zawiasie blisko jej końca normalny obrót o 90° przemieścił lokalny punkt mocowania do `(0,-0.8)`, poza cienką belkę; obrót wokół zawiasu zachował `(0.8,0)` w materiale. Skrócenie samej belki przeniosło istniejące mocowanie poza jej obrys; skrócenie z zachowaniem proporcjonalnego położenia mocowania pozostawiło je wewnątrz bryły. Każdy wariant pozostawał prawidłowym dokumentem i uruchamiał się w rzeczywistym Planck.js. **Zewnętrzny punkt przegubu sam w sobie nie jest błędem** — może być zamierzoną konstrukcją.

**Świadomie minimalne rozwiązanie**: przy bryle połączonej *dokładnie jednym* zawiasem do świata pojawia się jawny, domyślnie wyłączony przełącznik `Zachowaj mocowanie`. Gdy WŁ., obrót 15° odbywa się wokół istniejącej osi zawiasu bez zmiany lokalnego punktu mocowania, a powiększanie i skracanie części skaluje lokalny punkt proporcjonalnie do nowych wymiarów z zachowaniem globalnej osi. Gdy WYŁ., operacje pozostają *zmianą samej geometrii*, z jawnym komunikatem o możliwym przemieszczeniu lokalnego zaczepu. Dla dwóch lub więcej przegubów tryb jest ukryty zamiast pozorować rozwiązanie całości grafu.

**[Próba interfejsu E2g](e2g-mount-intent-browser-test.html): 20/20 PASS w rzeczywistej Operze** na kodzie `5ebd5cf805e8ebe0f3321b9d01b51e8289abd5ed`, dodatkowe UI test źródło `3dddf3e8e0341f1f85d1ba8cc87376578a99f380`. Sprawdzono gest selekcji, domyślną i świadomie włączoną interpretację, rotację, skalowanie, stały world-hinge identity, zachowanie lokalnego mocowania, atomowy undo, import i odmowę dostępu do funkcji dla grafu z dwoma przegubami.

**Regresja na E2g:** dotychczasowe browser-suites [20/20](e2e-browser-rehearsal.html), [22/22](e2e-empty-world-falsifier.html), [18/18](e2f-connected-move-test.html) oraz [12/12](e2g-geometry-intent-falsifier.html) ponownie PASS na kodzie `5ebd5cf`. Jest to wciąż techniczny rehearsal na *syntetycznych* gestach, bez faktycznego Owner first-contact, telefonu, długoterminowej stabilności, rzeczywistego systemu Studio i jakości swobodnej kreatywności.

**Co nie zostało rozwiązane**: dla przegubów między dwiema fizycznymi częściami ani dla mechanizmów wieloosiowych nie istnieje jedno domyślne poprawne zachowanie obrotu/skalowania. Wciąż otwarte są ergonomia wyboru zakrytych części na realnym telefonie, live-edit na działającej symulacji i koszt uwagi Ownera. Nie eskalować tego w architekturę nowych local frames bez prób uzasadniających.

## E2h · niegubienie części pod nakładającą się geometrią

**Wcześniejszy MATERIAL FINDING:** [oryginalny falsyfikator](e2h-overlap-picking-falsifier.html) przy aplikacji E2e przed poprawką (`6f5032bee5a36a5b11ac0c6a49feb687bc0ddf55`) zwrócił częściowo ukrytą dużą belkę #1 zamiast widocznego na wierzchu koła #2, bo stary hit test wybierał najbardziej ujemną odległość od krawędzi, nie ostatnią narysowaną warstwę. Mała, fizycznie współpołożona część nie była domyślnie wybieralna.

**Rozstrzygnięcie na source `17488a1c90438f8d8be976e73ac7b8b7bbf53434`:** trafienie odpowiada kolejności rysowania (ostatnia bryła na wierzchu). Przy nakładaniu pojawia się wyłącznie kontekstowo przycisk `Wybierz inną część (1/N)`, który cyklicznie wybiera wszystkie geometrie pod wskazanym miejscem. Wybrana zakryta bryła zachowuje żółty obrys widoczny **nad** innymi bryłami. Rozwiązanie współpracuje z autorskim przesuwaniem, punktem startowym zawiasu, usuwaniem i undo, bez dodawania nowych stałych trybów. Po geometrii się zmienia wybór spod spodu jest ponownie rozstrzygany, a nie traktowany jako wieczna więź.

**[Browser E2h: 15/15 PASS](e2h-overlap-browser-test.html)** (test commit `a81a2c918a5d526b02ea2673942d98baaa174c0c`, aplikacja z `17488a1`). W realnej Operze przetestowano 2/3 w pełni nakładające się ciała, wybór wierzchniej warstwy, cykliczny dostęp do niższych, drag, joint do wybranej ukrytej części, delete/undo. Pierwotny falsyfikator po tej samej poprawce zgłasza `TARGET BEHAVIOR`. Regresja 20/20, 22/22, 18/18 i 20/20 E2g również przeszła ponownie na tym źródle.

**Zakres:** przeszły syntetyczne zdarzenia touch-typu wewnątrz prawdziwej przeglądarki. Nie stwierdzono Owner UX PASS, prawdziwego dotyku, niezależnego agentowego odzyskania sensu elementów ani lepszego projektu 3D. Wybór zakrytych elementów może wciąż wymagać zbyt wielu kliknięć, a pozycje kontrolek na telefonie nie są zweryfikowane. Nie używać punktowego PASS jako argumentu za finalnym UX.

## Co rzeczywiście jest dostępne

Wąska wersja 2D: belka lub koło, zmiana rozmiaru i obrotu, dodawanie/przesuwanie/usuwanie ciał, zawias do świata lub między wybranymi ciałami, pryzmatyczna prowadnica w dowolnym kierunku do świata, motor na zawiasie, realny Planck kontakt. `Zapisz projekt` przenosi tylko świadomie authorowaną strukturę (`medium.material-workshop.v0`); `Start` uruchamia fizykę z projektu; `Stop` jawnie wraca do projektu, więc chwila dynamiki nie staje się ukrytą intencją autora. Cofanie edycji źródłowych. Import jest walidowany i fizycznie staged przed zmianą aktywnego projektu. Nowy świat może być całkiem pusty.

Przykład JSON jest **prawdziwym edytowalnym dokumentem projektu**, bez zależności od rozmowy. Umożliwia następnemu agentowi odzyskanie mechanizmu i świadome zmiany, ale sam fakt istnienia pliku NIE potwierdza niezależnej, zimnej agentowej kontynuacji.

## Najważniejsze otwarte FAIL / ryzyka

1. **Najbardziej brakuje jakości obsługi.** Jest zbyt wiele trybów. Zawias między ciałami wymaga dwóch trafionych miejsc blisko siebie, a przy nakładających się bryłach wybór jest niejednoznaczny. Zmniejszenie liczby przycisków nie dowodzi naturalnego authoringu.
2. **Brak live-edit → test → live-edit bez resetu.** To świadoma, uczciwa granica E1 (projekt vs chwilowa poza), ale może być materialnym Owner FAIL. Należy podważać tę decyzję doświadczeniem, nie usuwać jej po cichu.
3. **Fizyka ograniczona:** brak zaawansowanych brył, 3D, prawdziwych component assets, świata reagującego na trwałe zmiany, przenośnych lokalnych ramek przegubów jako pełnego języka authoringu, grawitacja celowo zero, motor stały, brak wielopunktowej manipulacji, mało kontroli nad parametrami. Zbieżność rozwiązania fizycznego przy sprzecznych więzach nie jest szeroko zbadana.
4. **Dostarczenie:** Planck `1.5.1` przez wersjonowany CDN, NIE byte-pinned/offline; brak testu realnego telefonu, Jaskini/Operowego `Przyrządu` i bezpiecznej trwałości na różnych originach. Hostowany preview to **publiczny eksperyment, nie prywatny nośnik**; bez materiałów osobistych.
5. **Brak Owner PASS i cold-agent PASS.** Testy zostały napisane przez tego samego agenta i deterministycznie odgrywają przygotowane zadania. Dalsze automatyczne zielone metryki nie zmienią tej granicy.

## Co dalej, bez rozpędu

**Nie** rozwijać E2e automatycznie w ogólny builder ani wdrażać do Jaskini. **Najbliższe sensowne kryterium:** gdy realnie jest możliwy bezpieczny, dobrowolny first-contact, obserwować swobodne zbudowanie własnego, nieprzewidzianego mechanizmu i jego przebudowę. Jeżeli nowy język pozostaje serią niewygodnych przycisków, **FAIL** mimo realnej fizyki. W razie dalszej pracy bez Ownera lepsze są testy autorskich semantyk i cold-agent kontynuacji z portable JSON niż produkowanie coraz lepszego solver demo.

Cel wyższego rzędu: **Jaskinia jest jednym Domem; Medium ma otwierać działanie ludzi i agentów bez konkurującej rzeczywistości, bez wymuszania monolitu i bez zmieniania autonomicznych projektów w nasze laboratorium.**

Żadnego merge/PR do Jaskini, Studia, ReflexBrain, JV i Medium main, ani automatycznego hostingu. Wszystkie zmiany mieszczą się w folderze izolowanych eksperymentów gałęzi Medium.


## Video audit: measured Owner friction (26 Oct 2026; private evidence, public findings only)

**New factual evidence superseding a mere usability hypothesis:** Owner-supplied screen recording lasts **519.87 s at 30 fps (1866×874)** and accompanies a second self-authored `medium.material-workshop.v0` document. The private review package contains 22 outputs: six 30-fps excerpts, image atlases, a timestamped status-event trace and a full analytical report. **Neither the recording, the project JSON nor the review package is included in this public repository.** This is a qualified summary, not independently replayable public media.

- A video-status scan sampled the UI at 5 fps and found **20 distinct visible periods of the message `Anulowano wskazywanie`**, concentrated near joint-building (including about **01:58–02:16**); the UI subsequently reports a new hinge around **02:17**. A second cluster occurs around **03:08–03:11**. These are **status intervals, not raw click/mousedown events**. The screen alone does not reveal whether each cancellation was intentional.
- **26 distinct running-world intervals** appear in the UI state trace. This is evidence of repeated author→try→stop→author loops, not proof that every interval was enjoyable or frustrating.
- The exported document contains **19 bodies (5 pinned, 7 free discs), 8 authored joints (6 hinges, 2 rails) and 2 active motors**. The two motor-driven paths each form a closed constraint cycle with the world. After directly computing body-local anchors with the archived part dimensions/angles, **4/6 hinges (IDs 12,14,20,22) have at least one pivot outside its joined body**; hinge **20** is outside **both**. This is not by itself invalid physics; Owner independently described off-body anchors as a forced workaround for authoring coincident/contacting bodies.
- The `rail` gesture at **~02:30–02:33** gives a contrasting observable operation: a spatial direction drag with a preview, followed by `Prowadnica utworzona`. This supports **only** a limited interaction-language hypothesis, not general UX approval.
- Later, Owner added multiple unlinked balls and fixed ramps to obtain interacting physical behavior without authoring an individual script for every interaction. **Owner explicitly says the result was interesting and fun while building it required extreme effort.** Both observations matter.
- A cross-project, no-action-request donor note was posted to [Feniks Studio Tworzywo PR #2](https://github.com/Jozzpoly/Feniks-Studio/pull/2#issuecomment-6406092834). Tworzywo's authored 3D manipulations, Jaskinia Ruch's kinematics and E2e's physical contact are **partial independent capabilities**, not a proposed automatic merged architecture.

**Resulting bounded pressure, NOT a specification:** future authoring work should distinguish selecting a part, locating the attachment in meaningful geometry, declaring its allowed motion, and manipulating the living world. Scripted PASS counts do not certify this. Explicit contact geometry must not be silently converted into an automatically welded/jointed topology. Preserve the choice to *not connect* touching parts. Avoid another E2e patch cycle until a genuinely different candidate is tested through natural Owner interaction.
