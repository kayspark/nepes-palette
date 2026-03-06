from pathlib import Path
from nepes_palette.palette import load_palette, resolve_color, get_semantic_colors


PALETTE_PATH = Path(__file__).parent.parent / "palette.toml"


def test_load_palette_returns_all_sections():
    p = load_palette(PALETTE_PATH)
    assert "brand" in p
    assert "dark" in p
    assert "light" in p
    assert "semantic" in p


def test_dark_has_bg_and_fg():
    p = load_palette(PALETTE_PATH)
    assert p["dark"]["bg"] == "#1E1C1A"
    assert p["dark"]["fg"] == "#DCD8D4"


def test_dark_ansi_has_16_colors():
    p = load_palette(PALETTE_PATH)
    ansi = p["dark"]["ansi"]
    assert len(ansi) == 16


def test_semantic_has_keyword():
    p = load_palette(PALETTE_PATH)
    assert p["semantic"]["keyword"] == "blue"


def test_resolve_color_from_theme():
    p = load_palette(PALETTE_PATH)
    assert resolve_color(p, "dark", "blue") == "#6A84CA"


def test_resolve_color_falls_back_to_brand():
    p = load_palette(PALETTE_PATH)
    # "bg" exists only in dark theme, not brand — test theme lookup
    assert resolve_color(p, "dark", "bg") == "#1E1C1A"


def test_get_semantic_colors():
    p = load_palette(PALETTE_PATH)
    sem = get_semantic_colors(p, "dark")
    assert sem["keyword"] == "#6A84CA"  # blue in dark theme
    assert sem["string"] == "#43AD49"   # green in dark theme
    assert sem["error"] == "#E1575C"    # red in dark theme
