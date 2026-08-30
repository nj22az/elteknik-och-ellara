"""Build pptx/master.pptx — v3 sample master. Do NOT rebuild vecka-01..09.

Theme: dk1/ink #111111, lt1/paper #FFFFFF, accent1 M01 #E6002D,
accent2 M02 #F39700, hlink #111111. Latin typeface IBM Plex Sans.
0 radius on every shape. Patch theme XML (python-pptx leaves Office blue).
"""
from __future__ import annotations

import sys
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

sys.path.insert(0, str(Path(__file__).resolve().parent))

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

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"

INK = RGBColor(0x11, 0x11, 0x11)
PAPER = RGBColor(0xFF, 0xFF, 0xFF)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

# Footer / title-row mapping per sample slide (M-code, V-code)
SLIDE_CHROME = [
    ("M01", "V1"),  # a title
    ("M01", "V1"),  # b modul M01
    ("M01", "V1"),  # c stötväg
    ("M01", "V1"),  # d figur 1.1
    ("M01", "V1"),  # e OBS/FARA
    ("M02", "V2"),  # f modul M02
    ("M02", "V2"),  # g figur 2.1
    ("M01", "V1"),  # h två spår (classroom-v1 slide 3)
]


def _rgb(tup):
    return RGBColor(*tup)


def _set_srgb(parent, hex6: str):
    """Replace children with a:srgbClr."""
    for child in list(parent):
        parent.remove(child)
    el = etree.SubElement(parent, qn("a:srgbClr"))
    el.set("val", hex6)


def patch_theme(
    prs: Presentation,
    *,
    accent1: str = "E6002D",
    accent2: str = "F39700",
    accent3: str = "1A1A1A",
    accent4: str = "6B2D5B",
) -> None:
    master = prs.slide_masters[0]
    theme_part = None
    for rel in master.part.rels.values():
        if "theme" in rel.reltype:
            theme_part = rel.target_part
            break
    if theme_part is None:
        raise RuntimeError("no theme part on slide master")
    root = etree.fromstring(theme_part.blob)
    if root.get("name") is not None:
        root.set("name", "Elteknik v3")
    ns = {"a": A_NS}

    scheme = root.find(".//a:clrScheme", ns)
    scheme.set("name", "Elteknik v3")
    _set_srgb(scheme.find("a:dk1", ns), "111111")
    _set_srgb(scheme.find("a:lt1", ns), "FFFFFF")
    _set_srgb(scheme.find("a:dk2", ns), "111111")
    _set_srgb(scheme.find("a:lt2", ns), "FFFFFF")
    _set_srgb(scheme.find("a:accent1", ns), accent1)
    _set_srgb(scheme.find("a:accent2", ns), accent2)
    _set_srgb(scheme.find("a:accent3", ns), accent3)
    _set_srgb(scheme.find("a:accent4", ns), accent4)
    _set_srgb(scheme.find("a:accent5", ns), "111111")
    _set_srgb(scheme.find("a:accent6", ns), "111111")
    _set_srgb(scheme.find("a:hlink", ns), "111111")
    _set_srgb(scheme.find("a:folHlink", ns), "111111")

    for tag in ("a:majorFont", "a:minorFont"):
        node = root.find(f".//{tag}", ns)
        latin = node.find("a:latin", ns)
        latin.set("typeface", "IBM Plex Sans")
        ea = node.find("a:ea", ns)
        if ea is not None:
            ea.set("typeface", "IBM Plex Sans")
        cs = node.find("a:cs", ns)
        if cs is not None:
            cs.set("typeface", "IBM Plex Sans")
        # Drop Japanese script identity; keep latin gothic
        for f in list(node.findall("a:font", ns)):
            if f.get("script") in ("Jpan", "Hang", "Hans", "Hant"):
                f.set("typeface", "IBM Plex Sans")

    theme_part._blob = etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)

    # Master background paper
    bg = master.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = PAPER


    # Replace Calibri identity in master/layout XML
    xml = master._element
    for el in xml.iter():
        if el.get("typeface") in ("Calibri", "Calibri Light", "Arial"):
            el.set("typeface", "IBM Plex Sans")
    for layout in master.slide_layouts:
        for el in layout._element.iter():
            if el.get("typeface") in ("Calibri", "Calibri Light", "Arial"):
                el.set("typeface", "IBM Plex Sans")

    # Master txStyles → IBM Plex Sans, ink
    sp_tree = master._element.cSld.spTree
    # placeholders: zero radius already (rect). Hide leftover title chrome
    # by not using them; sample slides use blank layout.


