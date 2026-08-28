# 01 — TS-hubben Elinstallationer (levande URL-lista)

**Status:** källpack, primärkällor. Parafras, inte avskrift av hela sidor/tabeller.
**Hämtat:** 28 augusti 2026 (användarens zon UTC+7). HTML-nav på hubben + WebFetch.
**Avgränsning:** TSFS 2017:26 5 kap. 1–7 § (installationskarta) görs **inte** om här.

PDF:er i `/workspace/kallpack/` och `src/`. Officiella TSFS-URL:er: `https://www.transportstyrelsen.se/TSFS/TSFS%20YYYY_N.pdf` (konsoliderad: `…_Nk.pdf`).

---

## A. Hubklustret — varje URL med titel

Källa för sidträdet: HTML-nav på hubben 2026-08-28. Alla undersidor under `/elinstallationer/` som fanns i sidans länkar. Relaterade sidor som hubben/krav-sidan pekar på men som **inte** ligger i samma katalog: se avsnitt B.

| # | Titel (sidans H1) | URL |
|---|---|---|
| 1 | Elinstallationer | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/ |
| 2 | Lagar, föreskrifter och standarder | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/ |
| 3 | Krav för elektrisk installation på fartyg | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/ |
| 4 | Minimikrav för IP klass | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/ |
| 5 | Att tänka på vid kabelinstallationer på fartyg | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/kabelinstallationer/ |
| 6 | Batteriinstallationer | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/batteriinstallationer/ |
| 7 | Elektrifiering av fartyg | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/elektrifiering-av-fartyg/ |
| 8 | Laddning av el-bilar på svenska ro-ro passagerarfartyg | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/ |
| 9 | Risker med el-bilar (batterier) | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/risker-med-el-bilar-batterier/ |
| 10 | Säkerhetsåtgärder ombord Ro-Ro fartyg gällande el-bilar | https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/laddning-av-elbilar-ombord/sakerhetsatgarder-ombord-for-el-bilar/ |

**Ingen** undersida med slug `landstrom`, `landanslutning` eller `olyckor` fanns i hubbens HTML-träd. Landström och olyckor ligger på relaterade sidor (B).

---

## B. Relaterade TS-sidor som hubben/krav-sidan pekar på (inte barn till `/elinstallationer/`)

| Titel | URL | Varför den hör till klustret |
|---|---|---|
| 5 kap. Elektrisk utrustning och elinstallationer (kompletterande upplysningar till TSFS 2017:26) | https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/ | Funktionskrav + vägledning; EMC-hänvisning till ELSÄK-FS 2016:3 |
| Regler för nationell sjöfart | https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/ | Tre nivåer: regler / allmänna råd / kompletterande upplysningar; retroaktiv 5 kap. 7 § landnät senast 2020-04-01 |
| Olyckor relaterade till elinstallationer ombord | https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/ | Publicerad 24 jan 2025; hubben länkar som ”Olyckor relaterad till elinstallationer ombord” |
| Riktlinjer och rekommendationer för anslutningar av fartyg och fritidsbåtar till landbaserat elnät | https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/riktlinjer-och-rekommendationer-for-anslutningar-av-fartyg-och-fritidsbatar-till-landbaserat-elnat/ | Krav-sidan pekar hit; utgiven 2015-04-20; vägledning, inte föreskrift |
| Transportstyrelsens riktlinjer för elektrifiering av fartyg (TSG 2023-1338) | https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/transportstyrelsens-riktlinjer-for-elektrifiering-av-fartyg/ | Utgiven 2023-02-20; batterisidan/elektrifieringssidan pekar hit + EMSA BESS |
| Charging of electric vehicles onboard Swedish Ropax vessels (TSG 2018-3106) | https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/ | Katalogpost 2018-07-11; PDF-filnamn inte utläst från katalogsidan (GAP) |
| EMSA BESS (extern, TS rekommenderar) | https://emsa.europa.eu/ (sökväg: Ship Safety Standards – Battery Energy Storage Systems) | Inte TS-föreskrift |

---

## C. Hubben (#1) — parafras

Fartygsel liknar industriell el mer än villael: hög driftsäkerhet, extrema miljöer, avbrottsfri drift. Livsviktiga funktioner är elberoende. Elinstallatörer ska vara kompetenta och känna regelverket.

**Internationellt:** övergripande krav från IMO; detaljkrav via IEC.

