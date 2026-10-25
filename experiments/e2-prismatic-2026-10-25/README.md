# E2 · Prowadnica — test brakującego języka mechanizmów

**Status: source/real-Chromium PASS; Owner experience NIEPOTWIERDZONE.** Jeden niezależny donor-lab Medium, nie nowa wersja Jaskini, ŁĄCZNIKA ani przyszłego Jozz Vehicle. Nie otwierano karty w Operze i nie dotykano zapisów Ownera.

## Zobacz różnicę

[**Samodzielna strona E2**](e2-rail-witness.html) — dwa warianty tej samej korby, korbowodu i wyjścia. Parametry: kotwica (160,260), promień korby 60, długość korbowodu 180, napęd 1,05 rad/s, grawitacja i 120 Hz.

- **A · ŁĄCZNIK** — oryginalny silnik PBD z dwoma więzami długości i napędem korby. Rysunek prowadnicy **nie jest** fizycznym ograniczeniem.
- **B · Ten sam ŁĄCZNIK PBD** — identyczny stan początkowy, motor, grawitacja, kroki i 20 iteracji rozwiązywania długości; do trzeciego punktu dochodzi tylko *jeden* dodatkowy więz: **y = poziom prowadnicy**. Prawa strona nie używa Rapiera, Plancka ani osobnej zamkniętej analitycznej animacji.

[Oficjalne Rapier joints](https://rapier.rs/docs/user_guides/javascript/joints/) rozróżniają *revolute* (jeden obrót) i *prismatic* (jedno przesunięcie). Nasza **pojedyncza pozioma prowadnica** nie jest jeszcze ogólnym złączeniem dwóch sztywnych brył; to mały, specjalizowany więz dla punktu. Nie mylić z kompletną fizyką przegubów ani silnikiem brył.

## Powtórzone pomiary

| Kontrola przy 720 krokach (6 s) | Bez prowadnicy | Z prowadnicą |
|---|---:|---:|
| Maks. zejście końcówki poza poziom y=260 | **216,944** jednostki | **0** |
| Maks. niespełnienie długości prętów | praktycznie **0** | praktycznie **0** |
| Trajektoria napędzanej korby | taka sama | taka sama |
| Możliwość regulacji poziomu prowadnicy | zmienia tylko rysunek | zmienia dozwolony ruch |

Nie wolno mówić, że „fizyka A jest zła”. Więzy A są spełnione; model A nie ma pojęcia prowadnicy. B pokazuje, że dla **tej** potrzeby nie trzeba od razu wymieniać całego solvera: należy wzbogacić **język konstrukcji**.

**Granice podważające PASS:** prawa reguła jest zaprogramowana dla punktu 3, a nie dodawana przez swobodną operację edytora; UI pozwala jedynie przesuwać poziom istniejącej prowadnicy. Ponadto pełne złącze pryzmatyczne brył ma orientację, punkty/układy lokalne, siły, granice ruchu i interakcje kontaktowe, których tu nie ma. Test nie ocenia kolizji, rzeczywistych mas ani wpływu ograniczenia na wszystkie rodzaje mechanizmów. Podczas 6 s swobodna końcówka może wypaść poza kadr, więc widok jawnie pokazuje jej współrzędną; to nie jest znakomity edytor.

## Reprodukcja, zamiast wiary w obrazek

- `node e2-test-core.cjs` — **15** kontroli źródłowego modelu, deterministyczne 720 kroków oraz kontrola wspólnego napędu i dodatkowego więzu.
- `python e2-test-browser.py` — **33** kontrole na rzeczywistym headless Chromium z `set_content`: desktop 1300 px i wąski widok 390 px, klikanie, obie symulacje, test wewnętrznego steppera na pauzie, zmiana prowadnicy, przeciągnięcie swobodnego punktu i prowadnicy, brak wyjątków JS. *390 px oznacza szerokość okna, nie test fizycznego telefonu ani prawdziwego touch inputu.*

W autorskim przeglądzie badawczym wykryto błąd debug steppera: krok wykonywany z pauzy poruszał tylko A, a B pozostawał na początku. Naprawiono i dodano kontrolę wymagającą **identycznego napędu korby w obu egzemplarzach**, również dla ręcznego stepping. To ważne: screenshot sprzed poprawki mógł myląco wykazać różnicę. Aktualny Git blob samodzielnego HTML: `7b3d5e4b82412920d6d1e31c882d811ea3afad83`.

Zrzuty i lokalny egzemplarz są dostępne w przebiegu badawczym; testy w repo są przenośne i nie wymagają żadnych prywatnych danych, CDN ani produkcyjnej Jaskini. Chromium jest testem wykonania i interakcji, nie testem jakości Ownera.

## Rozstrzygnięcie i granica kampanii

**ADEQUATE** dla wąskiej hipotezy: „aktualny język punktów i długości nie wyraża wprost zależności suwaka”; „dodanie jednego ograniczenia osi radykalnie zmienia dostępny ruch bez zamiany silnika”. **NIEUDOWODNIONE:** że taki język jest wygodny dla artysty; że skalowanie go wystarczy do prawdziwych brył i części; że transfer agent↔Owner zachowuje intencję; że integracja z Jaskinią poprawia doświadczenie.

Kolejny znaczący falsifier nie powinien dodawać biblioteki joints dla samego dodania. Należy stworzyć sposób, aby **autor sam wybrał punkt i założył prowadnicę jako edytowalną relację**, a następnie skonfrontować koszt gestów i zakres konstrukcji z alternatywną reprezentacją sztywnych brył. Bez tworzenia konkurencyjnego Domu czy narzucania Rapiera innym projektom.

Kontekst: [szersza kampania E1–E4](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/experiment/medium-relational-linkage-2026-10-25/experiments/relational-linkage-2026-10-25/CAMPAIGN.md) · [stan E1](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/experiment/medium-relational-linkage-2026-10-25/experiments/relational-linkage-2026-10-25/README.md) · [Opusowy Ruch](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/4) · [ReflexBrain R8](https://github.com/Jozzpoly/ReflexBrain-Lab/pull/89).
