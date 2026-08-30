# PowerPoint — Elteknik och ellära 45 p

Widescreen 16:9. Svenska.

## Master (v3)

`master.pptx` is the **riktlinje v3** sample master. Not a week deck.

- Type: IBM Plex Sans (TTF in `pptx/fonts/`: Regular 400, Medium 500, SemiBold 600). Fallback Arial. Never Calibri identity. Never light.
- Paper `#FFFFFF`, ink `#111111`. Accent1 M01 `#E6002D`, accent2 M02 `#F39700`. Color is line ID only.
- 0 radius on every shape. No shadow, gradient, or 980 px pill. No green `#1f4d3a` bar.
- Title row: M-lozenge + module name + V-square. Footer hairline: Mxx + module, Vx, tabular slide number.
- OBS: ink tab, paper body, 1 px rule, one sentence. FARA: ink header, rule-heavy frame, not red.
- Callout disks: 28 pt circles, ink fill, white 600 tabular numbers.

Rebuild: `pptx/src/build_master.py` (after figures). Tokens in `pptx/src/v3_tokens.py` and `pptx/src/tokens.py`.

Sample slides in the master (pattern). **Week decks vecka-01..09 and `kurs-overblick.pptx` match this master (v3).**

1. Title — Elteknik och ellära / YH · 45 p / Fartyg och automation; M01–M12 lozenge swatches
2. Modul M01 Elsäkerhet (lozenge + name, V1)
3. Stötväg — disks 1–3 from `classroom-v1-slides.md` slide 4
4. Figur 1.1 (embedded `bok/figur-1-1-stotvag-ventil-skarm.png`) + numbered legend
5. OBS / FARA from kapitel-01 stop/warning lines
6. Modul M02 Isolering (lozenge + name, V2)
7. Figur 2.1 (embedded `bok/figur-2-1-isolering-kedja-skarm.png`) + numbered legend
8. Två spår — Elektriker / Ingenjör from `classroom-v1-slides.md` slide 3

Figures: `pptx/src/build_figures.py` (Pillow + IBM Plex). Print PNG 6.00 in column, 300 dpi grayscale; `*-skarm.png` RGB line-color.

Speaker notes on the **week files** = talk track from markdownfältet `Notes:`.

Decken **matchar Classroom-veckorna** (vecka 1–9). Innehåll från `kurs/lararhandledning/classroom-v*-slides.md` och figurer i `bok/`. Ingen ny marin-ellag. Ingen IP-tabell, ingen TSFS-PDF, ingen 1 MΩ som lag, ingen Arduino, ingen EX/80005/nöd som kursinnehåll. STENA GERMANICA bara i vecka 1 (låst lektion 1.1).

Studentsajt: https://nj22az.github.io/elteknik-och-ellara/

| Fil | Classroom | Källa | Slides |
|---|---|---|---|
| `kurs-overblick.pptx` | hela kursen | kurskarta v2 | 13 |
| `vecka-01.pptx` | vecka 1 | `classroom-v1-slides.md` + figur 1.1 | 18 |
| `vecka-02.pptx` | vecka 2 | `classroom-v2-slides.md` + figur 2.1 | 18 |
| `vecka-03.pptx` | vecka 3 | `classroom-v3-slides.md` + figur 3.1 | 18 |
| `vecka-04.pptx` | vecka 4 | `classroom-v4-slides.md` + figur 4.1 | 18 |
| `vecka-05.pptx` | vecka 5 | `classroom-v5-slides.md` + figur 5.1 | 18 |
| `vecka-06.pptx` | vecka 6 | `classroom-v6-slides.md` + figur 6.1 | 18 |
| `vecka-07.pptx` | vecka 7 | `classroom-v7-slides.md` sedan `classroom-v8-slides.md` (m7+m8) + figur 7.1 och 8.1 | 35 |
| `vecka-08.pptx` | vecka 8 | `classroom-v9-slides.md` sedan `classroom-v10-slides.md` (m9+m10) + figur 9.1 och 10.1 | 35 |
| `vecka-09.pptx` | vecka 9 | `classroom-v11-slides.md` sedan `classroom-v12-slides.md` (m11+m12) + figur 11.1 och 12.1; sista slidarna = skriftligt prov, bara elevblad, inget facit | 39 |

Varje veckodeck: veckotitel + en PPT-slide per `## Slide` + kursfigur efter modultiteln. **These week files match v3** (IBM Plex Sans, M-lozenge + V-square, 0 radius). Speaker notes copied verbatim from the pre-restyle decks.

`kurs-overblick.pptx`: titel, nio veckors kalender, tolv moduler, labbdag efter vecka 8, IG/G/VG, dual-entry elektriker mot fartygsingenjör, vad som inte ingår, studentsajt-URL.
