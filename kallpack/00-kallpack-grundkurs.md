# Källpaket v1 — Elteknik och ellära 45 p
**Till:** Elon (vidare till Kurs, Manus). **Från:** Regler. **Datum:** 2026-08-28.
**Kurs:** Elteknik och ellära, 45 YH-poäng (Kurskarta v1 död). Dual entry: landelektriker (ELSÄK/SS 436 40 00) + fartygsingenjör.
**Bok:** Fartygselektriker. Från landel till TSFS. Inte STCW ETO.

Parafras, inga avskrifter av föreskrift eller IEC. Inga IP-tabeller i materialet — peka URL.

---

## 0. Citatnivåer (låsta)

| Nivå | Vad | Användning i lektion |
|---|---|---|
| **Skall** | TSFS-paragraf "ska" | "Proposed rule" |
| **Allmänna råd** | "bör" i samma TSFS | Förväntan, inte skall |
| **Kompletterande upplysningar** | TS webb, bl.a. "Så här görs kontroll" | Jobbet / labben. Inte lag |
| **Avledning** | Yrkessteg som TS inte rubriksätter | Märk "avledning". Ex: återställd IP |
| **GAP** | Ingen primärkälla | Skriv inte som regel |

Låst av Elon: 5 kap. 1–7 § = funktionskrav. 1 MΩ och fartområde A–E-tider är **inte** skall. Återställd IP = avledning. Intyg har ingen TS-blankett (GAP). Klistra inte in IEC/IP-tabeller.

**TSFS 2017:26 kap. 5 är funktionsbaserad.** IEC 60092 m.fl. är *verifiering* via 1 kap. 14 § (nationell), inte inkorporerade i 5 kap. **TSFS 2019:4 16 kap. 1 §** gör IEC 60092 till **ska** för fartyg med internationellt säkerhetscertifikat — det är SOLAS-spåret, inte 45 p-kärnan.

---

## 1. Isolation före arbete (kärna)

**Skall:** TSFS 2017:26 5 kap. 5 § — system ska utformas och installeras så att kortslutning, brand, explosion, elchock, materiella skador och EMC minimeras.

**Allmänna råd till 5 §:** ojordade kretsar (utom ≤ 50 V) bör ha **jordfelsövervakning** (inte frånkoppling). Åtgärder mot vagabonderande strömmar. Oskyddade metalldelar jordade utom klenspänning.

**SOLAS-spår (inte 45 p-kärna, men samma siffra):** TSFS 2019:4 22 kap. 10 § — kontinuerlig isolationsövervakning på ojordat system. Allmänna råd: isolationsmotstånd **lägst 1 MΩ**.

**1 MΩ på TS krav-sida** (nationell vägledning, inte 2017:26-skall):
https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/

**Kontroll (kompletterande upplysningar, Isolationsprov):**
- Instrument ombord → daglig avläsning.
- Saknas instrument → fackman **megger** isolerade delar + protokoll.
- Underhållsexempel: vart 6:e år eller vid problem. Exemplet är inte föreskrift.

**På jobbet:** Landalektriker väntar JFB som slår ifrån. Ombord är IT/ojordat + övervakning. Megger **före** arbete på avstängd anläggning; isolationsinstrument **under** drift. Läckströmmar korroderar skrov/propeller/axel.

**Lab:** isolation/megger enligt "Så här görs kontroll" + protokoll. Inte Arduino.

**URL:** https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/

---

## 2. Stötar (kärna)

**Skall:** samma 5 kap. 5 § (elchock). FSL 2 kap. 1 § sjövärdighet; 4 kap. arbetsmiljö ombord (befälhavaren arbetsgivarlik).

**TS olyckor-sida (2025-01-24):** livsfarlig ström trots att installation följt krav; oftast *slitage*. Enstaka dödsolyckor.
https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/

