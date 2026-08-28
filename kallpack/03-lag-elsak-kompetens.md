# 03 — Lag, ELSÄK-undantag, TSFS-tillämpning och kompetens

**Status:** källpack (primärkällor). Inga påhittade citat. Parafras, inte avskrift av hela författningar.
**Hämtat:** 28 augusti 2026 (UTC+7).
**Urval:** riksdagen.se/SFS, elsakerhetsverket.se, regeringen.se, transportstyrelsen.se. PDF:er i `/workspace/kallpack/` och `src/`.
**Inte gjort om:** TSFS 2017:26 5 kap. 1–7 § installationskarta.

---

## Sammanfattning (det som efterfrågades)

### TSFS-tillämpning — en rad vardera

| Föreskrift | Vem den gäller (enligt 1 § / undantag i samma författning) |
|---|---|
| **TSFS 2019:4** | Fartyg med krav på **internationellt säkerhetscertifikat**; utländska i den utsträckning internationella regelverk kräver. El: 16–22 kap. för fartyg byggda 1986-07-01 eller senare (äldre: bilaga 2). PDF: `https://www.transportstyrelsen.se/TSFS/TSFS%202019_4.pdf` |
| **TSFS 2017:26** | **Svenska passagerarfartyg oavsett skrovlängd** + övriga **svenska fartyg med skrov ≥ 5 m**. Gäller **inte**: internationellt säkerhetscertifikat; dir. 2009/45/EG; fiskedir. 97/70 (≥24 m); fritid ≤24 m; existerande fritid brutto <100; **inland**; örlog. Konsoliderad t.o.m. TSFS 2026:9: `https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf` |
| **TSFS 2019:120** | Passagerarfartyg **skrov ≥ 24 m** och höghastighetspassagerarfartyg **oavsett längd**, på **inrikes resa**. Inte: örlog, segel, ej mekaniskt, enkel trä, traditions, försörjning, tender (ej HSC), inland, **enbart fartområde E**, icke-stål (utom HSC). TS lagsida pekar på **del C** för el. Konsoliderad t.o.m. TSFS 2025:63. |
| **TSFS 2018:60** | Inland / unionscertifikat (dir. (EU) 2016/1629). **Upphävd 2026-05-01** av TSFS 2026:20. |
| **TSFS 2026:20** | Ersätter 2018:60 från **1 maj 2026**. Fartyg som vid trafik på inre vattenvägar ska ha **unionscertifikat** (eller Rhencertifikat art. 22); även frivilligt unionscertifikat enligt FSF 3 kap. 4 a §. El: zon 1–2 ska ha huvudkraft + oberoende nödkraft (≥ 3 h, passagerarkrav i ES-TRIN/bilaga II); landström via AFIR (EU) 2023/1804 (12 §). |
| **TSFS 2024:58** | **Landström till svenska fartyg**, system som tas i bruk från ikraftträdandet (äldre: vid förnyelse). Gäller **inte**: nationell sjöfart; inland; fritid; Försvarsmakten/militärt befäl; övriga (utom passagerare) skrov **< 15 m**. |
| **TSFS 2026:9** | Ändrar 2017:26 **1 kap. 9, 9 a, 10, 28 §§** (ISM/SMS-hänvisning, allmänna råd till 28 § tas bort). Ikraft **1 mars 2026**. **Ändrar inte kap. 5 eller landström.** |
| **TSFS 2026:37** | Ändrar 2017:26 **1 kap. 11 §** definitionen ”fartyg i inlandssjöfart” → **TSFS 2026:20**. Ikraft **1 maj 2026**. Inte elteknik. |
| **TSFS 2026:44** | Ändrar **2024:58 6 §** samma inland-definition → TSFS 2026:20. Ikraft **1 maj 2026**. **Ändrar inte landströmkraven i sak.** |
| **TSFS 2019:59 / 2021:101** | Ändringar i 2019:4 (maskin/länsa/nöd-36 h m.m.). Inte tillämpningsområde. |
| **TSFS 2024:59** | Upphäver SJÖFS 2008:82 (äldre landanslutning) från **1 nov 2024**. |

### ELSÄK — citat med paragraf (inte utan URL)

