# Visuell riktlinje v3

En spec för sajt, PPTX och bokfigurer. Inte en lektion. Inte CSS-implementation här.

Språk i formen: japansk informationsdesign. Tokyo Metros wayfinding + JIS-etikett + pillerask. Inte Apple-glas. Inte Palatino-lärobok. Inte Material. Inte MUJI-tomhet.

Svenska etiketter bara. Ingen japansk copy i kursen.

Efter denna fil: sitt. Skylt, Figur och sajtbygge läser här.

---

## Vad som är dött

- Frostad nav, `backdrop-filter`, SF Pro, system-ui som identitet
- 980 px-piller, ett enda accent `#1f4d3a`, 2.5 rem display-h1
- Palatino, Iowan, Georgia, serif någonstans
- Material-elevation, ripple, rundade kort-som-app
- Tom yta som estetik (MUJI). Luft får finnas. Densitet är default.

---

## Typ

Gothic sans. Tabular figures. Samma stack överallt (sajt, slide, figurtext).

**Stack**

`IBM Plex Sans`, `Noto Sans`, `Arial`, `Helvetica`, sans-serif

- Vikt: 400 bröd, 500 UI, 600 kod/etikett/rubrik. Aldrig light.
- Siffror: `font-variant-numeric: tabular-nums lining-nums`. Linjekoder och callouts ska inte hoppa i bredd.
- Linjekod (M01, V7): 600, tracking 0.06 em, cap-height, aldrig gemener.
- Etikett (modulnamn, OBS, FARA): 600, versaler eller title case enligt tabellen nedan. Inte meningssats i kromet.
- Bröd på sajt: 16 px / 1.45. Inte 17 px Apple-luft.
- Display: 22–28 px 600. Wayfinding-stor, inte hero.
- PPTX: samma familj. Fallback Arial. Rubrik 28 pt, bröd 18 pt, etikett 12 pt, linjekod 14 pt.
- Bokfigur: etikett 8–9 pt, linjekod 8 pt, callout-siffra 8 pt i disken. Svart 100 % K.

Ingen andra familj för UI. Ingen serif i figurer.

---

## Tokens (bläck, papper, hårstreck)

| Token | Värde | Användning |
| --- | --- | --- |
| `--ink` | `#111111` | Text, regler, diskar, boxlinjer. Print: 100 % K |
| `--paper` | `#FFFFFF` | Sid-, slide- och figurgrund |
| `--rule` | `1px solid #111111` | Hårstreck. Print: 0.35 pt |
| `--rule-heavy` | `2px solid #111111` | FARA-ram, aktiv stationsmarkör |
| `--muted` | `#111111` at 100 %, size down — inte grå text | Hierarki via storlek och vikt, inte blekgrått |
| `--fill-obs` | `--paper` med `--rule` | OBS-modul |
| `--fill-fara` | `--ink` i huvudet, `--paper` i kroppen | FARA-modul |

Färg är **linje-ID**, inte dekoration och inte semantik (säkerhet är inte “rött”). Kromet är svart på vitt. Linjefärg syns bara på linjekodens lozenge, på kartstreck, och som 4 px vänsterkant när en modul är aktiv.

---

## Linjer M01–M12

Tolv linjer = tolv låsta moduler. En färg var. Identitet är **koden**, färgen är hjälp på skärm.

| Kod | Linje (svensk etikett) | Färg | Print (gråskala) |
| --- | --- | --- | --- |
| M01 | Elsäkerhet | `#E6002D` | Svart lozenge, vit kod. Streck: heldragen |
| M02 | Isolering | `#F39700` | Svart lozenge. Streck: lång streckad |
| M03 | Resistiv DC | `#8A99A3` | Svart lozenge. Streck: prick-streck |
| M04 | Enfas AC | `#00A7DB` | Svart lozenge. Streck: dubbel tunn |
| M05 | Trefas | `#00B261` | Svart lozenge. Streck: heldragen tjock |
| M06 | Maskiner | `#E85298` | Svart lozenge. Streck: streck-prick-streck |
| M07 | Eltavla | `#8F76D6` | Svart lozenge. Streck: heldragen |
| M08 | Verktyg | `#00ADA9` | Svart lozenge. Streck: streckad |
| M09 | Ritningar | `#C4A35A` | Svart lozenge. Streck: dubbel |
| M10 | Hållkrets | `#9C5E31` | Svart lozenge. Streck: prickad |
| M11 | Elarbete | `#0078C8` | Svart lozenge. Streck: heldragen |
| M12 | Felsökning | `#5A2D27` | Svart lozenge. Streck: tjock streckad |