def _no_shadow(shape) -> None:
    try:
        shape.shadow.inherit = False
    except Exception:
        pass
    spPr = shape._element.spPr
    # remove effectLst if present
    el = spPr.find(qn("a:effectLst"))
    if el is not None:
        spPr.remove(el)


def add_rect(slide, l, t, w, h, *, fill=None, line=None, line_pt=0.75):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    _no_shadow(sh)
    # force prstGeom rect, no adj
    spPr = sh._element.spPr
    geom = spPr.find(qn("a:prstGeom"))
    if geom is not None:
        geom.set("prst", "rect")
        av = geom.find(qn("a:avLst"))
        if av is not None:
            geom.remove(av)
            etree.SubElement(geom, qn("a:avLst"))
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid()
        sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = Pt(line_pt)
    return sh


def add_oval(slide, l, t, w, h, *, fill, line=None):
    sh = slide.shapes.add_shape(MSO_SHAPE.OVAL, l, t, w, h)
    _no_shadow(sh)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line
        sh.line.width = Pt(0.35)
    return sh


def _font(run, *, size, weight, color, tracking_em=0.0, caps=False):
    # 400 IBM Plex Sans, 500 Medium, 600 SemiBold. NEVER light. Never Calibri.
    if weight >= 600:
        name = "IBM Plex Sans SemiBold"
    elif weight >= 500:
        name = "IBM Plex Sans Medium"
    else:
        name = "IBM Plex Sans"
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = False
    run.font.italic = False
    run.font.color.rgb = color
    rPr = run._r.get_or_add_rPr()
    rPr.set("dirty", "0")
    # latin typeface on rPr (overrides theme Calibri)
    latin = rPr.find(qn("a:latin"))
    if latin is None:
        latin = etree.SubElement(rPr, qn("a:latin"))
    latin.set("typeface", name)
    ea = rPr.find(qn("a:ea"))
    if ea is None:
        ea = etree.SubElement(rPr, qn("a:ea"))
    ea.set("typeface", name)
    if tracking_em:
        # spc is 100ths of a point
        rPr.set("spc", str(int(round(tracking_em * size * 100))))
    if caps:
        rPr.set("cap", "all")


def _tf_prep(shape, *, anchor=MSO_ANCHOR.MIDDLE, margin_pt=4):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.anchor = anchor
    m = Pt(margin_pt)
    tf.margin_left = m
    tf.margin_right = m
    tf.margin_top = Emu(0)
    tf.margin_bottom = Emu(0)
    return tf


def set_single(shape, text, *, size, weight, color, align=PP_ALIGN.LEFT,
               tracking_em=0.0, caps=False, anchor=MSO_ANCHOR.MIDDLE, margin_pt=4):
    tf = _tf_prep(shape, anchor=anchor, margin_pt=margin_pt)
    p = tf.paragraphs[0]
    p.alignment = align
    p.clear()
    # clear leftover
    for r in list(p.runs):
        r._r.getparent().remove(r._r)
    run = p.add_run()
    run.text = text
    _font(run, size=size, weight=weight, color=color, tracking_em=tracking_em, caps=caps)
    return tf


def add_text_box(slide, l, t, w, h, text, *, size, weight, color,
                 align=PP_ALIGN.LEFT, tracking_em=0.0, caps=False,
                 anchor=MSO_ANCHOR.MIDDLE):
    sh = slide.shapes.add_textbox(l, t, w, h)
    _no_shadow(sh)
    set_single(sh, text, size=size, weight=weight, color=color, align=align,
               tracking_em=tracking_em, caps=caps, anchor=anchor, margin_pt=2)
    return sh


