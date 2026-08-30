# QC — teachability v1

Kurs: Elteknik och ellära (45 p), Kurskarta v2 (12 moduler).
Datum: 2026-08-30 (Europe/Stockholm).
Fråga: kan Patrik (landelektriker) eller Lina (fartygsingenjör) **göra ett jobb** från materialet, eller bara recitera TSFS/SHK?

Låsta ramar respekterade i bedömningen (rekommenderar inte: EX, BESS, nödström, 80005, TSFS 2024:58, IEC/IP-tabeller, 1 MΩ som skall, Germanica utanför kap. 1, 8-veckors 172-slids-kärna).

---

## Tabell

| Vecka | Modul | Teachability | En rad |
|---|---|---|---|
| 1 | 1.1 Stötväg | **FAIL** | Ticket + figur finns, men figuren är facit och quizzen är källtaxonomi |
| 2 | 2.1 Isolering | **FAIL** | Kedjan är ett jobb — men inget ifyllt meggerkort och inga mätarfoton |
| 3 | 3.1 DC | **FAIL** | Samma stencil; DMM-foton/talblad “läraren lägger” |
| 4 | 4.1 Enfas AC | **FAIL** | Samma; rms/topp beskrivs, ingen sinus-uppgift med tal |
| 5 | 5.1 Trefas | **FAIL** | Samma; look-not-touch att recitera, ingen enlinje att märka |
| 6 | 6.1 Maskiner | **FAIL** | Samma; märkskyltsfoto saknas i paketet |
| 7 | 7.1 Eltavla | **FAIL** | Samma; tre tavelfoton saknas |
| 8 | 8.1 Verktyg | **FAIL** | Jobb→instrument-tabell i lektionen är närmast ett jobb; foton saknas |
| 9 | 9.1 Ritningar | **FAIL** | Samma; enlinje/kretsschema “läraren lägger” |

Vecka 8 (lektion 8.1) är minst dålig: matchningen tre jobb / tre instrument sitter i själva bladet. Resten av 3–9 är samma mönster som 1–2.

---

## Vecka 1 — 1.1 Stötväg ombord — **FAIL**

Patrik kan säga “leta inte JFB”. Lina kan säga “läckagesökning är elarbete”. Ingen av dem kan *göra* läckagejobbet från en blank yta: figuren har redan ritat stötvägen och skrivit “packning saknas / ingen PE / ser inte”. Quizzen testar om de kan klassa källor, inte om de stannar.

### Usable today

- **Job ticket:** “Det läcker vid pumpen, känn efter var.”
- **Dual-entry, en rad:** elektriker = leta inte JFB; ingenjör = läckage vid spänningssatt komponent är elarbete.
- **Figur 1.1** (`bok/figur-1-1-stotvag-ventil.png`) som *lärarbild*: hölje → hand → skrov, IR blind för sidokrets. Inte en märkfigur — etiketterna är facit.
- **Symptomtabell** i kap. 1.3 (symptom / första sak / orsak / gör inte).
- **G/VG/IG-rubrik** som beteende, inte som lagcitat.
- **ASCII-labbprotokoll B** i kap. 1.5 (tomma fält). Inte utskrivet elevblad, inget ifyllt G-exempel.
- Germanica (SHK 2024:04) som genomgånget fel, **bara här** — rätt lås.

### Source regurgitation

- Samma 5 kap. 5 §-parafras + “inte skall”-tabell + URL-dump i lektion, bok, slides, lärarhandledning, Classroom-post.
- Quiz 4 frågor: skall vs upplysning, “1 MΩ är inte lag”, ELSÄK-hål. En enda fråga (JFB/IR) är jobb-nära. 1 MΩ-frågan hör till m2; här är den lås-undervisning.
- Källhygien reciterad som innehåll: “olyckor-sidan namnger inte Germanica”, “inte 2024:58”, “inte 2008:1”. Rätt lås, fel lektionsyta.
- Classroom-inlägget är ett stycke av samma fakta, inte en arbetsorder eleven fyller.

### Saknas (ett)

**Omärkt elevexemplar av figur 1.1 + tvåval STOP/GO på läckageticketen.**  
Eleven ritar stötväg hölje→kropp→skrov, ringar två av tre fel (packning / PE / utanför IR), kryssar STOP på “känn efter var”. Inte mer Germanica-prosa. Inte 1 MΩ. Inte megger.

---

## Vecka 2 — 2.1 Isolering före arbete — **FAIL**

