def _hex_to_rgb(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))


def _linearize(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    r, g, b = _hex_to_rgb(hex_color)
    return 0.2126 * _linearize(r) + 0.7152 * _linearize(g) + 0.0722 * _linearize(b)


def contrast_ratio(fg: str, bg: str) -> float:
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def check_wcag(fg: str, bg: str) -> dict:
    ratio = contrast_ratio(fg, bg)
    return {"ratio": round(ratio, 2), "aa": ratio >= 4.5, "aaa": ratio >= 7.0}


def validate_palette(palette: dict) -> list[dict]:
    """Check all semantic fg colors against theme backgrounds.

    Returns list of results with pass/fail for each pair.
    """
    from .palette import get_semantic_colors

    results = []
    for theme in ("dark", "light"):
        bg = palette[theme]["bg"]
        semantic = get_semantic_colors(palette, theme)
        for role, color in semantic.items():
            wcag = check_wcag(color, bg)
            results.append({"theme": theme, "role": role, "fg": color, "bg": bg, **wcag})
    return results
