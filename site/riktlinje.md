# Visuell riktlinje

Chrome för sajten. Inte en lektion. Svenska etiketter. Ett accent. Mycket luft.

## Färg

Svart, vitt, grått — och **en** grön. Inget mer.

| Token | Värde | Användning |
| --- | --- | --- |
| `--ink` | `#1d1d1f` | Brödtext, rubriker |
| `--muted` | `#6e6e73` | Kicker, lead, hjälptext |
| `--line` | `rgba(0,0,0,.08)` | Hårstreck, 1 px |
| `--bg` | `#f5f5f7` | Sidbakgrund |
| `--paper` | `#ffffff` | Kort, sheet, kortyta |
| `--accent` | `#1f4d3a` | **Enda** accent: länkar, primärknapp, aktiv nav-text |
| `--accent-soft` | `rgba(31, 77, 58, .12)` | Aktiv nav-fyllnad, rätt svar, mjuk hover |
| `--err` | `#8b1e1e` | Fel, felaktigt svar |
| `--nav-bg` | `rgba(245, 245, 247, .72)` | Frostat nav |

Aktiv nav: `--accent-soft` som fyllnad, `--accent` som text. Ingen infälld understreckslist.

## Typ

Stack (överallt, även quiz-knappar):

`-apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", system-ui, sans-serif`

- Bröd: **17 px / 1.47**, `-webkit-font-smoothing: antialiased`
- Display (h1 på gate/start): ~**2.5 rem (40 px)**, vikt **600**, tracking **−0.022 em**
- Mindre UI (kicker, nav, meta): samma stack, inte en andra familj
- Lärarskal får 16 px för skanning. Bokskal 19 px / 1.6 för läsning.

## Layout

- Mått styrs av skal (se nedan). Inte den gamla 760 px-spalten som default överallt.
- `main`: padding ca **3 rem 1.6 rem 5 rem**. Sektionsluckor **2 rem+**.
- Nav `.top`: sticky, `--nav-bg`, `backdrop-filter: saturate(180%) blur(20px)` plus `-webkit-` prefix, 1 px hårstreck `--line`. Inte en solid vit tegelvägg.
- Kort, CTA, gate, quiz, slide: radie **16 px**, hårstreck, mycket lätt skugga.
- Knappar och nav-piller: `border-radius: 980px`.
- Gate: centrerat Apple-sheet — stor titel, luft, vitt/frostat kort 16 px.

## Tre skal

Sätts på `<html data-shell="…">`.

**elev** (`lära`) — default  
Mått ~**40 rem**. Stor typ, luftiga veckorutnät, path och kort med luft. Kursens startsida, vecka, labb, prov.

**lärare** (`undervisa`)  
Mått ~**60 rem**. `.main` får kännas brett. Bildspel och `.notes` mer närvarande: vänster streck i `--accent`, inte grått. Något tätare (16 px ok). Samma typsnitt.

**bok** (`läsa`)  
Mått ~**38 rem**. Bröd **19 px / 1.6**. Extra vertikal padding. Tystare krom (`.course-bar` sparsam). Figurer med radie, inte tung svart ram. Kapitel-nav rymligt.

## Förbjudet

- Palatino, Iowan, Georgia eller någon serif — även i quiz-alternativ.
- Andra accentfärger (blå länkar, gul varning, lila pills).
- Tät lärobokstabell som krom (nav, kort, quiz, knappar).
- Infälld grön understreckslist på aktiv nav.
- Solid vit nav-tegel. Material-skuggor. 1.6 rem Palatino-h1.