def m_lozenge(slide, l, t, code: str, *, code_pt=PPTX_CODE_PT):
    code = code.upper()
    # height 1.15em, pad 0.15em 0.4em
    h = Inches(code_pt * 1.15 / 72.0)
    # width: 3 chars + tracking + pad
    w = Inches((code_pt * (0.62 * len(code) + CODE_TRACK() + 0.80)) / 72.0)
    fill = _rgb(M_LINES[code]["color"])
    sh = add_rect(slide, l, t, w, h, fill=fill, line=None)
    set_single(sh, code, size=code_pt, weight=600, color=WHITE,
               align=PP_ALIGN.CENTER, tracking_em=0.06, caps=True, margin_pt=1)
    return sh, w, h


def CODE_TRACK():
    return 0.06 * 2  # rough extra for 3-letter tracking


def v_square(slide, l, t, code: str, *, code_pt=PPTX_CODE_PT, active=False):
    code = code.upper()
    side = Inches(max(code_pt * 1.35, 16) / 72.0)
    fill = _rgb(V_STATIONS[code]["color"])
    if active:
        # 2px ink frame outside
        frame = Inches(2 / 96)
        add_rect(slide, l - frame, t - frame, side + 2 * frame, side + 2 * frame,
                 fill=None, line=INK, line_pt=1.5)
    sh = add_rect(slide, l, t, side, side, fill=fill, line=None)
    set_single(sh, code, size=code_pt, weight=600, color=WHITE,
               align=PP_ALIGN.CENTER, tracking_em=0.06, caps=True, margin_pt=0)
    return sh, side


def disk(slide, l, t, number: int, *, diameter_pt=28):
    d = Inches(diameter_pt / 72.0)
    sh = add_oval(slide, l, t, d, d, fill=INK)
    set_single(sh, str(number), size=14, weight=600, color=WHITE,
               align=PP_ALIGN.CENTER, margin_pt=0)
    return sh, d


def hairline(slide, l, t, w):
    sh = add_rect(slide, l, t, w, Pt(0.35), fill=INK, line=None)
    return sh


def chrome_title_row(slide, m_code, v_code):
    """Title row: M lozenge + module name + V square. No green bar."""
    left = Inches(0.45)
    top = Inches(0.22)
    sh, mw, mh = m_lozenge(slide, left, top, m_code)
    name = M_LINES[m_code]["name"]
    add_text_box(slide, left + mw + Inches(0.12), top, Inches(4.5), mh,
                 name, size=PPTX_HEADING_PT, weight=600, color=INK, anchor=MSO_ANCHOR.MIDDLE)
    # V square on the right of the name
    vx = left + mw + Inches(0.12) + Inches(4.6)
    v_square(slide, vx, top - Inches(0.02), v_code, active=True)
    week = V_STATIONS[v_code]["name"]
    vs = Inches(max(PPTX_CODE_PT * 1.35, 16) / 72.0)
    add_text_box(slide, vx + vs + Inches(0.10), top, Inches(1.8), mh,
                 week, size=PPTX_LABEL_PT, weight=500, color=INK)
    hairline(slide, Inches(0.45), Inches(0.72), Inches(12.43))