**Nationellt:** TSFS 2017:26 (sedan 2017) är heltäckande och funktionsbaserad. Kapitel 5 = elektrisk utrustning och elinstallationer. Kompletterande upplysningar = stöd vid ny-/ombyggnad, inte föreskrift.

Sidan pekar vidare till lagar/föreskrifter/standarder och till krav för elektrisk installation.

---

## D. Lagar, föreskrifter och standarder (#2) — fullt utläst

Sidans rubrik: *För elinstallationer och hantering av elektrisk utrustning på fartyg gäller*

### D.1 TS-föreskrifter som TS listar (ordning enligt sidan)

1. **TSFS 2019:4** — maskininstallation, elektrisk installation och periodvis obemannat maskinrum, **16–22 kap.**, bilaga 1 och 2.
2. **TSFS 2017:26** — fartyg i nationell sjöfart, **del 5**.
3. **TSFS 2019:120** — passagerarfartyg på inrikes resa, **del C**.
4. **TSFS 2018:60** — fartyg i inlandssjöfart. *Obs 2026:* denna är **upphävd** från 1 maj 2026 av TSFS 2026:20 (se 03). Hub-sidan var **inte** uppdaterad till 2026:20 vid hämtning.
5. **SJÖFS 2002:17** — säkerheten på passagerarfartyg i inrikes trafik, **del D** (Sjöfartsverket).
6. **SJÖFS 1999:27** — fiskefartyg ≥ 24 m, **del C**.

**GAP:** sidan nämner inte TSFS 2024:58 (landström) och inte TSFS 2026:20 (inland). Landström står på krav-sidan.

### D.2 ”När gäller Elsäkerhetsverkets föreskrifter?”

TS:s egen mening:

> Elsäkerhetsverkets föreskrifter gäller varken på fartyg eller på fritidsbåtar, enda undantaget är elektromagnetisk kompatibilitet (EMC) och när fritidsbåtar har tagits upp på land för vinterförvaring eller för reparation.

Detta är **TS-vägledning**. Primärkällor hos Elsäkerhetsverket och ELSÄK-FS: se `03-lag-elsak-kompetens.md`. ”Båtar på land” har **ingen** motsvarande mening i ELSÄK-FS 2022:1 eller elsäkerhetslagen.

### D.3 Standarder som TS namnger (ingen standardtext här)

- **IEC 60092** — all elektrisk utrustning på fartyg (IMO-godkänd serie enligt TS).
- **IEC 60079** — explosiva atmosfärer.
- **IEC/IEEE 80005-1:2019** — HVSC (högspänning landström).
- **IEC/IEEE 80005-2:2016** — data/övervakning landström HV/LV.
- **IEC PAS 80005-3:2014** — LVSC.
- Övriga som TS nämner: **IEC 60533:2015** (EMC på fartyg med metallskrov), **SS-EN ISO 13297:2021** (båtar, elsystem AC/DC; ersätter ISO 10133:2012), **SS EN 60092–507** (små fartyg).

---

## E. Krav för elektrisk installation (#3) — parafras (ingen kap.5-karta)

**Kompetens (bör):** fartygsingenjör, elektroingenjör, eltekniker enligt STCW, fartygselektriker, eller annan utbildning/erfarenhet (t.ex. marinens el). Även varvspersonal eller behörig elinstallatör **med kunskap om fartygsel och regelverket**.

**Intyg (bör):** den som utfört arbetet bör utfärda intyg att installationen uppfyller gällande regelverk **och tillämpad standard**; ingår i fartygets dokumentation. Bindande *ska* för SOLAS-fartyg: TSFS 2019:4 16 kap. 2 § (se 03).

**Utrustning:** krav varierar med fartygstyp, byggnadsdatum och storlek. Vid ombyggnad: senaste standard/regelverk.

**IP/EX:** rätt klass mot utrymme; nödutrustning får inte placeras för om kollisionsskottet.

**EMC:** lagreglerat; IEC 60533; Elsäkerhetsverket är EMC-myndighet **även på fartyg**.

**Jordning, kretsskydd, isolation:** inte slarva med jord; varje krets ska skyddas mot överlast och kortslutning; isolationsmotstånd **bör** vara lägst **1 MΩ** (siffran står här, inte som siffra i 2017:26 5 kap. 5 § ska-text).

**Landanslutning:** pekar på **TSFS 2024:58** + nationella riktlinjer 2015 + IEC/IEEE 80005-1/2/3.

