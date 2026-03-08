from nepes_palette.colors import rgba, lighten, darken, hex_to_rgb, chart_series


def test_rgba_full_opacity():
    assert rgba("#FF0000", 1.0) == "rgba(255, 0, 0, 1.0)"

def test_rgba_half_opacity():
    assert rgba("#1E1C1A", 0.35) == "rgba(30, 28, 26, 0.35)"

def test_rgba_strips_hash():
    assert rgba("AABBCC", 0.5) == "rgba(170, 187, 204, 0.5)"

def test_lighten_white_stays_white():
    result = lighten("#FFFFFF", 0.1)
    assert result == "#FFFFFF"

def test_lighten_black():
    result = lighten("#000000", 0.5)
    assert result != "#000000"

def test_darken_black_stays_black():
    result = darken("#000000", 0.1)
    assert result == "#000000"

def test_darken_white():
    result = darken("#FFFFFF", 0.5)
    assert result != "#FFFFFF"

def test_lighten_darken_roundtrip():
    original = "#6A84CA"
    lighter = lighten(original, 0.1)
    assert lighter != original
    r1, g1, b1 = hex_to_rgb(original)
    r2, g2, b2 = hex_to_rgb(lighter)
    assert (r2 + g2 + b2) > (r1 + g1 + b1)

def test_hex_to_rgb():
    assert hex_to_rgb("#FF0000") == (255, 0, 0)
    assert hex_to_rgb("#00FF00") == (0, 255, 0)
    assert hex_to_rgb("#1E1C1A") == (30, 28, 26)

def test_chart_series_returns_n_colors():
    base = ["#FEA413", "#6A84CA", "#43AD49"]
    result = chart_series(base, 6)
    assert len(result) == 6
    assert result[:3] == base

def test_chart_series_all_valid_hex():
    base = ["#FEA413", "#6A84CA", "#43AD49", "#E1575C", "#A5A8AF"]
    result = chart_series(base, 10)
    for c in result:
        assert c.startswith("#")
        assert len(c) == 7
