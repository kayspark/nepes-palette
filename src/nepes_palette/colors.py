"""Color computation helpers for the nepes palette."""

import colorsys


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert '#AABBCC' to (170, 187, 204)."""
    h = hex_color.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def _rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert (170, 187, 204) to '#AABBCC'."""
    return f"#{r:02X}{g:02X}{b:02X}"


def rgba(hex_color: str, alpha: float) -> str:
    """Convert '#AABBCC', 0.35 to 'rgba(170, 187, 204, 0.35)'."""
    r, g, b = hex_to_rgb(hex_color)
    return f"rgba({r}, {g}, {b}, {alpha})"


def lighten(hex_color: str, amount: float) -> str:
    """Lighten a hex color by amount (0-1) in HLS space."""
    r, g, b = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    l = min(1.0, l + amount)
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return _rgb_to_hex(round(r2 * 255), round(g2 * 255), round(b2 * 255))


def darken(hex_color: str, amount: float) -> str:
    """Darken a hex color by amount (0-1) in HLS space."""
    r, g, b = hex_to_rgb(hex_color)
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    l = max(0.0, l - amount)
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return _rgb_to_hex(round(r2 * 255), round(g2 * 255), round(b2 * 255))


def chart_series(base_colors: list[str], n: int) -> list[str]:
    """Generate n chart colors from base hues.

    Returns the base colors first, then generates additional colors
    by lightening the base hues in a cycle.
    """
    result = list(base_colors)
    i = 0
    while len(result) < n:
        base = base_colors[i % len(base_colors)]
        result.append(lighten(base, 0.15 + 0.05 * (i // len(base_colors))))
        i += 1
    return result[:n]
