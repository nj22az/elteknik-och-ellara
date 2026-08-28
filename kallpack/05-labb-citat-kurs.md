# Sex labbcitat för Kurs (unblock)

Datum: 2026-08-28. Primärkällor. Parafras, inte avskrift. Funktionskrav vs vägledning markerat.

## Källnivå (viktigt för lektionerna)

- **Skall-krav (funktionsbaserad föreskrift):** TSFS 2017:26 5 kap. 1–7 §§. Konsoliderad text: https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf (fil även /workspace/kallpack/TSFS_2017_26k.pdf).
- **Allmänna råd** i samma kapitel = bör, inte skall.
- **Kompletterande upplysningar** = TS vägledning för verifiering och "Så här görs kontroll". Inte föreskriftstext. Copyright: parafrasera, klistra inte in sidans tabeller/långa stycken i bok/kurs. https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/
- **Krav-sidan** (kompetens, intyg, 1 MΩ, landströmpekare): https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/
- **IP-tabell:** https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/ (TS citerar IEC 60529; IEC-text får inte kopieras in i boken).

## 1) Isolation / megger

- Funktionskrav: 5 kap. 5 § (system ska minimera kortslutning, brand, elchock m.m.). Allmänna råd: ojordade kretsar >50 V bör ha jordfelsövervakning.
- Vägledning "Isolationsprov": jordfelsövervakning och meggning. Läckströmmar/vagabonderande strömmar → korrosion på skrov/propeller/axel.
- Siffra **lägst 1 MΩ** står på krav-sidan, inte som siffra i 5 § skall-texten. Flagga det i lektionen.
- Kontroll: har fartyget isolationsinstrument → daglig avläsning. Saknas instrument → fackman megger isolerade delar och upprättar protokoll. Underhållsrutin t.ex. vart 6:e år eller vid problem.
- Lab: megger enligt TS kontrollpunkt + protokoll. Inte Arduino.

## 2) Blackout

- Funktionskrav: 5 kap. 2 § (nödström när huvudkraft faller) + 4 § (vilka förbrukare som ska leva, passagerarfartyg alla längder / övriga ≥15 m skrovlängd).
- Allmänna råd till 4 §: automatisk övergång omedelbart vid batterinödkraft, **inom 45 s** för nödgenerator.
- Vägledning rubrik "Blackouttest-test med larm": bryt ordinarie ström; mät tid tills nöd är inne; kolla att nöd-förbrukare är inkopplade och på; kolla nödkraft under last. Rutin t.ex. kvartal eller efter reparation.
- Lab: blackouttest = den kontrollpunkten. Tidsgräns 45 s är allmänna råd, inte skall.

## 3) Nödstart

- Funktionskrav: 2–3 §§ (funktion + placering). 3 §: inte i maskinrum / för om kollisionsskott / under vattenlinjen (allmänna råd för placering).
- 1 § allmänna råd: elstart av huvudmotor utan alternativ → dubblerad startkrets.
- Vägledning: okulärbesiktning; bryt ordinarie och prova reservkraft; förbränningsmotor: starta, startanordningar, bränsle för tänkt fartområde; återställ auto-omkopplare efter lokal start. Nöddiesel **provstart t.ex. en gång i veckan**. Intervall månad för mer komplett kontroll.
- Driftstidstabell (passagerare / L≤24 / L>24 mot fartområde A–E) finns **bara** i kompletterande upplysningar, inte i 2 § skall-texten. Använd som vägledning, märk den så.
- Lab: nödstart + återställ auto + last.

## 4) Landanslutning

- Funktionskrav: 5 kap. 7 §. Allmänna råd: anslutningscentral, fast don för flexibel kabel, spänningsindikering, instruktion för in-/urkoppling + elkraft/energibehov.
- Föreskrift landström: TSFS 2024:58. Krav-sidan pekar dit + IEC/IEEE 80005-1/2/3.
- Vägledning: galvaniska/vagabonderande strömmar (isolering från landjord); kabel dimension, nötning, värme/fukt/frost; upplindad kabel → värme/brand. HV: IEC/IEEE 80005-1, EU 2016:917 nämns av TS.
- Lab: följ TS inkopplingsinstruktion vid centralen; kolla don, indikering, jord/isolation mot land, kabel inte upplindad under last.

## 5) IP (och "återställd IP")

- Funktionskrav: 5 § (minimera risk). Vägledning: utrustning ska ha rätt skyddsklass mot tabell.
- Tabell publicerad både i kompletterande upplysningar och på IP-sidan, enligt IEC 60529. Exempel ur TS-tabellen (peka på URL, kopiera inte hela tabellen in i boken): maskinrum över durk utan VS IP22, med VS IP44; under durk eltavla N; öppet däck IP56; inredning/brygga IP20; våtutrymmen uttag = **JFB** (enda JFB-cellen).
- **GAP:** TS har ingen rubrik "återställd IP". Labbsteg "återställ kapsling/IP efter arbete" är en yrkesavledning av kontrollpunkten "rätt IP mot tabell" + att kapsling som lämnas öppen inte längre uppfyller klassen. Märk det som avledning, inte som paragraf.
- JFB: inte generellt krav ombord. 5 § allmänna råd = jordfels*övervakning* på ojordade kretsar >50 V. JFB i tabellen = våtutrymmen/uttag.

## 6) Intyg

- Krav-sidan: den som utfört arbetet bör utfärda intyg att installationen uppfyller gällande regelverk och **tillämpad standard**; bevis på kompetens; ingår i fartygets dokumentation.
- Kompletterande upplysningar (under 5 §): 2 kap. 6 § fackmässigt; 1 kap. 29 § dokumentation; huvudregel = intyg till **befälhavaren** att marina standarder och regelverk följts. Kontrollpunkt: finns intyg för genomfört arbete.
- Kompetens (krav-sidan, "bör"): fartygsingenjör, elektroingenjör, eltekniker enligt STCW, fartygselektriker, eller annan utbildning/erfarenhet (t.ex. marinens el); även varvspersonal eller behörig elinstallatör **med kunskap om fartygsel och regelverket**. Inte ELSÄK-behörighet som sådan.
- Intyget ska enligt TS nämna: att installationen uppfyller regelverk + vilken standard som tillämpats. Mall-fält utöver det = GAP (TS publicerar ingen blankett).

## Copyright / vad Kurs och Manus inte får göra

- Inte klistra in TSFS-kapitel, inte IEC 60529/60092-text, inte hela IP-tabellen som om den vore egen. Peka URL + parafras + 1–2 exempelceller.
- Kompletterande upplysningar är stöd, inte lag. Lektionens "proposed rule" = 5 kap. skall-mening; "på jobbet" = allmänna råd + kontrollpunkterna.
