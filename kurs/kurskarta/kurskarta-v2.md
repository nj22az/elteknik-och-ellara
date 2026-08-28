# Elteknik och ellära — kurskarta v2

Kurs: Elteknik och ellära. Utbildning: Elingenjör, fartyg och automation. 45 YH-poäng. Valbar: nej.
Status: v2 mot officiell kursplan. **v1 (14-modul övergångsspinen) är ersatt** och är inte boss här.
Utfall: grundläggande elteknik i industriella och marintekniska miljöer. Inte STCW ETO. Inte full fartygselektriker-övergång.
Genomförande: teori huvudsakligen distans. Praktiska moment i labb vid fysiska träffar. Fördjupad praktik under LIA.
Kunskapskontroll: skriftligt prov + praktiska laborationer. Betyg: IG / G / VG.
Tid: 45 p ≈ 9 heltidsveckor ≈ 360 studenttimmar (1 p ≈ 8 h). Timmar är ish.

Inga påhittade paragrafnummer utöver det Elon låst. Lektionsruta 1 bär källnivå (skall / vägledning / vår härledning / väntar). Ingen lektionsprosa här.

---

## Låsta källnivåer (Regler via Elon)

| Nivå | Vad | Hur kursen får använda det |
|---|---|---|
| Funktionskrav (skall) | TSFS 2017:26 5 kap. 1–7 § | Får nämnas som skall. Parafrasera, klistra inte in hela föreslagen regel. |
| Vägledning (inte skall) | ”Så här görs kontroll” på kap. 5-upplysningarna | Får träna mot. Får inte skrivas som lagkrav. |
| TS-upplysning / väntar | 1 MΩ | Finns **inte** i skall-text. Labgräns = TS-upplysning eller **väntar på källa**. Aldrig ”lagen kräver 1 MΩ”. |
| Vår härledning (inte TS-rubrik) | ”Återställd IP” | Kommer från IP-krav + olycksnotis. Inte en TS-kontrollpunkt-rubrik. |
| Intyg | till befälhavaren: regelverk + tillämpad standard | Ingen TS-blankett. Krav-sidan. |

Låsta URL:er:
- Krav-sidan: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/
- Kap. 5 upplysningar (Så här görs kontroll): https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/
- IP-utrymmen: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/
- TSFS 2017:26k: https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf
- Nav: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/

ELSÄK styr inte elinstallation ombord (undantag EMC, båtar iland). **väntar på källa** för exakt avgränsning i lektionstext.

---

## 1) Moduler 1:1 mot kunskaper / färdigheter / kompetenser

Tolv moduler. Poäng summerar 45. Varje lärandemål har ett hem. Ingen nödström-, EX- eller 80005-modul.

| Nr | Modul | p | Student-h ish | Kunskaper | Färdigheter | Kompetenser |
|---|---|---|---|---|---|---|
| 1 | Elsäkerhet, stötar, elens verkningar | 3 | 24 | elsäkerhet, stötar, elens verkningar | — | identifiera och bedöma risker; säkerhet, kvalitet, arbetsmiljö |
| 2 | Isolering, SMS, säkerhetsåtgärder innan arbete | 4 | 32 | (stöd till m1) | isolering av utrustning; säkerhetsåtgärder innan arbete | enklare arbeten med säkerhet och regelverk |
| 3 | DC-kretsar: mätning och beräkning (resistiva, serie/parallell) | 5 | 40 | DC; mätning/beräkning resistiva DC-kretsar | mätning och analys | — |
| 4 | Enfas AC: mätning och beräkning | 4 | 32 | AC; mätning/beräkning enfas-AC | mätning och analys | — |
| 5 | Trefas, system och komponenter, spänningstyper ombord | 4 | 32 | trefas; system och komponenter | — | — |
| 6 | DC/AC-utrustning, maskiner, konstruktion och drift | 4 | 32 | DC/AC konstruktion och drift | — | — |
| 7 | Eltavla / elcentral | 3 | 24 | eltavlor/elcentraler | — | — |
| 8 | Verktyg och mätinstrument | 3 | 24 | — | välja och använda verktyg och instrument | ansvar för verktyg och metoder |
| 9 | Ritningar, kopplingsschema, måttsättning | 4 | 32 | ritningar och kopplingsschema | tolka enklare ritningar och måttsättning | — |
| 10 | Enklare styrkrets / hållkrets | 3 | 24 | enklare styrkrets/hållkrets | — | — |
| 11 | Enklare elarbete, funktionsprovning, enkel IP, intyg | 5 | 40 | — | enklare elarbete (losskoppling/anslutning i befintlig gruppledning) | enklare arbeten med säkerhet och regelverk; säkerhet, kvalitet |
| 12 | Risk, strukturerad felsökning, självständighet (VG-spåret) | 3 | 24 | — | mätning och analys (fördjupad) | identifiera och bedöma risker; strukturerad självständig felsökning och enklare elarbete |