**Kablar / batterier:** länkar till #5 och #6.

---

## F. IP-tabell (#4)

Minimikrav enligt **IEC 60529**. Tabell per utrymme × utrustningstyp (eltavlor, belysning, motorer, värmare, uttag, boxar/brytare, instrument). Förklaringar på sidan: VS = vattenspridning; EX = explosionsklassad; N = installation tillåts inte; JFB = jordfelsbrytare (enda JFB-cellen: våtutrymmen/uttag); parentes IP44 om i box; IP55+T3 om ventilation 10 luftväxlingar/tim och 450 mm över däck.

**Copyright:** kopiera inte hela tabellen in i kurs/bok. Peka URL + enstaka exempelceller. Se även kompletterande upplysningar (samma tabell enligt TS).

---

## G. Kabelinstallationer (#5) — checklista (parafras)

Tio punkter: flamhämmande kablar; metallmantel/armering kontinuerlig och jordad; märkdata invid överlastskydd; varje krets skyddad mot kortslutning/överlast; planera brandkonsekvens; separera kraft/signal och särskilt huvudkraft från nödkraft (nöd inte nära maskinrum A, avgas, fordonsutrymmen, kök, tvätt); godkända brandtätningar, inga borrhål för enskilda kablar; brandsäker kabel brandpump–nödtavla genom brandfarligt utrymme; EX-kablar godkända och separerade, egensäkra kretsar blå/svart med blå märkning, zenerbarriär EX även utanför zon; fäst så att skav/värme inte skadar (vertikala stegar: stålband).

Tabell **fästavstånd** efter ytterdiameter, armerad/oarmerad (t.ex. < 8 mm: 200 / 250 mm). **Inte** föreskriftstext; TS-checklista.

---

## H. Batteriinstallationer (#6)

Användning: huvudkraft/belysning, nöd, start, radio/nav, numera även framdrivning.

**Hög energitäthet (t.ex. Li-ion) för framdrivning/hjälp/nöd:** planera enligt sammanhållet regelverk/standard **eller** riskhantering. **Anmälan till och godkännande av TS.** Kontakta TS i planeringsfasen. Nationella riktlinjer (TSG 2023-1338) **behålls tills vidare**; alternativ: EMSA BESS (svenskt initiativ enligt TS). Bygg inte innan anmälan.

**Dokumentation:** verifiering av funktionskrav, typgodkännande, riskhantering, elbalansschema, ritningar, tillverkarens anvisningar, drift/underhåll. TS citerar **FSL 2 kap. 1 §** (sjövärdighet) och nämner dokumentationskontroll enligt **”fartygssäkerhetslagens 4a §”** — det är **5 kap. 4 a §** FSL (dokumentationskontroll). Formuleringen på sidan är slarvig.

**Elbalansschema ska minst:** Ah, systemspänning, förbrukare/effekt per grupp, spänningsfall (avstånd + åldrande), omgivningstemperatur, tidskrav vid nödkraft (fartområde).

**Spänning:** tåla nödbelastning utan omladdning; under urladdning inom ±12 % av nominell. Startbatterier: kyla + laddningsmottaglighet. Stationära: hålladdning.

**Placering (TS-text, blandar ska/bör):** hög energitäthet i batterirum med brandsäkerhet. Bly 5–20 kWh: ventilerad låda med lock + upptagningskärl, ventilation till fria luften; < 5 kWh: ventilation till rummet kan räcka. **> 20 kWh:** särskilt ventilerat rum avskilt från maskinrum; bara nödvändig el (t.ex. belysning); **all el i batterirum EX-klassad**. UPS med ventilreglerade batterier: ventilerat utrymme, **inte** EX-krav. Fastsatta mot rullning; poler beröringsskyddade; inga hängsäkringar; larm (över/under, jordfel, avbrott, AC, laddare). Hänvisning **SS-EN 62485**.

---

## I. Elektrifiering (#7)

Samma anmälnings-/regelverkskrav som batterisidan för Li-ion m.m. Alternativ utformning = riskhantering. EMSA BESS: mål/funktionsbaserad; gäller **Li-ion > 5 kWh** på fartyg i nationell **eller** internationell sjöfart, oavsett konstruktionsmaterial. EMSA omfattar **inte** < 5 kWh och **inte** second life. Kapitel 1–6 + bilagor A–C enligt sidans översikt. Alternativ design: MSC/Circ.1002 eller MSC.1/Circ.1455.