| Påstående | Primärkälla | Paragraf |
|---|---|---|
| Elarbete på **fartyg** omfattas **inte** av elsäkerhetslagen | Elsäkerhetsverket FAQ (granskad 2024-06-24): https://www.elsakerhetsverket.se/fragor-och-svar/arkiv-fragor/omfattas-elarbete-pa-fordon-av-elsakerhetslagen/ + **prop. 2015/16:163 s. 20 ff.** | Inte en lagparagraf — avgränsning via definitionen av elinstallationsarbete (lagen **4 §**). Lagen **räknar inte upp** fartyg. |
| Gällande starkströmsföreskrift **2026** | **ELSÄK-FS 2022:1** (gäller från 2022-12-01; upphäver 2008:1). PDF: https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2022-1.pdf — **1 kap. 1–2 §§**: utförande = elinstallationsarbete enligt **elsäkerhetslagen 4 §**; omfattar starkströmsanläggningar enligt **lagen 3 §**. **Ingen fartygsmening.** 1 kap. 4 § = ELSÄK får medge undantag (dispens), inte ett fartygsundantag. | 1 kap. 1–2 §§ |
| Uttryckligt ”gäller inte fartyg, inklusive fritidsbåtar” | **ELSÄK-FS 2008:1 2 §** — **upphävd** 2022-12-01. Historisk. PDF: https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2008-1-konsoliderad.pdf | 2 § (ej gällande) |
| EMC **gäller utrustning; fartyg inte undantagna** | **ELSÄK-FS 2016:3** 1 kap. 1 § (ändrad 2016:4). Konsoliderad: https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2016-3-konsoliderad.pdf — undantag: RED/radioutrustning, luftfartsprodukter, radioamatör (ej på marknaden), låg emissions-/immunitetsrelevans, R&D-byggsatser. **Fartyg står inte på listan.** 1 kap. 2 §: lex specialis om annan unionslagstiftning specificerar väsentliga krav. | 1 kap. 1–2 §§ |
| TS: ELSÄK gäller inte på fartyg/fritidsbåtar **utom EMC och båtar på land** | Endast TS lagsida: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/ | Ingen ELSÄK-paragraf |

### Fartygssäkerhetslagen — kapitel som bär utrustning, tillsyn, delegation

Officiell text t.o.m. SFS 2024:843: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetslag-2003364_sfs-2003-364/

- **1 kap. 1 §** tillämpning: alla fartyg i sjöfart **inom Sveriges sjöterritorium** + **svenska fartyg utanför**. Även svenska rederier och utländska rederier med svenskt fartyg eller annat fartyg i svenskt sjöterritorium, om inte annat anges. Inte mot särskild föreskrift / folkrätt. **Örlog** endast om regeringen föreskriver. ISM-EG 336/2006 tar över vissa säkerhetsorganisationsbestämmelser.
- **2 kap. 1 §** sjövärdighet = konstruerat, byggt, **utrustat** och hållet i stånd. (El nämns inte vid namn.)
- **2 kap. 3 §** certifikat; utfärdas av TS.
- **2 kap. 6–7 §§** befälhavare (sjöklarhet) / teknisk chef (maskineri med tillhörande anordningar + brand). **2 kap. 8 §:** 6–7 §§ gäller utländska fartyg endast om regeringen föreskriver.
- **5 kap. 1 §** TS tillsyn av **fartyg och deras utrustning**. **5 kap. 4–4 a, 5–9 §§** tillsynsförrättningar; utländska genom **inspektion** (5 kap. 9 §). **5 kap. 20–22, 26–28, 30 §§** redare/befäl, ritningar, dokumentation ombord.
- **7 kap. 2 § 1** — regeringen eller den myndighet regeringen bestämmer får föreskriva hur fartyg ska vara konstruerat, byggt, **utrustat** och hållet i stånd för sjövärdighet enligt 2 kap. 1 §. **Detta är fästet för TSFS om el.** **7 kap. 3, 5, 6 §§** certifikat, arbetsmiljöutformning, tillsyn/ritningar/egenkontroll.

**FSF 2003:438** t.o.m. SFS 2025:1245: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetsforordning-2003438_sfs-2003-438/ — **inga tekniska elregler**. **2 kap. 1 §** delegerar 7 kap. 2 § 1 FSL till TS. **2 kap. 2 §** radio efter samråd med PTS. **3 kap. 2 §** extra certifikat/intyg. **6 kap. 7 och 11 §§** tillsyn, egenkontroll, ritningar.

