"""Canonical palette definition — single source of truth.

Every hex value is WCAG-validated and pinned. Only computed sections
(chart, border_subtle, bg_glass, motion) derive values at import time.
"""

from .colors import chart_series, rgba

# ── Brand Colors ────────────────────────────────────────────
_brand = {
    "blue": "#23438E",
    "orange": "#FEA413",
    "red": "#D4252C",
    "green": "#43AD49",
    "gray": "#A5A8AF",
    "light_gray": "#E7E6E6",
    "dark": "#1E1C1A",
    "dark_gray": "#44546A",
}

# ── Dark Theme ──────────────────────────────────────────────
_dark = {
    # Background ramp (6 steps: deep -> surface -> overlay)
    "bg_deep": "#161412",
    "bg": "#1E1C1A",
    "bg_dim": "#262422",
    "bg_alt": "#2E2C2A",
    "bg_hl": "#3E3A38",
    "bg_overlay": "#504848",
    # Foreground ramp (4 steps: main -> dim -> subtle -> muted)
    "fg": "#DCD8D4",
    "fg_dim": "#B6B0AC",
    "fg_subtle": "#96908C",
    "fg_muted": "#787068",
    # Core colors
    "blue": "#6A84CA",
    "blue_dim": "#23438E",
    "blue_bright": "#6B8AD8",
    "red": "#E1575C",
    "red_dim": "#A81E23",
    "red_bright": "#E85B61",
    "green": "#43AD49",
    "green_dim": "#348A3A",
    "green_bright": "#6BCF70",
    "orange": "#FEA413",
    "orange_dim": "#CC8410",
    "orange_bright": "#FFBD4A",
    # Extended colors
    "magenta": "#A274C3",
    "magenta_dim": "#7A4FA0",
    "magenta_bright": "#BB8EDA",
    "cyan": "#3A9BA5",
    "cyan_dim": "#2D7A82",
    "cyan_bright": "#5CBDC7",
    "yellow": "#E8C55A",
    "yellow_dim": "#C9A63E",
    "yellow_bright": "#F5DA7F",
    # Utility
    "cursor": "#DCD8D4",
    "selection": "#2D4A6A",
    "border": "#3E3A38",
    "comment": "#8D847B",
    # ANSI 16
    "ansi": {
        "black": "#161412",
        "red": "#E1575C",
        "green": "#43AD49",
        "yellow": "#FEA413",
        "blue": "#6A84CA",
        "magenta": "#A274C3",
        "cyan": "#3A9BA5",
        "white": "#A5A8AF",
        "bright_black": "#8D847B",
        "bright_red": "#E85B61",
        "bright_green": "#6BCF70",
        "bright_yellow": "#FFBD4A",
        "bright_blue": "#6B8AD8",
        "bright_magenta": "#BB8EDA",
        "bright_cyan": "#5CBDC7",
        "bright_white": "#DCD8D4",
    },
    # Per-theme semantic overrides (dark has none)
    "semantic": {},
}