Undervisningspunkter (parafras):
- **Oftast ingen JFB** i fartygsnätet — driftsäkerhet. Personskydd = slitagekontroll, intakt IP, jordfels*övervakning*.
- JFB *ändå*: landström ≤ 125 A (TSFS 2024:58 bilaga p. 13: ≤ 30 mA *eller* isolertransformator) — landgränssnitt, inte kärna 45 p. IP-vägledningstabellen har "JFB" i cellen våtutrymmen/uttag — peka URL, kopiera inte tabellen.
- **Flexibla kablar** = främsta personskaderisk (landkabel, ro-ro överkörning, rullande kök med avsiten jord).
- **Arbete på höjd:** stöten dödar inte alltid; **fallet** gör det.

**SHK 2024:04** (S-150/22, STENA GERMANICA): död + senare stöt vid barlastpump. Packning saknades, ingen skyddsjordning, ventil spänningssatt under drift, **lokalt jordad TT-sidokrets utanför** isolationsövervakade nätet. SHK till TS: bara den med kunskap om el *och fartygets elsystem* ska göra elarbete.
https://shk.se/sok-utredningar/sjofart/2023-04-13-personolycka-ombord-pa-ett-ro-ro-fartyg-pa-resa-mellan-goteborg-och-kiel

**Lab-fel att räkna på:** packning/IP, jord saknas, sidokrets utanför IR-vakten, stöt → sjukvård iland (SHK-rekommendation).

---

## 3. SMS (kärna)

TS olyckor-sida: lägg rutiner i **SMS** för flexibla kablar, genomföringar, elskåp, kopplingsboxar; byt/återställ i tid.

FSL 2 kap. 9–10 §§ rederiets säkerhetsorganisation. 5 kap. 30 § handlingar ombord.

**SMS-checklista för 45 p (källa i parentes):**
1. Ingen JFB i isolerat huvudnät; jordfelsövervakning (olyckor-sida; 5 § AR).
2. Återställ IP efter varje öppning — **avledning**, ingen TS-rubrik (olyckor-sida + IP-kontrollpunkt).
3. Flexkabel: nötning, jordledare, inte upplindad under last (olyckor-sida; 2024:58 för land, appendix).
4. Fallskydd vid elarbete på höjd (olyckor-sida).
5. Bara fartygsel-kompetens; intyg (krav-sida; 2019:4 16 kap. 2 § för SOLAS; 2017:26 2 kap. 6 § fackmässigt).
6. Sidokretsar utanför IR-vakt (SHK 2024:04).
7. Stöt → ilandsjukvård (SHK).
8. Isolationsrutin i underhållssystem (kompletterande upplysningar; intervall = exempel).

**Återställd IP:** efter arbete ska kapsling, packning och genomföring återge den klass utrustningen hade mot TS IP-tabell. Märk avledning. Tabell-URL (kopiera inte): https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/

---

## 4. Eltavla / elcentral (kärna)

**Skall:** 5 kap. 5 § (minimera risk). Allmänna råd: separat huvudbrytare per kraftkälla; varje krets skydd mot kortslutning och överlast; märkning.

**Kompletterande upplysningar (skydd mot elolyckor / eltavlor) — vägledning:**
- Inga oskyddade spänningsförande delar > 50 V DC/AC på tavelframsida.
- Tillträde fram och bak utan fara; gavlar/baksida skyddade.
- Ledande golv: mattor/trallar av oledande material.
- Avstånd tavla–stålskott < 0,9 m → klä skottet 1,9 m med oledande material.
- Utrymme bakom för tillsyn: djup i regel ≥ 0,6 m (0,5 m vid spant).
- Skylt med högsta spänning på dörr bakom tavla.
- Grupper/säkringar märkta: märkström, area, förbrukare.
- Generator: överström/kortslutning enligt tillverkare; test av behörig elektriker (exempelvärden på webb — inte skall).

**SOLAS-detalj (appendix, inte kärna):** TSFS 2019:4 22 kap. 4 § m.fl. samma tavellogik.

**Kontroll:** elskåp rätt monterade (brand/vatten); kablar klamrade; böjradie; rätt IP mot tabell (URL); intyg finns.

**Lab:** tavla som arbetsorder — märkning, skydd, bakre tillträde, IR-instrument, återställd kåpa.

---

## 5. Ritningar (kärna)

