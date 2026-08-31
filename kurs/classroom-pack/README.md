# Classroom-pack — Elteknik och ellära 45 p

Utskrivbara **PDF** och **Word (.docx)** för Google Classroom. Inte markdown. Inte studentsajten.

A4, svart på vitt, IBM Plex Sans, 0 radius. Metro v3. Byggs från `kurs/elevblad/` (när filen finns), `kurs/lektioner/`, `kurs/lararhandledning/classroom-v*-vecka*.md` och `kurs/prov/` (vecka 9). Elevblad bara om källfilen ligger i `kurs/elevblad/` — ingen påhittad biljett.

Återbygg: från repots rot, `.venv/bin/python kurs/classroom-pack/build.py`

## Recept — vad som går till eleven

**Elev** = `lektion-*`, `elev-*` och `elev-skriftligt-prov`.  
**Lärare** = allt `larare-*` eller `*facit*`. Filnamn med `facit` eller `larare-` aldrig på studentsajten / Classroom-elevströmmen. Lärarsajten får ladda ner allt.

| Classroom | Till eleverna (material / uppgift) | Bara lärare (publicera inte) |
| --- | --- | --- |
| Vecka 1 | `elev-stotvag.pdf` + `.docx`, `lektion-1.1-stotar.pdf` + `.docx` | `larare-stotvag-facit.pdf` + `.docx`, `larare-inlagg-vecka1.pdf` + `.docx` |
| Vecka 2 | `elev-meggerkort.pdf` + `.docx`, `lektion-2.1-isolering.pdf` + `.docx` | `larare-meggerkort-facit.pdf` + `.docx`, `larare-inlagg-vecka2.pdf` + `.docx` |
| Vecka 3 | `elev-dc.pdf` + `.docx`, `lektion-3.1-dc.pdf` + `.docx` | `larare-dc-facit.pdf` + `.docx`, `larare-inlagg-vecka3.pdf` + `.docx` |
| Vecka 4 | `elev-enfas.pdf` + `.docx`, `lektion-4.1-enfas-ac.pdf` + `.docx` | `larare-enfas-facit.pdf` + `.docx`, `larare-inlagg-vecka4.pdf` + `.docx` |
| Vecka 5 | `elev-trefas.pdf` + `.docx`, `lektion-5.1-trefas.pdf` + `.docx` | `larare-trefas-facit.pdf` + `.docx`, `larare-inlagg-vecka5.pdf` + `.docx` |
| Vecka 6 | `elev-maskiner.pdf` + `.docx`, `lektion-6.1-maskiner.pdf` + `.docx` | `larare-maskiner-facit.pdf` + `.docx`, `larare-inlagg-vecka6.pdf` + `.docx` |
| Vecka 7 | `elev-tavla-verktyg.pdf` + `.docx`, `lektion-7.1-eltavla.pdf` + `.docx`, `lektion-8.1-verktyg.pdf` + `.docx` | `larare-tavla-verktyg-facit.pdf` + `.docx`, `larare-inlagg-vecka7.pdf` + `.docx`, `larare-inlagg-vecka7b.pdf` + `.docx` |
| Vecka 8 | `elev-ritning-hallkrets.pdf` + `.docx`, `lektion-9.1-ritningar.pdf` + `.docx`, `lektion-10.1-hallkrets.pdf` + `.docx` | `larare-ritning-hallkrets-facit.pdf` + `.docx`, `larare-inlagg-vecka8.pdf` + `.docx`, `larare-inlagg-vecka8b.pdf` + `.docx` |
| Vecka 9 | `elev-arbete-felsok.pdf` + `.docx`, `lektion-11.1-arbete-ip-intyg.pdf` + `.docx`, `lektion-12.1-felsokning.pdf` + `.docx`, `elev-skriftligt-prov.pdf` + `.docx` | `larare-arbete-felsok-facit.pdf` + `.docx`, `larare-inlagg-vecka9.pdf` + `.docx`, `larare-inlagg-vecka9b.pdf` + `.docx`, `larare-inlagg-prov-vecka9.pdf` + `.docx`, `larare-skriftligt-prov-facit.pdf` + `.docx` |

Filnamn med `facit` eller `larare-` är läraronly. Länka dem inte från elev-nav och inte från GitHub Pages elevskal. `site/app.js` `okPath` spärrar redan `*facit*` för elev.

PDF är utskriften. Word är samma blad om eleven ska fylla digitalt. Quiz-markdown skrivs inte ut.

## Vecka 1 — V1 · M01 Elsäkerhet (stötväg)

**Till eleverna**

- `vecka-01/elev-stotvag.pdf` / `.docx` — STOP/GO, rita stötväg, ring två fel
- `vecka-01/lektion-1.1-stotar.pdf` / `.docx` — lektion 1.1 + figur 1.1

**Till dig**

