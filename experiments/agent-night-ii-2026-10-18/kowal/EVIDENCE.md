# KOWAL — NAPIĘCIE / Noc II

19.10.2026. Źródłem aktualnej próby jest odzyskany lokalny `kowal_napiecie_workpiece.html`, a nie HTML z GitHuba. Nowy lokalny workpiece: 11 284 B, SHA256 `01f881c6234c962f211b8408c6851a701d27af47c12dcb2a46cc7bbcf6c7aa63`. Do czasu osobnego potwierdzenia zapisu nie twierdzić, że jest w repo.

**Wybrana zmiana:** jedno dotknięcie liny podczas lotu kuli natychmiast uzbraja następną próbę, bez celowania w przycisk. Podgląd toru i lot korzystają z *tej samej* funkcji krokowej (grawitacja, tłumienie, odbicia, ruch celu). Dodatkowo korekta ponownego chwytu podczas sprężystego powrotu liny oraz przeliczenie sceny przy zmianie wymiarów.

**Wykonane sprawdzenia:** Chromium + CDP-emulacja dotyku (nie fizyczny telefon), 390×844, 360×740, 1024×800. Gest `(-65,+130)` z centrum liny: podgląd przewidział trafienie po ok. 20–21 krokach, a symulacja faktycznie zaliczyła trafienie; gest `(-20,+120)` na telefonicznym viewporcie nie trafił. Zarejestrowano bezbłędny szybki ponowny chwyt podczas lotu. Sprawdzono też anulowanie gestu bez strzału, dotknięcie tła bez strzału, przełącznik podglądu i zmianę orientacji bez błędu JS.

**Kontrprzykład:** ten sam ruch palca `(-65,+130)` blisko kotwic (t=.05 i .95) przesuwa siodełko o ok. 34×68 zamiast 65×130 jednostek przy środku; w tych dwóch przypadkach podgląd nie przewidział trafienia. To ujawnia ograniczenie uproszczonego modelu: 'chwyć gdziekolwiek' nie znaczy 'ten sam efekt'. Preview nie dowodzi dobrego feelingu, a emulator nie zastępuje Owner-playtestu. Kolejny ruch: świadomie rozstrzygnąć, czy fizyczna nierównomierność naciągu jest zaletą czy przeszkodą; nie dodawać poziomów tylko dla liczby.
