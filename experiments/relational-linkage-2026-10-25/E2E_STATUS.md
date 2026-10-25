# E2e · od mechanicznego dowodu do bezpośredniego authoringu (25.10.2026)

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

**Co nie zostało rozwiązane**: dla przegubów między dwiema fizycznymi częściami ani dla mechanizmów wieloosiowych nie istnieje jedno domyślne poprawne zachowanie obrotu/skalowania. Wciąż otwarte są selection w złożonej nakładającej się geometrii, live-edit na działającej symulacji i koszt uwagi Ownera. Nie eskalować tego w architekturę nowych local frames bez prób uzasadniających.

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