**Skall:**
- TSFS 2017:26 **1 kap. 27 §** — dokumentation så sjövärdighet, drift, underhåll, felsökning och tillsyn kan bedömas. Ska visa hur kraven verifierats. Allmänna råd: tillämpade regelverk/standarder, installationsritningar, systemscheman, material-/utrustningscertifikat, provningsrapporter, egenkontrollintyg, besiktningsintyg.
- **1 kap. 29 §** — dokumentation uppdaterad; väsentliga ändringar spårbara.
- **1 kap. 13–14 §§** — verifiering mot funktionskrav via sammanhållet regelverk/standard, jämförande/riskanalys och/eller empiri. Nybyggnad: senaste lydelse (AR).
- FSL **5 kap. 26–28 §§** — ritningar till nybygge/ombyggnad som ska besiktigas ges in till TS (el faller under utrustning/anordningar; lagen säger inte "el").

**Kompletterande upplysningar (Elsystem-överensstämmelse med ritningar):**
- Hela elsystemet dokumenterat så felsökning är möjlig.
- Mindre/gamla fartyg: enkelt enlinjeschema kan räcka.
- Ändring utan uppdaterad ritning = inbyggt fel.
- Kontroll: ritningar finns och är uppdaterade. Ingå i underhållssystem.

**På jobbet:** landelektrikerns relationsritning har en fartygsmotsvarighet. Ingen uppdatering → SHK-läget (sidokrets ingen känner).

**Lab:** jämför tavla mot enlinje; rita avvikelse; märk spårbar ändring mot 1 kap. 29 §.

---

## 6. ELSÄK-undantaget (kärna — landelektrikerns första krock)

**TS lagar-sida:**
> Elsäkerhetsverkets föreskrifter gäller varken på fartyg eller på fritidsbåtar, enda undantaget är elektromagnetisk kompatibilitet (EMC) och när fritidsbåtar har tagits upp på land för vinterförvaring eller för reparation.
https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/

**Vad som faktiskt är lag vs webb:**

| Påstående | Primärkälla | Flagga |
|---|---|---|
| Elinstallationsregler gäller inte på fartyg | Elsäkerhetsverket FAQ + prop. 2015/16:163 s. 20–21. Avgränsning via *stationär* starkströmsanläggning, inte en fartygsmening i elsäkerhetslagen (2016:732) | ELSÄK-FS **2022:1 har ingen fartygsmening**. Den uttryckliga meningen fanns i **upphävda** ELSÄK-FS 2008:1. Citera inte 2008:1 som gällande |
| EMC gäller på fartyg | ELSÄK-FS 2016:3 undantar inte fartyg. TS kompletterande upplysningar nämner 2016:3 uttryckligen. IEC 60533 = marin verifieringsstandard | EMC-myndighet = ELSÄK även ombord |
| Fritidsbåt på land = ELSÄK | **Endast TS-sidan.** Inte ELSÄK-FS, inte elsäkerhetslagen | Får inte skrivas som lagtext. GAP hur "stationär anläggning" slår när båten står på land |

FAQ: https://www.elsakerhetsverket.se/fragor-och-svar/arkiv-fragor/omfattas-elarbete-pa-fordon-av-elsakerhetslagen/
Prop.: https://regeringen.se/rattsliga-dokument/proposition/2016/04/prop.-201516163
ELSÄK-FS 2022:1: https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2022-1/
ELSÄK-FS 2016:3: https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2016-3-konsoliderad-version/

**Kompetens (ska vs bör):**
- **Nationell (45 p-världen):** 2017:26 2 kap. 6 § *fackmässigt*. Personkrets = vägledning (kompletterande upplysningar + krav-sida).
- **SOLAS:** TSFS 2019:4 **16 kap. 2 § ska:** el-teknisk bakgrund + goda kunskaper om fartygs elinstallationsprinciper och gällande standarder. Intyg **ska** att installationen uppfyller **tillämpad standard**, **innan** godkännande.
- **Bör-lista** (samma AR + TS webb): fartygsingenjör, elektroingenjör, STCW-eltekniker, fartygselektriker, eller likvärdig (t.ex. marinens el). Webb tillägger varv / landauktoriserad elinstallatör **om** fartygsel-kunskap finns.
- **ELSÄK-auktorisation räcker inte ensam.**

