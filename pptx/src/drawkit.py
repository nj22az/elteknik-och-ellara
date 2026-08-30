"""Pillow drawing primitives for v3. 0 radius except callout disks.

Canvas API is used by build_figures.py. Tokens from v3_tokens.py.
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from v3_tokens import (
    DISK_DIAMETER_MM,
    FONT_DIR,
    FONT_FILES,
    HAIRLINE_PT,
    HI_DPI,
    INK,
    INK_K,
    LIVE_WIDTH_IN,
    LOZENGE_HEIGHT_EM,
    LOZENGE_PAD_X_EM,
    M_LINES,
    OBS_TRACKING_EM,
    OUT_DPI,
    PAPER,
    CODE_TRACKING_EM,
)


def load_font(weight: int, size_px: float) -> ImageFont.FreeTypeFont:
    name = FONT_FILES[weight]
    path = FONT_DIR / name
    if path.exists():
        return ImageFont.truetype(str(path), size=max(1, int(round(size_px))))
    for fallback in (
        "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        if Path(fallback).exists():
            return ImageFont.truetype(fallback, max(1, int(round(size_px))))
    return ImageFont.load_default()


def font_ok() -> bool:
    try:
        for w in (400, 500, 600):
            f = load_font(w, 48)
            for ch in "\u00c5\u00c4\u00d6\u00e5\u00e4\u00f6":
                if f.getlength(ch) < 2:
                    return False
        return True
    except OSError:
        return False


def _em(font: ImageFont.FreeTypeFont) -> float:
    return float(getattr(font, "size", 12))


def text_width(font: ImageFont.FreeTypeFont, text: str, tracking_em: float = 0.0) -> float:
    if not text:
        return 0.0
    if tracking_em == 0:
        return float(font.getlength(text))
    extra = tracking_em * _em(font)
    w = 0.0
    for i, ch in enumerate(text):
        w += float(font.getlength(ch))
        if i < len(text) - 1:
            w += extra
    return w


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill,
    tracking_em: float = 0.0,
    anchor: str = "lt",
) -> float:
    """Pillow-like anchors: l/m/r + t/m/b. Tracked runs for codes."""
    x, y = xy
    w = text_width(font, text, tracking_em)
    bb = draw.textbbox((0, 0), text or "M", font=font)
    h = bb[3] - bb[1]
    ax, ay = anchor[0], anchor[1] if len(anchor) > 1 else "t"
    if ax == "m":
        x -= w / 2.0
    elif ax == "r":
        x -= w
    if ay == "m":
        y -= (bb[3] + bb[1]) / 2.0
    elif ay == "b":
        y -= bb[3]
    extra = tracking_em * _em(font)
    cx = x
    for i, ch in enumerate(text):
        draw.text((cx, y), ch, font=font, fill=fill)
        cx += float(font.getlength(ch))
        if i < len(text) - 1:
            cx += extra
    return w


def line_color(c: "Canvas", code: str):
    if c.print_mode:
        return c.ink
    return M_LINES[code]["color"]


def metro_width(c: "Canvas", kind: str) -> int:
    if kind == "thick":
        return max(8, c.pt(1.6))
    if kind == "mid":
        return max(6, c.pt(1.1))
    return c.hair()


class Canvas:
    def __init__(self, width_in: float, height_in: float, *, print_mode: bool):
        self.width_in = width_in
        self.height_in = height_in
        self.print_mode = print_mode
        self.dpi = HI_DPI
        self.out_dpi = OUT_DPI
        self.w = int(round(width_in * HI_DPI))
        self.h = int(round(height_in * HI_DPI))
        self.ink = INK_K if print_mode else INK
        self.paper = PAPER
        self.im = Image.new("RGB", (self.w, self.h), PAPER)
        self.draw = ImageDraw.Draw(self.im)

    def inch(self, v: float) -> float:
        return v * self.dpi

    def pt(self, v: float) -> int:
        return max(1, int(round(v / 72.0 * self.dpi)))

    def mm(self, v: float) -> float:
        return v / 25.4 * self.dpi

    def hair(self) -> int:
        return max(3, self.pt(HAIRLINE_PT))

    def heavy(self) -> int:
        return max(self.hair() + 2, self.pt(0.7))

    def font(self, weight: int, pt: float) -> ImageFont.FreeTypeFont:
        return load_font(weight, pt / 72.0 * self.dpi)

    def line(self, a, b, *, width=None, fill=None):
        self.draw.line([a, b], fill=fill or self.ink, width=width or self.hair())

    def dashed(self, a, b, *, dash=None, gap=None, width=None, fill=None):
        dash = int(dash or self.pt(2.5))
        gap = int(gap or self.pt(1.6))
        _dash(self.draw, a, b, fill or self.ink, width or self.hair(), (dash, gap))

    def long_dash(self, a, b, *, width=None, fill=None):
        _dash(self.draw, a, b, fill or self.ink, width or self.hair(), (self.pt(8), self.pt(2.4)))

    def rect(self, box, *, fill=None, outline=None, width=None):
        x0, y0, x1, y1 = box
        w = width or self.hair()
        if fill is not None:
            self.draw.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=w if outline else 0)
        else:
            self.draw.rectangle([x0, y0, x1, y1], outline=outline or self.ink, width=w)

    def hatch(self, box, *, spacing=8):
        x0, y0, x1, y1 = box
        span = (x1 - x0) + (y1 - y0)
        s = max(4, int(spacing))
        for d in range(-int(y1 - y0), int(x1 - x0) + int(y1 - y0), s):
            self.draw.line([(x0 + d, y0), (x0 + d - (y1 - y0), y1)], fill=self.ink, width=1)

    def m_lozenge(self, xy, code: str, *, pt: float = 8):
        code = code.upper()
        font = self.font(600, pt)
        pad_x = LOZENGE_PAD_X_EM * _em(font)
        tw = text_width(font, code, CODE_TRACKING_EM)
        h = LOZENGE_HEIGHT_EM * _em(font)
        w = tw + 2 * pad_x
        x, y = xy
        fill = self.ink if self.print_mode else M_LINES[code]["color"]
        self.draw.rectangle([x, y, x + w, y + h], fill=fill)
        draw_text(self.draw, (x + w / 2, y + h / 2), code, font, (255, 255, 255),
                  tracking_em=CODE_TRACKING_EM, anchor="mm")
        return (x, y, x + w, y + h)

    def disk(self, center, number: int):
        cx, cy = center
        d = self.mm(DISK_DIAMETER_MM)
        r = d / 2.0
        self.draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=self.ink)
        font = self.font(600, 8)
        draw_text(self.draw, (cx, cy), str(number), font, (255, 255, 255), anchor="mm")

    def leader(self, a, b):
        # from disk edge toward target, straight
        ax, ay = a
        bx, by = b
        r = self.mm(DISK_DIAMETER_MM) / 2.0 + 2
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1
        sx, sy = ax + dx / L * r, ay + dy / L * r
        self.draw.line([(sx, sy), (bx, by)], fill=self.ink, width=self.hair())

    def obs_box(self, box, sentence: str):
        x0, y0, x1, y1 = box
        tab_f = self.font(600, 8)
        body_f = self.font(400, 9)
        tab_h = 1.15 * _em(tab_f)
        tab_w = text_width(tab_f, "OBS", OBS_TRACKING_EM) + 0.8 * _em(tab_f)
        self.draw.rectangle([x0, y0, x1, y1], fill=PAPER, outline=self.ink, width=self.hair())
        self.draw.rectangle([x0, y0, x0 + tab_w, y0 + tab_h], fill=self.ink)
        draw_text(self.draw, (x0 + tab_w / 2, y0 + tab_h / 2), "OBS", tab_f, (255, 255, 255),
                  tracking_em=OBS_TRACKING_EM, anchor="mm")
        pad = 0.25 * _em(body_f)
        _wrap(self.draw, (x0 + pad, y0 + tab_h + pad, x1 - pad, y1 - pad), sentence, body_f, self.ink)

    def fara_box(self, box, sentence: str):
        x0, y0, x1, y1 = box
        tab_f = self.font(600, 8)
        body_f = self.font(400, 9)
        head_h = 1.25 * _em(tab_f)
        self.draw.rectangle([x0, y0, x1, y1], fill=PAPER, outline=self.ink, width=self.heavy())
        self.draw.rectangle([x0, y0, x1, y0 + head_h], fill=self.ink)
        draw_text(self.draw, (x0 + 0.35 * _em(tab_f), y0 + head_h / 2), "FARA", tab_f, (255, 255, 255),
                  tracking_em=OBS_TRACKING_EM, anchor="lm")
        pad = 0.25 * _em(body_f)
        _wrap(self.draw, (x0 + pad, y0 + head_h + pad, x1 - pad, y1 - pad), sentence, body_f, self.ink)

    def save(self, dest: Path, *, grayscale: bool) -> Image.Image:
        dest = Path(dest)
        w300 = int(round(self.width_in * OUT_DPI))
        h300 = int(round(self.height_in * OUT_DPI))
        out = self.im.resize((w300, h300), Image.Resampling.LANCZOS)
        if grayscale:
            out = out.convert("L")
        dest.parent.mkdir(parents=True, exist_ok=True)
        out.save(dest, format="PNG", dpi=(OUT_DPI, OUT_DPI), optimize=True)
        return out


def _dash(draw, a, b, fill, width, pattern):
    x0, y0 = a
    x1, y1 = b
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    if length < 1:
        return
    ux, uy = dx / length, dy / length
    dist = 0.0
    on = True
    pi = 0
    pat = list(pattern)
    while dist < length:
        seglen = pat[pi % len(pat)]
        nxt = min(length, dist + seglen)
        if on:
            draw.line(
                [(x0 + ux * dist, y0 + uy * dist), (x0 + ux * nxt, y0 + uy * nxt)],
                fill=fill,
                width=width,
            )
        on = not on
        pi += 1
        dist = nxt


def _wrap(draw, box, text, font, fill):
    x0, y0, x1, y1 = box
    max_w = max(10, x1 - x0)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if font.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    lh = int(_em(font) * 1.25)
    y = y0
    for ln in lines:
        if y + lh > y1 + 4:
            break
        draw.text((x0, y), ln, font=font, fill=fill)
        y += lh


# ---------------------------------------------------------------------------
# Functional API used by build_figures.py (module-level, not Canvas methods)
# ---------------------------------------------------------------------------
from tokens import (  # noqa: E402
    COLUMN_IN,
    DISK_PX_600,
    FONT_MED,
    FONT_REG,
    FONT_SEM,
    HAIRLINE_PX,
    LINES as TOK_LINES,
    PRINT_DPI,
    RENDER_DPI,
    RULE_HEAVY_PX,
    RULE_PX,
    WHITE,
)


def plex_loaded() -> bool:
    return FONT_REG.exists() and FONT_MED.exists() and FONT_SEM.exists()


def font_pt(weight: int, pt: float, dpi: int = RENDER_DPI):
    path = FONT_SEM if weight >= 600 else FONT_MED if weight >= 500 else FONT_REG
    px = max(8, int(round(pt / 72.0 * dpi)))
    if path.exists():
        return ImageFont.truetype(str(path), px)
    return load_font(weight, px)


def draw_tracked(draw, xy, text, font, fill=INK, tracking_em: float = 0.0):
    x, y = xy
    extra = tracking_em * float(font.size)
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + extra
    return x


def tracked_width(draw, text, font, tracking_em: float) -> float:
    extra = tracking_em * float(font.size)
    if not text:
        return 0.0
    return sum(draw.textlength(ch, font=font) for ch in text) + extra * max(0, len(text) - 1)


def lozenge(draw, xy, code, *, print_mode, font=None, line_id=None):
    code = code.upper()
    font = font or font_pt(600, 8)
    lid = line_id or code
    color = TOK_LINES.get(lid, {}).get("color", INK)
    fill = INK if print_mode else color
    pad_x = 0.40 * float(font.size)
    tw = tracked_width(draw, code, font, 0.06)
    h = int(round(1.15 * float(font.size)))
    w = int(round(tw + 2 * pad_x))
    x, y = xy
    draw.rectangle([x, y, x + w, y + h], fill=fill)
    draw_tracked(draw, (x + (w - tw) / 2.0, y + h * 0.12), code, font, fill=WHITE, tracking_em=0.06)
    return (x, y, x + w, y + h)


def disk(draw, center, number, *, diameter=DISK_PX_600, font=None):
    cx, cy = center
    r = diameter // 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=INK)
    font = font or font_pt(600, 8)
    bb = draw.textbbox((0, 0), str(number), font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    draw.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), str(number), font=font, fill=WHITE)


def leader(draw, a, b, *, width=HAIRLINE_PX):
    draw.line([a, b], fill=INK, width=width)


def dashed_segment(draw, p0, p1, *, fill=INK, width=8, dash=(80, 24)):
    _dash(draw, p0, p1, fill, width, dash)


def polyline(draw, pts, *, fill=INK, width=8, dash=None):
    if dash:
        for a, b in zip(pts, pts[1:]):
            dashed_segment(draw, a, b, fill=fill, width=width, dash=dash)
    else:
        draw.line(pts, fill=fill, width=width)


def metro_line(draw, pts, *, print_mode, line_id, width=18):
    color = INK if print_mode else TOK_LINES[line_id]["color"]
    dash = TOK_LINES[line_id]["print_dash"] if print_mode else None
    if isinstance(dash, tuple):
        polyline(draw, pts, fill=color, width=width, dash=dash)
    else:
        polyline(draw, pts, fill=color, width=width)


def hull_symbol(draw, origin, *, scale=1):
    x, y = origin
    w = 46 * scale
    draw.line([(x, y), (x + w, y)], fill=INK, width=RULE_HEAVY_PX)
    for i, ww in enumerate((34, 22, 10)):
        yy = y + (10 + i * 10) * scale
        draw.line([(x + (w - ww * scale) / 2, yy), (x + (w + ww * scale) / 2, yy)], fill=INK, width=RULE_PX)


def obs_box(draw, box, sentence, *, body_font=None, tab_font=None):
    x0, y0, x1, y1 = box
    tab_font = tab_font or font_pt(600, 8)
    body_font = body_font or font_pt(400, 9)
    tab_h = int(1.15 * float(tab_font.size))
    tab_w = int(tracked_width(draw, "OBS", tab_font, 0.08) + 0.8 * float(tab_font.size))
    draw.rectangle([x0, y0, x1, y1], fill=PAPER, outline=INK, width=RULE_PX)
    draw.rectangle([x0, y0, x0 + tab_w, y0 + tab_h], fill=INK)
    tw = tracked_width(draw, "OBS", tab_font, 0.08)
    draw_tracked(draw, (x0 + (tab_w - tw) / 2, y0 + 4), "OBS", tab_font, fill=WHITE, tracking_em=0.08)
    pad = int(0.25 * float(body_font.size))
    _wrap(draw, (x0 + pad, y0 + tab_h + pad, x1 - pad, y1 - pad), sentence, body_font, INK)


def fara_box(draw, box, sentence, *, body_font=None, tab_font=None):
    x0, y0, x1, y1 = box
    tab_font = tab_font or font_pt(600, 8)
    body_font = body_font or font_pt(400, 9)
    head_h = int(1.25 * float(tab_font.size))
    draw.rectangle([x0, y0, x1, y1], fill=PAPER, outline=INK, width=RULE_HEAVY_PX)
    draw.rectangle([x0, y0, x1, y0 + head_h], fill=INK)
    draw_tracked(draw, (x0 + 10, y0 + 6), "FARA", tab_font, fill=WHITE, tracking_em=0.08)
    pad = int(0.25 * float(body_font.size))
    _wrap(draw, (x0 + pad, y0 + head_h + pad, x1 - pad, y1 - pad), sentence, body_font, INK)


def downsample_and_save(im, dest, *, print_mode, height_in):
    dest = Path(dest)
    w300 = int(round(COLUMN_IN * PRINT_DPI))
    h300 = int(round(height_in * PRINT_DPI))
    out = im.resize((w300, h300), Image.Resampling.LANCZOS)
    if print_mode:
        out = out.convert("L")
    dest.parent.mkdir(parents=True, exist_ok=True)
    out.save(dest, format="PNG", dpi=(PRINT_DPI, PRINT_DPI), optimize=True)
    return {"path": str(dest), "size": out.size, "mode": out.mode, "dpi": PRINT_DPI}