TSFS 2017:26 är teknikneutral: **second life** kan användas om funktionskraven verifieras; då teknisk analys enligt **MSC.1/Circ.1455**.

---

## J. Laddning av elbilar ombord (#8–10)

Inget förbud i svensk lagstiftning mot laddning på svenska ro-ro-passagerarfartyg (jfr danska rederier efter Pearl of Scandinavia 2010-11-16; den bilen var inte fabrikstillverkad). Redaren ansvarar för säkerhetsåtgärder och brandbekämpning. Riskbedömning **ska** enligt TS.

**Risker (#9):** hög spänning (upp till 600 V), termisk rusning, gas/HF, svår släckning p.g.a. inkapsling. Orsaker: kemisk reaktion, deformation, felhantering, överladdning, kortslutning, skadat batteri, fel laddare/nät, överhettning.

**Åtgärder (#10, bör/ska blandat i TS-text):** marin godkänd utrustning eller TS-godkänd riskanalys; minst **IP56** (IP44 i box); skydd mot mekanisk skada; bryt+larm vid fel. Laddning helst väderdäck; isolera brand. Slutna lastutrymmen: SOLAS II-2/20.3.2.2 (IP55, T3, 450 mm, 10 luftväxlingar) **eller** Ex enligt II-2/20.3.2.1. Brandutrustning enligt SOLAS II-2/20.6 (TSFS 2009:98). Ingå i ISM. Experimentbilar **får inte** laddas. Europeiska AFV-riktlinjer rekommenderas.

---

## K. Olyckor (relaterad, 24 jan 2025)

Fartyg har oftast **inte** JFB (driftsäkerhet). Personsäkerhet = slitagekontroll, **intakt IP**, korrekt eftermontage. Rapporterade händelser: slitage, förlorad IP, utrustning öppnad och inte återställd. Dödsolyckor har förekommit enligt TS.

Tre riskområden: (1) flexibla kablar — landanslutning, ro-ro-matning till fordon/kylcontainrar, rörlig köksutrustning (jordledare kan falla bort); (2) utrustning med IP-krav, särskilt > 50 V i fukt; (3) arbete på höjd (fallet skadar mer än chocken) — **befälhavarens** arbetsmiljöansvar.

TS: rutiner i **SMS**. Länk till IP-sidan.

**GAP:** TS har ingen rubrik ”återställd IP”; det är yrkesavledning av kontrollpunkten.

---

## L. Landström — var det står (ingen hub-undersida)

| Nivå | Källa |
|---|---|
| Bindande, SOLAS-segment | TSFS 2024:58 (svenska fartyg; **inte** nationell/inland/fritids/<15 m utom passagerare). Ändrad av TSFS 2026:44 (definition inland → TSFS 2026:20), ikraft 1 maj 2026. Upphäver SJÖFS 2008:82 via TSFS 2024:59 (1 nov 2024). |
| Bindande funktionskrav nationell | TSFS 2017:26 5 kap. 7 § (retroaktivt senast 2020-04-01 enligt TS nationell-sida). **Inte** ändrad av 2026:9/37. |
| Inland | TSFS 2026:20 12 § pekar på förordning (EU) 2023/1804 (AFIR); ingen egen landström-TSFS för inland. |
| Vägledning | Krav-sidan + riktlinjer 2015-04-20 + IEC/IEEE 80005. |

---

## M. GAP i hubklustret

1. Hubbens lagsida listar fortfarande **TSFS 2018:60**, inte **TSFS 2026:20** (upphävde 2018:60 2026-05-01).
2. Lagsidan listar **inte** TSFS 2024:58.
3. Ingen landström-undersida i `/elinstallationer/`-trädet.
4. Olyckor ligger under `/aktuell-information/`, inte i hubträdet.
5. Riktlinjer landanslutning 2015: katalogpost utan artikelnummer; PDF-länk inte utläst från katalogsidan i denna hämtning.
6. Charging-rapport TSG 2018-3106: katalogpost, PDF-URL inte utläst.
7. SJÖFS 2002:17 del D och SJÖFS 1999:27 del C: listade av TS; elinnehåll **inte** utdraget i detta pack.
8. TSFS 2019:120 **del C**: listad som elrelevant; detaljer inte utdragna här (se 03, gap).
