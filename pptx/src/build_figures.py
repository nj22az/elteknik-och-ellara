"""Build Figur 1.1 and Figur 2.1 — print grayscale + screen RGB.

Content locked to kapitel-01 / kapitel-02. Do not invent lesson text.
Render at 600 dpi, Lanczos-downsample to 300 dpi so 0.35 pt hairlines survive.

v3 tokens: ink #111111 (100% K print), paper #FFFFFF, 0.35 pt hairline,
rule-heavy 2px, 0 radius except callout disks, M-lozenge line-color on
screen / black in print, color is LINE ID only (red = M01 not danger).
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from drawkit import Canvas, draw_text, font_ok, line_color, metro_width, text_width
from v3_tokens import BOK, BOOK_LABEL_PT, BOOK_TITLE_PT, LIVE_WIDTH_IN, PAPER

FIG11_H_IN = 5.30
FIG21_H_IN = 5.10


def _label(c, xy, text, *, weight=400, pt=None, anchor="lt", tracking=0.0):
    font = c.font(weight, pt or BOOK_LABEL_PT)
    draw_text(c.draw, xy, text, font, c.ink, tracking_em=tracking, anchor=anchor)


def draw_figur_11(print_mode: bool) -> Canvas:
    c = Canvas(LIVE_WIDTH_IN, FIG11_H_IN, print_mode=print_mode)
    m = c.inch(0.10)
    box = c.m_lozenge((m, m), "M01", pt=8)
    _label(c, (box[2] + c.pt(8), (box[1] + box[3]) / 2), "FIGUR 1.1",
           weight=600, pt=9, anchor="lm", tracking=0.06)
    _label(c, (box[2] + c.pt(78), (box[1] + box[3]) / 2),
           "Stotvag — magnetventil".replace("Stotvag", "Stötväg"),
           weight=500, pt=BOOK_TITLE_PT, anchor="lm")
    y_rule = box[3] + c.pt(6)
    c.line((m, y_rule), (c.w - m, y_rule))
    y0 = y_rule + c.pt(10)
    y_leg = c.h - c.inch(1.55)
    mid_x = c.w * 0.50
    c.line((mid_x, y0), (mid_x, y_leg - c.pt(8)))
    _phys(c, m, y0, mid_x - c.pt(8), y_leg)
    _metro11(c, mid_x + c.pt(10), y0, c.w - m, y_leg)

    legend = [
        "Packning saknas mellan kontakt och spole.",
        "Ingen PE.",
        "Stötväg: hölje · hand · skrov.",
        "IR-vakt ser bara huvudnätet.",
        "Sidokrets lokalt jordad, utanför IR.",
    ]
    ly = y_leg + c.pt(4)
    c.line((m, ly), (c.w - m, ly))
    font = c.font(400, 8)
    col_w = (c.w - 2 * m) / 2
    for i, sentence in enumerate(legend):
        col, row = i % 2, i // 2
        x = m + col * col_w
        y = ly + c.pt(6) + row * c.pt(12)
        r = c.mm(2.4)
        c.draw.ellipse((x, y, x + 2 * r, y + 2 * r), fill=c.ink)
        draw_text(c.draw, (x + r, y + r), str(i + 1), c.font(600, 6.5), (255, 255, 255), anchor="mm")
        draw_text(c.draw, (x + 2 * r + c.pt(4), y + r), sentence, font, c.ink, anchor="lm")

    yb = c.h - c.inch(0.62)
    gap = c.pt(10)
    half = (c.w - 2 * m - gap) / 2
    c.obs_box((m, yb, m + half, c.h - c.inch(0.08)),
              "IR-vakten ser bara det nät den sitter på.")
    c.fara_box((m + half + gap, yb, c.w - m, c.h - c.inch(0.08)),
               "Ingen hand mot stomme som första steg.")
    return c


def _phys(c, x0, y0, x1, y1):
    _label(c, ((x0 + x1) / 2, y0 + c.pt(2)), "FYSISKT", weight=600, pt=7.5, anchor="mt", tracking=0.08)

    pump_x = x0 + c.inch(0.16)
    pump_y = y0 + c.inch(1.30)
    motor_w, motor_h = c.inch(0.70), c.inch(0.52)
    c.rect((pump_x, pump_y, pump_x + motor_w, pump_y + motor_h), outline=c.ink, width=c.hair())
    cx = pump_x + motor_w * 0.38
    cy = pump_y + motor_h / 2
    r = motor_h * 0.28
    c.draw.ellipse((cx - r, cy - r, cx + r, cy + r), outline=c.ink, width=c.hair())
    c.draw.ellipse((cx - r * 0.35, cy - r * 0.35, cx + r * 0.35, cy + r * 0.35), outline=c.ink, width=c.hair())
    vx = pump_x + motor_w + c.inch(0.04)
    vr = c.inch(0.30)
    c.draw.ellipse((vx, cy - vr, vx + 2 * vr, cy + vr), outline=c.ink, width=c.hair())
    c.line((pump_x + motor_w, cy), (vx + 4, cy), width=c.heavy())
    _label(c, (pump_x + motor_w * 0.5, pump_y + motor_h + c.pt(10)), "BALLASTPUMP",
           weight=600, pt=7, anchor="mt", tracking=0.04)

    pipe_y = cy
    valve_x = x0 + c.inch(1.95)
    c.line((vx + 2 * vr, pipe_y - 4), (valve_x, pipe_y - 4))
    c.line((vx + 2 * vr, pipe_y + 4), (valve_x, pipe_y + 4))
    c.line((vx + vr - 4, cy - vr), (vx + vr - 4, y0 + c.inch(0.50)))
    c.line((vx + vr + 4, cy - vr), (vx + vr + 4, y0 + c.inch(0.50)))

    coil_w, coil_h = c.inch(0.40), c.inch(0.46)
    coil_x, coil_y = valve_x, pipe_y - coil_h - c.inch(0.16)
    c.rect((coil_x, coil_y, coil_x + coil_w, coil_y + coil_h), outline=c.ink, width=c.hair())
    c.hatch((coil_x + 4, coil_y + 4, coil_x + coil_w - 4, coil_y + coil_h - 4), spacing=c.pt(2.4))
    _label(c, (coil_x + coil_w / 2, coil_y + coil_h / 2), "SPOLE", weight=600, pt=6.5, anchor="mm")

    gap_y0 = coil_y - c.inch(0.09)
    conn_h = c.inch(0.20)
    conn_y = gap_y0 - conn_h
    c.rect((coil_x + c.inch(0.04), conn_y, coil_x + coil_w - c.inch(0.04), gap_y0), outline=c.ink, width=c.hair())
    for i in range(3):
        px = coil_x + c.inch(0.10) + i * c.inch(0.10)
        c.line((px, gap_y0), (px, coil_y))
    _label(c, (coil_x + coil_w / 2, conn_y - c.pt(3)), "KONTAKT", weight=600, pt=6.5, anchor="mb")

    bw = c.inch(0.20)
    c.draw.polygon(
        [
            (valve_x - bw, pipe_y - 14),
            (valve_x + coil_w + bw, pipe_y - 14),
            (valve_x + coil_w / 2, pipe_y),
            (valve_x + coil_w + bw, pipe_y + 14),
            (valve_x - bw, pipe_y + 14),
            (valve_x + coil_w / 2, pipe_y),
        ],
        outline=c.ink,
    )
    c.line((coil_x + coil_w / 2, coil_y + coil_h), (coil_x + coil_w / 2, pipe_y - 14))
    _label(c, (coil_x + coil_w / 2, pipe_y + c.inch(0.26)), "MAGNETVENTIL",
           weight=600, pt=7, anchor="mt", tracking=0.04)
    c.line((valve_x + coil_w + bw, pipe_y - 4), (x1 - c.inch(0.06), pipe_y - 4))
    c.line((valve_x + coil_w + bw, pipe_y + 4), (x1 - c.inch(0.06), pipe_y + 4))

    pe_x = coil_x + coil_w + c.inch(0.10)
    pe_y = coil_y + coil_h * 0.30
    c.rect((pe_x, pe_y, pe_x + c.inch(0.15), pe_y + c.inch(0.15)), outline=c.ink, width=c.hair())
    ex = pe_x + c.inch(0.075)
    ey = pe_y + c.inch(0.22)
    c.line((ex, pe_y + c.inch(0.15)), (ex, ey))
    c.line((ex - 10, ey), (ex + 10, ey))
    c.line((ex - 7, ey + 5), (ex + 7, ey + 5))
    c.line((ex - 4, ey + 10), (ex + 4, ey + 10))
    c.line((pe_x, pe_y), (pe_x + c.inch(0.15), pe_y + c.inch(0.15)), width=c.heavy())
    c.line((pe_x + c.inch(0.15), pe_y), (pe_x, pe_y + c.inch(0.15)), width=c.heavy())

    hand_touch = (coil_x + coil_w + 2, coil_y + coil_h * 0.72)
    _hand(c, hand_touch)

    hull_y = y1 - c.inch(0.38)
    c.line((x0 + c.pt(4), hull_y), (x1 - c.pt(4), hull_y), width=c.heavy())
    c.line((x0 + c.pt(4), hull_y + 8), (x1 - c.pt(4), hull_y + 8))
    c.hatch((x0 + c.pt(4), hull_y, x1 - c.pt(4), hull_y + c.inch(0.20)), spacing=c.pt(3.2))
    _label(c, (x0 + c.pt(8), hull_y + c.inch(0.24)), "SKROV", weight=600, pt=8, anchor="lt", tracking=0.06)

    hx, hy = hand_touch
    path = [
        (coil_x + coil_w, coil_y + coil_h * 0.7),
        (hx + c.inch(0.14), hy + c.inch(0.12)),
        (hx + c.inch(0.32), hy + c.inch(0.52)),
        (hx + c.inch(0.18), hull_y),
    ]
    for a, b in zip(path, path[1:]):
        c.dashed(a, b, dash=c.pt(2.2), gap=c.pt(1.4))
    dot = path[-1]
    c.draw.ellipse((dot[0] - 5, dot[1] - 5, dot[0] + 5, dot[1] + 5), fill=c.ink)

    _label(c, (coil_x - c.inch(0.06), (gap_y0 + coil_y) / 2), "packning saknas",
           weight=500, pt=7, anchor="rm")
    _label(c, (pe_x + c.inch(0.18), pe_y - c.pt(4)), "ingen PE", weight=500, pt=7, anchor="lb")

    d1 = (coil_x - c.inch(0.40), conn_y + conn_h * 0.2)
    d2 = (pe_x + c.inch(0.40), pe_y - c.inch(0.16))
    d3 = (hx + c.inch(0.58), hy + c.inch(0.40))
    c.disk(d1, 1)
    c.leader(d1, (coil_x + coil_w * 0.3, (gap_y0 + coil_y) / 2))
    c.disk(d2, 2)
    c.leader(d2, (pe_x + c.inch(0.07), pe_y))
    c.disk(d3, 3)
    c.leader(d3, (hx + c.inch(0.20), hy + c.inch(0.26)))


def _hand(c, touch):
    tx, ty = touch
    px, py = tx + c.inch(0.07), ty - c.inch(0.10)
    pw, ph = c.inch(0.30), c.inch(0.26)
    c.rect((px, py, px + pw, py + ph), outline=c.ink, width=c.hair())
    fh, fw = c.inch(0.05), c.inch(0.15)
    for i in range(4):
        fy = py + i * (ph / 4) + 2
        c.rect((px - fw, fy, px, fy + fh), outline=c.ink, width=c.hair())
    c.rect((px + pw * 0.15, py + ph, px + pw * 0.15 + c.inch(0.09), py + ph + c.inch(0.13)),
           outline=c.ink, width=c.hair())
    c.rect((px + pw, py + ph * 0.25, px + pw + c.inch(0.16), py + ph * 0.75),
           outline=c.ink, width=c.hair())


def _metro11(c, x0, y0, x1, y1):
    _label(c, ((x0 + x1) / 2, y0 + c.pt(2)), "ELEKTRISKT", weight=600, pt=7.5, anchor="mt", tracking=0.08)
    col = line_color(c, "M01")
    thick = metro_width(c, "thick")
    mid = metro_width(c, "mid")
    line_y = y0 + c.inch(0.82)
    _label(c, (x0 + c.pt(4), line_y - c.inch(0.26)), "HUVUDNÄT (ISOLERAT)",
           weight=600, pt=8, anchor="lt", tracking=0.04)
    c.line((x0 + c.pt(4), line_y), (x1 - c.pt(4), line_y), width=int(thick), fill=col)

    st = c.inch(0.26)
    st_x = x0 + (x1 - x0) * 0.38 - st / 2
    st_y = line_y - st / 2
    c.rect((st_x, st_y, st_x + st, st_y + st), fill=PAPER, outline=c.ink, width=c.heavy())
    _label(c, (st_x + st / 2, st_y + st / 2), "IR", weight=600, pt=7, anchor="mm")
    _label(c, (st_x + st / 2, st_y + st + c.pt(10)), "IR-VAKT", weight=600, pt=7.5, anchor="mt", tracking=0.06)

    d4 = (st_x + st + c.inch(0.50), st_y - c.inch(0.20))
    c.disk(d4, 4)
    c.leader(d4, (st_x + st, st_y + st * 0.2))

    gx = st_x + st / 2
    gap_y = line_y + c.inch(0.52)
    c.dashed((gx, line_y + st / 2 + 4), (gx, gap_y), dash=c.pt(1.6), gap=c.pt(1.6))
    brk = gap_y + c.pt(2)
    s = 8
    c.line((gx - s, brk - s), (gx + s, brk + s))
    c.line((gx + s, brk - s), (gx - s, brk + s))
    _label(c, (gx + c.pt(12), brk), "ser inte", weight=500, pt=7.5, anchor="lm")
    _label(c, (gx + c.pt(12), brk + c.pt(12)), "utanför IR", weight=400, pt=7, anchor="lt")

    side_y = y0 + c.inch(1.90)
    _label(c, (x0 + c.pt(4), side_y - c.inch(0.20)), "SIDOKRETS", weight=600, pt=8, anchor="lt", tracking=0.04)
    c.long_dash((x0 + c.pt(4), side_y), (x1 - c.pt(4), side_y), width=int(mid), fill=c.ink)

    mv = c.inch(0.26)
    mv_x = x0 + (x1 - x0) * 0.55 - mv / 2
    mv_y = side_y - mv / 2
    c.rect((mv_x, mv_y, mv_x + mv, mv_y + mv), fill=PAPER, outline=c.ink, width=c.hair())
    _label(c, (mv_x + mv / 2, mv_y + mv / 2), "MV", weight=600, pt=7, anchor="mm")
    _label(c, (mv_x + mv / 2, mv_y + mv + c.pt(10)), "MAGNETVENTIL", weight=600, pt=7, anchor="mt", tracking=0.04)
    _label(c, (mv_x + mv / 2, mv_y + mv + c.pt(20)), "lokalt jordad", weight=400, pt=7, anchor="mt")

    earth_y = y1 - c.inch(0.40)
    c.line((mv_x + mv / 2, mv_y + mv + c.pt(24)), (mv_x + mv / 2, earth_y))
    ex = mv_x + mv / 2
    c.line((ex - 14, earth_y), (ex + 14, earth_y))
    c.line((ex - 10, earth_y + 6), (ex + 10, earth_y + 6))
    c.line((ex - 5, earth_y + 12), (ex + 5, earth_y + 12))
    _label(c, (ex + c.pt(16), earth_y), "SKROV", weight=600, pt=7.5, anchor="lm", tracking=0.06)

    d5 = (mv_x - c.inch(0.52), side_y - c.inch(0.40))
    c.disk(d5, 5)
    c.leader(d5, (mv_x, mv_y + 4))


def draw_figur_21(print_mode: bool) -> Canvas:
    c = Canvas(LIVE_WIDTH_IN, FIG21_H_IN, print_mode=print_mode)
    m = c.inch(0.10)
    box = c.m_lozenge((m, m), "M02", pt=8)
    _label(c, (box[2] + c.pt(8), (box[1] + box[3]) / 2), "FIGUR 2.1",
           weight=600, pt=9, anchor="lm", tracking=0.06)
    _label(c, (box[2] + c.pt(78), (box[1] + box[3]) / 2),
           "Isolering före arbete", weight=500, pt=BOOK_TITLE_PT, anchor="lm")
    y_rule = box[3] + c.pt(6)
    c.line((m, y_rule), (c.w - m, y_rule))
    y0 = y_rule + c.pt(8)
    y_obs = c.h - c.inch(0.58)
    mid_x = c.w * 0.46
    c.line((mid_x, y0), (mid_x, y_obs - c.pt(10)))
    _metro21(c, m, y0, mid_x - c.pt(8), y_obs - c.pt(8))
    _tider(c, mid_x + c.pt(10), y0, c.w - m, y_obs - c.pt(8))
    c.obs_box((m, y_obs, c.w - m, c.h - c.inch(0.08)),
              "Megger och tvåpol mot skrov, inte PE-skena.")
    return c


def _metro21(c, x0, y0, x1, y1):
    col = line_color(c, "M02")
    thick = int(metro_width(c, "thick"))
    _label(c, (x0, y0 + c.pt(2)), "FÖRE ARBETE", weight=600, pt=8, anchor="lt", tracking=0.08)
    stations = ["FRÅN", "LÅS/SKYLT", "PROVA DÖD", "MEGGER"]
    n = len(stations)
    line_x = x0 + c.inch(0.58)
    top = y0 + c.inch(0.40)
    bot = y1 - c.inch(0.10)
    c.long_dash((line_x, top), (line_x, bot), width=thick, fill=col)
    side = c.inch(0.24)
    for i, name in enumerate(stations):
        t = i / (n - 1)
        cy = top + t * (bot - top)
        sx, sy = line_x - side / 2, cy - side / 2
        c.rect((sx, sy, sx + side, sy + side), fill=PAPER, outline=c.ink, width=c.hair())
        _label(c, (sx + side + c.pt(10), cy), name, weight=600, pt=9, anchor="lm", tracking=0.05)
        d = (x0 + c.inch(0.20), cy)
        c.disk(d, i + 1)
        c.leader(d, (sx, cy))
        _pico(c, i, x0 + c.inch(1.95), cy)


def _pico(c, i, px, cy):
    w, h = c.inch(0.34), c.inch(0.20)
    box = (px, cy - h / 2, px + w, cy + h / 2)
    if i == 0:
        c.rect(box, outline=c.ink, width=c.hair())
        c.line((px + 6, cy), (px + w * 0.4, cy))
        c.line((px + w * 0.65, cy - 8), (px + w - 6, cy))
        c.draw.ellipse((px + 4, cy - 3, px + 10, cy + 3), fill=c.ink)
        c.draw.ellipse((px + w - 10, cy - 3, px + w - 4, cy + 3), fill=c.ink)
    elif i == 1:
        c.rect((px + 4, cy - 2, px + w * 0.45, cy + h / 2), outline=c.ink, width=c.hair())
        c.draw.arc((px + 8, cy - h / 2 + 2, px + w * 0.45 - 4, cy + 2), 0, 180, fill=c.ink, width=c.hair())
        c.rect((px + w * 0.5, cy - 4, px + w - 2, cy + h / 2), outline=c.ink, width=c.hair())
    elif i == 2:
        c.line((px, cy - 8), (px + w * 0.55, cy + 4))
        c.line((px + 8, cy - 8), (px + w * 0.55 + 8, cy + 4))
        c.rect((px + w * 0.55, cy + 2, px + w, cy + h / 2), outline=c.ink, width=c.hair())
    else:
        c.rect(box, outline=c.ink, width=c.hair())
        _label(c, (px + w / 2, cy), "MΩ", weight=600, pt=7, anchor="mm")


def _tider(c, x0, y0, x1, y1):
    _label(c, (x0, y0 + c.pt(2)), "TVÅ TIDER", weight=600, pt=8, anchor="lt", tracking=0.08)
    gap = c.pt(10)
    top_h = (y1 - y0 - c.pt(16) - gap) / 2
    a0, a1 = y0 + c.pt(16), y0 + c.pt(16) + top_h
    b0, b1 = a1 + gap, y1

    c.rect((x0, a0, x1, a1), outline=c.ink, width=c.hair())
    tab_f = c.font(600, 7.5)
    tw = text_width(tab_f, "UNDER DRIFT", 0.06)
    tab_h = 1.15 * tab_f.size
    c.draw.rectangle((x0, a0, x0 + tw + c.pt(12), a0 + tab_h), fill=c.ink)
    draw_text(c.draw, (x0 + (tw + c.pt(12)) / 2, a0 + tab_h / 2),
              "UNDER DRIFT", tab_f, (255, 255, 255), tracking_em=0.06, anchor="mm")

    rail_y1 = a0 + tab_h + c.inch(0.28)
    c.line((x0 + c.pt(16), rail_y1), (x1 - c.pt(16), rail_y1),
           width=int(metro_width(c, "mid")),
           fill=line_color(c, "M02"))
    ir_x = x0 + (x1 - x0) * 0.22
    ir_w, ir_h = c.inch(0.70), c.inch(0.30)
    c.rect((ir_x, rail_y1 + 4, ir_x + ir_w, rail_y1 + 4 + ir_h), fill=PAPER, outline=c.ink, width=c.hair())
    _label(c, (ir_x + ir_w / 2, rail_y1 + 4 + ir_h / 2), "IR-VAKT", weight=600, pt=7, anchor="mm", tracking=0.05)
    _label(c, (ir_x + ir_w + c.pt(10), rail_y1 + 4 + ir_h / 2),
           "larmar, slår inte ifrån", weight=400, pt=8, anchor="lm")

    c.rect((x0, b0, x1, b1), outline=c.ink, width=c.hair())
    tw2 = text_width(tab_f, "AVSTÄLLD GRUPP", 0.06)
    c.draw.rectangle((x0, b0, x0 + tw2 + c.pt(12), b0 + tab_h), fill=c.ink)
    draw_text(c.draw, (x0 + (tw2 + c.pt(12)) / 2, b0 + tab_h / 2),
              "AVSTÄLLD GRUPP", tab_f, (255, 255, 255), tracking_em=0.06, anchor="mm")

    gy = b0 + tab_h + c.inch(0.22)
    _label(c, (x0 + c.pt(16), gy), "megger mot skrov", weight=400, pt=8.5, anchor="lm")
    mx, my = x0 + c.pt(16), gy + c.pt(12)
    c.rect((mx, my, mx + c.inch(0.52), my + c.inch(0.30)), outline=c.ink, width=c.hair())
    _label(c, (mx + c.inch(0.26), my + c.inch(0.15)), "MΩ", weight=600, pt=8, anchor="mm")
    c.line((mx + c.inch(0.52), my + c.inch(0.15)), (mx + c.inch(1.10), my + c.inch(0.15)))
    ex, ey = mx + c.inch(1.14), my + c.inch(0.15)
    c.line((ex - 12, ey), (ex + 12, ey))
    c.line((ex - 8, ey + 5), (ex + 8, ey + 5))
    c.line((ex - 4, ey + 10), (ex + 4, ey + 10))
    _label(c, (ex + c.pt(16), ey), "SKROV", weight=600, pt=7.5, anchor="lm", tracking=0.05)

    pex = x0 + (x1 - x0) * 0.52
    pey = my - c.pt(4)
    pew, peh = c.inch(1.10), c.inch(0.36)
    c.rect((pex, pey, pex + pew, pey + peh), outline=c.ink, width=c.hair())
    c.rect((pex + 6, pey + peh * 0.35, pex + pew - 6, pey + peh * 0.55), fill=c.ink)
    _label(c, (pex + pew / 2, pey + c.pt(6)), "PE-SKENA", weight=600, pt=6.5, anchor="mt", tracking=0.05)
    c.line((pex, pey), (pex + pew, pey + peh), width=c.heavy())
    c.line((pex + pew, pey), (pex, pey + peh), width=c.heavy())
    _label(c, (pex + pew / 2, pey + peh + c.pt(10)), "inte PE-skena", weight=600, pt=8, anchor="mt")


def main():
    assert font_ok(), "IBM Plex Sans Regular/Medium/SemiBold must load with ÅÄÖ"
    jobs = [
        (draw_figur_11, BOK / "figur-1-1-stotvag-ventil.png", BOK / "figur-1-1-stotvag-ventil-skarm.png"),
        (draw_figur_21, BOK / "figur-2-1-isolering-kedja.png", BOK / "figur-2-1-isolering-kedja-skarm.png"),
    ]
    for fn, print_path, screen_path in jobs:
        pc = fn(True)
        out_p = pc.save(print_path, grayscale=True)
        sc = fn(False)
        out_s = sc.save(screen_path, grayscale=False)
        print("PRINT", print_path, out_p.size, "mode=" + out_p.mode, "dpi=" + str(pc.out_dpi))
        print("SKARM", screen_path, out_s.size, "mode=" + out_s.mode, "dpi=" + str(sc.out_dpi))
    print("IBM Plex loaded: True")


if __name__ == "__main__":
    main()
