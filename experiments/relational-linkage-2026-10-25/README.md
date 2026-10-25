# ŁĄCZNIK — mechaniczne relacje zamiast gotowych animacji (25.10.2026)

> **Aktualne kontrpróby E2b–E2d:** [status, granice i następny falsyfikator](E2B_STATUS.md) · [własne prowadnice E2b](authorable-rails.html) · [brak kontaktu E2c](contact-ablation.html) · [przeguby + kontakt E2d (Planck)](planck-joint-contact-probe.html). Żaden wynik nie stanowi Owner PASS ani wdrożenia do Jaskini.

**Eksperyment Medium, nie Jaskinia v6.5, Ruch 2.0, nowy builder JV ani gotowy produkt.**

**[Szersza kampania i krytyczne hipotezy (25 października)](CAMPAIGN.md)** — czytaj przed następnym etapem implementacji. ŁĄCZNIK jest tylko jednym konkurencyjnym egzemplarzem, nie domyślną architekturą. Celem jest możliwie tanio sfalsyfikować jedną hipotezę: *czy tworzenie i zmienianie zależności między własnymi elementami daje odczuwalnie większą sprawczość niż parametryzowanie ruchu przygotowanych części?*

## Wejście

- [**ŁĄCZNIK — pojedynczy samowystarczalny HTML**](workbench.html). Nie wymaga zewnętrznych bibliotek ani serwera.
- [Oryginalny przyrząd Jaskini v1](https://github.com/Jozzpoly/Jozz-Cave-Workbench/blob/85aaaaec7334428cbc85ce9379930e17b4f5d6cb/docs/przyrzad/KONTRAKT.md): strona może działać samodzielnie lub jako zwykły zewnętrzny `Przyrząd` w **oryginalnej** Jaskini. Odpowiada na `hi/state?`, przesyła wyłącznie liczniki i bieżącą odchyłkę więzów jako `state/signals`. Nie przenosi geometrii ani plików do hosta.
- [Szybki podgląd publicznego eksperymentu](https://raw.githack.com/Jozzpoly/Shared-Work-Medium-Lab/8bf45fa9f438af1f155fe3d52bd4350248d3ccdf/experiments/relational-linkage-2026-10-25/workbench.html) — adres przygotowany do dobrowolnego otwarcia, **nieprzetestowany w żywej przeglądarce** w tej iteracji. Trzeci origin preview nie jest prywatnym hostingiem. Nigdy nie wprowadzać do tego egzemplarza wartościowych/prywatnych materiałów.

## Jeden konkretny test swobody

Początkowa scena ma cztery węzły, trzy sztywne pręty, dwie kotwice i jeden napęd. Użytkownik może **uruchomić**, **chwycić węzeł**, **dodać nowy punkt**, **połączyć go jednym lub kilkoma prętami**, **zmienić kotwice/napęd**, **usunąć zależność** i zobaczyć zmianę zachowania całego układu. Nie ma przygotowanej jedynej „prawidłowej” konstrukcji ani zaprogramowanej ścieżki animacji każdego ogniwa.

Natywne gesty myszy/dotyku trafiają do jednego canvasa. Zależności pozostają aktywne także podczas chwytania i na pauzie. E1 rozdziela dwa jawne, świadome eksporty: **`Zapisz projekt`** przenosi ostatnią autorską strukturę i tylko celowo edytowane elementy, natomiast **`Zapisz pozę`** przenosi aktualne położenia jako nowy punkt startowy, **bez prędkości, historii i zegara symulacji**. Oba mają envelope `medium.linkage.transfer.v1` z czytelnym `kind: design|pose` oraz wewnętrznym dokumentem geometrii `medium.linkage.v1`. Stary surowy plik `v1` można otworzyć, ale jego geneza pozostaje **nieznana**. Import pliku `pose` jest świadomą decyzją zamiany chwilowej pozy na punkt startowy. **Brak autosave jest świadomą granicą tego badania, nie oceną wartości eksportu.** Przywracanie importu sprawdza referencje, duplikaty i zakresy danych przed zamianą aktywnego modelu. Cofnięcie dotyczy autorskiej zmiany, nie każdej klatki symulacji. Aktywne przeciąganie należy tylko do jednego `pointerId`; drugi palec nie może go zakończyć.

**Istotna kontrpróba E1:** podczas symulacji samo dodanie punktu wcześniej niepostrzeżenie zmieniało również zapisywane pozycje wszystkich ruchomych węzłów. Teraz authoring aktualizuje tylko wymienione w operacji punkty/relacje; ciągły ruch pozostałych nie zapisuje się do projektu. **Nie jest to rozwiązanie absolutne:** połączenie prętem w bieżącej pozie może dać inną długość niż odległość w pierwotnej pozie projektu. W reproduktorze: 317,63 vs 194,16 jednostek, odchyłka po odtworzeniu projektu ~123,47. Program zgłasza to przy eksporcie projektu zamiast udawać tożsamość projektu i widoku. Dopiero `Zapisz pozę` zachowuje aktualną konfigurację jako nowy projekt startowy. To otwarty problem UX i semantyki, a nie błędna fizyka sama w sobie.

## Co jest prawdziwe, a co uproszczone

Model: punkty poddane grawitacji, więzy stałej długości rozwiązane iteracyjnym *position-based dynamics* (20 iteracji na krok, 120 Hz), kotwice w świecie i **jeden kinematyczny napęd ramienia**. To nie silnik brył sztywnych; nie symuluje masy prętów, momentów bezwładności, kolizji pręt–pręt, tarcia ani realistycznego momentu napędu. Silnie nadmiernie związane układy mogą się odkształcić: pręty o dużej odchyłce czerwienieją, a `odchylka` jest pomiarem, nie zapewnieniem poprawności. Negatywna kontrola przesuwa jedną z dwóch stałych kotwic tak, że ich połączenie ma 580 zamiast 260 jednostek — instrument zgłasza **320 jednostek niespełnionego więzu**, zamiast udawać poprawną fizykę. To wystarcza do ograniczonego testu „tworzenie relacji ≠ ustawianie animacji”, ale **nie wystarcza do oceny finalnej mechaniki Jozz Vehicle**.

**Ważny donor i antywzorzec:**
- Jaskinia **Ruch** v6.4.1: technicznie poprawiony, lecz negatywny osąd dotyczy samej swobody tworzenia mechanizmów, nie liczby testów.
- [ReflexBrain R8 PR #89](https://github.com/Jozzpoly/ReflexBrain-Lab/pull/89): prawdziwe ciała Rapier, kotwiczenie, manipulacja, ale odmienne pytanie eksperymentalne; nie kopiowano jego kodu ani nie zmieniano tego projektu.
- [ŚLAD/PRZESMYK](../dual-interpretation-2026-10-23/README.md): doświadczenie spontanicznego użycia wewnątrz Jaskini oraz wartość jawnego, świadomego eksportu, nie gotowy model mechaniki.

## Weryfikacja i poziomy dowodu

```
node test.cjs
node test-ui.cjs
```

**41/41** testów źródłowych na odczytanym kodzie repo: 25 model/dane + 16 syntetycznych zdarzeń UI. **19/19** dalszych kontroli w **prawdziwym headless Chromium 144** na bajtach HTML o *tym samym Git blob SHA co w repo*: prawdziwy canvas, klikanie, RAF, przeglądarkowe pobieranie dwóch różnych plików, ich import, odmowa sfałszowanego pliku, kontynuacja w drugim świeżym oknie i **dotyk emulowany przez Chromium** przy 390 px. [Przenośny reproduktor](test-browser.py) używa `page.set_content` — administrator blokuje nawigację do `file:` i `data:`, ale nie wczytanie treści do pustej kontrolowanej strony. To **NIE** jest test pod rzeczywistym adresem URL, osadzeniem w Operze/Jaskini, fizycznym urządzeniem ani Owner acceptance. Obejrzenie zrzutów wykazało też **problem mobilnego UX**: zachowany świat 1000×650 zajmuje tylko środkowy, poziomy pas wysokiego telefonu, pozostawiając za dużo pustego miejsca. Zielone testy dotyku tego nie unieważniają. Nie mylić 41 testów JS i 19 Chromium z 60 testami Ownera.


**Dodatkowa negatywna próba w prawdziwym Chromium:** po połączeniu dwóch punktów podczas ruchu bieżący pręt miał długość **285,82**, a jego końcówki w zamrożonym projekcie były oddalone o **194,16** — różnica **91,65**. W świeżej karcie po imporcie rzeczywiście pojawił się **czerwony pręt** z odchyłką 91,65. Poprawiono także komunikat przy **imporcie**, aby odbiorca od razu zobaczył, że projekt zawiera napięte więzy; test w prawdziwym Chromium przeszedł. Takiego wyniku nie wolno maskować przez zmianę kolorów ani nazywać zachowaniem tej samej pozy.

**Test rozstrzygający, jeśli będzie bezpieczna okazja:** bez instruktażu i bez otwierania przez agenta nowej karty bez wyraźnej wartości, czy w realnym przyrządzie Owner potrafi w jednej krótkiej spontanicznej sesji przejść od obserwacji przykładu do **własnego, działającego układu relacji**? Czy przewidywanie i naprawianie jego zachowania jest czytelne? Czy wariant bez napędu nadal daje interesującą manipulację? Jeżeli narzędzie pozostaje zestawem niezrozumiałych kontrolek albo zachowanie jest zbyt sztuczne, zamknąć to jako *FAIL* i zachować dowód. Nie tworzyć automatycznie kolejnego generica.

## Granice repozytorium

Gałąź `experiment/medium-relational-linkage-2026-10-25` powstała od `main` Medium i zawiera wyłącznie folder tego eksperymentu. Żadnych zmian w `main`, Jaskini Opusa, ReflexBrain, assetach użytkownika, publikacji Pages ani wdrożeniu. Nie zmieniać własności projektów i nie sugerować merge na podstawie samej sprawności solvera.