- `vecka-01/larare-stotvag-facit.pdf` / `.docx` — G = STOP, hölje → kropp → skrov, två av tre fel
- `vecka-01/larare-inlagg-vecka1.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 2 — V2 · M02 Isolering (meggerkort)

**Till eleverna**

- `vecka-02/elev-meggerkort.pdf` / `.docx` — blandad kedja, 2,4 / 0,4, 1 MΩ = upplysning
- `vecka-02/lektion-2.1-isolering.pdf` / `.docx` — lektion 2.1 + figur 2.1

**Till dig**

- `vecka-02/larare-meggerkort-facit.pdf` / `.docx` — kedja från → lås → tvåpol → megger → protokoll; 2,4 GO efter kåpa; 0,4 STOP; 1 MΩ upplysning
- `vecka-02/larare-inlagg-vecka2.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 3 — V3 · M03 Resistiv DC

**Till eleverna**

- `vecka-03/elev-dc.pdf` / `.docx` — räkna serie/parallell, DMM-läge, STOP/GO
- `vecka-03/lektion-3.1-dc.pdf` / `.docx` — lektion 3.1 + figur 3.1

**Till dig**

- `vecka-03/larare-dc-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-03/larare-inlagg-vecka3.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 4 — V4 · M04 Enfas AC

**Till eleverna**

- `vecka-04/elev-enfas.pdf` / `.docx` — rms mot topp, AC-läge
- `vecka-04/lektion-4.1-enfas-ac.pdf` / `.docx` — lektion 4.1 + figur 4.1

**Till dig**

- `vecka-04/larare-enfas-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-04/larare-inlagg-vecka4.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 5 — V5 · M05 Trefas

**Till eleverna**

- `vecka-05/elev-trefas.pdf` / `.docx` — linje mot fas, tre spänningstyper
- `vecka-05/lektion-5.1-trefas.pdf` / `.docx` — lektion 5.1 + figur 5.1

**Till dig**

- `vecka-05/larare-trefas-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-05/larare-inlagg-vecka5.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 6 — V6 · M06 Maskiner

**Till eleverna**

- `vecka-06/elev-maskiner.pdf` / `.docx` — märkskylt, tyst ≠ av
- `vecka-06/lektion-6.1-maskiner.pdf` / `.docx` — lektion 6.1 + figur 6.1

**Till dig**

- `vecka-06/larare-maskiner-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-06/larare-inlagg-vecka6.pdf` / `.docx` — klistra inlägget i Classroom som det står

## Vecka 7 — V7 · M07 Eltavla + M08 Verktyg

**Till eleverna**

- `vecka-07/elev-tavla-verktyg.pdf` / `.docx` — huvudtavla/grupptavla + instrumentval
- `vecka-07/lektion-7.1-eltavla.pdf` / `.docx` — lektion 7.1 + figur 7.1
- `vecka-07/lektion-8.1-verktyg.pdf` / `.docx` — lektion 8.1 + figur 8.1

**Till dig**

- `vecka-07/larare-tavla-verktyg-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-07/larare-inlagg-vecka7.pdf` / `.docx` — 7.1, klistra inlägget som det står
- `vecka-07/larare-inlagg-vecka7b.pdf` / `.docx` — 8.1, klistra inlägget som det står

## Vecka 8 — V8 · M09 Ritningar + M10 Hållkrets

**Till eleverna**

- `vecka-08/elev-ritning-hallkrets.pdf` / `.docx` — enlinje/kretsschema + hållkrets
- `vecka-08/lektion-9.1-ritningar.pdf` / `.docx` — lektion 9.1 + figur 9.1
- `vecka-08/lektion-10.1-hallkrets.pdf` / `.docx` — lektion 10.1 + figur 10.1

**Till dig**

- `vecka-08/larare-ritning-hallkrets-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-08/larare-inlagg-vecka8.pdf` / `.docx` — 9.1, klistra inlägget som det står
- `vecka-08/larare-inlagg-vecka8b.pdf` / `.docx` — 10.1, klistra inlägget som det står

## Vecka 9 — V9 · M11 Elarbete + M12 Felsökning

**Till eleverna**

- `vecka-09/elev-arbete-felsok.pdf` / `.docx` — intyg + felsök på papper
- `vecka-09/lektion-11.1-arbete-ip-intyg.pdf` / `.docx` — lektion 11.1 + figur 11.1
- `vecka-09/lektion-12.1-felsokning.pdf` / `.docx` — lektion 12.1 + figur 12.1
- `vecka-09/elev-skriftligt-prov.pdf` / `.docx` — skriftligt prov, inget facit

**Till dig**

- `vecka-09/larare-arbete-felsok-facit.pdf` / `.docx` — facit till elevbladet
- `vecka-09/larare-inlagg-vecka9.pdf` / `.docx` — 11.1, klistra inlägget som det står
- `vecka-09/larare-inlagg-vecka9b.pdf` / `.docx` — 12.1, klistra inlägget som det står
- `vecka-09/larare-inlagg-prov-vecka9.pdf` / `.docx` — skriftligt prov, klistra inlägget som det står
- `vecka-09/larare-skriftligt-prov-facit.pdf` / `.docx` — facit till skriftligt prov. Inte till elev.

## Inte

- Facit på studentsajten
- Markdown som elevhandout
- EX, BESS, nödström, IEC/IEEE 80005
- Ny kursplan eller ny lagtext
- Quiz-markdown i packen
- Påhittat elevblad — bara print av filer som finns i `kurs/elevblad/`