**Innehåll täckt, inte som egna moduler:** funktionsprovning strömbrytare/uttag → m11. Serie/parallell praktiskt → m3 + m11. Spänningstyper ombord → m5 (kontext, inte fartygselanläggning som design). SMS-rutiner → m2. Elektroteknik och elektriska maskiner → m6.

**Lektionsmall** (samma skelett, ingen prosa): mål kopplat till K/F/Komp + G/VG; spårhål; (1) föreslagen regel i vanlig svenska med källnivå; (2) vad det betyder i jobbet; (3) genomgånget fel; (4) labb som arbetsorder; (5) dokumentation/intyg där labbet kräver det. Inte Arduino.

---

## 2) Distans vs fysisk labb vs LIA

| Nr | Distans (huvuddel) | Fysisk träff / labb | LIA (fördjupad praktik) |
|---|---|---|---|
| 1 | Stötar, verkningar, riskbegrepp, varför isolation | Demo stötväg / skyddsåtgärd; Lab B | Se verkliga risker i anläggningen, under handledning |
| 2 | SMS-rutin, LOTO-logik, megger som begrepp | Lab A isolation/megger; Lab C SMS | Isolera verklig utrustning enligt fartygets SMS |
| 3 | Ohms lag, serie/parallell, beräkningsövningar | Lab F DC-mätning | Mäta på resistiva kretsar i driftmiljö |
| 4 | Enfas, instrumentval, beräkning | Lab F AC-del | Mäta spänning/ström på enfasutrustning |
| 5 | Trefasbegrepp, system, spänningstyper ombord | Tavla: peka ut system (ingen blackout) | Känna igen spänningstyper där eleven går |
| 6 | Maskiner/utrustning konstruktion och drift | Visning motor/tavla, inte nödstart | Följa en maskin i drift, inte serva nödnät |
| 7 | Tavla/central uppbyggnad | Lab J läsa tavla mot ritning | Orientera sig i fartygets/anläggningens tavla |
| 8 | Instrument, noggrannhet, vård | Verktygsprov i labb | Ansvar för egen väska under LIA |
| 9 | Symboler, schema, måttsättning | Lab J + schema till hållkrets | Tolka as-built mot verklighet |
| 10 | Hållkrets i teori | Lab G bygg/prova hållkrets | Känna igen hållkrets i styrskåp |
| 11 | Regel/intyg på avstånd (krav-sidan parafras) | Lab D IP, Lab E intyg, Lab H elarbete + funktionsprov | Losskoppling/anslutning under handledning |
| 12 | Felsökningsmetod, riskbedömning som text | Lab I felsök; VG-samtal motivera åtgärd | Självständig felsökning mot handledarkrav |

Skriftligt prov ligger efter m1–m11 på distansplattformen eller vid sista fysiska träffen. Praktiska labb A–J måste vara gjorda för G.

---

## 3) Dual-entry-hål (bara där grundkursen faktiskt splittar)

Ingen parallell m3∥m4-bana som i v1. Samma kö för alla. Spårboxar och tempo, inte två kartor.

**Elektriker (ELSÄK / SS 436 40 00) tar med sig:** DC/AC-räkning, instrument, ritning, hållkrets, losskoppling på land.
**Elektriker saknar (denna kurs):** SMS som fartygsrutin; isolation mot skrov/IT, inte PE; att ELSÄK inte är toppnod ombord; spänningstyper ombord; intyg till *befälhavaren*; IP per utrymme (tabell som verifiering av funktionskrav).
**Komprimera för elektriker:** m3, m4, m8, m9, m10. **Fördjupa:** m1, m2, m5, m11 (intyg/IP).

