# Källpack 04 — Standarder, landström och elolyckor (svensk sjöfart)

**Syfte:** Primärkällor för IMO/IEC/ISO i Transportstyrelsens (TS) tillämpning, landström, elrelaterade olyckor/SMS-punkter och tillämplighet inland–kust–internationellt.

**Avgränsning:** Standarder *namnges* med katalogår där det går att läsa av IEC/SIS-katalogsidor. **Ingen återgivning av upphovsrättsskyddad standardtext.** Inga påhittade IEC-klausulnummer. Ingen egen IP-tabell — TS:s IP-tabell hänvisas till med URL.

**Hämtat:** 2026-08-28 (användarens zon: Asia/Ho_Chi_Minh, UTC+7).

---

## Funktionsbaserad lag vs standard för verifiering (flagga)

Detta är den viktigaste distinktionen i svensk TS-kontext. **Blanda inte ihop bindande funktionskrav med verifieringsstandard.**

| Nivå | Vad det är | Rättslig status i TS-kontext |
|---|---|---|
| **Föreskrift (ska)** | Funktionskrav: *vad* som ska uppnås | Bindande. Ex. TSFS 2017:26 5 kap. (nationell sjöfart); TSFS 2019:4 16–22 kap. (internationellt certifikat); TSFS 2024:58 (landström för de fartyg som omfattas) |
| **Allmänna råd (bör)** | TS:s rekommenderade sätt att uppfylla funktionskravet | Inte bindande. Annan lösning tillåten om den är i nivå och dokumenterad |
| **Kompletterande upplysningar** | Vägledning, exempel på regelverk/standarder, gapanalys | Inte bindande. Stöd vid ny-/ombyggnad |
| **IEC/ISO/SS-EN** | Teknisk standard | **Verifieringsverktyg** i nationell sjöfart (TSFS 2017:26 1 kap. 14 §). **I TSFS 2019:4 16 kap. 1 § är IEC 60092-serien däremot föreskriven** (konstruktion, tillverkning, underhåll ska ske enligt IEC 60092 *och* en erkänd organisations tillämpliga regler) |
| **Klassregler** | DNV, BV, LR, ABS, RINA m.fl. | Vanligt *sammanhållet regelverk* för verifiering; inte TS-föreskrift i sig |
| **Elsäkerhetsverkets föreskrifter** | Landel | Gäller **inte** på fartyg eller fritidsbåtar, **undantag:** EMC samt fritidsbåt upptagen på land (vinterförvaring/reparation) |

**Nationell sjöfart — verifieringskedjan (TSFS 2017:26):**

1. Funktionskrav i kap. 5 (och kap. 1–2) ska uppfyllas.
2. Redaren verifierar enligt 1 kap. 14 § genom (a) etablerat sammanhållet regelverk / vedertagen teknisk standard, (b) jämförande analys eller riskanalys, och/eller (c) empiri.
3. Allmänna råd: vid nybyggnad och omfattande ombyggnad bör senaste lydelse av relevant standard/regelverk användas.
4. Dokumentera valt regelverk och gapanalys mot varje paragraf i 5 kap. (1 kap. 27 §; kompletterande upplysningar till 5 kap.).
5. Installatörsintyg om tillämpad standard ingår i fartygets dokumentation (TS-vägledning; allmänt råd i kompletterande upplysningar).

**Internationell sjöfart — mer preskriptivt:** TSFS 2019:4 *motsvarar SOLAS 74 kap. II-1 del A och C–E*. Där är IEC 60092 (och för Ex IEC 60079 / IEC 60092-502) införd som **ska**-krav i vissa paragrafer, inte bara som verifieringsstöd.

**Källor till distinktionen**

- [TS: Elinstallationer](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/) — IMO ger övergripande krav; IEC ger detaljkrav. TSFS 2017:26 är *heltäckande, funktionsbaserad*.
- [TS: Regler för nationell sjöfart](https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/) — tre nivåer: regler / allmänna råd / kompletterande upplysningar.
- [TS: 5 kap. kompletterande upplysningar](https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/) — verifieringssteg, gapanalys, dokumentation.
- TSFS 2017:26 1 kap. 13–14, 27 §§ och 5 kap. (konsoliderad: `https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf`).
- TSFS 2019:4 1 kap. 1 § och 16 kap. 1 § (`https://www.transportstyrelsen.se/TSFS/TSFS%202019_4.pdf`).

---

## A. Regelträd IMO / IEC / ISO i svensk TS-kontext

Svensk utgivning: **SIS** säljer/publicerar SS-EN. Elektrotekniska SS-EN IEC tas fram av **SEK Svensk Elstandard** (anges som "Framtagen av" på SIS-produktsidor). Köp/katalog: sis.se. **Ingen standardtext återges här.**

### A.1 Bindande lager (lag / förordning / TSFS)

```
IMO SOLAS kap. II-1 (särskilt Part D Electrical installations, reglerna 40–45 m.fl.)
        │  införd i svensk rätt för fartyg med internationellt säkerhetscertifikat
        ▼
TSFS 2019:4  — maskininstallation, elektrisk installation, UMS
  16–22 kap. = elektrisk installation (motsvarar SOLAS II-1 del A och C–E)
  16 kap. 1 §  SKA: konstruktion, tillverkning, underhåll enligt IEC 60092 + erkänd organisation
  22 kap.      skyddsåtgärder mot elchock, brand m.m.
        │
        ├── IEC 60092-serien          (föreskriven i 16 kap. 1 §)
        ├── IEC 60092-502             (tankfartyg / riskområden; SOLAS II-1/45.11)
        └── IEC 60079-serien          (Ex-utrustning; 22 kap. 25–26 §§)

IMO MSC-cirkulär som TS *faktiskt citerar* i landströmsföreskriften:
  • MSC.1/Circ.1675   — drift av OPS (allmänt råd i TSFS 2024:58 14 §)
  • MSC.1/Circ.1212/Rev.1 — alternativ design SOLAS II-1 och III (TSFS 2024:58 25 §)

Nationell sjöfart (ej internationellt certifikat, ej EU-passagerardirektiv 2009/45, ej inland):
        ▼
TSFS 2017:26  — funktionsbaserad
  5 kap. elektrisk utrustning och elinstallationer
  5 kap. 7 § landnät (retroaktivt senast 2020-04-01 enligt TS-sidan)

Inrikes passagerarfartyg enligt direktiv 2009/45/EG:
        ▼
TSFS 2019:120  — passagerarfartyg på inrikes resa
  Originaltryck 2019: bilaga kapitel II-1 **Del C – Elektrisk installation**
  Konsoliderad 2019:120k (t.o.m. TSFS 2025:63): huvudtexten hänvisar till
  dir. 2009/45/EG bilaga I i stället för att återtrycka hela bilagan.
  4 §: erkänd organisations regler om skrov, maskineri **och elektrisk installation**.
  Gäller L ≥ 24 m (och HSC oavsett L) på inrikes resa.
  Gäller **inte** inland, **inte** enbart fartområde E, **inte** örlog/segel/trä/traditionsfartyg m.m. (2 §).

Inland / inre vattenvägar:
        ▼
Direktiv (EU) 2016/1629 + ES-TRIN (CESNI)
        ▼
TSFS 2026:20  (i kraft 2026-05-01; upphäver TSFS 2018:60)
  11 § huvud-/nödkraft zon 1–2
  12 § landström → hänvisning till AFIR (EU) 2023/1804
  Tekniska detaljer i direktivets bilaga II / ES-TRIN kap. 10 (el)

Landström (fartygssidan, svenska fartyg som *inte* är nationella/inland/fritid):
        ▼
TSFS 2024:58  (i kraft 2024-11-01) + TSFS 2026:44 (i kraft 2026-05-01, definitionsändring inland)
  SJÖFS 2008:82 upphävd genom TSFS 2024:59 samma dag
```

