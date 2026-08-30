"""Rebuild pptx/vecka-01.pptx … vecka-05.pptx to v3 chrome (riktlinje v3).

Opens each original deck, copies speaker notes verbatim, restyles slides
with the same chrome as build_master.py. Does not rewrite classroom markdown
or book figures. Does not touch vecka-06..09 or kurs-overblick.pptx.

Backups of the pre-restyle files live in /tmp/pptx-bak/ (not in the repo).
"""
from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_master import (  # noqa: E402
    INK,
    PAPER,
    WHITE,
    _strip_calibri_zip,
    add_rect,
    add_text_box,
    blank,
    chrome_footer,
    chrome_title_row,
    disk,
    fara_module,
    hairline,
    m_lozenge,
    obs_module,
    patch_theme,
    set_single,
    v_square,
)
from v3_tokens import (  # noqa: E402
    BOK,
    M_LINES,
    PPTX_BODY_PT,
    PPTX_CODE_PT,
    PPTX_DIR,
    PPTX_HEADING_PT,
    PPTX_LABEL_PT,
    SLIDE_IN,
    V_STATIONS,
)

BAK = Path("/tmp/pptx-bak")


def hex_rgb(tup) -> str:
    return f"{tup[0]:02X}{tup[1]:02X}{tup[2]:02X}"


def get_notes(slide) -> str:
    try:
        return slide.notes_slide.notes_text_frame.text
    except Exception:
        return ""


def put_notes(slide, text: str) -> None:
    tf = slide.notes_slide.notes_text_frame
    tf.text = text if text is not None else ""


def new_prs(m_code: str, v_code: str) -> Presentation:
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_IN[0])
    prs.slide_height = Inches(SLIDE_IN[1])
    m = M_LINES[m_code]["color"]
    v = V_STATIONS[v_code]["color"]
    patch_theme(
        prs,
        accent1=hex_rgb(m),
        accent2=hex_rgb(v),
        accent3="111111",
        accent4="111111",
    )
    return prs


def heading(slide, text: str, *, top=0.90, height=0.48):
    return add_text_box(
        slide,
        Inches(0.45),
        Inches(top),
        Inches(12.4),
        Inches(height),
        text,
        size=PPTX_HEADING_PT,
        weight=600,
        color=INK,
        anchor=MSO_ANCHOR.BOTTOM,
    )