**Intyg:**
- Skall (SOLAS): "uppfyller tillämpad standard".
- Bör (nationell webb): regelverk + tillämpad standard; till **befälhavaren**; ingår i dokumentationen.
- **GAP:** ingen mall, inga obligatoriska fält. Manus mall = pedagogisk, inte TS-blankett.

---

## Regelträd (kort, för 45 p)

```
Fartygssäkerhetslagen (2003:364)
  2 kap. 1 § sjövärdighet (el nämns inte vid namn)
  7 kap. 2 § 1 → FSF 2003:438 2 kap. 1 § → TS föreskrifter
        │
        ├─ TSFS 2017:26  nationell  (45 p-spåret)
        │    funktionsbaserad; 5 kap. el; verifiering 1 kap. 14 §
        │    gäller: svenska pax alla L; övriga svenska L≥5 m
        │    undantar: intl certifikat, 2009/45, fisk ≥24 m (97/70),
        │              fritid ≤24 m, inland, örlog
        │
        ├─ TSFS 2019:4   intl säkerhetscertifikat / SOLAS II-1
        │    16–22 kap. detalj; IEC 60092 SKA
        │
        ├─ TSFS 2019:120 inrikes pax 2009/45 (L≥24 m / HSC; inte enbart E)
        ├─ TSFS 2026:20  inland (ersätter 2018:60 fr.o.m. 2026-05-01)
        └─ TSFS 2024:58  landström — GÄLLER INTE nationell sjöfart (2 §)
```

IMO ger övergripande krav; IEC detalj. TS hub: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/

**Kap. 5 1–7 § i en mening vardera (installatör):**
1. Väsentlig el med hög tillförlitlighet. Två aggregat >24 m = AR.
2. Nödåtgärder ska kunna strömförsörjas om huvudkraft dör. **Tider A–E = webb, appendix.**
3. Nödkraft placerad där vatten/brand minimeras. Inte maskinrum/under VL = AR.
4. Pax alla L + övriga ≥15 m: komm, larm, NUC-ljus, utrymnings-/sjösättningsljus. 45 s nödgenerator = AR.
5. Minimera kortslutning/brand/explosion/elchock/EMC. IR-vakt >50 V = AR. IP/skrov-återledare = webb.
6. Batterier: placering, ventilation, nödvändig övervakning.
7. Landnät: tillfredsställande säkerhet. Central/fast don = AR. 2024:58 gäller **inte** denna population.

Konsoliderad: https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf
**OBS:** 2017_26k t.o.m. TSFS 2026:9. TSFS 2026:37 (ikraft 2026-05-01) saknas i k-PDF (inlandsdefinition → 2026:20). Kap. 5 orört.

---

## Appendix — inte 45 p-kärna (URL + en rad)

**Nödström A–E-tider** (kompletterande upplysningar, *inte* 2 §): pax 1/3/3/6/12/24 h mot nära-E … A; övriga L≤24: 1/1/3/6/8/18; L>24: 1/3/3/6/12/18. Samma sida som kap. 5-upplysningar.

**EX/tank:** TSFS 2019:4 22 kap. 25–26 §§ IEC 60079 / IEC 60092-502. Skrov som återledare **förbjudet** på tankfartyg (22 kap. 5–8 §§). Nationell 5 § kan inte uppfyllas med skrovåterledare på tank (webb, inte 2017:26-mening).

**HV-landström:** TSFS 2024:58 + TSFS 2026:44 (bara inlandsdefinition). Gäller **inte** nationell/inland/fritid. HV via AFIR (EU) 2023/1804; IEC/IEEE 80005-1:2019 på TS-webb. LV *bör* PAS 80005-3:2014 i föreskriften; katalog 2026 = IEC/IEEE 80005-3:2025 (TSFS inte uppdaterad). FuelEU 2023/1805 = användning vid kaj, inte installatörsklausul.

**Inland:** TSFS 2026:20, ES-TRIN kap. 10. TS-webb kan fortfarande säga 2018:60 — inaktuellt efter 2026-05-01.

---

## Levande URL-lista