**Fartygsingenjör tar med sig:** anläggningen, maskiner, tavlor som rum, trefas som drift.
**Fartygsingenjör saknar (denna kurs):** megger som arbetsmoment; dokumenterad isolation innan ”vi kan anläggningen”; resistiv beräkning och mätdisciplin; ritning/hållkrets med händerna; losskoppling/anslutning; intyg; motiverad riskbedömning som elektrikerjobb.
**Komprimera för ingenjör:** m5 kontext, m6, m7 orientering. **Fördjupa:** m2, m3, m4, m8, m9, m10, m11, m12.

Hål som **inte** längre får egen modul: sluta tänka SS 436 40 00 som kurskärna (bara box i m1/m2/m5). Regelträd TSFS-djup. Klassintyg. EX-zon-arbete.

---

## 4) Labblista: G och VG

VG = alla G-mål med god kvalitet **plus** självständighet, noggrannhet och **motiverad riskbedömning**. IG om säkerhetssteg hoppas.

### Labbar som får Reglers låsta källor (karta v2 har dem)

**Lab A — Isolation / megger** (m2)
- Ticket: Isolera en 230 V-grupp. Megga. Dokumentera. Inte spänningssätt vid dålig isolation.
- Skall: TSFS 2017:26 5 kap. 1–7 § (funktionskrav; bl.a. minimera elchock m.m. i 5 §). Parafras.
- Vägledning: ”Så här görs kontroll” (jordfel, mätprotokoll). Inte skall.
- 1 MΩ: **inte skall.** Märk TS-upplysning / **väntar på källa**. Aldrig som lagkrav i ruta 1.
- G: följer isolation + mäter + skriver värde, med handledning.
- VG: gör kedjan själv och **motiverar varje steg från riskbedömning**.
- Elektrikerhål: megger mot PE. Ingenjörshål: ”den gick ju”.

**Lab B — Risk / stötar** (m1)
- Ticket: Peka ut stötväg i en given krets/tavla. Vad stoppar stöt. Vad gör du innan arbete.
- Källa: samma funktionskrav 5 kap. 1–7 § (parafras). **väntar på källa** för pedagogisk detalj utöver det.
- G: identifierar risk och skyddsåtgärd.
- VG: skriftlig motiverad riskbedömning, självständigt.

**Lab C — SMS innan arbete** (m2, samma träff som A)
- Ticket: Följ SMS: spänningslöshet bevisad, skylt, vem som får starta.
- Källa: SMS som kursinnehåll; koppling till säkerhetsåtgärder innan arbete. Exakt rederi-SMS = LIA. Regelstöd: funktionskrav + krav-sidan. **väntar på källa** utöver låst kap. 5.
- G: följer listan.
- VG: väljer metod och motiverar mot risk.

**Lab D — Enkel IP efter öppnad kapsling** (m11)
- Ticket: Öppna, arbete, packning/lock tillbaka, slå upp IP för utrymmet.
- Inte TS-rubrik. **Vår härledning** från IP-krav (funktionskrav + IP-tabell som verifiering) och olycksnotis.
- URL IP-utrymmen: tabellen är verifieringshjälp, inte skall-text i 5 kap. 1–7 §.
- G: kapsling stängd, rimlig IP uppslagen, handledning OK.
- VG: självständig, motiverar IP mot utrymme.

**Lab E — Intyg till befälhavaren** (m11, sista rutan på A/D/H)
- Ticket: Efter jobbet: intyg att arbetet följer regelverk + tillämpad standard. Till befälhavaren. Ingen TS-blankett.
- Källa: krav-sidan (intyg om tillämpad standard).
- G: ifyllt intyg med namn, vad, när.
- VG: utomstående förstår utan att fråga eleven.

### Labbar utan TS-kontrollpunkt (träffar G/VG på mätning, arbete, ritning)

**Lab F — DC- och enfas-AC-mätning** (m3+m4)  
G: rätt instrument, rimliga värden, enkel beräkning stämmer. VG: analyserar samband serie/parallell, hög noggrannhet, hittar eget mätfel.