def est_h(text: str, width_in: float = 11.4, pt: float = PPTX_BODY_PT) -> float:
    # ~0.55 em average char width for IBM Plex Sans 18pt
    cpl = max(18, int(width_in * 72.0 / (pt * 0.52)))
    lines = max(1, (len(text) + cpl - 1) // cpl)
    return 0.28 * lines + 0.08


def add_disk_list(slide, items, *, y0=1.50, numbered=True, x=0.50, width=12.0):
    y = y0
    for i, text in enumerate(items, start=1):
        if numbered:
            disk(slide, Inches(x), Inches(y), i)
            d_in = 28 / 72.0
            tx = x + d_in + 0.16
            h = max(d_in, est_h(text, width - 0.7))
        else:
            sq = Inches(0.10)
            add_rect(
                slide,
                Inches(x),
                Inches(y + 0.10),
                sq,
                sq,
                fill=INK,
                line=None,
            )
            tx = x + 0.24
            h = max(0.36, est_h(text, width - 0.4))
        add_text_box(
            slide,
            Inches(tx),
            Inches(y),
            Inches(width - (tx - x)),
            Inches(h),
            text,
            size=PPTX_BODY_PT,
            weight=400,
            color=INK,
            anchor=MSO_ANCHOR.TOP,
        )
        y += h + 0.10
    return y


def add_paras(slide, lines, *, y0=1.50, x=0.45, width=12.4, size=PPTX_BODY_PT, weight=400):
    y = y0
    for text in lines:
        h = max(0.40, est_h(text, width, size) + 0.06)
        add_text_box(
            slide,
            Inches(x),
            Inches(y),
            Inches(width),
            Inches(h),
            text,
            size=size,
            weight=weight,
            color=INK,
            anchor=MSO_ANCHOR.TOP,
        )
        y += h + 0.10
    return y


def two_panels(slide, left_h, left_b, right_h, right_b, *, y=1.50):
    add_rect(
        slide,
        Inches(0.45),
        Inches(y),
        Inches(6.00),
        Inches(4.40),
        fill=PAPER,
        line=INK,
        line_pt=0.75,
    )
    add_rect(
        slide,
        Inches(6.85),
        Inches(y),
        Inches(6.00),
        Inches(4.40),
        fill=PAPER,
        line=INK,
        line_pt=0.75,
    )
    add_text_box(
        slide,
        Inches(0.65),
        Inches(y + 0.18),
        Inches(5.6),
        Inches(0.42),
        left_h,
        size=PPTX_BODY_PT,
        weight=600,
        color=INK,
    )
    add_text_box(
        slide,
        Inches(0.65),
        Inches(y + 0.70),
        Inches(5.6),
        Inches(3.4),
        left_b,
        size=PPTX_BODY_PT,
        weight=400,
        color=INK,
        anchor=MSO_ANCHOR.TOP,
    )
    add_text_box(
        slide,
        Inches(7.05),
        Inches(y + 0.18),
        Inches(5.6),
        Inches(0.42),
        right_h,
        size=PPTX_BODY_PT,
        weight=600,
        color=INK,
    )
    add_text_box(
        slide,
        Inches(7.05),
        Inches(y + 0.70),
        Inches(5.6),
        Inches(3.4),
        right_b,
        size=PPTX_BODY_PT,
        weight=400,
        color=INK,
        anchor=MSO_ANCHOR.TOP,
    )


def ink_table(slide, headers, rows, *, y=1.50):
    x = Inches(0.45)
    w = Inches(12.4)
    col0 = Inches(8.2)
    col1 = w - col0
    row_h = Inches(0.52)
    # header
    head = add_rect(slide, x, Inches(y), w, row_h, fill=INK, line=None)
    set_single(
        head,
        headers[0],
        size=PPTX_LABEL_PT,
        weight=600,
        color=WHITE,
        align=PP_ALIGN.LEFT,
        margin_pt=10,
    )
    h1 = add_rect(slide, x + col0, Inches(y), col1, row_h, fill=INK, line=None)
    set_single(
        h1,
        headers[1],
        size=PPTX_LABEL_PT,
        weight=600,
        color=WHITE,
        align=PP_ALIGN.LEFT,
        margin_pt=10,
    )
    yy = y + row_h.inches
    for i, row in enumerate(rows):
        add_rect(
            slide,
            x,
            Inches(yy),
            w,
            row_h,
            fill=PAPER,
            line=INK,
            line_pt=0.75,
        )
        add_text_box(
            slide,
            x,
            Inches(yy),
            col0,
            row_h,
            row[0],
            size=PPTX_BODY_PT,
            weight=400,
            color=INK,
            anchor=MSO_ANCHOR.MIDDLE,
        )
        add_text_box(
            slide,
            x + col0,
            Inches(yy),
            col1,
            row_h,
            row[1],
            size=PPTX_BODY_PT,
            weight=400,
            color=INK,
            anchor=MSO_ANCHOR.MIDDLE,
        )
        yy += row_h.inches


def add_picture_fit(slide, path, left, top, max_w, max_h):
    im = Image.open(path)
    ar = im.size[0] / im.size[1]
    w = max_w
    h = w / ar
    if h > max_h:
        h = max_h
        w = h * ar
    slide.shapes.add_picture(str(path), left, top, width=Inches(w), height=Inches(h))
    return w, h


def figure_slide(slide, png: Path, legend: list[str]):
    max_w, max_h = 8.35, 5.95
    # leave room for legend on the right
    legend_x = 8.95
    pic_w, pic_h = add_picture_fit(
        slide, png, Inches(0.40), Inches(0.85), max_w, max_h
    )
    if pic_w > 8.4:
        # shouldn't happen
        pass
    add_text_box(
        slide,
        Inches(legend_x),
        Inches(0.85),
        Inches(4.0),
        Inches(0.32),
        "Legend",
        size=PPTX_LABEL_PT,
        weight=600,
        color=INK,
        tracking_em=0.06,
        caps=True,
    )
    y = 1.22
    gap = 0.62 if len(legend) > 4 else 0.78
    if len(legend) >= 5:
        gap = 0.58
    for i, text in enumerate(legend, start=1):
        _, d = disk(slide, Inches(legend_x), Inches(y), i, diameter_pt=22)
        add_text_box(
            slide,
            Inches(legend_x) + d + Inches(0.10),
            Inches(y),
            Inches(3.55),
            Inches(max(d.inches + 0.12, est_h(text, 3.4, 12) + 0.12)),
            text,
            size=12,
            weight=400,
            color=INK,
            anchor=MSO_ANCHOR.TOP,
        )
        y += gap


def fara_list(slide, items, *, y=1.50):
    h = 4.40
    l, t, w = Inches(0.45), Inches(y), Inches(12.4)
    add_rect(slide, l, t, w, Inches(h), fill=PAPER, line=INK, line_pt=1.5)
    head_h = Inches(0.36)
    head = add_rect(slide, l, t, w, head_h, fill=INK, line=None)
    set_single(
        head,
        "FARA",
        size=PPTX_LABEL_PT,
        weight=600,
        color=WHITE,
        align=PP_ALIGN.LEFT,
        tracking_em=0.08,
        caps=True,
        margin_pt=8,
    )
    add_disk_list(
        slide,
        items,
        y0=y + 0.50,
        numbered=False,
        x=0.65,
        width=11.9,
    )


def cover_slide(prs, spec, m_code, v_code, number):
    s = blank(prs)
    add_text_box(
        s,
        Inches(0.45),
        Inches(1.85),
        Inches(12.4),
        Inches(0.40),
        spec["kicker"],
        size=PPTX_LABEL_PT,
        weight=500,
        color=INK,
        tracking_em=0.06,
        caps=True,
    )
    add_text_box(
        s,
        Inches(0.45),
        Inches(2.25),
        Inches(12.4),
        Inches(0.70),
        spec["title"],
        size=PPTX_HEADING_PT,
        weight=600,
        color=INK,
    )
    hairline(s, Inches(0.45), Inches(3.00), Inches(4.2))
    add_text_box(
        s,
        Inches(0.45),
        Inches(3.15),
        Inches(12.4),
        Inches(0.40),
        spec["sub"],
        size=PPTX_BODY_PT,
        weight=500,
        color=INK,
    )
    add_text_box(
        s,
        Inches(0.45),
        Inches(3.60),
        Inches(12.4),
        Inches(0.80),
        spec["line"],
        size=PPTX_BODY_PT,
        weight=400,
        color=INK,
        anchor=MSO_ANCHOR.TOP,
    )
    sh, mw, mh = m_lozenge(s, Inches(0.45), Inches(4.70), m_code, code_pt=PPTX_CODE_PT)
    add_text_box(
        s,
        Inches(0.45) + mw + Inches(0.12),
        Inches(4.70),
        Inches(4.5),
        mh,
        M_LINES[m_code]["name"],
        size=PPTX_BODY_PT,
        weight=600,
        color=INK,
    )
    vx = Inches(7.2)
    v_square(s, vx, Inches(4.68), v_code, active=True)
    vs = Inches(max(PPTX_CODE_PT * 1.35, 16) / 72.0)
    add_text_box(
        s,
        vx + vs + Inches(0.10),
        Inches(4.70),
        Inches(2.4),
        mh,
        V_STATIONS[v_code]["name"],
        size=PPTX_LABEL_PT,
        weight=500,
        color=INK,
    )
    chrome_footer(s, m_code, v_code, number)
    return s


def content_slide(prs, spec, m_code, v_code, number):
    s = blank(prs)
    chrome_title_row(s, m_code, v_code)
    kind = spec["kind"]
    if kind == "lesson_title":
        heading(s, spec["title"])
        add_paras(s, spec["lines"], y0=1.55)
    elif kind == "figure":
        figure_slide(s, spec["png"], spec["legend"])
    elif kind == "bullets":
        heading(s, spec["title"])
        y0 = 1.52
        if spec.get("lead"):
            y0 = add_paras(s, [spec["lead"]], y0=1.48, weight=400) + 0.06
        add_disk_list(
            s,
            spec["items"],
            y0=y0,
            numbered=spec.get("numbered", False),
        )
    elif kind == "body":
        heading(s, spec["title"])
        add_paras(s, spec["lines"], y0=1.52)
        extra = spec.get("sublines") or []
        if extra:
            add_paras(s, extra, y0=3.35, size=PPTX_BODY_PT, weight=400)
    elif kind == "two_tracks":
        heading(s, spec["title"])
        two_panels(
            s,
            spec["left_h"],
            spec["left"],
            spec["right_h"],
            spec["right"],
            y=1.52,
        )
    elif kind == "table":
        heading(s, spec["title"])
        ink_table(s, spec["headers"], spec["rows"], y=1.52)
    elif kind == "obs":
        heading(s, spec["title"])
        obs_module(s, Inches(0.45), Inches(1.55), Inches(12.4), Inches(2.10), spec["sentence"])
        extra = spec.get("lines") or []
        if extra:
            add_paras(s, extra, y0=3.85)
    elif kind == "fara":
        heading(s, spec["title"])
        fara_module(s, Inches(0.45), Inches(1.55), Inches(12.4), Inches(2.20), spec["sentence"])
        extra = spec.get("lines") or []
        if extra:
            add_paras(s, extra, y0=3.95)
    elif kind == "fara_list":
        heading(s, spec["title"])
        fara_list(s, spec["items"], y=1.52)
    elif kind == "gv":
        heading(s, spec["title"])
        if spec.get("lead"):
            add_paras(s, [spec["lead"]], y0=1.48)
            y = 2.45
        else:
            y = 1.52
        two_panels(s, "G", spec["g"], "VG", spec["vg"], y=y)
    elif kind == "quiz":
        heading(s, spec["title"])
        y = 1.50
        if spec.get("lead"):
            y = add_paras(s, [spec["lead"]], y0=1.50, weight=500)
        add_disk_list(s, spec["items"], y0=y + 0.05, numbered=False)
        if spec.get("foot"):
            add_paras(s, [spec["foot"]], y0=5.55, weight=400)
    elif kind == "not_in":
        heading(s, spec["title"])
        add_paras(s, [spec["body"]], y0=1.52)
        if spec.get("lia"):
            add_paras(s, [spec["lia"]], y0=4.20)
    else:
        raise ValueError(f"unknown kind {kind}")
    chrome_footer(s, m_code, v_code, number)
    return s


def build_week(week: dict, notes: list[str]) -> Presentation:
    m_code, v_code = week["m"], week["v"]
    prs = new_prs(m_code, v_code)
    specs = week["slides"]
    if len(specs) != len(notes):
        # still build; notes applied up to min length
        pass
    for i, spec in enumerate(specs, start=1):
        if spec["kind"] == "cover":
            s = cover_slide(prs, spec, m_code, v_code, i)
        else:
            s = content_slide(prs, spec, m_code, v_code, i)
        if i - 1 < len(notes):
            put_notes(s, notes[i - 1])
    return prs


def weeks() -> list[dict]:
    return [
        week01(),
        week02(),
        week03(),
        week04(),
        week05(),
    ]


def week01() -> dict:
    png = BOK / "figur-1-1-stotvag-ventil-skarm.png"
    return {
        "file": "vecka-01.pptx",
        "m": "M01",
        "v": "V1",
        "slides": [
            {
                "kind": "cover",
                "kicker": "Elteknik och ellära  ·  45 YH-poäng  ·  Vecka 1",
                "title": "Stötväg ombord",
                "sub": "Modul 1  ·  elsäkerhet, stötar, elens verkningar",
                "line": "Distans. SHK 2024:04 / STENA GERMANICA som låst fall. Inte megger den här veckan.",
            },
            {
                "kind": "lesson_title",
                "title": "1.1 Stötväg ombord",
                "lines": [
                    "Elteknik och ellära · vecka 1 · distans",
                    "SHK 2024:04 som namngivet fall. Inte megger.",
                ],
            },
            {
                "kind": "figure",
                "png": png,
                "legend": [
                    "Packning saknas mellan kontakt och spole.",
                    "Ingen PE.",
                    "Stötväg: hölje · hand · skrov.",
                    "IR-vakt ser bara huvudnätet.",
                    "Sidokrets lokalt jordad, utanför IR.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Efter den här veckan",
                "items": [
                    "Peka stötväg in och ut",
                    "Säg att ELSÄK-JFB inte är skyddet ombord",
                    "Koppla en SMS-punkt: packning, jord, eller krets utanför IR",
                    "VG: varför IR-vakten var tyst, vad du gör innan beröring, stöt → vård iland",
                ],
            },
            {
                "kind": "two_tracks",
                "title": "Två spår",
                "left_h": "Elektriker",
                "left": "Leta inte JFB.",
                "right_h": "Ingenjör",
                "right": "Läckagesökning är elarbete när komponenten kan vara spänningssatt.",
            },
            {
                "kind": "bullets",
                "title": "Stötväg",
                "items": [
                    "Ström genom kroppen: en väg in, en väg ut",
                    "Ofta skrov",
                    "Fukt gör höljet till ledare",
                    "Pannrum, barlastpump, magnetventil",
                    "Inte kaj. Inte EX. Inte nödgenerator.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Varför vi bryr oss",
                "items": [
                    "Kramp, släppförmåga, hjärta — G-golv, inte medicinkurs",
                    "Höjd: stöten dödar inte alltid. Fallet kan göra det. (TS olyckor-sida, upplysning)",
                ],
            },
            {
                "kind": "body",
                "title": "Skall, en mening",
                "lines": [
                    "El ombord ska vara gjord och monterad så att risken för stöt — och för brand, kortslutning och explosion — blir så liten som det går.",
                    "TSFS 2017:26 5 kap. 5 §. Parafras. Inte lagtext på sliden.",
                ],
            },
            {
                "kind": "table",
                "title": "Inte skall",
                "headers": ["Påstående", "Nivå"],
                "rows": [
                    ["”Så här görs kontroll”", "upplysning"],
                    ["1 MΩ", "upplysning, inte 5 §-skall"],
                    ["IR-vakt på ojordade kretsar > 50 V", "allmänna råd"],
                    ["Packning tillbaka", "avledning, ingen TS-rubrik"],
                ],
            },
            {
                "kind": "bullets",
                "title": "ELSÄK-hålet",
                "items": [
                    "Installationsregler styr i allmänhet inte på fartyg",
                    "Undantag: EMC (ELSÄK-FS 2016:3) — inte den här lektionens djup",
                    "ELSÄK-auktorisation räcker inte ensam",
                    "Inte upphävda 2008:1",
                    "”Båt på land = ELSÄK” är TS-webb, inte lag",
                ],
            },
            {
                "kind": "bullets",
                "title": "Inte JFB-jakt",
                "items": [
                    "Oftast ingen JFB i isolerat huvudnät (driftsäkerhet)",
                    "IR-vakt larmar. Den slår inte ifrån.",
                    "Den ser bara det nät den sitter på",
                    "En lokalt jordad sidokrets syns inte",
                ],
            },
            {
                "kind": "bullets",
                "title": "SMS, var rutinerna bor",
                "items": [
                    "FSL 2 kap. 9–10 §§: rutinerna i rederiets SMS, inte i huvudet",
                    "Olyckor-sidan: slitage, packning, skåp, genomföringar — byt i tid",
                    "Isolationsrutin i underhåll = SMS, övas i m2",
                ],
            },
            {
                "kind": "bullets",
                "title": "Germanica, fem punkter",
                "lead": "SHK 2024:04. Parafras, inte rapportbilaga.",
                "numbered": True,
                "items": [
                    "Packning saknades",
                    "Ingen skyddsjord",
                    "Kablar skiftade: ventilen spänningssatt så länge pumpen gick",
                    "Kretsen lokalt jordad, utanför IR — vakten tyst",
                    "Felen rörde inte driften → ingen indikation",
                ],
            },
            {
                "kind": "bullets",
                "title": "Rätt kedja",
                "numbered": True,
                "items": [
                    "Fas i hölje → våt hand → skrov",
                    "Packning + jord + sidokrets utanför IR",
                    "SMS: packning åter, jord, sidokrets övervakad eller behandlad som spänningssatt",
                    "Efter stöt: vård iland, inte ”skaka av det”",
                ],
            },
            {
                "kind": "fara_list",
                "title": "Stopp den här veckan",
                "items": [
                    "Ingen beröring av våt elkomponent",
                    "Ingen ”jag kan anläggningen”",
                    "Ingen megger som ersättning för stötbedömning",
                    "Ingen lucka på jobbet som läxa",
                ],
            },
            {
                "kind": "gv",
                "title": "Hemuppgift: labbprotokoll B",
                "lead": "Felanmälan: ”Det läcker vid pumpen, känn efter var.” Foto i Classroom. Inte ett namngivet övningsfartyg på intyg.",
                "g": "stötväg in/ut; minst två av packning / jord / utanför IR; en SMS-åtgärd du inte hoppar; ELSÄK-JFB är inte skyddet.",
                "vg": "fyra rader själv: varför IR var tyst; vad innan beröring och varför; stöt → iland.",
            },
            {
                "kind": "quiz",
                "title": "Quiz",
                "lead": "Två saker ni ska kunna skilja:",
                "items": [
                    "Skall: 5 kap. 1–7 §",
                    "Inte skall: ”Så här görs kontroll”, 1 MΩ",
                ],
                "foot": "Gör quizzen i Classroom den här veckan.",
            },
            {
                "kind": "not_in",
                "title": "Inte i 1.1",
                "body": "Meggerprocedur. 1 MΩ som labbgräns. Hållkrets. Losskoppling. IP-tabell. Intyg. Nöd. Landström. 2024:58. EX. Arduino.",
                "lia": "LIA: samma pekning under handledare. Isolation själv efter m2.",
            },
        ],
    }


def week02() -> dict:
    png = BOK / "figur-2-1-isolering-kedja-skarm.png"
    return {
        "file": "vecka-02.pptx",
        "m": "M02",
        "v": "V2",
        "slides": [
            {
                "kind": "cover",
                "kicker": "Elteknik och ellära  ·  45 YH-poäng  ·  Vecka 2",
                "title": "Isolering före arbete",
                "sub": "Modul 2  ·  SMS, kedjan innan handen",
                "line": "Distans. På papper. Megger med händerna = varvsdagen. Inte omberättad Germanica.",
            },
            {
                "kind": "lesson_title",
                "title": "2.1 Isolering före arbete",
                "lines": [
                    "Elteknik och ellära · vecka 2 · distans",
                    "På papper. Megger med händerna = varvsdagen.",
                ],
            },
            {
                "kind": "figure",
                "png": png,
                "legend": [
                    "FRÅN",
                    "LÅS/SKYLT",
                    "PROVA DÖD",
                    "MEGGER",
                ],
            },
            {
                "kind": "bullets",
                "title": "Efter den här veckan",
                "items": [
                    "Ordna SMS-kedjan innan arbete",
                    "Skilja IR *under drift* från megger *på avställd* grupp",
                    "Behandla 1 MΩ som upplysning, inte lag",
                    "Fylla protokoll från given bild och siffra",
                    "VG: motivera stegen; vad om varvet saknar megger",
                ],
            },
            {
                "kind": "two_tracks",
                "title": "Två spår",
                "left_h": "Elektriker",
                "left": "Referens är inte PE-skenan hemma.",
                "right_h": "Ingenjör",
                "right": "Tyst maskin är inte bevisad spänningslöshet.",
            },
            {
                "kind": "body",
                "title": "Skall, en mening",
                "lines": [
                    "El ombord ska vara gjord så att risken för stöt, brand och kortslutning blir så liten som det går. Innan du tar i en grupp: gör den död, *visa* att den är död, mät isolation, skriv det.",
                    "TSFS 2017:26 5 kap. 5 §. Parafras. SMS: rutinerna i rederiets organisation (FSL 2 kap. 9–10 §§). Utförande: fackmässigt (2 kap. 6 §). Inte ELSÄK-auktorisation som enda bevis.",
                ],
            },
            {
                "kind": "table",
                "title": "Inte skall",
                "headers": ["Påstående", "Nivå"],
                "rows": [
                    ["Isolationsprov (instrument ombord / fackman megger + protokoll)", "upplysning, “Så här görs kontroll”"],
                    ["1 MΩ", "upplysning. Inte 5 §-skall"],
                    ["IR-vakt på ojordade kretsar > 50 V", "allmänna råd"],
                    ["“t.ex. vart 6:e år”", "exempel, inte föreskrift"],
                    ["Packning tillbaka", "avledning"],
                ],
            },
            {
                "kind": "body",
                "title": "Två mätningar, två tider",
                "lines": [
                    "Under drift: IR-vakt. Larmar. Tar inte bort spänningen.",
                    "Före arbete på avställd grupp: från, lås, skylt, tvåpol död, *sedan* megger. Protokoll.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Kedjan",
                "numbered": True,
                "items": [
                    "Från",
                    "Lås / skylt",
                    "Tvåpolsprova död",
                    "Megger",
                    "Skriv värde och referens",
                    "Under upplysningsgräns → inte spänningssätt",
                    "Kåpa tillbaka",
                ],
            },
            {
                "kind": "bullets",
                "title": "SMS den här veckan",
                "items": [
                    "Inte räkna med JFB; räkna med IR-vakt",
                    "Packning/kåpa tillbaka (avledning, inte TS-rubrik)",
                    "Isolationsrutin i underhåll (upplysning; intervall = exempel)",
                    "Sidokrets utanför IR (punkten från 1.1, inte omberättad)",
                    "Stöt → vård iland",
                ],
            },
            {
                "kind": "bullets",
                "title": "1 MΩ i jobbet",
                "items": [
                    "Märk upplysning, inte lag",
                    "Givet värde under gräns: inte spänningssätt, skriv avvikelse",
                    "Inte “olagligt enligt 5 §”",
                ],
            },
            {
                "kind": "body",
                "title": "Fotoövningen",
                "lines": [
                    "Ticket: “230 V-grupp inredning, kabel bytt. Isolera på papper. Megga inte live.”",
                    "Två övningsfoton i Classroom:",
                    "IR-instrument *i drift*",
                    "Megger på *avställd* grupp: 2,4 MΩ och 0,4 MΩ",
                ],
            },
            {
                "kind": "body",
                "title": "Om varvet saknar megger",
                "lines": [
                    "VG-mening: tvåpolsprova död + flagga gapet. Inte hitta på en andra tavla. Inte live. Inte 440 V.",
                ],
            },
            {
                "kind": "body",
                "title": "Genomgånget fel",
                "lines": [
                    "230 V-grupp belysning inredning. Ingenjör: “den är av, jag såg brytaren.” Elektriker: megger mot PE som hemma, “bra” tal.",
                    "Saknas: lås/skylt, tvåpol mot stomme/skrov, megger på den *avställda* gruppen mot rätt referens, protokoll.",
                ],
            },
            {
                "kind": "fara_list",
                "title": "Stopp",
                "items": [
                    "Ingen megger på spänningssatt",
                    "Ingen lucka utan lås",
                    "Ingen “jag kan anläggningen”",
                    "Ingen händer-megger som läxa",
                ],
            },
            {
                "kind": "gv",
                "title": "Hemuppgift: protokoll",
                "lead": "Namn, grupp, kedja, given siffra, referens, 1 MΩ upplysning ja, en SMS-punkt.",
                "g": "kedja + IR vs megger + 0,4 inte tillslag + en SMS-punkt.",
                "vg": "motivera varje steg mot risk; gap om megger saknas.",
            },
            {
                "kind": "quiz",
                "title": "Quiz",
                "lead": "Tre saker:",
                "items": [
                    "1 MΩ är upplysning, inte lag",
                    "IR ≠ megger",
                    "0,4 MΩ = inte spänningssätt",
                ],
                "foot": "Gör quizzen i Classroom den här veckan.",
            },
            {
                "kind": "not_in",
                "title": "Inte i 2.1",
                "body": "Stötväg som 1.1-lektion. Nöd, EX, land, blackout. 230 mot 24 V (väntar på varvet). Hållkrets. Losskoppling som eget pass. Intyg som TS-produkt. Arduino.",
                "lia": "LIA: isolation enligt fartygets SMS, under handledning.",
            },
        ],
    }


def week03() -> dict:
    png = BOK / "figur-3-1-dc-matning.png"
    return {
        "file": "vecka-03.pptx",
        "m": "M03",
        "v": "V3",
        "slides": [
            {
                "kind": "cover",
                "kicker": "Elteknik och ellära  ·  45 YH-poäng  ·  Vecka 3",
                "title": "Resistiv DC",
                "sub": "Modul 3  ·  mät och räkna",
                "line": "Distans. Papper och ELV-foto. Inte trefas. Inte 440 V. Händer-DMM = varvsdagen.",
            },
            {
                "kind": "lesson_title",
                "title": "3.1 Resistiv DC: mät och räkna",
                "lines": [
                    "Elteknik och ellära · vecka 3 · distans",
                    "Papper och ELV-foto. Händer-DMM = varvsdagen, isolerad tränare.",
                ],
            },
            {
                "kind": "figure",
                "png": png,
                "legend": [
                    "Serie, 24 V",
                    "Parallell, 24 V",
                    "Rätt volt parallellt över last",
                    "Fel ampere över last — kortslutning",
                ],
            },
            {
                "kind": "bullets",
                "title": "Efter den här veckan",
                "items": [
                    "Räkna U, I, R i serie och parallell",
                    "Rätt polaritet",
                    "Volt över, ström i serie",
                    "Enkel beräkning stämmer mot given avläsning",
                    "VG: fel område = kort; motivera instrumentval",
                ],
            },
            {
                "kind": "two_tracks",
                "title": "Två spår",
                "left_h": "Elektriker",
                "left": "Minus är inte PE.",
                "right_h": "Ingenjör",
                "right": "Räkna I innan du klämmer på.",
            },
            {
                "kind": "body",
                "title": "Skall, en mening",
                "lines": [
                    "Mät så att du inte gör kortslutning eller stöt av mätningen. Rätt funktion, rätt polaritet, ström i serie, spänning över. Räkna slingan innan du kopplar.",
                    "TSFS 2017:26 5 kap. 5 §. Parafras: el ska vara gjord så att kortslutning och stöt minimeras. En DMM på fel område *är* en kortslutning.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Inte den här veckan",
                "items": [
                    "Trefas, enfas-AC (senare)",
                    "440 V, MSB, live fartygsnät",
                    "Isolation/megger (2.1)",
                    "1 MΩ som labbgräns",
                    "Händer-DMM hemma",
                ],
            },
            {
                "kind": "body",
                "title": "Räkna först",
                "lines": [
                    "Serie: samma I, U delas. Parallell: samma U, I delas. R = U/I.",
                    "Avläsning mot räkning: om de inte stämmer är det mätfel eller fel krets, inte “ungefär”.",
                ],
            },
            {
                "kind": "body",
                "title": "Serie och parallell",
                "lines": [
                    "Två R i serie: räkna I och U över varje. Två R i parallell: räkna I i varje gren.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Tre mätningar",
                "items": [
                    "Spänning: parallellt över komponenten, volt-område, röd mot plus",
                    "Ström: bryt slingan, mätare *i serie*, ström-område",
                    "Resistans: spänningslöst, ohm-område. Inte ohm på spänningssatt",
                ],
            },
            {
                "kind": "body",
                "title": "Polaritet",
                "lines": [
                    "Röd mot plus. Svart mot minus. Minus är inte PE. Skrov som retur är inte din-skena hemma.",
                ],
            },
            {
                "kind": "fara",
                "title": "Ampere över last = kort",
                "sentence": "Strömområde *över* last eller batteri = du har lagt en nästan noll-ohm-väg över källan. Säkring eller mätare dör. Det är kortslutning, inte en mätning.",
            },
            {
                "kind": "gv",
                "title": "Fotoövningen",
                "lead": "I Classroom: schema serie + parallell, U given. Foto 1: DMM volt-läge, rätt över last. Foto 2: DMM ampere-läge, felkopplad över last (märkt övning).",
                "g": "räkna; peka rätt volt; peka ut kortet; röd mot plus.",
                "vg": "en mening risk, fel område.",
            },
            {
                "kind": "body",
                "title": "Genomgånget fel",
                "lines": [
                    "24 V till magnetventil. Ingenjör: DMM på strömområde, mäter *över* polerna. Mätaren dör. Elektriker: polaritet baklänges, skyller på skrovet som nolla.",
                    "Första räkning: 24 V, last t.ex. 48 Ω → 0,5 A. Ström i serie, inte som volt över.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Rätt kedja",
                "numbered": True,
                "items": [
                    "Räkna I",
                    "Välj volt eller ampere medvetet",
                    "Polaritet",
                    "Spänning parallellt / ström i serie",
                    "Jämför med räkning",
                    "Fel område = kortslutningsrisk",
                ],
            },
            {
                "kind": "fara_list",
                "title": "Stopp",
                "items": [
                    "Amperemeter över batteri/last",
                    "Mätning på live MSB / 440 V",
                    "Polaritet “det går väl”",
                    "Tång runt ledare och läs “volt”",
                    "Händer-DMM som läxa",
                ],
            },
            {
                "kind": "quiz",
                "title": "Quiz",
                "lead": "Tre saker:",
                "items": [
                    "Ström mäts i serie",
                    "Röd mot plus; minus är inte PE",
                    "Ampere över last = kort",
                ],
                "foot": "Gör quizzen i Classroom den här veckan.",
            },
            {
                "kind": "not_in",
                "title": "Inte i 3.1",
                "body": "AC/trefas. Isolation/megger. Stötväg. 230 V-uttag och hållkrets. 1 MΩ som labbgräns. Live fartygsnät. Arduino.",
                "lia": "LIA: samma räkna-sedan-mät under handledning, inte på spänningssatt huvudtavla.",
            },
        ],
    }


def week04() -> dict:
    png = BOK / "figur-4-1-enfas-ac.png"
    return {
        "file": "vecka-04.pptx",
        "m": "M04",
        "v": "V4",
        "slides": [
            {
                "kind": "cover",
                "kicker": "Elteknik och ellära  ·  45 YH-poäng  ·  Vecka 4",
                "title": "Enfas AC",
                "sub": "Modul 4  ·  rms, mät och räkna",
                "line": "Distans. Papper och ELV-foto. Inte trefas. Inte 440 V.",
            },
            {
                "kind": "lesson_title",
                "title": "4.1 Enfas AC: rms, mät och räkna",
                "lines": [
                    "Elteknik och ellära · vecka 4 · distans",
                    "Papper och ELV-foto. Händer = varvsdagen, isolerad tränare eller död tavla.",
                ],
            },
            {
                "kind": "figure",
                "png": png,
                "legend": [
                    "230 V är rms, topp cirka 325 V",
                    "DMM i AC-läge",
                    "DMM i DC-läge — noll är inte bevisad död",
                ],
            },
            {
                "kind": "bullets",
                "title": "Efter den här veckan",
                "items": [
                    "Rms mot topp på sinus",
                    "I = U_rms / R på resistiv enfas",
                    "Läsa DMM i AC-läge",
                    "VG: DC-läge på AC är mätfel och risk",
                ],
            },
            {
                "kind": "two_tracks",
                "title": "Två spår",
                "left_h": "Elektriker",
                "left": "230 V ombord ≠ lägenhet.",
                "right_h": "Ingenjör",
                "right": "Rms innan du klämmer på.",
            },
            {
                "kind": "body",
                "title": "Skall, en mening",
                "lines": [
                    "Mät enfas så att mätningen inte blir stöt eller kort. AC-spänning läses som rms i AC-läge. Räkna slingan. Inte DC-område på AC. Inte live huvudtavla.",
                    "TSFS 2017:26 5 kap. 5 §. Parafras. Klistra inte lagtext.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Inte den här veckan",
                "items": [
                    "Trefas, fasföljd (m5)",
                    "440 V, MSB, live fartygsnät",
                    "Isolation/megger (2.1)",
                    "DC serie/parallell (3.1)",
                    "Händer-DMM hemma",
                ],
            },
            {
                "kind": "body",
                "title": "Rms och topp",
                "lines": [
                    "“230 V” är rms. På sinus: topp ≈ rms × √2, runt 325 V. DMM i AC-läge visar rms, inte toppen.",
                ],
            },
            {
                "kind": "body",
                "title": "Räkna resistiv enfas",
                "lines": [
                    "I = Urms/R.",
                    "Exempel i bladet: 230 V rms, 1 kΩ → I ≈ 0,23 A. Topp ≈ 325 V.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Mät AC",
                "items": [
                    "DMM AC V parallellt över last",
                    "Ström: AC-ström i serie, eller tång kring *en* ledare — inte som volt",
                    "Inte DC-läge på AC",
                    "AC har ingen fast plus. Inte “hitta nollan som PE”",
                ],
            },
            {
                "kind": "fara",
                "title": "DC-läge på AC är fel",
                "sentence": "Visningen ljuger eller mätaren far illa. Nära noll i DC-läge är inte bevisad spänningslöshet.",
            },
            {
                "kind": "body",
                "title": "230 V ombord ≠ lägenhet",
                "lines": [
                    "Inte lägenhetens TN. Referens kan vara skrov/IT, inte PE-nolla hemma. Isolation först = 2.1, inte “det sitter JFB”.",
                ],
            },
            {
                "kind": "gv",
                "title": "Fotoövningen",
                "lead": "I Classroom: sinus rms mot topp; resistiv enfas med U_rms och R. Foto 1: DMM AC V, avläsning. Foto 2: DMM DC V på samma AC-övning (märkt fel).",
                "g": "rms och ungefär topp; räkna I; välj AC-bilden; en mening att DC-bilden är fel läge.",
                "vg": "risk: falskt “av” eller skada. Koppla till 5 §.",
            },
            {
                "kind": "body",
                "title": "Genomgånget fel",
                "lines": [
                    "230 V-enfas till värmare. Ingenjör: DMM kvar i DC-läge. Visar noll eller skräp. “Det är av.” Elektriker: mäter mot skrov som PE, utgår från JFB.",
                    "Räkning som saknades: 230 V rms, 1 kΩ → 0,23 A. Topp ≈ 325 V.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Rätt kedja",
                "numbered": True,
                "items": [
                    "AC-läge",
                    "Rms i räkningen",
                    "Volt över / ström i serie",
                    "Jämför avläsning",
                    "Noll i DC-läge på AC är inte av",
                ],
            },
            {
                "kind": "fara_list",
                "title": "Stopp",
                "items": [
                    "DC-område på AC",
                    "Mätning på live MSB / 440 V",
                    "Ampère över källan",
                    "“24 V tål allt”",
                    "Händer-DMM som läxa",
                ],
            },
            {
                "kind": "quiz",
                "title": "Quiz",
                "lead": "Tre saker:",
                "items": [
                    "230 V är rms",
                    "DC-läge på AC är fel",
                    "Noll i DC är inte av",
                ],
                "foot": "Gör quizzen i Classroom den här veckan.",
            },
            {
                "kind": "not_in",
                "title": "Inte i 4.1",
                "body": "Trefas/fasföljd. DC-räkning. Isolation/megger. Stötväg. 230 V-uttag som installation. Live fartygsnät. Arduino.",
                "lia": "LIA: samma rms-och-AC-läge under handledning, inte på spänningssatt huvudtavla.",
            },
        ],
    }


def week05() -> dict:
    png = BOK / "figur-5-1-trefas-spanning.png"
    return {
        "file": "vecka-05.pptx",
        "m": "M05",
        "v": "V5",
        "slides": [
            {
                "kind": "cover",
                "kicker": "Elteknik och ellära  ·  45 YH-poäng  ·  Vecka 5",
                "title": "Trefas och spänningstyper",
                "sub": "Modul 5  ·  linje, fas, 24 / 230 / 400–440",
                "line": "Distans. Papper och foto. 440 V = look-not-touch. Inte 80005. Inte IEC-tabell.",
            },
            {
                "kind": "lesson_title",
                "title": "5.1 Trefas och spänningstyper ombord",
                "lines": [
                    "Elteknik och ellära · vecka 5 · distans",
                    "Papper och foto. 440 V = look-not-touch.",
                ],
            },
            {
                "kind": "figure",
                "png": png,
                "legend": [
                    "Tre ledare till motor",
                    "Linje mellan L1 och L2",
                    "Skrov är inte N",
                    "24 V DC, 230 V enfas, 400/440 V trefas",
                    "Stängd 440-tavla: look-not-touch",
                ],
            },
            {
                "kind": "bullets",
                "title": "Efter den här veckan",
                "items": [
                    "Linje vs fas",
                    "Tre ledare",
                    "Varför trefas till maskiner",
                    "Namnge 24 V DC, 230 V enfas, 400/440 V trefas",
                    "440 V-tavla: titta, inte röra, utan värdtillstånd",
                    "VG: varför inte mäta trefas som enfas-DC",
                ],
            },
            {
                "kind": "two_tracks",
                "title": "Två spår",
                "left_h": "Elektriker",
                "left": "Skrov ≠ N.",
                "right_h": "Ingenjör",
                "right": "440 V är inte ett rum, det är tre spänningar.",
            },
            {
                "kind": "body",
                "title": "Skall, en mening",
                "lines": [
                    "Känn igen vilken spänning du står vid. Trefas är linje mellan faser, inte tre lösa enfas mot skrov. 440 V-tavla rör du inte utan att värden isolerat och gett tillstånd. Mät inte trefas som DC.",
                    "TSFS 2017:26 5 kap. 5 §. Parafras. Klistra inte lagtext.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Inte den här veckan",
                "items": [
                    "DMM på MSB / live 440",
                    "Landström, 80005",
                    "IEC-spänningstabell, IP-matris",
                    "Nöd, EX, blackout",
                    "Hållkrets, maskinkonstruktion",
                ],
            },
            {
                "kind": "bullets",
                "title": "Tre spänningstyper",
                "lead": "Kursens låsta begrepp, ingen IEC-matris:",
                "items": [
                    "24 V DC — styr/håll. 3.1",
                    "230 V enfas — inredning, rms. 4.1. Inte lägenhetens TN bara för att talet är 230",
                    "400/440 V trefas — maskiner. Linje mellan faser. 440 på tavlan = look-not-touch",
                ],
            },
            {
                "kind": "body",
                "title": "Linje vs fas",
                "lines": [
                    "Linje = mellan två faser (L1–L2). Fas = en fas mot systemets nolla *om den finns*. Ombord saknas ofta den nolla du är van vid.",
                ],
            },
            {
                "kind": "body",
                "title": "Skrov ≠ N",
                "lines": [
                    "Skrov är inte lägenhetens nolla. Du mäter inte fas mot skrov som PE hemma.",
                ],
            },
            {
                "kind": "body",
                "title": "Tre ledare till maskinen",
                "lines": [
                    "Trefasmaskin: tre ledare räcker. Inte “tre enfas i samma rör”. Jämnare effekt; motor som begrepp, inte m6.",
                ],
            },
            {
                "kind": "body",
                "title": "440 look-not-touch",
                "lines": [
                    "Lucka stängd. Proberna i fickan. Utan värdtillstånd: titta, inte röra. 440 är inte “lite mer än 400, jag mäter”.",
                ],
            },
            {
                "kind": "gv",
                "title": "Fotoövningen",
                "lead": "I Classroom: enlinje 24 / 230 / 400–440; schema tre ledare; foto 440-tavla lucka stängd.",
                "g": "linje vs fas; tre spänningstyper; varför tre ledare; look-not-touch.",
                "vg": "varför fas–skrov inte är nolla hemma; varför DC-läge på trefas är fel (4.1 + 5 §).",
            },
            {
                "kind": "body",
                "title": "Genomgånget fel",
                "lines": [
                    "Elektriker “kollar 440”: mäter en fas mot skrov som PE, får inte linje. Ingenjör: “tre faser, tre enfas, mät en.” DMM i DC-läge kvar från 24 V.",
                ],
            },
            {
                "kind": "bullets",
                "title": "Rätt kedja",
                "numbered": True,
                "items": [
                    "Namnge systemet: 24 / 230 / 400–440",
                    "Linje mellan faser, inte mot skrov som nolla",
                    "AC-läge",
                    "440 V-tavla: titta",
                    "Mätning bara på isolerad tränare/död tavla enligt v2",
                ],
            },
            {
                "kind": "fara_list",
                "title": "Stopp",
                "items": [
                    "Prober fas–skrov som nolla hemma",
                    "Live-wiring, DMM på MSB",
                    "“Tre enfas”",
                    "Påhittad spänningstabell",
                    "Landström / 80005",
                ],
            },
            {
                "kind": "quiz",
                "title": "Quiz",
                "lead": "Fyra saker:",
                "items": [
                    "L1–L2 är linje",
                    "Skrov ≠ N",
                    "440 look-not-touch",
                    "Inte tre enfas",
                ],
                "foot": "Gör quizzen i Classroom den här veckan.",
            },
            {
                "kind": "not_in",
                "title": "Inte i 5.1",
                "body": "Nödström. Batterimodul. Landström. EX. IEC-spänningstabell. IP-tabell. Live trefasmätning. Hållkrets. Maskinkonstruktion.",
                "lia": "LIA: peka rätt spänningstyp från däck under handledning, proberna i fickan på 440.",
            },
        ],
    }


def extract_notes(path: Path) -> list[str]:
    prs = Presentation(str(path))
    return [get_notes(s) for s in prs.slides]


def verify_file(path: Path, bak: Path) -> dict:
    prs = Presentation(str(path))
    old = Presentation(str(bak))
    notes_new = [get_notes(s) for s in prs.slides]
    notes_old = [get_notes(s) for s in old.slides]
    notes_ok = notes_new == notes_old
    mismatches = []
    if not notes_ok:
        for i, (a, b) in enumerate(zip(notes_old, notes_new), start=1):
            if a != b:
                mismatches.append(i)
        if len(notes_old) != len(notes_new):
            mismatches.append(f"count {len(notes_old)}->{len(notes_new)}")
    # package checks
    data = path.read_bytes()
    has_calibri = b"Calibri" in data
    has_green = b"1F4D3A" in data.upper() or b"1f4d3a" in data
    pics = 0
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for s in prs.slides:
        for sh in s.shapes:
            if sh.shape_type == MSO_SHAPE_TYPE.PICTURE:
                pics += 1
    xml_hit = False
    with zipfile.ZipFile(path, "r") as z:
        for name in z.namelist():
            if name.endswith(".xml"):
                blob = z.read(name)
                if b"Calibri" in blob:
                    xml_hit = True
                    break
    return {
        "slides": len(prs.slides),
        "size": f"{prs.slide_width.inches:.3f}x{prs.slide_height.inches:.3f}",
        "notes_ok": notes_ok,
        "mismatches": mismatches,
        "pics": pics,
        "calibri": has_calibri or xml_hit,
        "green_bar": has_green,
    }


def main():
    BAK.mkdir(parents=True, exist_ok=True)
    report = []
    for week in weeks():
        name = week["file"]
        src = PPTX_DIR / name
        bak = BAK / name
        if not src.exists():
            report.append(f"{name}: MISSING source")
            continue
        if not bak.exists():
            shutil.copy2(src, bak)
        notes = extract_notes(bak)
        nspec = len(week["slides"])
        if nspec != len(notes):
            print(f"warn {name}: specs={nspec} notes={len(notes)}")
        # germanica lead: already in spec as numbered; SHK line is in classroom
        prs = build_week(week, notes)
        out = PPTX_DIR / name
        prs.save(str(out))
        _strip_calibri_zip(out)
        info = verify_file(out, bak)
        report.append((name, info, len(notes)))
        print(
            f"wrote {out} slides={info['slides']} {info['size']}in "
            f"notes_ok={info['notes_ok']} pics={info['pics']} "
            f"calibri={info['calibri']} green={info['green_bar']}"
        )
        if info["mismatches"]:
            print(f"  note mismatches: {info['mismatches']}")
    return report


if __name__ == "__main__":
    main()