### Hub och 45 p
- https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/
- https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/
- https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/
- https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/
- https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/
- https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/
- https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf
- https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetslag-2003364_sfs-2003-364/
- https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetsforordning-2003438_sfs-2003-438/
- ELSÄK FAQ, 2022:1, 2016:3, prop. 2015/16:163 (URL ovan i §6)
- SHK 2024:04 (URL ovan i §2)

### Hub-undersidor (appendix / senare)
- Kablar https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/kabelinstallationer/
- Batterier https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/batteriinstallationer/
- Elektrifiering/BESS (anmäl TS före bygg; EMSA >5 kWh) https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/elektrifiering-av-fartyg/
- Elbilsladdning ro-ro https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/
- Elbilsrisker https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/risker-med-el-bilar-batterier/
- Elbilssäkerhet ro-ro https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/sakerhetsatgarder-ombord-for-el-bilar/

### Senare / appendix
- TSFS 2019:4 https://www.transportstyrelsen.se/TSFS/TSFS%202019_4.pdf
- TSFS 2019:120 https://www.transportstyrelsen.se/TSFS/TSFS%202019_120k.pdf
- TSFS 2024:58 https://www.transportstyrelsen.se/TSFS/TSFS%202024_58.pdf
- TSFS 2026:44 https://www.transportstyrelsen.se/TSFS/TSFS%202026_44.pdf
- TSFS 2026:20 https://www.transportstyrelsen.se/TSFS/TSFS%202026_20.pdf
- TSFS 2026:37 https://www.transportstyrelsen.se/TSFS/TSFS%202026_37.pdf (2017:26 inlandspekare)
- Landströmsriktlinje 2015 (äldre än 2024:58) https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/riktlinjer-och-rekommendationer-for-anslutningar-av-fartyg-och-fritidsbatar-till-landbaserat-elnat/
- FuelEU https://www.transportstyrelsen.se/sv/sjofart/miljo-och-halsa/klimat-och-energi/fueleu-maritime/
- Inland https://www.transportstyrelsen.se/sv/sjofart/fartyg/fartyg-i-inlandssjofart-inre-vattenvagar/regler-for-fartyg-i-inlandssjofart/
- Fartområden https://www.transportstyrelsen.se/sv/sjofart/sjotrafik-och-hamnar/fartomraden/fartygets-konstruktion-och-utrustning/
- ES-TRIN https://www.cesni.eu/en/technical-requirements/
- IEC-katalog (årtal, inte innehåll): 60092 SER, 60079 SER, 60533:2015, 80005-1/2/3
- SIS: SS-EN ISO 13297:2021, SS-EN 60092-507, SS-EN IEC/IEEE 80005-1 utg 1:2026

---

## Copyright

- Parafrasera TSFS och kompletterande upplysningar. Ingen kapitelavskrift i bok/kurs.
- IEC/ISO säljs via SIS/SEK. Namnge, kopiera inte.
- IP-tabellen på TS-sidan bygger på IEC 60529 — peka URL, 1–2 exempelceller max (t.ex. inredning IP20, öppet däck IP56). Inte hela matrisen.
- Levande standardlista på URL, inte fryst i boken (Manus/KDP-regel).

---

## GAP (skriv inte som regel)

1. Ingen TS-blankett för intyg; inga obligatoriska fält.
2. 1 MΩ och A–E-tider och IP-matris sitter inte i 2017:26 skall-text.
3. Återställd IP = avledning.
4. "Båtar på land = ELSÄK" bara TS-webb.
5. ELSÄK-FS 2022:1 saknar fartygsmening (2008:1 upphävd).
6. Inland kompetens/intyg: ingen regel i 2018:60/2026:20.
7. TSFS 2019:120 del C el inte utdragen (el via klass + 2009/45-bilaga).
8. TS el-sida citerar upphävda SJÖFS 2008:81/82, 2002:17; 1999:27 kap. III el upphävd 2006.
9. 80005-årtal krockar: webb 2012/2014/2019 vs katalog 2025/2026.
10. Ingen namngiven TS-olycksrapport bakom olyckor-sidan utöver syntes + SHK 2024:04.
11. TSFS 2019:4 landanslutning saknas i 16–22 kap. — landström intl = 2024:58.
12. 2017_26k saknar 2026:37.

Levande lista: kolla TS nummerordning 2026 vid varje nytryck.