---

## A. Fartygssäkerhetslagen (2003:364) — mer detalj

Lagen nämner **inte** el, elektrisk installation eller starkström. El ligger under sjövärdighet och tillsyn av utrustning.

### Tillämpningsområde

- **1 kap. 1 §:** se sammanfattningen.
- **1 kap. 2 §:** vad som sägs om redare gäller den som i redarens ställe utövar avgörande inflytande över driften (undantag 3 kap. 16 §).
- **1 kap. 3 §:** passagerarfartyg = fler än tolv passagerare.

**Utländska fartyg — inskränkningar lagen själv anger:**

| Bestämmelse | Innehåll |
|---|---|
| 2 kap. 8 § | Befälhavares och teknisk chefs skyldigheter (6–7 §§) endast om regeringen föreskriver |
| 3 kap. 8 § | Fribord 4–7 §§ endast om regeringen föreskriver |
| 3 kap. 18 § | Säkerhetsbesättning/bemanning gäller **inte** utländska fartyg |
| 4 kap. 18 § | Arbetsmiljökapitlet endast om regeringen föreskriver |
| 5 kap. 9 § | Tillsyn av utländska = **inspektion** (hamnstatskontroll) enligt 7 kap. 6 § |
| 6 kap. 2 § tredje stycket | Vissa utländska certifikatkrav bara när fartyget **anlöper eller lämnar svensk hamn** |

**GAP:** lagen talar inte om ”utländska fartyg i svensk hamn” som eget tillämpningsområde.

### Kapitelkarta

**2 kap.** 1 § sjövärdighet; 3 § certifikat; 6 § befälhavare; 7 § teknisk chef; 9–10 §§ rederi/ISM-dokument.

**3 kap.** 1 § fartcertifikat: svenskt skrov ≥ 15 m **eller** passagerarfartyg; fritid endast skrov > 24 m. 1 a–1 b §§ unionscertifikat inland. 2–3 §§ passagerarfartygscertifikat.

**4 kap.** arbetsmiljö (elarbete som fartygsarbete, inte ELSÄK). Befälhavaren har arbetsgivarliknande skyldigheter (4 kap. 9 §).

**5 kap.** 1 § TS tillsyn fartyg/utrustning; 3 § erkänd organisation; 4–8 §§ förrättningar; 6–7 §§ nybygge/större ombyggnad; 20–22 §§ redare; 26–28 §§ ritningar (elritningar faller under utrustning/anordningar — lagen säger inte ”el”); 30 § handlingar ombord.

**6 kap.** reseförbud vid osjövärdighet, saknade certifikat m.m.

**7 kap. 2 § 1** utrustning/sjövärdighet → TSFS. 3 § extra certifikat/utländska handlingar. 5 § arbetsmiljöutformning. 6 § tillsyn, ritningar, egenkontroll. 8–9 §§ fiskefartyg/särbeskaffenhet. 11–11 c §§ överlåtelse av certifikat.

**8 kap.** straff bl.a. användning utan certifikat, underlåten sjöklarhet.

### Fartygssäkerhetsförordningen — elrelevant

Inga tekniska elinstallationsregler. Delegering:

- **2 kap. 1 §** → TSFS 2019:4, 2017:26, 2024:58, 2026:20 m.fl.
- **2 kap. 2 §** radio (PTS).
- **3 kap. 2 §** extra dokument/certifikat/intyg.
- **5 kap. 10 §** utformning/inredning/utrustning för arbetsmiljö (samråd AV).
- **5 kap. 11 §** vissa FSL 4 kap.-regler även utländska i svenskt sjöterritorium.
- **6 kap. 7, 11 §§** tillsyn, egenkontroll, ritningar.
- **6 kap. 8 b §** marin utrustning (2016:768) vid certifikat — **inte ELSÄK**.
- **8 kap. 1–2 §§** fiskefartyg/särbeskaffenhet.
- **10 kap. 5 §** verkställighet.

**GAP i förordningen:** ingen paragraf om vem som får installera el, vad ett installationsintyg ska innehålla, eller om ELSÄK.