### A.2 Standarder — var de sitter (bindande vs verifiering)

**Viktigt om årtal:** TS-sidor anger ofta *serie* utan utgåveår, eller ett visst år. IEC-katalogens aktuella samlingspaket kan vara nyare. I nationell sjöfart gäller den utgåva som redaren *valt och dokumenterat* för verifiering (normalt senaste vid nybyggnad). I TSFS 2019:4 kan fotnoter peka på "den lydelse som var i kraft då anläggningen installerades" (äldre fartyg). **Kontrollera alltid mot den utgåva TS/redaren faktiskt åberopar.**

| Standard | Vad den täcker (katalogtitel, inget innehåll) | TS-användning | Bindande / verifiering | Aktuellt katalogår (2026-08, *inte* TS-antaget år) | Svensk utgåva (SIS) |
|---|---|---|---|---|---|
| **IEC 60092-serien** | Electrical installations in ships (alla delar). TC 18. | TS: "godkänd av IMO", avsedd för all elektrisk utrustning på fartyg. TSFS 2019:4 16 kap. 1 § *ska*. Nationell sjöfart: primärt verifieringsregelverk för L>24 m (kompletterande upplysningar pekar även på TSFS 2019:4 / klass). | **Bindande** för fartyg under TSFS 2019:4. **Verifiering** under TSFS 2017:26. | Samling **IEC 60092:2026 SER** (IEC webstore, 2026-07-10). Delar har olika år; bl.a. IEC 60092-507:2014, IEC 60092-504:2026, IEC 60092-502:1999 (5th) | Delar som SS-IEC / SS-EN via SIS/SEK |
| **IEC 60092-507** | Small vessels (längd upp till 50 m *eller* GT ≤ 500; trefas AC ≤ 500 V). | TS listar **SS EN 60092–507 (små fartyg)**. Kompletterande upplysningar: landanslutning systemspänning upp till 500 V trefas. | Verifiering (små fartyg / trefas). TS varnar: CE-fritidsbåtsstandarder är normalt *inte* lämpliga för passagerarfartyg. | IEC 60092-507:**2014** (i 2026 SER-paketet) | **SS-EN 60092-507** utg. 2, fastställd 2015-03-11 (EN 60092-507:2015). SEK. [SIS](https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ssen600925072/) |
| **IEC 60079-serien** | Explosive atmospheres. | TS: IMO-godkänd, elektrisk utrustning för explosiva atmosfärer. TSFS 2019:4 22 kap. 25 § p. 4 *ska* uppfylla relevant del av IEC 60079. Tankfartyg 2007–: IEC 60092-502 *eller likvärdig*. | **Bindande** i TSFS 2019:4 för Ex-utrymmen. Nationell: kompletterande upplysningar (EX i tabell, tank/ro-ro). | Samling **IEC 60079:2026 SER** (2026-07-23). IEC 60079-0:**2026** (ed. 8.0, 2026-06-16) | SS-EN IEC 60079-delar via SIS/SEK |
| **IEC 60533** | EMC, ships with metallic hull. Katalogtext (IEC, inte TS): stöd för SOLAS kap. IV reg. 6 och kap. V reg. 17; IMO res. A.813(19). | TS: EMC-standard för fartyg. EMC är *lagreglerad*; Elsäkerhetsverket föreskriver (ELSÄK-FS 2016:3) även för fartyg. Kompletterande upplysningar 5 kap.: "i första hand" IEC 60533:2015. | **EMC-krav bindande via ELSÄK-FS**; IEC 60533 är den marina *verifieringsstandarden* TS pekar på. Inte en TSFS-paragraf med "ska enligt IEC 60533". | **IEC 60533:2015** (ed. 3.0, 2015-08-25; IEC anger stability date 2026; ed. 4 under development, forecast 2026-12-25) | SS-EN 60533 / motsv. via SIS/SEK (SIS-produktsida ej hämtad) |
| **IEC/IEEE 80005-1** | HVSC, högspänningslandström, allmänna fordringar. | TS krav-sida: IEC/IEEE 80005-1:**2019**. TSFS 2024:58 3 §: ytterligare HV-bestämmelser i **AFIR (EU) 2023/1804**. Kompletterande upplysningar: "lämpligt" IEC/IEEE 80005-1:2019; *samma sida listar även den äldre* ISO/IEC/IEEE 80005-1:**2012** — se gap. | HV: AFIR är bindande EU-förordning. 80005-1 är den tekniska standard TS/AFIR pekar mot — **inte** införd som "ska IEC/IEEE 80005-1" i TSFS 2024:58:s huvudtext. Allmänt råd / kompletterande. | IEC/IEEE 80005-1:**2019** + AMD1:2022 + AMD2:2023 | **SS-EN IEC/IEEE 80005-1, utg 1:2026**, fastställd 2026-06-10, SEK. AMD1+AMD2 inarbetade. [SIS](https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ss-en-iecieee-80005-1-utg-12026/) |
| **IEC/IEEE 80005-2** | Data communication for HV/LV shore connection. | TSFS 2024:58 8 § allmänt råd: *bör* IEC/IEEE 80005-2:**2016**. TS lagar-sida samma år. | Allmänt råd (bör), inte ska. | **IEC/IEEE 80005-2:2016** (TS och katalog samstämmiga) | SS-EN IEC/IEEE 80005-2 via SIS/SEK |
| **IEC/IEEE 80005-3** (tidigare PAS) | LVSC lågspänningslandström. | TSFS 2024:58 3 § allmänt råd: *bör* **IEC/PAS 80005-3:2014**. TS lagar-sida: IEC PAS 80005-3:2014. Kompletterande upplysningar anger felaktigt/åldrat "IEC PAS 80005-3:**2019**". | Allmänt råd. Inland undantas i 80005-3:s egen scope (katalog). | **IEC/IEEE 80005-3:2025** (ed. 1.0, 2025-12-08) ersätter PAS 2014. TS har **inte** uppdaterat hänvisningen till 2025 i TSFS 2024:58. | Kontrollera SIS; svensk SS-EN kan släpa efter |
| **SS-EN ISO 13297** | Small craft electrical systems: DC ≤ 50 V och 1-fas AC ≤ 250 V. Trefas hänvisas till IEC 60092-507. Ersätter ISO 10133:2012 (DC). | TS lagar-sida: **SS-EN ISO 13297:2021** (båtar, elsystem, växel- och likström; ersätter ISO 10133:2012). | Verifiering för småbåt/fritid AC/DC. **Inte** TS:s rekommenderade verifiering för passagerarfartyg (CE-standarder "normalt inte lämpliga"). | ISO 13297:**2020**; EN ISO 13297:2021 + A1:2022 + A11:2023 | **SS-EN ISO 13297:2021** utg. 5, 2021-04-21, SIS/TK 232. [SIS](https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ss-en-iso-132972021/) |
| **IEC 60364-7-709** | Katalogtitel (IEC webstore): *Low-voltage electrical installations – Part 7-709: Requirements for special installations or locations – Marinas and similar locations*. | TSFS 2024:58 bilaga p. 15: för landanslutning ≤ 230 V *får* IEC 60364-7-709 tillämpas. Fotnot 14 i 2024:58 anger äldre titel och **"utgåva 1"**. Kompletterande upplysningar: landanslutningar ≤ 230 V. | Valfri tillämpning i bilaga till 2024:58 (äldre system). Landanläggning i övrigt är Elsäkerhetsverket — utanför fartygssidan. | IEC-katalog **2007+AMD1:2012 CSV** (ed. 2.1, 2012-03-26). Ed. 1.0 (1994) är *Revised*. TS-fotnoten "utgåva 1" stämmer alltså **inte** mot aktuell katalogutgåva. | SS-EN 60364-7-709 via SIS/SEK |
| **IEC 60309** | Industriuttagsdon. | TSFS 2024:58: anslutningsdon lågspänning *bör* IEC 60309-1; bilaga: SS-EN 60309 i den lydelse som gällde vid installation. | Allmänt råd / bilaga för äldre system. | Namngiven; år enligt installationsdatum | SS-EN 60309 |
| **IEC 60529** | IP-kod. | TS minimikrav-sida: tabell "i enlighet med IEC 60529". **Tabellen återges inte här.** | TS-vägledning / kompletterande upplysningar, inte TSFS-tabell i 2017:26:s bindande text. | Namngiven av TS | SS-EN 60529 |