Lozenge: rektangel, **0 radius**. Höjd = 1.15 em av koden. Padding 0.15 em 0.4 em. På skärm: linjefärg i fyllnad, vit kod. I KDP: svart fyllnad, vit kod. Aldrig rund pill (980 px är död).

Skriv koden som `M01` inte `m1` och inte `Modul 1` i kromet. Modulnamnet står bredvid, inte inuti lozengen.

---

## Stationer V1–V9

Nio kalenderveckor = nio stationer **och** nio stamlinjer. Varje V-kod har egen färg (linje-ID), skild från M-linjerna. Identitet är koden. På kartan är V-stammen den horisontella spåren; M-linjerna ansluter.

| Kod | Station | Stannande M-linjer | Färg | Print (gråskala) |
| --- | --- | --- | --- | --- |
| V1 | Vecka 1 | M01 | `#1A1A1A` | Svart kvadrat, vit kod. Stam: heldragen |
| V2 | Vecka 2 | M02 | `#6B2D5B` | Svart kvadrat. Stam: streckad |
| V3 | Vecka 3 | M03 | `#245C3A` | Svart kvadrat. Stam: prick-streck |
| V4 | Vecka 4 | M04 | `#1B3A5C` | Svart kvadrat. Stam: dubbel tunn |
| V5 | Vecka 5 | M05 | `#5C3B00` | Svart kvadrat. Stam: heldragen tjock |
| V6 | Vecka 6 | M06 | `#3D2458` | Svart kvadrat. Stam: streck-prick |
| V7 | Vecka 7 | M07 · M08 (byte) | `#0E4A4A` | Svart kvadrat. Stam: dubbel |
| V8 | Vecka 8 | M09 · M10 (byte) | `#4A3B2A` | Svart kvadrat. Stam: prickad |
| V9 | Vecka 9 | M11 · M12 (byte) | `#2A3340` | Svart kvadrat. Stam: tjock streckad |

Stationsmarkör: kvadrat, **0 radius**, kod `V1` i 600 tabular. På skärm: V-färgen i fyllnad, vit kod. I KDP: svart fyllnad, vit kod. Aktiv station: 2 px ink-ram utanpå. Byte-station (V7–V9): V-kvadrat plus två M-lozenger sida vid sida, inte ett blandat färgfält.

Karta (kursöversikt): horisontell V-stam i respektive V-färg, M-streck in i stationen i M-färg. Som metro, inte som veckorutor i en LMS-grid. Skriv `V1` inte `v1` och inte `Vecka 1` i kromet — veckonamnet står bredvid.

---

## OBS- och FARA-moduler

Pillerask / JIS-varning. Boxade. 0 radius. Svenska ord.

**OBS** (upplysning, inte nöd)

```
┌─ OBS ─────────────────────────┐
│  En mening. Inte ett stycke.  │
└───────────────────────────────┘
```

- Ram: `--rule` (1 px ink)
- Tab uppe till vänster: rektangel, ink-fyllnad, vit text `OBS` 600 11 px, tracking 0.08 em
- Kropp: paper, ink-text 16 px (sajt) / 12 pt (PPTX) / 9 pt (bok)
- Inte gul. Inte ikon. Inte trekant.

**FARA** (fara, stopp, gör inte)

```
████ FARA ██████████████████████
│  En mening. Vad som händer.  │
└──────────────────────────────┘
```

- Huvudlist: 100 % ink, vit `FARA` 600, tracking 0.08 em
- Kropp: paper, ink, `--rule-heavy` runt hela
- Inte röd (rött är M01:s linjefärg). Kontrast via svart fyllnad, inte hue.

En box, en mening. Inte nästlade varningar. Inte emoji. Inte “Viktigt!”.

---

## Numrerade callout-diskar

För figurer och slides. Som metro-utgångsnummer / pillerasks steg.

