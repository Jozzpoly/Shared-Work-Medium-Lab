# OBCY / CIENIONOŚNE — pierwszy przebieg, 18.10.2026

## Wybrana czynność
Nie kontrolować postaci, lecz **tworzyć jej podłoże przez zasłanianie światła**. Przeciągany kamień rzuca cień; nad przepaścią tylko zacienione komórki stają się materialnym mostem. Wędrowiec sam wyszukuje drogę. Usunięcie cienia podczas przejścia odbiera mu podłoże.

## Próby w lokalnym Chromium (Playwright, nie Owner-playtest)
- **Kontrola bez cienia:** kamień (225,112), `bridgeMid=false`, `pathNodes=0`, postać czeka.
- **Interwencja:** przeciągnięcie kamienia do (225,300) daje `bridgeMid=true`, ruch postaci i po ok. 8 s `mode=won`.
- **Falsyfikat odwracalności:** usunięcie kamienia, gdy postać jest nad przepaścią (x≈475), daje `mode=falling`; po 1,4 s powrót do startu, bez drogi.
- **Chromium mobile emulation 390×844, CDP touch:** obrót planszy do pionu, drag z (225,112) do (225,300) powoduje `mode=walking`; brak JS page errors.
- Źródło zostało sprawdzone przez `node --check`; lokalny plik 13 833 B, SHA256 `e1991b12bb803a9d347db3f6c7e8bb37269a95d5999bdb6700cf679492ca9bce`.

## Granice
Nie wykonano testu fizycznego telefonu, Owner acceptance ani jakości zabawy. Mechanika ma tylko jeden prosty cel i może się znudzić po minucie. Browser emulation nie dowodzi odporności na mobilne gesty i specyfikę systemowej przeglądarki. Cień jest celowo fantastycznym materiałem, nie symulacją optyki/fizyki świata.

## Następna hipoteza
Czy zmiana cienia **w trakcie marszu** może być twórczą manipulacją, a nie tylko prostym przełącznikiem „most jest / nie ma”? Testować bez dodawania drugiego poziomu i sztucznego tutorialu.