def chrome_footer(slide, m_code, v_code, number: int):
    """Footer hairline: M-lozenge + module name, V-square, tabular slide number."""
    y = Inches(7.08)
    hairline(slide, Inches(0.45), y, Inches(12.43))
    fy = Inches(7.14)
    sh, mw, mh = m_lozenge(slide, Inches(0.45), fy, m_code, code_pt=12)
    add_text_box(slide, Inches(0.45) + mw + Inches(0.08), fy, Inches(2.4), mh,
                 M_LINES[m_code]["name"], size=PPTX_LABEL_PT, weight=500, color=INK)
    vx = Inches(4.4)
    v_square(slide, vx, fy, v_code, code_pt=12, active=False)
    vs = Inches(max(12 * 1.35, 16) / 72.0)
    add_text_box(slide, vx + vs + Inches(0.08), fy, Inches(1.6), mh,
                 V_STATIONS[v_code]["name"], size=PPTX_LABEL_PT, weight=500, color=INK)
    add_text_box(slide, Inches(11.7), fy, Inches(1.15), mh,
                 f"{number:02d}", size=PPTX_LABEL_PT, weight=600, color=INK,
                 align=PP_ALIGN.RIGHT, tracking_em=0.06)


def obs_module(slide, l, t, w, h, sentence: str):
    """0 radius. Top-left tab ink fill, white OBS 600 tracking 0.08em.
    Body paper, ink, 1px rule. One sentence. No yellow, no icon, no triangle.
    """
    add_rect(slide, l, t, w, h, fill=PAPER, line=INK, line_pt=0.75)
    tab_w, tab_h = Inches(0.70), Inches(0.28)
    tab = add_rect(slide, l, t, tab_w, tab_h, fill=INK, line=None)
    set_single(tab, "OBS", size=PPTX_LABEL_PT, weight=600, color=WHITE,
               align=PP_ALIGN.CENTER, tracking_em=0.08, caps=True, margin_pt=1)
    add_text_box(slide, l + Inches(0.16), t + tab_h, w - Inches(0.28), h - tab_h,
                 sentence, size=PPTX_BODY_PT, weight=400, color=INK,
                 anchor=MSO_ANCHOR.MIDDLE)


def fara_module(slide, l, t, w, h, sentence: str):
    """Ink header bar, white FARA 600. Body paper + ink, 2px rule-heavy.
    NOT red. One sentence. No emoji.
    """
    add_rect(slide, l, t, w, h, fill=PAPER, line=INK, line_pt=1.5)
    head_h = Inches(0.36)
    head = add_rect(slide, l, t, w, head_h, fill=INK, line=None)
    set_single(head, "FARA", size=PPTX_LABEL_PT, weight=600, color=WHITE,
               align=PP_ALIGN.LEFT, tracking_em=0.08, caps=True, margin_pt=8)
    add_text_box(slide, l + Inches(0.16), t + head_h, w - Inches(0.28), h - head_h,
                 sentence, size=PPTX_BODY_PT, weight=400, color=INK,
                 anchor=MSO_ANCHOR.MIDDLE)


