# KOWAL — NAPIĘCIE / Noc II

Stan (19.10.2026): **nowa wersja gry wyłącznie jako lokalny HTML**, `kowal_napiecie_workpiece.html`, 11 597 bajtów, SHA256 `2561fe7b576aa461f0573e6fd99714d8933fb4406a199557c95ea3e2cc8689e5`. Nie twierdzić, że HTML istnieje w repo. Wcześniejsze lokalne warianty nie są obecnym workpiece.

Decyzja: po rzeczywistym feedbacku, że jednym palcem należy chwytać *samą linę*, porzucono sterowanie dwoma uchwytami i kapryśną symulację wielu segmentów. Nowa wersja to świadomie uproszczona **elastyczna proca**: dotyk dowolnego odcinka liny, naciąg jedną ręką, zwolnienie wypuszcza kulę; deformacja i wizualizacja trajektorii odpowiadają temu samemu modelowi rzutu. Nie jest to pełna symulacja dynamicznej liny i kontaktów kula–lina; kula jest chwilowo utrzymywana w siodełku.

Weryfikacja: lokalne Chromium + CDP-emulacja dotyku, 390×844, 360×740 i 1024×800; na wszystkich trzech viewportach ten sam celowany gest dał po jednym trafieniu bez błędów JS. Sprawdzono odrzucenie dotyku pustego tła, mały naciąg bez wystrzału, przeciwny gest bez nowego trafienia, chwyt poza środkiem (działa, lecz daje słaby rzut), przełączanie poziomów, reset i ponowne załadowanie. Zrzuty oglądane lokalnie: scena zachowuje proporcje na telefonie i desktopie. **Nie było fizycznego telefonu ani Owner-playtestu tej wersji.**

Kontrprzykład: chwycenie liny blisko kotwicy słabo porusza siodełko, więc może być mało satysfakcjonujące. Sukces pojedynczego wyreżyserowanego gestu nie dowodzi łatwego celowania ani mięsistości. Kolejny ruch: rzeczywisty Owner-playtest jednoręcznego naciągu, potem strojenie kontroli/feel, nie nowe poziomy.