**IEC 60092-delar som TS faktiskt *namnger* (utan klausulcitat):**

- IEC 60092-350, -353, -360 — kablar (allmänna råd TSFS 2024:58 17 §)
- IEC 60092-502 — tankers special features (TSFS 2019:4; SOLAS II-1/45.11)
- IEC 60092-506 — ships carrying specific dangerous goods (allmänt råd i 2019:4-bilaga)
- IEC 60092-507 — små fartyg / LV landanslutning trefas (kompletterande upplysningar)

**IMO MSC-cirkulär — vad TS citerar vs vad som *finns* på IMO-nivå**

| Cirkulär | Ämne | TS-citat? |
|---|---|---|
| MSC.1/Circ.1675 | Interim guidelines on safe operation of OPS in port (internationell fart) | **Ja** — TSFS 2024:58 14 § allmänt råd |
| MSC.1/Circ.1212/Rev.1 | Alternative design SOLAS II-1 och III | **Ja** — TSFS 2024:58 25 § (likvärdighet) |
| MSC.1/Circ.1557/Rev.1 (2023-09-05) | Hazardous area classification, SOLAS II-1/45.11 vs IEC 60092-502:1999; IMO-instrument *går före* IEC vid konflikt | **Inte funnet** som uttryckligt TS-citat. TSFS 2019:4 26 § inför SOLAS II-1/45.11 via IEC 60092-502 "eller likvärdig" + TS-godkänd riskanalys. Cirkuläret är relevant IMO-kontext men ska inte påstås vara TS-hänvisat. |
| IMO res. A.813(19) | EMC | Nämns i IEC 60533:s katalogbeskrivning, inte i hämtad TS-text |

### A.3 Elsäkerhetsverket vs TS

Källa: [TS lagar, föreskrifter och standarder](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/)

> Elsäkerhetsverkets föreskrifter gäller varken på fartyg eller på fritidsbåtar, enda undantaget är elektromagnetisk kompatibilitet (EMC) och när fritidsbåtar har tagits upp på land för vinterförvaring eller för reparation.

ELSÄK-FS 2016:3 (EMC) nämns i kompletterande upplysningar till 5 kap.

### A.4 Installatörskompetens (TS-vägledning, inte elsäkerhetsbehörighet land)

[Krav för elektrisk installation på fartyg](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/) — *bör* utföras av fartygsingenjör, elektroingenjör, STCW-eltekniker, fartygselektriker, eller annan med dokumenterad marinkunskap (t.ex. marinens elutbildning); även varv/behörig elinstallatör *med kunskap om fartygsel*. **Intyg om tillämpad standard** bör utfärdas. Vid ombyggnad: *senaste* standard och regelverk.

TSFS 2019:4 16 kap. 2 § är skarpare (*ska* elteknisk bakgrund + intyg innan godkännande).

---

## B. Landström

### B.1 Bindande fartygssida