# ── Light Theme ─────────────────────────────────────────────
_light = {
    # Background ramp
    "bg_deep": "#FFFFFF",
    "bg": "#F8F8F8",
    "bg_dim": "#F0F0F0",
    "bg_alt": "#E7E6E6",
    "bg_hl": "#D8D7D7",
    "bg_overlay": "#C9C8C8",
    # Foreground ramp
    "fg": "#1C1C1E",
    "fg_dim": "#3A3A3E",
    "fg_subtle": "#5A5A64",
    "fg_muted": "#7A7A84",
    # Core colors
    "blue": "#23438E",
    "blue_dim": "#1B3470",
    "blue_bright": "#2E55B0",
    "red": "#C4181F",
    "red_dim": "#9E1319",
    "red_bright": "#D4252C",
    "green": "#2A8030",
    "green_dim": "#246C29",
    "green_bright": "#43AD49",
    "orange": "#D08A10",
    "orange_dim": "#99640B",
    "orange_bright": "#FEA413",
    # Extended
    "magenta": "#7A4FA0",
    "magenta_dim": "#613E80",
    "magenta_bright": "#9B6ABF",
    "cyan": "#2D7A82",
    "cyan_dim": "#236068",
    "cyan_bright": "#3A9BA5",
    "yellow": "#866E1C",
    "yellow_dim": "#7C6519",
    "yellow_bright": "#C9A63E",
    # Utility
    "cursor": "#1C1C1E",
    "selection": "#B8D0F0",
    "border": "#D8D7D7",
    "comment": "#707079",
    # ANSI 16
    "ansi": {
        "black": "#1C1C1E",
        "red": "#C4181F",
        "green": "#2A8030",
        "yellow": "#D08A10",
        "blue": "#23438E",
        "magenta": "#7A4FA0",
        "cyan": "#2D7A82",
        "white": "#E7E6E6",
        "bright_black": "#707079",
        "bright_red": "#D4252C",
        "bright_green": "#43AD49",
        "bright_yellow": "#FEA413",
        "bright_blue": "#2E55B0",
        "bright_magenta": "#9B6ABF",
        "bright_cyan": "#3A9BA5",
        "bright_white": "#F8F8F8",
    },
    # Per-theme semantic overrides
    "semantic": {
        "constant": "orange_dim",
        "number": "orange_dim",
        "warning": "orange_dim",
        "changed": "orange_dim",
        "heading5": "orange_dim",
    },
}

# ── Semantic Mappings ───────────────────────────────────────
_semantic = {
    "keyword": "blue",
    "builtin": "blue_bright",
    "function": "cyan",
    "string": "green",
    "type": "magenta",
    "constant": "orange",
    "number": "orange",
    "variable": "fg",
    "parameter": "fg_dim",
    "operator": "fg_subtle",
    "comment": "comment",
    "error": "red",
    "warning": "orange",
    "info": "blue",
    "hint": "cyan",
    "success": "green",
    "added": "green",
    "changed": "orange",
    "removed": "red",
    # Heading rainbow (1-8 cycle)
    "heading1": "blue",
    "heading2": "magenta",
    "heading3": "cyan",
    "heading4": "green",
    "heading5": "orange",
    "heading6": "red",
    "heading7": "yellow",
    "heading8": "blue_bright",
}

# ── Computed: Chart Colors ──────────────────────────────────
_dark_chart_bases = [
    _dark["blue"],
    _dark["orange"],
    _dark["green"],
    _dark["magenta"],
    _dark["cyan"],
    _dark["red"],
]
_light_chart_bases = [
    _light["blue"],
    _light["orange"],
    _light["green"],
    _light["magenta"],
    _light["cyan"],
    _light["red"],
]

_dark["chart"] = {
    "series": chart_series(_dark_chart_bases, 12),
    "step_bg": rgba(_dark["blue"], 0.12),
    "recipe_bg": rgba(_dark["orange"], 0.10),
}

_light["chart"] = {
    "series": chart_series(_light_chart_bases, 12),
    "step_bg": rgba(_light["blue"], 0.08),
    "recipe_bg": rgba(_light["orange"], 0.07),
}

# ── Computed: Subtle Borders & Glass Backgrounds ────────────
_dark["border_subtle"] = rgba(_dark["border"], 0.5)
_dark["bg_glass"] = rgba(_dark["bg"], 0.85)

_light["border_subtle"] = rgba(_light["border"], 0.5)
_light["bg_glass"] = rgba(_light["bg"], 0.85)

# ── Motion / Animation Tokens ──────────────────────────────
_motion = {
    "duration_fast": "100ms",
    "duration_normal": "200ms",
    "duration_slow": "400ms",
    "easing_default": "cubic-bezier(0.4, 0, 0.2, 1)",
    "easing_enter": "cubic-bezier(0, 0, 0.2, 1)",
    "easing_exit": "cubic-bezier(0.4, 0, 1, 1)",
}

# ── Exported Palette ────────────────────────────────────────
PALETTE: dict = {
    "brand": _brand,
    "dark": _dark,
    "light": _light,
    "semantic": _semantic,
    "motion": _motion,
}