Närmare ett jobb än vecka 1: kedjan från→lås/skylt→tvåpol död→megger→protokoll är något Patrik och Lina kan *utföra på papper* om de får siffror. De får inte siffrorna. Figuren är en färdig infograf. Mätarfoton med 2,4 / 0,4 MΩ finns inte i repot (“läraren lägger i Classroom”). Quizzen blandar ett riktigt beslut (0,4 = inte tillslag) med källtaxonomi (1 MΩ = upplysning).

### Usable today

- **Job ticket:** “230 V-grupp inredning, kabel bytt. Isolera på papper. Megga inte live.”
- **Kedja** (slides 7, kap. 2.3, lektion §3) — det är veckans jobb.
- **Beslutsbit i quizzen:** IR ≠ megger; 0,4 MΩ → inte spänningssätt; rätt ordning (fråga 2–4).
- **Dual-entry:** referens är inte PE-skenan hemma / tyst maskin är inte död.
- **Figur 2.1** (`bok/figur-2-1-isolering-kedja.png`) som lärarbild: fyra steg + två tider (IR under drift vs megger på avställd, mot skrov inte PE). Åter facit, inte övningsblad. Visar `> 100 MΩ`, inte 0,4-beslutet.
- **ASCII-isolationsprotokoll** i kap. 2.5. Tomt. Inget ifyllt G/VG.
- 1 MΩ stannar **upplysning** (rätt lås). Germanica inte omberättad (rätt lås).

### Source regurgitation

- Samma 5 kap. 5 § + FSL 2 kap. 9–10 §§ + “inte skall”-tabell + URL:er som vecka 1, nu med Isolationsprov-sidan.
- SMS-lista 1–8 är i praktiken olyckor-sidan omnumrerad (JFB, packning, flexkabel, fallskydd, …). Tre punkter styr protokollet; resten är recitation.
- Quiz fråga 1: “är 1 MΩ skall?” — källnivå, inte meggerkort.
- Classroom-posten upprepar ticket + dual-entry + 0,4-regeln i ett stycke. Ingen blankett, inga foton.

### Saknas (ett)

**Ett ifyllt meggerkort (facit) plus tom elevkopia, mot två givna avläsningar.**  
Samma 230 V-inredningsgrupp. Referens skrov/stomme, inte PE. Kedja i ordning. 2,4 MΩ = OK att planera tillslag *efter* kåpa; 0,4 MΩ = inte spänningssätt, avvikelse, 1 MΩ märkt upplysning (inte “olagligt enligt 5 §”). VG-rad: saknas megger på varvet → tvåpol + gapflagga. Inga live-foton krävs om siffrorna står på kortet.

---

## Vecka 3–9 — samma mönster (en rad)

Alla lektioner 3.1–9.1 använder femrutan: 5 kap. 5 §-parafras, inte-skall-tabell, dual-entry, genomgånget fel, “läraren lägger foto”, ASCII-protokoll, 3-frågors fälla-quiz. Ticketen *beskrivs*. Elevbladet *finns inte*.

| Lektion | En rad |
|---|---|
| 3.1 DC | **FAIL** — Ohm som jobb, men inga tre tal och inga DMM-foton i filen |
| 4.1 Enfas | **FAIL** — rms vs DC-läge som fälla; ingen sinusuppgift med tal |
| 5.1 Trefas | **FAIL** — namnge 24/230/440 och look-not-touch; ingen enlinje att märka |
| 6.1 Maskiner | **FAIL** — stilla axel ≠ av (bra fälla); märkskylt saknas |
| 7.1 Eltavla | **FAIL** — MSB vs grupp vs död övningstavla; tre foton saknas |
| 8.1 Verktyg | **FAIL** — tabellen jobb→tvåpol/DMM/megger är usable text; foton saknas |
| 9.1 Ritningar | **FAIL** — enlinje vs krets + ett mått; ritningen ska läraren rita |

Quizzen från v3 och framåt är mer jobb-lika än v1 (ström i serie, DC-läge ≠ av, 440 look-not-touch). Det räddar inte teachability: utan blad att fylla reciterar Patrik/Lina fällan och lämnar in prosa.

---

## Inte detta

- Inte omskrivna kapitel.
- Inte 1 MΩ som skall. Inte Germanica i kap. 2. Inte 2024:58, EX, nöd, 80005, IEC/IP-tabell.
- Inte den gamla 8-veckors 172-slids-packen som kärna. `pptx/vecka-01.pptx` / `vecka-02.pptx` hoppades; bedömningen sitter på markdown-spåren (`classroom-v1-slides.md`, `classroom-v2-slides.md`).
