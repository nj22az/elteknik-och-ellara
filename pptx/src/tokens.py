# Visual tokens — riktlinje v3 (LOCKED).
# Japanese information design: Tokyo Metro wayfinding + JIS label + pillbox.
# Swedish labels only. No second type family. No serif. No gray text.
# Color is LINE ID only, never safety semantics.

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FONTS_DIR = ROOT / "pptx" / "fonts"
BOK_DIR = ROOT / "bok"
PPTX_DIR = ROOT / "pptx"

FONT_REG = FONTS_DIR / "IBMPlexSans-Regular.ttf"
FONT_MED = FONTS_DIR / "IBMPlexSans-Medium.ttf"
FONT_SEM = FONTS_DIR / "IBMPlexSans-SemiBold.ttf"

# Ink / paper. Print = 100% K.
INK = (0x11, 0x11, 0x11)
PAPER = (0xFF, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)

# Render at 600 dpi then Lanczos-downsample to 300 so 0.35 pt hairlines survive.
RENDER_DPI = 600
PRINT_DPI = 300
COLUMN_IN = 6.00  # KDP live width: 7.00 page - 0.625 gutter each side ≈ 5.75; spec = 6.00

# 0.35 pt hairline at 600 dpi ≈ 2.92 px.
HAIRLINE_PX = 3
RULE_PX = 3
RULE_HEAVY_PX = 6  # ~0.7 pt / 2 px at 300 dpi

# Book callout disk: 6.5 mm diameter.
DISK_MM = 6.5
DISK_PX_600 = round(DISK_MM / 25.4 * RENDER_DPI)  # 154

# Line table (M03–M12 are theme swatches on the master, not on these two figures).
LINES = {
    "M01": {"name": "Elsakerhet", "name_sv": "Elsäkerhet", "color": (0xE6, 0x00, 0x2D), "print_dash": None},
    "M02": {"name": "Isolering", "name_sv": "Isolering", "color": (0xF3, 0x97, 0x00), "print_dash": (80, 24)},
    "M03": {"name": "Resistiv DC", "name_sv": "Resistiv DC", "color": (0x8A, 0x99, 0xA3), "print_dash": (12, 10, 4, 10)},
    "M04": {"name": "Enfas AC", "name_sv": "Enfas AC", "color": (0x00, 0xA7, 0xDB), "print_dash": "double"},
    "M05": {"name": "Trefas", "name_sv": "Trefas", "color": (0x00, 0xB2, 0x61), "print_dash": None},
    "M06": {"name": "Maskiner", "name_sv": "Maskiner", "color": (0xE8, 0x52, 0x98), "print_dash": (28, 10, 4, 10, 4, 10)},
    "M07": {"name": "Eltavla", "name_sv": "Eltavla", "color": (0x8F, 0x76, 0xD6), "print_dash": None},
    "M08": {"name": "Verktyg", "name_sv": "Verktyg", "color": (0x00, 0xAD, 0xA9), "print_dash": (28, 16)},
    "M09": {"name": "Ritningar", "name_sv": "Ritningar", "color": (0xC4, 0xA3, 0x5A), "print_dash": "double"},
    "M10": {"name": "Hallkrets", "name_sv": "Hållkrets", "color": (0x9C, 0x5E, 0x31), "print_dash": (6, 10)},
    "M11": {"name": "Elarbete", "name_sv": "Elarbete", "color": (0x00, 0x78, 0xC8), "print_dash": None},
    "M12": {"name": "Felsokning", "name_sv": "Felsökning", "color": (0x5A, 0x2D, 0x27), "print_dash": (40, 12)},
}

STATIONS = {
    "V1": {"name": "Vecka 1", "lines": ["M01"], "color": (0x1A, 0x1A, 0x1A)},
    "V2": {"name": "Vecka 2", "lines": ["M02"], "color": (0x6B, 0x2D, 0x5B)},
    "V3": {"name": "Vecka 3", "lines": ["M03"], "color": (0x24, 0x5C, 0x3A)},
    "V4": {"name": "Vecka 4", "lines": ["M04"], "color": (0x1B, 0x3A, 0x5C)},
    "V5": {"name": "Vecka 5", "lines": ["M05"], "color": (0x5C, 0x3B, 0x00)},
    "V6": {"name": "Vecka 6", "lines": ["M06"], "color": (0x3D, 0x24, 0x58)},
    "V7": {"name": "Vecka 7", "lines": ["M07", "M08"], "color": (0x0E, 0x4A, 0x4A)},
    "V8": {"name": "Vecka 8", "lines": ["M09", "M10"], "color": (0x4A, 0x3B, 0x2A)},
    "V9": {"name": "Vecka 9", "lines": ["M11", "M12"], "color": (0x2A, 0x33, 0x40)},
}

# PPTX 16:9
SLIDE_W_IN = 13.333333
SLIDE_H_IN = 7.5
PPTX_HEADING_PT = 28
PPTX_BODY_PT = 18
PPTX_LABEL_PT = 12
PPTX_CODE_PT = 14
PPTX_DISK_PT = 28