| Instrument | Tillämpning | Ikraft |
|---|---|---|
| **TSFS 2024:58** | System för landströmsförsörjning till *svenska fartyg*, system som tas i bruk fr.o.m. ikraft; äldre system vid *förnyelse*. Fartyg byggda 2001-01-01 eller senare: **bilagan** tills förnyelse. | 2024-11-01. PDF: `https://www.transportstyrelsen.se/TSFS/TSFS%202024_58.pdf` |
| **TSFS 2026:44** | Ändrar **endast 6 §** definitionen "fartyg i inlandssjöfart" från TSFS 2018:60 → **TSFS 2026:20**. Inga tekniska ändringar i 7–26 §§ eller bilagan. | 2026-05-01. PDF: `https://www.transportstyrelsen.se/TSFS/TSFS%202026_44.pdf` |
| **TSFS 2024:59** | Upphäver SJÖFS 2008:82 (äldre landanslutningsföreskrift) | 2024-11-01 |
| **TSFS 2017:26 5 kap. 7 §** | Nationell sjöfart: funktionskrav "tillfredsställande säkerhet" vid landnät. Retroaktivt enligt TS-sidan (senast 2020-04-01). | Gäller nationella fartyg; **2024:58 gäller inte** nationell sjöfart (2 §) |
| **AFIR (EU) 2023/1804** | Utbyggnad av infrastruktur för alternativa drivmedel. TSFS 2024:58 3 §: ytterligare HV-bestämmelser. TSFS 2026:20 12 §: inlandslandström följer AFIR. Ersätter dir. 2014/94/EU. Äldre TS-text nämner fortfarande SFS 2016:917 / "EU-förordning 2016:917". | Gällande EU-förordning |
| **FuelEU Maritime (EU) 2023/1805** | Skyldighet att *använda* OPS/nollemission vid kaj från 2030 för passagerar- och containerfartyg > 5 000 GT i AFIR-hamnar (2035 alla EU-hamnar med OPS). TS är behörig myndighet. | TS-sida: förordningen från 2025-01-01. [FuelEU Maritime — TS](https://www.transportstyrelsen.se/sv/sjofart/miljo-och-halsa/klimat-och-energi/fueleu-maritime/) |

**TSFS 2024:58 gäller inte** (2 §): (1) fartyg i nationell sjöfart, (2) inlandssjöfart, (3) fritidsfartyg, (4) Försvarsmakten, (5) övriga fartyg utom passagerarfartyg med skrovlängd < 15 m.

**Konsekvens:** Installatör på *nationellt* fartyg verifierar 2017:26 5 kap. 7 § (funktionskrav + allmänna råd + kompletterande upplysningar). TS kompletterande upplysningar listar TSFS 2024:58 som *tillämplig föreskrift* om redaren *vill* verifiera mot den — det är en verifieringsväg, inte automatisk tillämplighet. Bekräftas i [1 kap. kompletterande upplysningar](https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/allmanna-bestammelser/): 2024:58 gäller om redaren vid ny-/ombyggnad/inflaggning vill redovisa verifiering i linje med kap. 4–5 i 2017:26.

### B.2 Standardhänvisningar i TSFS 2024:58 (namn, inget innehåll)

- Lågspänning: *bör* IEC/PAS 80005-3:**2014** (allmänt råd 3 §). Katalog 2026: ersatt av IEC/IEEE 80005-3:**2025** — **TSFS inte uppdaterad**.
- Datakommunikation: *bör* IEC/IEEE 80005-2:**2016** (8 §).
- Isolertransformator: *bör* SS-EN IEC 61558-1 eller likvärdig (9 §). Bilaga äldre system: SS-EN 60742 i då gällande lydelse.
- Kablar: IEC 60092-350, 60092-360, 60092-353, IEC 60502-2 (allmänna råd).
- Don LV: IEC 60309-1 / SS-EN 60309.
- ≤ 230 V: IEC 60364-7-709 *får* tillämpas (bilaga p. 15).
- Drift: MSC.1/Circ.1675 (allmänt råd).
- HV: AFIR 2023/1804 (3 §); TS-vägledning i övrigt: IEC/IEEE 80005-1:2019.

### B.3 Installatörsskyldigheter — fartygssida (parafras av TSFS 2024:58, inte standardtext)

Följande är **föreskriftskrav** för system som omfattas av 2024:58 (nya/förnyade). Bilagan gäller dessutom befintliga system på fartyg byggda ≥ 2001 till dess förnyelse.

**Inlopp / anslutningscentral (ship-side inlet)**

- Anslutningscentral eller motsvarande för överföring av landström (15 §). Bilaga p. 1: central för *flexibel kabel från land*.
- Fast kabel till huvudeltavla, dimensionerad för märkström, skyddad mot mekanisk åverkan (16 §; bilaga p. 2).
- Automatisk brytare eller flerpolsbrytare med överströmsskydd (bilaga p. 3).
- Indikering när centralen är spänningssatt (16 §; bilaga p. 6). Allmänt råd: spänning, fasföljd, effekt, frekvens.
- Synlig information: normalt/max effektbehov vid kaj, nominell spänning, frekvens, rutiner för anslutning/frånkoppling/nöd; polaritet vid DC (11 §; bilaga p. 8).
- Kapslingsklass lämplig; skydd mot vatten (9 §; allmänt råd 15 §).
- Teknisk dokumentation för drift/underhåll/felsökning ska finnas vid tillsyn (24 §).

**Förregling / interlock**

- Galvanisk separation från landnätet; reläskydd eller motsvarande, åskskydd, automatisk fasföljdsomkoppling (9 §).
- 18 § / bilaga p. 4: omkopplingsbrytare **med förregling** så att strömförande kablar inte kopplas ihop; bryter alla faser; jordledaren får inte brytas av överströmsskydd.
- 17 §: åtgärder mot manövrering av spänningssatta don.
- 22 §: anslutning/frånkoppling vid nominell ström **> 63 A endast i spänningslöst läge**.
- 23 §: > 63 A — automatisk frånkoppling + larm vid onormal dragpåkänning på kabeln.
- 20–21 §§: fastställda rutiner för manuell anslutning; riskhantering för automatiska arrangemang.

**Jordning / earth**

- Jordningsskena till lämplig jord; hänsyn till galvanisk korrosion och vagabonderande strömmar (bilaga p. 5).
- Kontakt med **inbyggd jordförbindelse så att jordning sker innan spänningsbärande ledare sammankopplas** (bilaga p. 9) — jord-först.
- 9 §: galvanisk separation (allmänt råd: isolertransformator *ombord*).
- Jordledaren opåverkad av utlöst överströmsskydd (18 §; bilaga p. 4).

**Kompatibilitet**

- 8 §: fartygets system **ska vara kompatibelt** med det landbaserade elkraftsystemet; nödvändig kommunikation med minsta risk för driftstörning. EMC enligt förordning (2016:363).
- 10 §: anpassning till maximalt landströmsbehov, inkl. lastning/lossning.
- 7 §: riskhantering explosion, brand, gnist, kortslutning, ljusbåge, elchock, materiell skada, driftstörning; särskild hänsyn vatten/is och landjord (vagabonderande strömmar, galvanisk korrosion).
- 13 §: tankfartyg / förhöjd brand- eller explosionsrisk — särskild dokumenterad riskhantering; anslutning utan gnistbildning.

**JFB vs isolertransformator (landström, inte fartygsnätet)**

- Bilaga p. 13: märkström **≤ 125 A** — strömkännande JFB märkutlösning **högst 30 mA** *eller* isolertransformator. Allmänt råd: båda *bör* sitta ombord.
- Bilaga p. 12: **> 125 A** — fast anslutning i centralen, enbart för detta ändamål.
- Detta är **landströmsgränssnittet**. Det ska inte läsas som krav på JFB i fartygets isolerade driftnät (se avsnitt C).

**Nationell sjöfart (2017:26 5 kap. 7 § allmänna råd, parafras):** anslutningscentral anpassad till energibehov; fast don som mottagning för inkommande flexibel kabel; tydlig spänningsindikering; instruktioner vid centralen. Kompletterande upplysningar: undvik galvaniska/vagabonderande strömmar (isolertransformator, ICCP eller offeranoder); kabel dimensionerad, skyddad, inte upplindad; HV "lämpligt" IEC/IEEE 80005-1:2019.

### B.4 TS-sidor och riktlinjer (vägledning, inte TSFS)

- [Krav för elektrisk installation — landanslutning](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/)
- [Riktlinjer och rekommendationer för anslutningar av fartyg och fritidsbåtar till landbaserat elnät](https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/riktlinjer-och-rekommendationer-for-anslutningar-av-fartyg-och-fritidsbatar-till-landbaserat-elnat/) — utgiven 2015-04-20. **Äldre än 2024:58**; fortfarande länkad av TS. Fulltext inte utdragen (gap).
- [FuelEU Maritime](https://www.transportstyrelsen.se/sv/sjofart/miljo-och-halsa/klimat-och-energi/fueleu-maritime/) — TS nämner OPS-skyldighet 2030 tillsammans med AFIR. Inga IEC-klausuler.

---

## C. Olyckor och SMS-punkter

### C.1 TS-undersida (primär undervisningskälla)

**[Olyckor relaterade till elinstallationer ombord](https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/)** — publicerad 24 jan 2025.

TS: trots att installationer följt krav/standard och skötts av behörig personal kan livsfarlig ström uppstå. **Flera incidenter och enstaka dödsolyckor.** Orsak oftast *slitage*. TS uppmanar redare att lägga in **rutiner i SMS**.

**Undervisningspunkter (parafras, inte citatblock av hela sidan):**

1. **Ingen JFB på fartyg (oftast) / när den inte krävs**  
   Skillnad mot land: ombord har man **oftast inte jordfelsbrytare**, för att inte äventyra *driftsäkerheten* (vilket i sin tur kan äventyra personsäkerheten om kritisk utrustning slås ut). Personskydd vilar därför på: slitagekontroll, **intakt IP-klass**, korrekt eftermontage, jordfels*övervakning* (inte frånkoppling) på ojordade kretsar > 50 V (2017:26 5 kap. 5 § allmänt råd).  
   **När JFB *ändå* dyker upp i TS-material:**  
   - landström ≤ 125 A (TSFS 2024:58 bilaga p. 13: JFB ≤ 30 mA *eller* isolertransformator);  
   - TS:s IP-vägledningstabell anger "JFB" för *uttag i våtutrymmen* — se [Minimikrav för IP klass](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/) (tabellen återges inte; läs originalet).  
   Detta är *inte* ett generellt JFB-krav i fartygets isolerade huvudnät.

2. **IP-återställning efter arbete**  
   Utrustning öppnas för felsökning/reparation och återställs *inte* till ursprunglig täthet: packningar felplacerade/åldrade, kåpa/kabelgenomföring slarvigt återställd. Vatten (spolning, maskinrum) gör utrustningen ledande → elchock. SMS: återställ samma IP efter varje ingrepp.

3. **Flexibla kablar** (TS: främsta personskaderisk)  
   - Landanslutningskablar på mark/hårda ytor → skadat ytterhölje, vatten, kortslutning/elchock; anslutningspunkt vid elskåp utsatt för belastning.  
   - Ro-ro: matning till lastbilar/kylcontainers; fordon kan köra över kablar.  
   - Passagerarfartyg: mobila köksmaskiner på hjul — jordledare kan slitas av så höljet blir spänningsförande för besättning *och passagerare*.

4. **Arbete på höjd**  
   Elchock i sig inte alltid dödlig; **fallet** från stege/höjd ger de livsfarliga skadorna. Befälhavarens arbetsmiljöansvar; skyddsåtgärder mot fall. Hänvisning till fartygets arbetsmiljörutiner (TSFS 2019:56 / SJÖFS 2005:25 nämns i 2024:58 4 §).

**SMS-krav enligt TS-sidan:** rutinbeskrivningar för återkommande kontroll av flexibla kablar, kabelgenomföringar, elskåp och kopplingsboxar; slitna delar byts/återställs i tid; ingå i säkerhetsmanualen.

Relaterade TS-sidor: [Elinstallationer](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/), [Minimikrav för IP klass](https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/).

**ON TS (olyckor-undersidan, 2025-01-24) — inte gap:**

| Undervisningspunkt | På TS olyckor-sida? |
|---|---|
| Oftast **ingen JFB** ombord (driftsäkerhet) | **JA** |
| **IP-återställning** efter öppning/arbete (packning, kåpa, kabelanslutning) | **JA** |
| **Flexibla kablar** (land, ro-ro-fordon, rullande kök; jordledare) | **JA** |
| **Arbete på höjd**/stege: elchock + fall | **JA** |
| SMS-rutiner för återkommande kontroll | **JA** |
| Namngivna fartyg, diarienummer, SHK-rapport | **NEJ — GAP** |
| Koppling till SHK 2024:04 / Germanica | **NEJ — GAP** (sidan talar om "enstaka dödsolyckor" utan namn) |

**Ingen namngiven TS-olycksrapport med diarienummer** hittades bakom denna undersida — den är en syntes av "incidentrapporter som myndigheten hittills har fått".

### C.2 SHK — marin el, namngiven rapport

**SHK 2024:04** — *Personolycka ombord på ett ro-ro-fartyg på resa mellan Göteborg och Kiel*  
Diarium **S-150/22**. Händelse 27 juni 2022 (dödsfall) + 14 juli 2022 (elchock). STENA GERMANICA. Slutrapport 17 april 2024.

- Svensk sida: https://shk.se/sok-utredningar/sjofart/2023-04-13-personolycka-ombord-pa-ett-ro-ro-fartyg-pa-resa-mellan-goteborg-och-kiel  
- Engelsk sida: https://shk.se/engelska/the-swedish-accident-investigation-authority/search-investigation/maritime-transport/2023-11-08-fatal-accident-on-board-a-ro-ro-ship-on-route-gothenburg-kiel  
- PDF slutrapport: länk från SHK-sidan ("Slutrapport SHK 2024:04").

**Parafras av SHK:s sammanfattning (inte rapportens tekniska bilagor):**

Fartygsingenjör hittades livlös vid barlastpump i pannrum; antogs först naturlig död. Två veckor senare fick kollega kraftig stöt från våt magnetventil vid samma pump. Flera samverkande fel: packning mellan kontakt och spole saknades; **ingen skyddsjordning**; inkommande kablar skiftade så ventilen var spänningssatt hela tiden pumpen gick. Felen påverkade *inte* driften — därför ingen indikation till besättningen. Kretsen var **lokalt jordad (TT)** utanför det ordinarie **isolationsfelsövervakade** fartygsnätet; lokalt jordade system kan ge höga felströmmar mot skrov. Bakomliggande: elarbete av personer utan tillräcklig kunskap; brister kan ha funnits redan vid nybyggnad.

**Rekommendationer:**  
- Rederi: familiarisering (kortare utryckningstid); rutin att konsultera ilandsjukvård vid *varje* stöt/strömgenomgång.  
- **TS:** i tillsynen uppmärksamma felaktigt utförda elarbeten; endast personer med kunskap om el *och fartygets särskilda elsystem* ska utföra elarbete.

Koppling till SMS/Elon-punkter: kompetens (samma som TS krav-sida och 2019:4 16 kap. 2 §); jordning; fukt/IP (packning); isolationsövervakning *täcker inte* sidokretsar som lagts som lokalt jordade.

**RS 2016:03** — *Tillbud till sjöss utanför Travemünde med passagerarfartyget FINNTRADER*  
Diarium **S-35/14**. Händelse 10 mars 2014. Slutrapport 13 april 2016.

- Svensk sida: https://shk.se/sok-utredningar/sjofart/2015-02-05-tillbud-till-sjoss-utanfor-travemunde-med-passagerarfartyget-finntrader
- PDF: länk "Slutrapport RS 2016:03" på samma sida.

**Parafras (SHK-sidan, inte rapportens tekniska bilagor):** driftstörning i maskinkontrollsystemet nära totalt strömbortfall (black out) med lots ombord. Mellanbrytare mellan axelgenerator och kraftnät gav inte positionssignal; generatorautomatiken försökte lägga last på generator som inte var inkopplad på samma nät → frekvensfall, höga strömmar, oväsentlig last löste ut. Ett av flera liknande tillbud under 14 månader; SHK tittade på hantering hos myndigheter och klass. **Inte** strömgenomgång/elchock — elkraftautomatik/blackout.

**Andra SHK-sjöutredningar där el *berörs* men inte är elolycka i TS-mening:**

- **RS 2014:09** ÄLV-SNABBEN 5 / STENA GERMANICA (S-109/13): kollision; bruten strömförsörjning till manöverspakar enligt samtida sjöfartspress. Primärt navigations-/manöverhändelse. https://shk.se/sok-utredningar/sjofart/2015-02-05-kollision-mellan-passagerarfartygen-alv-snabben-5-och-stena-germanica-i-goteborgs-hamn
- **S-236/22** STENA SCANDICA: bildäcksbrand (DMAIB-ledd); elsystem och manöverförmåga påverkades. Inte elinstallationsolycka. https://shk.se/sok-utredningar/sjofart/2022-09-14-brand-ombord-pa-passagerarfartyget-stena-scandica
- **SHK 2024:16** ROERBORG fallolycka Oxelösund: arbete på höjd, **inte** el. **GAP mot TS-punkten "arbete på höjd + el"** — ingen namngiven SHK-rapport som kombinerar elchock och fall från stege identifierades.

Gap: systematisk genomgång av hela SHK sjö-arkiv inte gjord. TS olyckor-sida nämner **inte** rapportnumren ovan.

### C.3 SMS-checklista (källa + punkt)

| SMS-punkt | Primärkälla |
|---|---|
| Inga JFB i isolerat fartygsnät (driftsäkerhet); jordfels*övervakning* i stället | TS olyckor-sida; 2017:26 5 kap. 5 § allmänt råd |
| JFB/isolertransformator vid landström ≤ 125 A | TSFS 2024:58 bilaga p. 13 |
| Återställ IP efter varje öppning; packningar, kåpor, genomföringar | TS olyckor-sida; IP-sida IEC 60529-tabell |
| Flexibla kablar: land, ro-ro-fordon, rullande kök — jordledare, nötning, inte upplindade | TS olyckor-sida; 2024:58 19 § / bilaga p. 11 |
| Arbete på höjd + el: fallskydd, befälhavaransvar | TS olyckor-sida |
| Endast personal med fartygsel-kompetens; intyg om standard | TS krav-sida; TSFS 2019:4 16 kap. 2 §; SHK 2024:04 R till TS |
| Sidokretsar utanför isolationsövervakning (lokalt jordade TT) | SHK 2024:04 |
| Generatorautomatik / positionssignal / blackout-risk | RS 2016:03 FINNTRADER |
| Elchock → kontakt med sjukvård iland | SHK 2024:04 R till rederi |
| EMC / LED / trådlöst vs radio | TS krav-sida; IEC 60533; ELSÄK-FS 2016:3 |
| Megger/isolationsprov i underhållssystem | Kompletterande upplysningar 5 kap. (intervall som *exempel*, inte föreskrift) |

---

## D. Inland vs kust/nationell vs internationell — tillämplighet

Källor räcker för en **översiktstabell**. Den är inte en komplett certifikatsmatris; redaren avgör via fartygssäkerhetslagen + aktuell TSFS.

### D.1 Fartområden A–E (kust/nationell, *inte* inlandszoner)

Definitioner i **fartygssäkerhetsförordningen (2003:438)**. TS-utläggning: [Fartygets konstruktion och utrustning / fartområden](https://www.transportstyrelsen.se/sv/sjofart/sjotrafik-och-hamnar/fartomraden/fartygets-konstruktion-och-utrustning/). Koordinater C–E: TSFS 2009:8.

| Fartområde | Kort (enligt FSF 2003:438 / TS-sida) |
|---|---|
| **E** | Hamnar, floder, kanaler, insjöar, skyddad skärgård; signifikanta vågor i regel ≤ 0,5 m. Insjöar = E utom Vänern och Vättern (TS-sida). |
| **D** | Signifikant våg > 1,5 m med < 10 % sannolikhet; högst **3 nm** från strandlinjen |
| **C** | Signifikant våg > 2,5 m med < 10 %; högst **5 nm** |
| **B** | Utanför C–E, högst **20 nm** från strandlinjen |
| **A** | Mer vidsträckt än B. TS certifierar underområden A, A(50), A(100), A(250) = max nm till skyddad plats; enbart "A" = obegränsad |

**Eurofins Work Boat Guidelines A–D vs fartområde A–E** — tabell *på* kompletterande upplysningar till 5 kap. (TS: allmän rekommendation, inte 1:1; annat kan vara mer ändamålsenligt i enskilda fall):

| Konstruktionskategori (Eurofins A–D) | Fartområde (TS A–E) |
|---|---|
| A | **B** |
| B | **C** |
| C | **D** |
| D | **E** |

**Observera:** Eurofins har fyra nivåer; TS har fem fartområden. **Fartområde A saknar motpart i tabellen.** Indelningen "stämmer inte helt överens" (TS:s egna ord). Nödkraftdriftstid i samma upplysningar varierar med fartområde och om passagerare / L ≷ 24 m (vägledning, inte 2017:26-tabell i bindande text).

### D.2 Regelval efter trafikslag (el)

| Trafik / certifikat | Typisk el-TSFS | Standardroll | Längd / passagerare / område |
|---|---|---|---|
| **Internationellt säkerhetscertifikat** (SOLAS) | **TSFS 2019:4** 16–22 kap. "gäller för fartyg som omfattas av krav på internationellt säkerhetscertifikat" (1 kap. 1 §). Motsvarar SOLAS II-1 del A, C–E. | IEC 60092 **ska** (16 kap. 1 §). IEC 60079 / 60092-502 i Ex. Landström: **TSFS 2024:58** om svensk och inte undantagen. | SOLAS-trösklar (passagerarfartyg; lastfartyg i praktiken ≥ 500 GT m.m. — detalj i SOLAS/FSF, inte omverifierad klausul för klausul här) |
| **Inrikes passagerarfartyg dir. 2009/45/EG** | **TSFS 2019:120**. TS lagar-sida säger "del C". Originalbilagan kap. II-1 Del C: tre funktionskrav (normal drift utan nöd; nödelfunktioner; skydd mot elolyckor), huvudkraftkälla/belysning, nödkraftkälla (tider 12/6/3 h för klass B/C/D), extra nödbelysning ro-ro, skyddsåtgärder mot stöt/brand (jordning, isolationsövervakning, flamhämmande kablar, kretskydd, batterirum). **Inga IEC-klausulnummer i Del C.** 4 § kräver dessutom erkänd organisations elregler. Undantagna från 2017:26. | EU-passagerarnormer (preskriptiva) + klassregler för el; IEC inte införd som ska-lista i 2019:120. | L ≥ 24 m (HSC oavsett). Klass A–D enligt direktivet (kopplade till fartområde). **Inte** inland (2 § 8). **Inte** enbart E (2 § 9). |
| **Nationell yrkestrafik** | **TSFS 2017:26** funktionsbaserad. Gäller svenska **passagerarfartyg oavsett skrovlängd** och **övriga svenska fartyg L ≥ 5 m** (1 kap. 2 §). Undantar internat. certifikat, 2009/45, fisk ≥ 24 m (97/70/EG), fritid ≤ 24 m, inland, örlog. | Standard = **verifiering** (1 kap. 14 §). Kompletterande upplysningar: L 5–15 m / 15–24 m / > 24 m olika exempelregelverk (klass, Eurofins, Nordisk båtstandard < 15 m, TSFS 2019:4 som *exempel* för > 24 m). | Fartområde A–E i certifikat. 5 kap. 4 § nödutrustning: passagerare alla L; övriga L ≥ 15 m. Huvudkraft två aggregat (allmänt råd): nya, L > 24 m, ej fritid |
| **Fisk ≥ 24 m** | **SJÖFS 1999:27** del C (TS lagar-sida); undantagna 2017:26 | Harmoniserade fiskeregler | L ≥ 24 m |
| **Inland / inre vattenvägar** | **TSFS 2026:20** (fr.o.m. 2026-05-01; ersätter 2018:60). Genomför dir. **2016/1629**. Teknisk minimistandard i bilaga II = **ES-TRIN** (CESNI). El: ES-TRIN **kapitel 10** (Electrical equipment and installations), inkl. art. 10.08 shore connection. | ES-TRIN är den harmoniserade *tekniska* normen via direktivet — mer preskriptiv än 2017:26. IEC 60092 är inte TS:s inlandshuvudspår. IEC/IEEE 80005-3:2025 **undantar** inland navigation vessels i sin scope. | Unionscertifikat: passagerarfartyg; bogserfartyg; andra med **L ≥ 20 m** *eller* L×B×T ≥ 100 m³ (fartygssäkerhetslagen, TS inland-sida). Zon **1–4** (våghöjd), *inte* A–E. Sverige: inledningsvis Göta älv, Vänern, Mälaren. **Frivilligt** på svenska inre vatten — redaren kan välja nationell certifiering istället. 2026:20 11 §: zon 1–2 ska ha huvudkraft + oberoende nödkraft ≥ 3 h. 12 § landström → AFIR |
| **Fritid ≤ 24 m** | Inte 2017:26 (undantag). Recreational Craft / SS-EN ISO 13297; trefas → 60092-507. Elsäkerhetsverket när båten är på land. | Harmoniserade fritidsbåtsstandarder | Skrovlängd ≤ 24 m, ≤ 12 passagerare (TSFS 2024:58 def. fritidsfartyg) |

**Längdtrösklar som återkommer i el-sammanhang (nationell):**

| Tröskel | Var den sitter |
|---|---|
| L ≥ 5 m | 2017:26 tillämplig för icke-passagerare |
| L 5–15 / 15–24 / > 24 m | Kompletterande upplysningar: vilka *exempelregelverk* som kan verifiera |
| L ≥ 15 m | 5 kap. 4 § nödutrustning för icke-passagerare; brandavgränsning i allmänna råd |
| L > 24 m | Två huvudaggregat och självständig nödkraft (allmänna råd); TSFS 2019:4 som exempelregelverk |
| Passagerare > 12 | Passagerarfartyg (FSF/fartygssäkerhetslagen); 2017:26 oavsett L |
| Inland L ≥ 20 m eller 100 m³ | Unionscertifikatplikt (utöver passagerar- och bogserfartyg) |

### D.3 Inland vs 2017:26 — el

TS inland-sida (hämtad 2026-08-28) nämnde fortfarande TSFS **2018:60** som konstruktionsföreskrift — **inaktuellt** efter 2026-05-01. Gällande: [Regler för fartyg i inlandssjöfart](https://www.transportstyrelsen.se/sv/sjofart/fartyg/fartyg-i-inlandssjofart-inre-vattenvagar/regler-for-fartyg-i-inlandssjofart/) pekar på **TSFS 2026:20**. Nytrycksinfo: https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/information-om-nya-eller-andrade-regler/nya-foreskrifter-om-transportstyrelsens-foreskrifter-om-fartyg-i-inlandssjofart/

**Inlandsspecifika elregler i TSFS (svensk text, inte ES-TRIN-citat):**

- **TSFS 2018:60 13 §** (upphävd 2026-05-01): zon 1 eller 2 ska ha oberoende huvud- och nödkraftkälla; normal drift utan nöd; nöd utformad enligt dir. 2016/1629 bilaga II (passagerarfartyg) med kapacitet **minst tre timmar**.
- **TSFS 2026:20 11 §** (gällande): samma kärna — huvudkraft + oberoende nöd; nöd enligt dir. 2016/1629 bilaga II (passagerarfartygskrav); nöd ≥ 3 h; normal utrustning utan nöd.
- **TSFS 2026:20 12 §:** landström följer **AFIR (EU) 2023/1804** (inte TSFS 2024:58 — inland undantas i 2024:58 2 §).
- Övrig elteknik: **inte utskriven** i 2026:20; följer av dir. 2016/1629 **bilaga II** = ES-TRIN.

ES-TRIN 2025/1 (CESNI PDF, engelsk) har kapitel 10 med bl.a. electricity supply, IP/ingress, explosion, earthing, voltages, distribution, **connection to the shore or other external networks (10.08)**, batteries, cables, EMC (10.21). **Ingen ES-TRIN-text återges.** Artikelnummer 10.08 är CESNI:s egen numrering, **inte** ett IEC-klausulnummer. https://www.cesni.eu/wp-content/uploads/2024/11/ES_TRIN_2025_signed_en.pdf

IEC/IEEE 80005-3:**2025** katalogscope **undantar inland navigation vessels** (IEC webstore 2025-12-08).

---

## Källförteckning (URL)

### Transportstyrelsen — el (levande)
- Hubb: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/
- Lagar/föreskrifter/standarder: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/
- Krav för elektrisk installation: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/
- Kabelinstallationer: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/kabelinstallationer/
- Minimikrav IP-klass: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-pa-inkapsling-for-olika-utrymmen/
- Batteriinstallationer: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/batteriinstallationer/
- **Olyckor relaterade till elinstallationer ombord:** https://www.transportstyrelsen.se/sv/sjofart/aktuell-information/olyckor-relaterad-till-elinstallationer-ombord/
- 5 kap. kompletterande upplysningar (Eurofins A–D vs fartområde A–E): https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/
- PDF-samling kompletterande upplysningar: https://www.transportstyrelsen.se/globalassets/global/sjofart/dokument/projekt-nationella-foreskrifter/kompletterande-upplysningar/kompletterande-upplysningar-till-tsfs-2017-26.pdf
- Inland regler: https://www.transportstyrelsen.se/sv/sjofart/fartyg/fartyg-i-inlandssjofart-inre-vattenvagar/regler-for-fartyg-i-inlandssjofart/
- TSFS 2026:20 nytryck: https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/information-om-nya-eller-andrade-regler/nya-foreskrifter-om-transportstyrelsens-foreskrifter-om-fartyg-i-inlandssjofart/

### TSFS PDF
- TSFS 2017:26k: https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf
- TSFS 2019:4: https://www.transportstyrelsen.se/TSFS/TSFS%202019_4.pdf
- TSFS 2019:120 (original, med Del C i bilaga): https://www.transportstyrelsen.se/TSFS/TSFS%202019_120.pdf
- TSFS 2019:120k: https://www.transportstyrelsen.se/TSFS/TSFS%202019_120k.pdf
- TSFS 2018:60 (upphävd 2026-05-01): https://www.transportstyrelsen.se/TSFS/TSFS%202018_60.pdf
- TSFS 2024:58: https://www.transportstyrelsen.se/TSFS/TSFS%202024_58.pdf
- TSFS 2026:44 (ändrar 2024:58 6 § inland-def.): https://www.transportstyrelsen.se/TSFS/TSFS%202026_44.pdf
- TSFS 2026:20: https://www.transportstyrelsen.se/TSFS/TSFS%202026_20.pdf
- Nummerordning 2024/2026: https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/forfattningssamling/ts-foreskrifter-i-nummerordning/2024/ respektive `.../2026/`

### Landström / FuelEU / inland / fartområde
- https://www.transportstyrelsen.se/sv/om-oss/publikationer-och-rapporter/publikationer/publikationer-inom-sjofart/fartyg/riktlinjer-och-rekommendationer-for-anslutningar-av-fartyg-och-fritidsbatar-till-landbaserat-elnat/
- https://www.transportstyrelsen.se/sv/sjofart/miljo-och-halsa/klimat-och-energi/fueleu-maritime/
- https://www.transportstyrelsen.se/sv/sjofart/fartyg/fartyg-i-inlandssjofart-inre-vattenvagar/inlandssjofart/
- https://www.transportstyrelsen.se/sv/sjofart/sjotrafik-och-hamnar/fartomraden/fartygets-konstruktion-och-utrustning/

### SHK (elrelaterade sjöutredningar)
- SHK 2024:04 STENA GERMANICA (S-150/22): https://shk.se/sok-utredningar/sjofart/2023-04-13-personolycka-ombord-pa-ett-ro-ro-fartyg-pa-resa-mellan-goteborg-och-kiel
- Engelsk sida samma ärende: https://shk.se/engelska/the-swedish-accident-investigation-authority/search-investigation/maritime-transport/2023-11-08-fatal-accident-on-board-a-ro-ro-ship-on-route-gothenburg-kiel
- RS 2016:03 FINNTRADER (S-35/14): https://shk.se/sok-utredningar/sjofart/2015-02-05-tillbud-till-sjoss-utanfor-travemunde-med-passagerarfartyget-finntrader
- RS 2014:09 ÄLV-SNABBEN 5 (S-109/13): https://shk.se/sok-utredningar/sjofart/2015-02-05-kollision-mellan-passagerarfartygen-alv-snabben-5-och-stena-germanica-i-goteborgs-hamn
- SHK sjöfart översikt: https://shk.se/utredningsomraden/sjofart
- TS-ingång SHK: https://www.transportstyrelsen.se/sv/sjofart/Olyckor-och-tillbud/Statens-Haverikommission/

### Katalog (årtal och titlar, inte innehåll — ingen standardtext)
- IEC 60092 SER (*Electrical installations in ships - ALL PARTS*, pack 2026-07-10): https://webstore.iec.ch/en/publication/62418
- IEC 60092-507:2014 (*Small vessels*): https://webstore.iec.ch/en/publication/709
- IEC 60092-101:2018 (*Definitions and general requirements*): https://webstore.iec.ch/en/publication/29989
- IEC 60079 SER (*Explosive atmospheres - ALL PARTS*, pack 2026-07-23): https://webstore.iec.ch/en/publication/62417
- IEC 60533:2015 bas (*Electrical and electronic installations in ships - EMC - Ships with a metallic hull*): https://webstore.iec.ch/en/publication/23161
- IEC 60533:2015 RLV: https://webstore.iec.ch/en/publication/23154
- IEC/IEEE 80005-1:2019 (*HVSC systems - General requirements*): https://webstore.iec.ch/en/publication/29485
- IEC/IEEE 80005-2:2016 (*Data communication for monitoring and control*): https://webstore.iec.ch/en/publication/25265
- IEC PAS 80005-3:2014 (*LVSC Systems - General requirements*, replaced): https://webstore.iec.ch/en/publication/7578
- IEC/IEEE 80005-3:2025 (*LVSC systems - General requirements*; scope undantar inland): https://webstore.iec.ch/en/publication/30632
- IEC 60364-7-709:2007+AMD1:2012 CSV (*Marinas and similar locations*): https://webstore.iec.ch/en/publication/1897
- SIS SS-EN ISO 13297:2021: https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ss-en-iso-132972021/
- SIS SS-EN 60092-507 (hämtning timeout 2026-08-28; URL enligt SIS-sök): https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ssen600925072/
- SIS SS-EN IEC/IEEE 80005-1 utg. 1:2026: https://www.sis.se/produkter/skeppbyggnadteknik-och-marina-konstruktioner/allmant/elinstallationer-i-fartyg-och-marina-konstruktioner/ss-en-iecieee-80005-1-utg-12026/
- ES-TRIN: https://www.cesni.eu/en/technical-requirements/

---

## Gap (medvetet ofullständigt)

1. **TSFS 2019:120 Del C** är nu parafraserad från originaltryckets bilaga (kap. II-1 Del C). Konsoliderad 2019:120k återtrycker inte hela bilagan — läs original-PDF för Del C. **SJÖFS 2002:17 del D** och **SJÖFS 1999:27 del C** (fisk ≥ 24 m) är listade på TS lagar-sida men **inte utdragna** (GAP).
2. **MSC.1/Circ.1557/Rev.1** (SOLAS II-1/45.11 vs IEC 60092-502) är IMO-primärkälla men **inte återfunnen som TS-citat**. Påstå inte att TS "tillämpar cirkuläret".
3. **Kompletterande upplysningar** blandar årtal för 80005 (2012 / PAS 2016 / PAS 2019). TSFS 2024:58 säger PAS 80005-3:**2014**. Katalog 2026: IEC/IEEE 80005-3:**2025**. Tre motstridiga TS-åldrar — redaren måste välja och dokumentera.
4. **IEC 60092:2026 SER** är samlingspaket; TSFS 2019:4 16 kap. 1 § säger "IEC 60092" utan utgåveår. För *befintliga* anläggningar kan fotnoter peka på lydelsen vid installation. **Påstå inte att 2026-serien är retroaktivt bindande.**
5. **TS landströmsriktlinje 2015** fulltext inte utdragen; kan avvika från 2024:58.
6. **TS olyckor-sida namnger inga rapporter.** SHK 2024:04 (elchock/dödsfall) och RS 2016:03 (blackout-automatik) är SHK-primärkällor, inte TS-citat. Flexibla kablar / IP-återställning / arbete på höjd+el saknar **egna** SHK-rapportnummer i denna sökning (**GAP mot de tre TS-undervisningspunkterna utöver JFB**).
7. **ES-TRIN kap. 10** svensk implementering via dir. 2016/1629 bilaga II — TSFS 2026:20 skriver inte ut elkapitlet. Inlandssidan hos TS var delvis eftersläpande (2018:60).
8. **IEC 60364-7-709:** katalog 2007+AMD1:2012 (ed. 2.1). TSFS 2024:58 fotnot 14 säger "utgåva 1" och äldre titel (*Electrical installations of buildings … Marinas and pleasure craft*). **Årtals-/titelkonflikt TS vs katalog.**
9. **SS-EN 60533** SIS-produktsida inte hämtad; IEC 60533:2015 är katalogårets källa.
10. **IP-tabellen** hos TS är vägledning kopplad till IEC 60529 — **kopiera inte in tabellen i utbildningsmaterial utan att kolla originalet**; värden ska inte "minnas".
11. **FuelEU/AFIR** handlar om *användning* och *hamninfrastruktur*, inte om IEC-klausuler för fartygsinstallatören. TSFS 2024:58 kopplar HV till AFIR men inte till FuelEU i föreskriftstexten.
12. Klassreglers elkapitel (DNV GL ST-0342 m.fl.) namnges som *exempel* i kompletterande upplysningar; innehåll inte hämtat.

---

*Dokumentet är ett källpack, inte rättsutlåtande. Vid konflikt: tryckt TSFS > konsoliderad elektronisk utgåva > kompletterande upplysningar > standardkatalogår.*