def blank(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def slide_a(prs):
    s = blank(prs)
    # Title: Elteknik och ellära / YH · 45 p / Fartyg och automation
    add_text_box(s, Inches(0.45), Inches(2.15), Inches(12.4), Inches(0.70),
                 "Elteknik och ellära", size=28, weight=600, color=INK)
    hairline(s, Inches(0.45), Inches(2.90), Inches(4.2))
    add_text_box(s, Inches(0.45), Inches(3.05), Inches(12.4), Inches(0.40),
                 "YH · 45 p", size=18, weight=500, color=INK)
    add_text_box(s, Inches(0.45), Inches(3.45), Inches(12.4), Inches(0.40),
                 "Fartyg och automation", size=18, weight=400, color=INK)
    # M01-M12 theme swatches (line ID only). Name sits beside on other slides.
    x = Inches(0.45)
    y = Inches(4.20)
    for code in ["M01","M02","M03","M04","M05","M06",
                 "M07","M08","M09","M10","M11","M12"]:
        sh, mw, mh = m_lozenge(s, x, y, code, code_pt=12)
        x = x + mw + Inches(0.10)
    chrome_footer(s, "M01", "V1", 1)
    return s


def slide_b(prs):
    s = blank(prs)
    chrome_title_row(s, "M01", "V1")
    add_text_box(s, Inches(0.45), Inches(1.05), Inches(12.4), Inches(0.50),
                 "Modul M01 Elsäkerhet", size=28, weight=600, color=INK)
    add_text_box(s, Inches(0.45), Inches(1.65), Inches(12.4), Inches(0.40),
                 "Station V1 · Vecka 1", size=18, weight=500, color=INK)
    chrome_footer(s, "M01", "V1", 2)
    return s


def slide_c(prs):
    """Stötväg bullets with numbered ink disks 1–3.
    Wording from classroom-v1-slides.md slide 4. Do not write new lesson text.
    """
    s = blank(prs)
    chrome_title_row(s, "M01", "V1")
    add_text_box(s, Inches(0.45), Inches(0.90), Inches(12.4), Inches(0.45),
                 "Stötväg", size=28, weight=600, color=INK)
    bullets = [
        "Ström genom kroppen: en väg in, en väg ut",
        "Ofta skrov",
        "Fukt gör höljet till ledare",
    ]
    y = Inches(1.60)
    for i, text in enumerate(bullets, start=1):
        _, d = disk(s, Inches(0.50), y, i)
        add_text_box(s, Inches(0.50) + d + Inches(0.18), y, Inches(11.5), d,
                     text, size=PPTX_BODY_PT, weight=400, color=INK)
        y += d + Inches(0.28)
    chrome_footer(s, "M01", "V1", 3)
    return s


def slide_d(prs):
    s = blank(prs)
    chrome_title_row(s, "M01", "V1")
    png = BOK / "figur-1-1-stotvag-ventil-skarm.png"
    # Figure left, legend right
    pic_w = Inches(8.4)
    s.shapes.add_picture(str(png), Inches(0.40), Inches(0.85), width=pic_w)
    legend = [
        "Packning saknas mellan kontakt och spole.",
        "Ingen PE.",
        "Stötväg: hölje · hand · skrov.",
        "IR-vakt ser bara huvudnätet.",
        "Sidokrets lokalt jordad, utanför IR.",
    ]
    y = Inches(0.95)
    lx = Inches(8.95)
    add_text_box(s, lx, Inches(0.85), Inches(4.0), Inches(0.32),
                 "Legend", size=PPTX_LABEL_PT, weight=600, color=INK,
                 tracking_em=0.06, caps=True)
    y = Inches(1.20)
    for i, text in enumerate(legend, start=1):
        _, d = disk(s, lx, y, i, diameter_pt=22)
        add_text_box(s, lx + d + Inches(0.10), y, Inches(3.55), d + Inches(0.18),
                     text, size=12, weight=400, color=INK, anchor=MSO_ANCHOR.TOP)
        y += Inches(0.70)
    chrome_footer(s, "M01", "V1", 4)
    return s


def slide_e(prs):
    """OBS and FARA example modules, one sentence each from chapter 1."""
    s = blank(prs)
    chrome_title_row(s, "M01", "V1")
    add_text_box(s, Inches(0.45), Inches(0.90), Inches(12.4), Inches(0.40),
                 "OBS och FARA", size=28, weight=600, color=INK)
    # Chapter 1.2: IR-vakten ser bara det nät den sitter på.
    # Chapter 1.0 Stopp: Ingen hand mot stomme som första steg.
    obs_module(s, Inches(0.45), Inches(1.55), Inches(12.4), Inches(1.70),
               "IR-vakten ser bara det nät den sitter på.")
    fara_module(s, Inches(0.45), Inches(3.50), Inches(12.4), Inches(1.90),
                "Ingen hand mot stomme som första steg.")
    chrome_footer(s, "M01", "V1", 5)
    return s


def slide_f(prs):
    s = blank(prs)
    chrome_title_row(s, "M02", "V2")
    add_text_box(s, Inches(0.45), Inches(1.05), Inches(12.4), Inches(0.50),
                 "Modul M02 Isolering", size=28, weight=600, color=INK)
    add_text_box(s, Inches(0.45), Inches(1.65), Inches(12.4), Inches(0.40),
                 "Station V2 · Vecka 2", size=18, weight=500, color=INK)
    chrome_footer(s, "M02", "V2", 6)
    return s


def slide_g(prs):
    s = blank(prs)
    chrome_title_row(s, "M02", "V2")
    png = BOK / "figur-2-1-isolering-kedja-skarm.png"
    pic_w = Inches(8.4)
    s.shapes.add_picture(str(png), Inches(0.40), Inches(0.85), width=pic_w)
    legend = [
        "FRÅN",
        "LÅS/SKYLT",
        "PROVA DÖD",
        "MEGGER",
    ]
    lx = Inches(8.95)
    add_text_box(s, lx, Inches(0.85), Inches(4.0), Inches(0.32),
                 "Legend", size=PPTX_LABEL_PT, weight=600, color=INK,
                 tracking_em=0.06, caps=True)
    y = Inches(1.25)
    for i, text in enumerate(legend, start=1):
        _, d = disk(s, lx, y, i, diameter_pt=22)
        add_text_box(s, lx + d + Inches(0.10), y, Inches(3.55), d,
                     text, size=PPTX_BODY_PT, weight=500, color=INK)
        y += Inches(0.70)
    chrome_footer(s, "M02", "V2", 7)
    return s


def slide_h(prs):
    """Två spår from classroom-v1-slides.md slide 3. Do not write new lesson text."""
    s = blank(prs)
    chrome_title_row(s, "M01", "V1")
    add_text_box(s, Inches(0.45), Inches(0.90), Inches(12.4), Inches(0.45),
                 "Två spår", size=28, weight=600, color=INK)
    # two 0-radius panels
    add_rect(s, Inches(0.45), Inches(1.55), Inches(6.00), Inches(4.40),
             fill=PAPER, line=INK, line_pt=0.75)
    add_rect(s, Inches(6.85), Inches(1.55), Inches(6.00), Inches(4.40),
             fill=PAPER, line=INK, line_pt=0.75)
    add_text_box(s, Inches(0.65), Inches(1.75), Inches(5.6), Inches(0.45),
                 "Elektriker", size=18, weight=600, color=INK)
    add_text_box(s, Inches(0.65), Inches(2.30), Inches(5.6), Inches(2.8),
                 "Leta inte JFB.", size=PPTX_BODY_PT, weight=400, color=INK,
                 anchor=MSO_ANCHOR.TOP)
    add_text_box(s, Inches(7.05), Inches(1.75), Inches(5.6), Inches(0.45),
                 "Ingenjör", size=18, weight=600, color=INK)
    add_text_box(s, Inches(7.05), Inches(2.30), Inches(5.6), Inches(2.8),
                 "Läckagesökning är elarbete när komponenten kan vara spänningssatt.",
                 size=PPTX_BODY_PT, weight=400, color=INK, anchor=MSO_ANCHOR.TOP)
    chrome_footer(s, "M01", "V1", 8)
    return s


def _strip_calibri_zip(path: Path) -> None:
    """Last pass: no Calibri identity left in the package."""
    import io
    import zipfile
    src = path.read_bytes()
    buf = io.BytesIO()
    with zipfile.ZipFile(io.BytesIO(src), "r") as zin, zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename.endswith(".xml"):
                data = data.replace(b"Calibri Light", b"IBM Plex Sans")
                data = data.replace(b"Calibri", b"IBM Plex Sans")
            zout.writestr(item, data)
    path.write_bytes(buf.getvalue())


def main():
    prs = Presentation()
    prs.slide_width = Inches(SLIDE_IN[0])
    prs.slide_height = Inches(SLIDE_IN[1])
    patch_theme(prs)

    slide_a(prs)
    slide_b(prs)
    slide_c(prs)
    slide_d(prs)
    slide_e(prs)
    slide_f(prs)
    slide_g(prs)
    slide_h(prs)

    out = PPTX_DIR / "master.pptx"
    prs.save(str(out))
    _strip_calibri_zip(out)
    print(f"wrote {out} slides={len(prs.slides)} {prs.slide_width.inches:.3f}x{prs.slide_height.inches:.3f}in")


if __name__ == "__main__":
    main()
