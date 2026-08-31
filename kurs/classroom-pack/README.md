# Classroom-pack — Elteknik och ellära 45 p

Utskrivbara **PDF** och **Word (.docx)** för Google Classroom. Inte markdown. Inte studentsajten.

A4, svart på vitt, IBM Plex Sans, 0 radius. Metro v3. Byggs från `kurs/elevblad/`, `kurs/lektioner/` och `kurs/lararhandledning/classroom-v1-vecka1.md` / `classroom-v2-vecka2.md`.

Återbygg: från repots rot, `.venv/bin/python kurs/classroom-pack/build.py`

## Recept — vad som går till eleven

| Classroom | Till eleverna (material / uppgift) | Bara lärare (publicera inte) |
| --- | --- | --- |
| Vecka 1 | `elev-stotvag.pdf` + `.docx`, `lektion-1.1-stotar.pdf` + `.docx` | `larare-stotvag-facit.pdf` + `.docx`, `larare-inlagg-vecka1.pdf` + `.docx` |
| Vecka 2 | `elev-meggerkort.pdf` + `.docx`, `lektion-2.1-isolering.pdf` + `.docx` | `larare-meggerkort-facit.pdf` + `.docx`, `larare-inlagg-vecka2.pdf` + `.docx` |

Filnamn med `facit` eller `larare-` är läraronly. Länka dem inte från elev-nav och inte från GitHub Pages elevskal. `site/app.js` `okPath` spärrar redan `*facit*` för elev.

PDF är utskriften. Word är samma blad om eleven ska fylla digitalt.

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

## Inte

- Facit på studentsajten
- Markdown som elevhandout
- EX, BESS, nödström, IEC/IEEE 80005
- Ny kursplan eller ny lagtext