---

## B. ELSÄK-undantaget

### Slutsats

Elsäkerhetsverkets **elsäkerhets- och elinstallationsregelverk** omfattar **inte** elarbete på fartyg. Det är **inte** ett uttryckligt undantag i elsäkerhetslagen, utan en avgränsning via definitionen av elinstallationsarbete, bekräftad i förarbeten och av Elsäkerhetsverket. **EMC** ligger i **annan lag**; ELSÄK-FS 2016:3 **undantar inte fartyg**. Påståendet ”båtar på land” finns **endast hos TS**, inte i ELSÄK-FS 2022:1.

### 1. Elsäkerhetsverket

FAQ *Omfattas elarbete på fordon av elsäkerhetslagen?* (senast granskad 2024-06-24):

Elektriskt arbete på **fartyg**, luftfartyg, spårfordon och övriga fordon **omfattas inte av elsäkerhetslagen (2016:732)**. Det har **inte uttryckligt undantagits** eftersom det inte ansetts nödvändigt, se **prop. 2015/16:163 s. 20 ff.** Installationen ska ändå vara säker. **TS** ansvarar för elinstallationer i fordon i Sverige.

https://www.elsakerhetsverket.se/fragor-och-svar/arkiv-fragor/omfattas-elarbete-pa-fordon-av-elsakerhetslagen/

**GAP:** sidan nämner **inte** fritidsbåtar på land / vinterförvaring.

### 2. Prop. 2015/16:163 avsnitt 5.1 (s. 20–21)

https://regeringen.se/rattsliga-dokument/proposition/2016/04/prop.-201516163  
PDF: https://regeringen.se/contentassets/932ff878dd5b447eb5c9297ee6c34e9d/elsakerhet-prop.pdf

Utredningen ville ha uttryckligt lagundantag för fartyg m.fl. Regeringen: redan avgränsat i direktiven (speciallagstiftning). ELSÄK:s föreskrifter omfattade redan då inte sådant arbete. Det som faller utanför **behöver inte räknas upp i lagtexten**. Avgränsning genom definitionen av elinstallationsarbete som arbete på **elektrisk starkströmsanläggning**. Frågan om bemyndigande för tillfälliga land-elinstallationsföretag på fartyg **omfattades inte** av beredningen.

### 3. Elsäkerhetslagen (2016:732)

https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/elsakerhetslag-2016732_sfs-2016-732/  
Ändrad t.o.m. SFS 2026:1294 (vissa lydelser träder i kraft 2027-01-01; **ingen fartygsmening tillkommer**).

- **1 § andra stycket:** EMC i lagen 1992:1512.
- **2–4 §§:** elektrisk anläggning / starkströmsanläggning / elinstallationsarbete — **ingen fartygslista**.
- **16–27, 47 §§:** elinstallationsföretag, auktorisation — knutna till 4 §.

### 4. ELSÄK-FS 2022:1 (gällande 2026)

https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2022-1/  
PDF: https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2022-1.pdf

- **1 kap. 1 §:** hur en starkströmsanläggning ska vara utförd = elinstallationsarbete enligt **4 § elsäkerhetslagen**.
- **1 kap. 2 §:** omfattar starkströmsanläggningar enligt **3 § elsäkerhetslagen**.
- **Ingen** lista ”gäller inte fartyg”.
- **6 kap. 7 §** (luftledning/sjötrafik) och elsäkerhetsförordningen 12 § gäller **luftledningar över sjötrafik** — **inte** fartygsinstallationer.

### 5. Upphävd: ELSÄK-FS 2008:1 2 §

Uttryckligen: föreskrifterna gäller **inte** starkströmsanläggningar på **fartyg, inklusive fritidsbåtar**. **Inte gällande rätt** efter 2022-12-01.

Ännu äldre (upphävd) ELSÄK-FS 1999:5: fritidsbåt avsedd att matas > 50 V från land — **inte** gällande.

### 6. ELSÄK-FS 2017:2 (elinstallationsarbete)

https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2017-2/  
Hänvisar till lagen 4 och 23–27 §§. Inget fartygsundantag i föreskriftstexten.

### 7. EMC — ELSÄK-FS 2016:3