- Cirkel. Diameter: sajt 28 px, PPTX 28 pt, bok 6.5 mm.
- Fyllnad `--ink`, siffra vit, gothic 600 tabular.
- Nummer 1, 2, 3 … aldrig ①-tecken (de ritar snett i PPTX och KDP).
- Disk på figuren, samma nummer i bildtexten: `1  Stötväg in i skrov`.
- Max 7 diskar per figur. Ingen pil-soup. Ingen färgkod per disk — disken är alltid ink.
- Placera disken på tom yta, inte på en linje. Ledare: hårstreck 0.35 pt, rakt, inga kurvor.

---

## Tre skal

Samma system. Olika densitet. `html data-shell="elev|larare|bok"`.

**elev** (lära)
Stam = stationer V1–V9. Eleven går en station i taget. Mått ~40 rem. Linjelozenge + stationskod i nav. Vecka som plattform, inte som kortgitter.

**lärare** (undervisa)
Stam = linjer M01–M12. Bredare ~60 rem. Bildspel med callout-diskar. Anteckning = OBS-modul, inte grå sidospalt. Facit och handledning syns. Stationsbyte (V7–V9) utmärkt.

**bok** (läsa)
Spalt ~38 rem. Bröd 18 px / 1.5 gothic (ingen serif). Figurer med diskar och linjekod uppe till vänster (`M03` lozenge). Kapitel = linje. Inga frostad bars. Kapitel-nav: föregående/nästa station, hårstreck.

Gate (lösen): paper sheet, hårstreck, 0 radius, stor gothic titel, ingen blur.

Nav: paper, 1 px ink under. Inte frostat. Aktiv länk = lozenge eller 4 px linjefärg vänster, inte underline-pill.

---

## KDP / gråskala

Paperback är svart på vitt. Färg får inte bära mening.

- Alltid koden (M05, V3, OBS, FARA, 1) synlig.
- Lozenger i tryck: svart fyllnad, vit kod. Linjefärg släpps.
- Linjer på karta: strecktyp enligt tabellen, inte hue.
- Callout-diskar: redan ink. De överlever 1-bit.
- Miniimi-kontrast text: 100 % K. Ingen 40 %-grå bröd.
- Hårstreck ≥ 0.35 pt. Inte hairline som försvinner i KDP-pod.
- Figurbredd: spalt, inte utfall. 7.00 × 10.00 in, svart tryck, vitt papper.

---

## PPTX

- 16:9. Master: paper, ink, hårstreck i sidfot med `Mxx` + `Vx` + sidnummer tabular.
- Titelrad: linjelozenge + modulnamn. Inte en grön list.
- En slide, en idé. Callout-diskar på diagram, samma nummer i punktlista till höger.
- OBS/FARA som box-moduler, inte SmartArt.
- Ingen skugga, ingen gradient, ingen avrundning.

---

## Sajtkrom (kontrakt till Skylt)

Behåll befintliga class-namn (`.top`, `.main`, `.card`, `.week-grid`, `.notes`, …). Byt ytan:

- 0 border-radius överallt
- Nav: solid paper + hårstreck, ingen blur
- Typ: IBM Plex Sans (eller Noto Sans), aldrig SF Pro / Palatino
- Primärknapp: ink-fyllnad, vit text, 0 radius. Ghost: hårstreck, ink-text
- Kort: hårstreck, paper, ingen skugga
- Linjelozenge för aktuell modul i `.course-bar`
- `data-shell` styr spalt och densitet som ovan

Rör inte lektionstext, kapitel eller quiz-innehåll.

---

## Förbjudet i krom och figurer

- Apple-glas, SF Pro, 980-piller, ett accent
- Palatino och all serif
- Material, gradient, drop shadow som djup
- Färg som enda signal (utan kod)
- Japansk copy, katakana-etiketter, “Tokyo” som dekoration
- Ikoner som ersätter OBS/FARA
- Rundade callouts i annan färg än ink
- Dekorativa IP-tabeller, extra accentregnbåge, “modern SaaS”

---

Version: v3. 2026-08-30. Design äger systemet. Kurs och Manus äger texten. Figur ritar mot denna spec. Skylt bygger krom mot denna spec.