**Lab G — Hållkrets** (m10)  
G: bygger/provar, funktion OK från schema. VG: felsöker själv från ritning.

**Lab H — Enklare elarbete + funktionsprovning** (m11)  
Ticket: losskoppling/anslutning i *befintlig* gruppledning; prova strömbrytare/uttag. Isolation först (Lab A-grind).  
G: säkert, korrekt, isolation gjort. VG: självständigt, noggrant, motiverad riskbedömning.

**Lab I — Strukturerad felsökning** (m12)  
G: hittar felet med ställning. VG: självständig kedja + motiverar åtgärd mot risk.

**Lab J — Tavla mot ritning** (m7+m9)  
G: hittar rätt grupp med hjälp. VG: tolkar systemuppbyggnad själv.

**Inte i denna kurs (v1-labbar utan lärandemål här):** blackouttest, nödstart, landanslutning/80005.

---

## 5) Skriftligt prov. Kurs vs bok för DENNA kurs

**Skriftligt prov (G-golv på kunskaper; VG-frågor märkta):**
- DC, AC, trefas: begrepp och system/komponenter
- Beräkning resistiva DC- och enfas-AC-kretsar (serie/parallell)
- Eltavla/elcentral uppbyggnad
- Hållkrets från enkelt schema
- Stötar, elens verkningar, varför isolation innan arbete
- SMS/säkerhetsåtgärder som princip (inte rederiets blankett utantill)
- Ritningssymboler och måttsättning
- Spänningstyper ombord på grundnivå
- Funktionskrav vs vägledning: eleven ska kunna säga att 5 kap. 1–7 § är skall och ”Så här görs kontroll” inte är skall (en kort fråga)
- Inte: blackoutordning, nödstartförregling, 80005, EX-zon, 1 MΩ som lagkrav

VG på prov: samband i kretsar, motivera skyddsåtgärd från risk, tolka ett schema väl.

**Kursen (inte boken):** distansmoduler, quiz, två spår i tempo, fysiska labb, G/VG-rubrik, rättning av intyg, skriftligt prov, LIA-brief, lärarhandledning, videor på händer (megger, isolation, hållkrets, losskoppling). Inte Arduino.

**Boken, för den här kursen:** kapitel som följer m1–m12. Regel i vanlig svenska med källnivå. Jobbet. Ett genomgånget fel. Utskrivbara arbetsordrar A–J. Spårboxar land/maskin. Symbol- och IP-tabell som *verifieringshjälp* med källa, inte som skall. Intygsmall till befälhavaren (vår blankett, inte TS). Inte tidsplan, inte quizpoäng, inte videomanus.

**Boken som appendix / senare i programmet:** v1-rester (nödström, EX/tank, landström 80005, EMC-djup). Inte denna 45 p-kärna.

---

## 6) Utanför denna kurs mot v1

| v1 | v2 45 p |
|---|---|
| 14-modul övergångsspine, 52–56 h | 12 moduler, 45 p, kursplanen är boss |
| m3∥m4 som parallella spår | samma kö, spårboxar |
| Nödström + lab B blackout + lab C nödstart | **ute** (inget lärandemål tvingar in dem) |
| Landanslutning / IEC/IEEE 80005 + lab D | **ute** |
| EX och tank | **ute** |
| EMC som modul | **ute** (ELSÄK-EMC bara om Regler/Elon låser en mening) |
| Batterier som modul | **ute** (kan nämnas under m6, inte kärna) |
| Kablar och restored IP som TS-punkt | IP **kvar som enkel lab D**, märkt vår härledning |
| Intyg som TS-kontrollprodukt | Intyg **kvar** som till befälhavaren, ingen TS-blankett |
| Isolation/megger 1 MΩ som TS-skall | Isolation/megger **kvar**; 1 MΩ = upplysning/väntar, inte skall |
| Regelträd / sluta tänka SS 436 som egna moduler | boxar i m1–m2–m5 |
| Yrket vs ETO som modul | en sida i m1, inte kurskärna |

---

## Inte i v2
Lektionsprosa, färdiga blanketter utöver intygets fältlista, KDP-manus, påhittade TSFS-nummer, blackout/nödstart/80005-labb.