Lag: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-19921512-om-elektromagnetisk-kompatibilitet_sfs-1992-1512/

**1 kap. 1 §:** tillämpas på **utrustning** med undantag enligt listan (RED, luftfart, radioamatör, låg relevans, R&D). **Fartyg inte på listan.**

**1 kap. 2 §:** om annan unionslagstiftning specificerar väsentliga krav, ska 2016:3 inte tillämpas för **de kraven**. Kan träffa MED/lagen 2016:768 eller RED — **inte** samma sak som att EMC inte gäller på fartyg.

TS kompletterande upplysningar 5 kap.: ELSÄK-föreskrifter i allmänhet inte tillämpliga på fartyg, men för EMC gäller **ELSÄK-FS 2016:3**; Elsäkerhetsverket ansvarar för EMC **även på fartyg**.

### Vem säger vad

| Påstående | Elsäkerhetsverket | Transportstyrelsen | Föreskriftstext |
|---|---|---|---|
| ELSÄK elsäkerhet gäller **inte** på fartyg | Ja (FAQ + prop.) | Ja | 2022:1: indirekt via lagen. 2008:1 (upphävd): uttryckligt |
| EMC 2016:3 **gäller** på fartyg | Inte uttalat som fartygsmening; 2016:3 undantar inte fartyg | Ja, med ELSÄK-FS 2016:3 | 1 kap. 1 §: utrustning |
| **Fritidsbåtar på land** = ELSÄK | **Inte funnet** på elsakerhetsverket.se | **Ja** — endast lagsidan | Ingen gällande ELSÄK-FS med den meningen |

**Flagga:** ”båt i sjön = TS, båt på land = ELSÄK” är **TS-vägledning**, inte lagtext.

---

## C. Kompetens och intyg (kort)

### C.1 TSFS 2019:4 (bindande för internationellt säkerhetscertifikat)

Stöd: FSF 2 kap. 1 §. Motsvarar SOLAS 74 kap. II-1 del A och C–E.

**16 kap. 1 § (ska):** konstruktion, tillverkning och underhåll enligt **IEC 60092** + erkänd organisations regler.

**16 kap. 2 § (ska):** elektrisk installation ska utföras av installatör med **el-teknisk bakgrund** och goda kunskaper om fartygs elinstallationsprinciper och gällande standarder. **Innan godkännande:** intyg att installationen uppfyller **tillämpad standard**.

**Allmänna råd till 16 kap. 2 § (bör):** fartygsingenjör; elektroingenjör; eltekniker enligt STCW; fartygselektriker; annan utbildning/erfarenhet (t.ex. marinens el).

### C.2 TS webb (bör) — krav-sidan

Samma lista + varvspersonal / behörig elinstallatör **med kunskap om fartygsel**. Intyg **bör** visa regelverk + tillämpad standard. För SOLAS-fartyg gäller föreskriftens **ska**.

ELSÄK-auktorisation **räcker inte ensam** (prop. + FAQ).

### C.3 Nationell sjöfart — TSFS 2017:26

**2 kap. 6 § (ska):** fackmässigt. **1 kap. 27 och 29 §§ (ska):** dokumentation, spårbarhet. **5 kap.:** funktionskrav, **ingen** personkrets motsvarande 16 kap. 2 §. Kompletterande upplysningar: yrkeskunnig person, intyg till **befälhavaren** (vägledning).

### C.4 Inland — TSFS 2026:20 (från 2026-05-01)

**11 §:** zon 1 eller 2: huvudkraft + oberoende nödkraft; nödkraft enligt passagerarkrav i dir. (EU) 2016/1629 bilaga II, minst **tre timmar**; normal drift utan nöd. **12 §:** landström enligt (EU) 2023/1804. **Ingen** funnen bestämmelse om installatörskompetens eller arbetsintyg.

### C.5 Intyg — vad som **måste** sägas

Bindande (2019:4 16 kap. 2 §): uppfyller **tillämpad standard**; före godkännande.

Vägledning (TS webb + kompletterande upplysningar): regelverk + standard; till befälhavaren; del av dokumentationen.

**Inte funnet:** mall, obligatoriska fält, språkkrav för arbetsintyg, koppling till ELSÄK-anmälan, särregel inland/fritid.

---

## D. Samlad källförteckning

