# NAPIĘCIE — Kowal, 2026-10-18

**Stan:** lokalny HTML sprawdzony w headless Chromium; źródło nie zostało jeszcze opublikowane w repo. Nie jest to test Ownera ani fizycznego telefonu.

Samodzielnie wybrałem zabawkę z dwoma ruchomymi uchwytami liny, której ugięcie i napięcie oddziałują z ciężką kulą. Uchwytów można używać równocześnie dwoma palcami. Celem jest przerzucenie kuli do świetlnego gniazda. Bez bibliotek i sieci.

**Lokalne bajty:** `/mnt/data/kowal_napiecie.html`, 10264 B, SHA256 `5487cc614e988a9ace0f26a98aaf8b31d94483c9177e65870d4eb20dcf784412`. Nie zakładam trwałości tej ścieżki między sesjami.

**Rzeczywiste testy:** Playwright z systemowym Chromium, `page.set_content` (bezpośrednia nawigacja file:// zablokowana), zero JS page errors. Kontrolowane przeciągnięcie lewego uchwytu z (188,330) do (220,105): kula weszła do celu, `scores=1`, `contacts=4`. Kontrpróba z przeciągnięciem lewego uchwytu w dół do (220,495): `scores=0`, kula spadła do ok. y536. W emulowanym mobilnym Chromium 390×844 dwa równoczesne touch points przesunęły oba uchwyty do (175,230) i (720,245); scena w pionie pozostaje wizualnie mała.

**Granice:** nie przeprowadzono fizycznego mobile ani Owner playtestu, trudność celu jest niekalibrowana, fizyka kontaktu przy dużych prędkościach może tunelować. Sam techniczny sukces nie dowodzi dobrego feelu.

**Następny ruch:** sprawdzić transfer dokładnych bajtów do workpiece w tej gałęzi, a następnie dalszą falsyfikację i poprawę bez mnożenia wariantów.
