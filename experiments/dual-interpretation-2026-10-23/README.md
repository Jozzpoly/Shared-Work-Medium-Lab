# Medium × Jaskinia — wejście do badań (24.10.2026)

**To mapa zachowanych eksperymentów, nie plan produktu ani nowa dokumentacyjna procedura.** [Pełny raport, decyzje i źródła](RESULT.md) pozostają głównym dowodem. Repozytorium Medium ma własny [START_HERE](../../START_HERE.md); decyzje i implementacja produkcyjnej Jaskini należą do Opusa.

## Właściwy stan, bez marketingu

- **Rzeczywiście uruchomione w Operze:** niezmieniona Jaskinia v6.4.1 Opusa (HEAD `85aaaae`) w odrębnym publicznym originie, w jej normalnych oknach `Przyrząd` i `Sygnały`. ŚLAD pokazał publiczną konstrukcję z 13 zmianami i dostarczył mierzone sygnały. Powrót odtwarzał układ i link do *początkowego* wariantu, nie wszystkie późniejsze gesty. Brak Owner acceptance dla całości.
- **Działają w testach JavaScript, nie w żywej przeglądarce:** zachowywanie i rewalidacja interpretacji, nierozróżnialność dwóch materialnie różnych światów w tej samej telemetrii, punktowy odczyt komórki, brak dowodu autorstwa z liczników, strumień pytań do *tego samego* testowego runtime oraz reprodukcja URL zawierającego geometrię w metadanych Jaskini. Zatwierdzona regresja w dniu zamknięcia: **95/95** kontroli *source-level*; nie 95 browser-PASS.
- **Nieudana późniejsza próba w Operze:** [obserwator punktowy](living-jaskinia-question-window.html) nie dostał odpowiedzi, ponieważ [inicjalizator](isolated-nested-jaskinia-inspection-seed.html) wykrył istniejący `jaskinia:v3` w originie testowym i odmówił nadpisania. To **STOP, nie PASS**. Nie kasować tego stanu w celu obchodzenia blokady.
- **Niesprawdzony szkic:** [sandbox z wirtualną pamięcią](sandbox-jaskinia-load-probe.html) nie był uruchomiony w prawdziwej Operze. Jego wstrzyknięcie kodu zmienia warunki uruchomienia oryginalnego buildu. Nie nazywać go czystą Jaskinią ani bezpiecznym środowiskiem dla prywatnych assetów.

## Wybór dowodu, bez przekopywania 27 plików

| Pytanie | Najkrótszy dowód |
|---|---|
| Czy można bezstratnie zachować własną interpretację tego samego materiału? | [12-zmianowy wariant z odbiornikiem](with-lens.json), [kod rewalidacji](revalidation.cjs), [donor PR #27](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27) |
| Czy zapis wariantu można świadomie przenieść? | [świadomy eksport/import ŚLADU](slad-worldlink-first-contact.html), [test](worldlink-smoke.cjs) |
| Czy aktualne sygnały opisują cały świat i przyszłe możliwości? | [Kontrprzykład geometrii i pochodzenia](observability.cjs) |
| Czy punktowe pytanie jest lepsze niż kopiowanie całego świata? | [Pytanie o komórkę i świeżość](scoped-perception.cjs), [test prototypu](living-question-smoke.cjs) |
| Co może przejść do paczki diagnostycznej przez `#world`? | [Reproduktor na fikcyjnych danych](host-url-carriage.cjs) |
| Co naprawdę wydarzyło się w przeglądarce? | [Raport — sekcje z obserwacjami Opery i ostatnią blokadą](RESULT.md) |

**Pozostałe pliki HTML zachowujemy jako historyczne, częściowo nieudane egzemplarze**. Nie należy ich losowo otwierać ani mylić z rekomendowanymi produktami. Żaden link raw.githack/rawcdn nie jest prywatnym magazynem ani izolowanym profilem.

## Owner intent — dwa błędy, których nie wolno powtórzyć

1. Owner nie korzystał z eksportu, bo **nie chciał zachowywać losowych bazgrołów testujących narzędzie**. To NIE znaczy, że eksport jest bezużyteczny, że nie warto go rozwijać lub że należy automatycznie archiwizować wszystko. Eksport wartościowego materiału pozostaje potrzebną opcją.
2. Medium ma **wzmacniać rzeczywiste możliwości i doświadczenie Jaskini**, nie tworzyć drugiego Domu, ogólnego API, nieustannej obserwacji ani mnożyć kolejne badawcze mini-strony. Foregroundowane przez Operę karty przyciągają uwagę Ownera, więc nie otwierać ich bez naprawdę wartościowego uzasadnienia.

## Najlepszy kolejny ruch — WARUNKOWY

**Przed kolejnym testem przeglądarkowym:** uzyskać rzeczywiście niezależny, pusty, zaufany runtime z oryginalnym buildem Jaskini i możliwością odtworzenia testu *bez* nadpisywania istniejących zapisów. W tej rozmowie wykryto, że lokalne Chromium/Playwright istnieje, ale nawigację blokuje polityka środowiska, a pobieranie oryginalnego buildu z sieci do kontenera nie działa. Nie ogłaszać tego gotowym rozwiązaniem.

Dopiero kiedy środowisko jest faktycznie dostępne: uruchomić oryginalne okna Jaskini i jeden publiczny instrument, uzyskać **jedną świeżą odpowiedź** na ściśle określone pytanie ze **znanego działającego runtime**, wykonać kontrolowaną zmianę i porównać odpowiedź. Odróżniać pytania do świata od wiedzy o intencji Ownera. Bez nowej wersji kontraktu i bez automatycznego importu do Jaskini.

Jeśli izolowanego uruchomienia nie da się uzyskać, **nie rozmnażać kolejnych obejść**. Wrócić do faktycznie używanej Jaskini, jej feelu, przydatności instrumentów albo pracy nad równie konkretną potrzebą Ownera. Żaden wynik z tego folderu nie upoważnia do merge'a w Opusowy PR.

[Medium Issue #7 — istniejąca koordynacja](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/issues/7) · [Opus PR #4 — uwagi dla Jaskini](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/4#issuecomment-6377167949)
