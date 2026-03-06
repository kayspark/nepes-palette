import colorsys
import statistics


def hex_to_hsl(hex_color: str) -> tuple[float, float, float]:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    h_val, l_val, s_val = colorsys.rgb_to_hls(r, g, b)
    return h_val * 360, s_val * 100, l_val * 100


def hue_distribution(colors: list[str]) -> dict:
    """Analyze how evenly hues are distributed on the color wheel."""
    hues = sorted(hex_to_hsl(c)[0] for c in colors)
    gaps = []
    for i in range(len(hues)):
        gap = (hues[(i + 1) % len(hues)] - hues[i]) % 360
        gaps.append(gap)
    ideal_gap = 360 / len(hues)
    gap_variance = statistics.variance(gaps) if len(gaps) > 1 else 0
    return {
        "hues": hues,
        "gaps": gaps,
        "ideal_gap": ideal_gap,
        "gap_variance": round(gap_variance, 2),
        "max_gap": max(gaps),
        "min_gap": min(gaps),
    }


def saturation_consistency(colors: list[str]) -> dict:
    """Check if saturations are consistent across base colors."""
    sats = [hex_to_hsl(c)[1] for c in colors]
    return {
        "saturations": [round(s, 1) for s in sats],
        "mean": round(statistics.mean(sats), 1),
        "std_dev": round(statistics.stdev(sats), 1) if len(sats) > 1 else 0,
    }


def lightness_balance(palette: dict) -> dict:
    """Compare lightness distribution between dark and light theme foreground colors."""
    from .palette import get_semantic_colors

    results = {}
    for theme in ("dark", "light"):
        semantic = get_semantic_colors(palette, theme)
        fg_colors = [v for k, v in semantic.items() if not k.startswith("heading")]
        lightnesses = [hex_to_hsl(c)[2] for c in fg_colors]
        results[theme] = {
            "mean_lightness": round(statistics.mean(lightnesses), 1),
            "std_dev": round(statistics.stdev(lightnesses), 1) if len(lightnesses) > 1 else 0,
        }
    return results


def analyze_harmony(palette: dict) -> dict:
    """Full harmony analysis of palette base colors."""
    base_colors = []
    for name in ("blue", "red", "green", "orange", "magenta", "cyan", "yellow"):
        if name in palette["dark"]:
            base_colors.append(palette["dark"][name])

    return {
        "hue_distribution": hue_distribution(base_colors),
        "saturation_consistency": saturation_consistency(base_colors),
        "lightness_balance": lightness_balance(palette),
    }
