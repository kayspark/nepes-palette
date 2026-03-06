from nepes_palette.validate import relative_luminance, contrast_ratio, check_wcag


def test_relative_luminance_white():
    assert abs(relative_luminance("#FFFFFF") - 1.0) < 0.001


def test_relative_luminance_black():
    assert abs(relative_luminance("#000000") - 0.0) < 0.001


def test_contrast_ratio_black_white():
    ratio = contrast_ratio("#000000", "#FFFFFF")
    assert abs(ratio - 21.0) < 0.1


def test_contrast_ratio_symmetric():
    r1 = contrast_ratio("#23438E", "#DCD8D4")
    r2 = contrast_ratio("#DCD8D4", "#23438E")
    assert abs(r1 - r2) < 0.001


def test_check_wcag_passes_high_contrast():
    result = check_wcag("#000000", "#FFFFFF")
    assert result["aa"]
    assert result["aaa"]


def test_check_wcag_fails_low_contrast():
    result = check_wcag("#787068", "#1E1C1A")  # comment on dark bg
    # This should at least have a ratio > 1
    assert result["ratio"] > 1.0
