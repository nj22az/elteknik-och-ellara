"""v3 visual tokens — site/riktlinje.md (v3 + V-station addendum).

Japanese information design: Tokyo Metro wayfinding + JIS label + pillbox.
NOT Apple glass, NOT Palatino, NOT Material. Swedish labels only.

Type: IBM Plex Sans static TTF. 400 body, 500 UI, 600 code/label/heading.
NEVER light. Tabular lining. Line codes M01/V1: 600, tracking ~0.06em, ALL CAPS.
No serif. No second family on figures.

Color is LINE ID only, never safety semantics (red is M01, not danger).
0 border-radius everywhere except numbered callout DISKS (circles).
No shadow. No gradient. No 980px pills.
"""
from __future__ import annotations

from pathlib import Path

# --- ink / paper / rule -------------------------------------------------
INK = (0x11, 0x11, 0x11)          # #111111 screen
INK_K = (0x00, 0x00, 0x00)        # 100% K in print
PAPER = (0xFF, 0xFF, 0xFF)        # #FFFFFF
# Hierarchy = size and weight only. NO gray text.
# rule: 1px solid ink (screen); print hairline 0.35 pt
# rule-heavy: 2px solid ink (FARA frame, active station)
HAIRLINE_PT = 0.35
RULE_HEAVY_PX_SCREEN = 2

# --- M-line colors (identity = code; hue is screen help only) -----------
M_LINES = {
    "M01": {"name": "Elsäkerhet",  "color": (0xE6, 0x00, 0x2D), "dash": "solid"},
    "M02": {"name": "Isolering",   "color": (0xF3, 0x97, 0x00), "dash": "long-dash"},
    "M03": {"name": "Resistiv DC", "color": (0x8A, 0x99, 0xA3), "dash": "dash-dot"},
    "M04": {"name": "Enfas AC",    "color": (0x00, 0xA7, 0xDB), "dash": "double-thin"},
    "M05": {"name": "Trefas",      "color": (0x00, 0xB2, 0x61), "dash": "solid-thick"},
    "M06": {"name": "Maskiner",    "color": (0xE8, 0x52, 0x98), "dash": "dash-dot-dash"},
    "M07": {"name": "Eltavla",     "color": (0x8F, 0x76, 0xD6), "dash": "solid"},
    "M08": {"name": "Verktyg",     "color": (0x00, 0xAD, 0xA9), "dash": "dashed"},
    "M09": {"name": "Ritningar",   "color": (0xC4, 0xA3, 0x5A), "dash": "double"},
    "M10": {"name": "Hållkrets",   "color": (0x9C, 0x5E, 0x31), "dash": "dotted"},
    "M11": {"name": "Elarbete",    "color": (0x00, 0x78, 0xC8), "dash": "solid"},
    "M12": {"name": "Felsökning",  "color": (0x5A, 0x2D, 0x27), "dash": "thick-dashed"},
}

# --- V-station colors (OWN, distinct from M-lines) ----------------------
V_STATIONS = {
    "V1": {"name": "Vecka 1", "color": (0x1A, 0x1A, 0x1A), "dash": "solid",        "stops": ("M01",)},
    "V2": {"name": "Vecka 2", "color": (0x6B, 0x2D, 0x5B), "dash": "dashed",       "stops": ("M02",)},
    "V3": {"name": "Vecka 3", "color": (0x24, 0x5C, 0x3A), "dash": "dash-dot",     "stops": ("M03",)},
    "V4": {"name": "Vecka 4", "color": (0x1B, 0x3A, 0x5C), "dash": "double-thin",  "stops": ("M04",)},
    "V5": {"name": "Vecka 5", "color": (0x5C, 0x3B, 0x00), "dash": "solid-thick",  "stops": ("M05",)},
    "V6": {"name": "Vecka 6", "color": (0x3D, 0x24, 0x58), "dash": "dash-dot",     "stops": ("M06",)},
    "V7": {"name": "Vecka 7", "color": (0x0E, 0x4A, 0x4A), "dash": "double",       "stops": ("M07", "M08")},
    "V8": {"name": "Vecka 8", "color": (0x4A, 0x3B, 0x2A), "dash": "dotted",       "stops": ("M09", "M10")},
    "V9": {"name": "Vecka 9", "color": (0x2A, 0x33, 0x40), "dash": "thick-dashed", "stops": ("M11", "M12")},
}

# M-lozenge: rectangle, 0 radius. Height 1.15em of the code.
# Padding ~0.15em 0.4em. SCREEN: M-line-color fill, white code.
# PRINT: black fill, white code. Write M01 not m1. Name sits BESIDE.
LOZENGE_HEIGHT_EM = 1.15
LOZENGE_PAD_Y_EM = 0.15
LOZENGE_PAD_X_EM = 0.40
CODE_TRACKING_EM = 0.06
OBS_TRACKING_EM = 0.08

# V-station: SQUARE, 0 radius. SCREEN: V-color fill, white code.
# PRINT: black fill, white code. Write V1 not v1. Week name sits beside.
# Active: 2px ink frame outside.
# Transfer V7–V9: V-square plus two M-lozenges side by side, no mixed fill.

# Callout disks: CIRCLE. Book diameter 6.5 mm. Fill ink, number white 600 tabular.
# Numbers 1,2,3 never ①. Max 7 per figure. Disk on empty space, not on a line.
# Leader: straight hairline 0.35pt, no curves. Disks always ink.
DISK_DIAMETER_MM = 6.5
DISK_PPTX_PT = 28

# KDP / print figures
PAGE_IN = (7.00, 10.00)
LIVE_WIDTH_IN = 6.00
FIG_HEIGHT_IN = (4.50, 5.50)
OUT_DPI = 300
HI_DPI = 600  # render here, Lanczos-downsample to 300 so hairlines survive

# PPTX 16:9
SLIDE_IN = (13.333333, 7.5)
PPTX_HEADING_PT = 28
PPTX_BODY_PT = 18
PPTX_LABEL_PT = 12
PPTX_CODE_PT = 14

# Book figure type (pt)
BOOK_LABEL_PT = 8.5
BOOK_CODE_PT = 8
BOOK_CALLOUT_PT = 8
BOOK_TITLE_PT = 11
BOOK_OBS_PT = 9

FONT_DIR = Path(__file__).resolve().parents[1] / "fonts"
FONT_FILES = {
    400: "IBMPlexSans-Regular.ttf",
    500: "IBMPlexSans-Medium.ttf",
    600: "IBMPlexSans-SemiBold.ttf",
}

REPO = Path(__file__).resolve().parents[2]
BOK = REPO / "bok"
PPTX_DIR = REPO / "pptx"
