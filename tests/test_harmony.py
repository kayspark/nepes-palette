from nepes_palette.harmony import hex_to_hsl, hue_distribution, saturation_consistency


def test_hex_to_hsl_red():
    h, s, l = hex_to_hsl("#FF0000")
    assert abs(h - 0.0) < 1.0  # hue ~0 degrees
    assert abs(s - 100.0) < 1.0
    assert abs(l - 50.0) < 1.0


def test_hex_to_hsl_blue():
    h, s, l = hex_to_hsl("#0000FF")
    assert abs(h - 240.0) < 1.0


def test_hue_distribution_even():
    # 6 evenly spaced hues should have low variance
    colors = ["#FF0000", "#FFFF00", "#00FF00", "#00FFFF", "#0000FF", "#FF00FF"]
    result = hue_distribution(colors)
    assert result["gap_variance"] < 100  # relatively even


def test_saturation_consistency():
    # Similar saturation colors
    colors = ["#4A6ABF", "#D4252C", "#43AD49"]
    result = saturation_consistency(colors)
    assert "std_dev" in result
    assert "mean" in result
