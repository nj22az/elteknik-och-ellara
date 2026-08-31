# Classroom-pack — Elteknik och ellära 45 p

Utskrivbara **PDF** och **Word (.docx)** för Google Classroom. Inte markdown.

A4, svart på vitt, IBM Plex Sans, 0 radius. Metro v3.
Återbygg: från repots rot, `.venv/bin/python kurs/classroom-pack/build.py`

Lärarsajten hämtar filerna här. **Elevvägar får inte peka på facit.**

## Elev mot Lärare

| Prefix | Roll | Classroom | Studentsajt | Lärarsajt |
| --- | --- | --- | --- | --- |
| `elev-*` | Elevblad | Lämna som material/uppgift | Får länkas | Får länkas |
| `lektion-*` | Elevlektion | Valfritt material | Får länkas | Får länkas |
| `larare-inlagg-*` | Classroom-inlägg att klistra in | **Inte** som elevfil | **Nej** | Ja |
| `larare-*-facit*` | Facit | **Aldrig** i strömmen | **Aldrig** | Ja |

Filnamn med `facit` eller prefix `larare-` är läraronly.

## Recept

| Classroom | Till eleverna | Bara lärare |
| --- | --- | --- |
| Vecka 1 | `elev-stotvag`, `lektion-1.1-stotar` | `larare-stotvag-facit`, `larare-inlagg-vecka1` |
| Vecka 2 | `elev-meggerkort`, `lektion-2.1-isolering` | `larare-meggerkort-facit`, `larare-inlagg-vecka2` |
| Vecka 3 | `elev-dc`, `lektion-3.1-dc` | `larare-dc-facit`, `larare-inlagg-vecka3` |
| Vecka 4 | `elev-enfas`, `lektion-4.1-enfas-ac` | `larare-enfas-facit`, `larare-inlagg-vecka4` |
| Vecka 5 | `elev-trefas`, `lektion-5.1-trefas` | `larare-trefas-facit`, `larare-inlagg-vecka5` |
| Vecka 6 | `elev-maskiner`, `lektion-6.1-maskiner` | `larare-maskiner-facit`, `larare-inlagg-vecka6` |
| Vecka 7 | `elev-tavla-verktyg`, `lektion-7.1-eltavla`, `lektion-8.1-verktyg` | `larare-tavla-verktyg-facit`, `larare-inlagg-vecka7`, `larare-inlagg-vecka7b` |
| Vecka 8 | `elev-ritning-hallkrets`, `lektion-9.1-ritningar`, `lektion-10.1-hallkrets` | `larare-ritning-hallkrets-facit`, `larare-inlagg-vecka8`, `larare-inlagg-vecka8b` |
| Vecka 9 | `elev-arbete-felsok`, `lektion-11.1-arbete-ip-intyg`, `lektion-12.1-felsokning` | `larare-arbete-felsok-facit`, `larare-inlagg-vecka9`, `larare-inlagg-vecka9b`, `larare-inlagg-prov-vecka9` |

PDF och `.docx` för varje namn. Skriftligt prov-facit stannar i `kurs/prov/`, inte som elevfil.

## Inte

- Facit på studentsajten eller i elevvägar
- Markdown som elevhandout
- EX, BESS, nödström, IEC/IEEE 80005
- Ny kursplan
