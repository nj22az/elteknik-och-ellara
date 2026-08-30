# Elteknik och ellära

YH-course **Elteknik och ellära** (45 credits) in *Elingenjör, fartyg och automation*, plus the matching KDP paperback.

Live: https://nj22az.github.io/elteknik-och-ellara/

## Three logins (courtesy gate)

The repo is **public**. The password is a courtesy gate only (SHA-256 in the browser, role stored in `sessionStorage`). Anyone can clone the files.

| Roll | Interface | Password | `elteknik-role` | `data-shell` |
| --- | --- | --- | --- | --- |
| Elev | Learn | `Fartyg45` | `student` | `elev` |
| Lärare | Teach | `Larare45` | `teacher` | `larare` |
| Bok | Read | `Bok45` | `book` | `bok` |

Pick a role on the unlock screen, then the password for that role. The wrong password on a role fails (even if it is another role password).

- **Elev:** start vecka 1, nine week cards (Lektion → Kapitel → Bildspel → Quiz), interactive quiz without `## Facit`, progress in `localStorage`, labbdag as a ticket, written exam student sheet only. No teacher facit.
- **Lärare:** “Så här kör du veckan”, classroom post, 16-slide talk track, quiz with facit, student lesson, book chapter, G–VG–IG. Facit unlocked including `kurs/prov/skriftligt-prov-facit.md`. Nav: Vecka · Körschema · Facit · Labbdag · Lås.
- **Bok:** immersive reader only. Cover *Elteknik och ellära* / *Fartyg och automation*, twelve chapters, kapitellista, prev/next. No quizzes, classroom, or facit.

## Status (2026-08-30)

Twelve modules = twelve book chapters. Nine calendar weeks. One physical lab day after week 8. Distans in Google Classroom otherwise. Grades IG / G / VG. 1 MΩ is guidance, not shall.

## Layout

```
bok/                 12 chapters, figures, kapitellista
kurs/kurskarta/      12-module spine
kurs/lektioner/      student lesson sheets
kurs/lararhandledning/  classroom posts, slides, quizzes
kurs/prov/           student sheet + teacher facit
site/                GitHub Pages app (Apple-like chrome)
kdp/                 print/Kindle production notes
kallpack/            citation levels and official URLs (paraphrase only)
```

## Locked product choices

- Title: *Elteknik och ellära*. Subtitle: *Fartyg och automation*
- Not STCW ETO. Grades IG / G / VG
- 100% remote Google Classroom except one physical yard lab day after week 8
- TSFS 2017:26 chapter 5 = functional shall for national shipping. 1 MΩ is guidance, not shall. TSFS 2024:58 shore power does not apply to this track.
- Visual chrome: `site/riktlinje.md` (system-ui / SF, accent `#1f4d3a`, frosted nav, `data-shell` elev | larare | bok). Palatino is out.

## Clone

```bash
git clone https://github.com/nj22az/elteknik-och-ellara.git
```

Then open the folder in Cursor or any editor.