1. FSL 2003:364: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetslag-2003364_sfs-2003-364/
2. FSF 2003:438: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/fartygssakerhetsforordning-2003438_sfs-2003-438/
3. Elsäkerhetslag 2016:732: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/elsakerhetslag-2016732_sfs-2016-732/
4. Lag 1992:1512 EMC: https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-19921512-om-elektromagnetisk-kompatibilitet_sfs-1992-1512/
5. Prop. 2015/16:163: https://regeringen.se/rattsliga-dokument/proposition/2016/04/prop.-201516163
6. ELSÄK FAQ fartyg: https://www.elsakerhetsverket.se/fragor-och-svar/arkiv-fragor/omfattas-elarbete-pa-fordon-av-elsakerhetslagen/
7. ELSÄK-FS 2022:1: https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2022-1/ — PDF https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2022-1.pdf
8. ELSÄK-FS 2008:1 (upphävd): https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2008-1-konsoliderad.pdf
9. ELSÄK-FS 2016:3 konsoliderad: https://www.elsakerhetsverket.se/globalassets/foreskrifter/elsak-fs-2016-3-konsoliderad.pdf
10. ELSÄK-FS 2017:2: https://www.elsakerhetsverket.se/om-oss/lag-och-ratt/foreskrifter/elsak-fs-2017-2/
11. TS lagsida el: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/lagar-foreskrifter-och-standarder/
12. TS krav-sida: https://www.transportstyrelsen.se/sv/sjofart/fartyg/utrustning-pa-fartyg/elinstallationer/krav-fore-elektrisk-installation-pa-fartyg/
13. TS kompletterande upplysningar 5 kap.: https://www.transportstyrelsen.se/sv/om-oss/dina-rattigheter-lagar-och-regler/lagar-och-regler/regler-for-sjofart/regler-for-nationell-sjofart/regler-kompletterade-upplysningar/elektrisk-utrustning-och-elinstallationer/
14. TSFS 2019:4: https://www.transportstyrelsen.se/TSFS/TSFS%202019_4.pdf
15. TSFS 2017:26k: https://www.transportstyrelsen.se/TSFS/TSFS%202017_26k.pdf
16. TSFS 2018:60 (upphävd): https://www.transportstyrelsen.se/TSFS/TSFS%202018_60.pdf
17. TSFS 2026:20: lokal `/workspace/kallpack/TSFS_2026_20.pdf` (officiell TSFS-URL-mönster `TSFS%202026_20.pdf`)
18. TSFS 2024:58: https://www.transportstyrelsen.se/TSFS/TSFS%202024_58.pdf
19. Hub: se `01-ts-hub.md`

---

## E. GAP-lista

1. FSL/FSF nämner inte el vid namn; koppling = sjövärdighet + 7 kap. 2 § 1 / FSF 2 kap. 1 §.
2. Elsäkerhetslagen har inget uttryckligt fartygsundantag; ELSÄK-FS 2022:1 har ingen fartygsmening (till skillnad från upphävda 2008:1 2 §).
3. ”Båtar på land” är **endast TS-vägledning**.
4. Inget bemyndigande i elsäkerhetslagen för tillfälliga land-elinstallationsföretag på fartyg (prop. sköt frågan).
5. Intygets innehåll utöver ”tillämpad standard” är inte föreskrivet (ingen mall).
6. Personkretsen i 2019:4 16 kap. 2 § är **allmänna råd** utom den vida ska-formeln.
7. Inland 2026:20: ingen kompetens-/intygsregel; landström via AFIR 12 §, inte TSFS 2024:58 (som undantar inland).
8. EMC 2016:3 2 § mot MED/lagen 2016:768 **inte utrett** här.
9. TS lagsida listar fortfarande 2018:60, inte 2026:20; listar inte 2024:58.
10. TSFS 2019:120 **del C** och SJÖFS 2002:17 del D / 1999:27 del C: elinnehåll inte utdraget.
11. TSFS 2026:9/37/44 ändrar **inte** 2017:26 kap. 5 och **inte** landströmkraven i sak — bara ISM-hänvisning resp. inland-definition.
12. Hubbens batterisida skriver ”fartygssäkerhetslagens 4a §”; korrekt är **5 kap. 4 a §** FSL.
