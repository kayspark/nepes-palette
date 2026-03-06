import tomllib
from pathlib import Path


def load_palette(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)


def resolve_color(palette: dict, theme: str, color_name: str) -> str:
    """Resolve a semantic color name to a hex value.

    Looks up in theme section first, falls back to brand.
    """
    theme_colors = palette.get(theme, {})
    if color_name in theme_colors:
        return theme_colors[color_name]
    if color_name in palette.get("brand", {}):
        return palette["brand"][color_name]
    raise KeyError(f"Color '{color_name}' not found in theme '{theme}' or brand")


def get_semantic_colors(palette: dict, theme: str) -> dict[str, str]:
    """Resolve all semantic mappings to hex values for a given theme.

    Per-theme overrides in [dark.semantic] or [light.semantic] take
    precedence over the shared [semantic] section.
    """
    semantic = dict(palette["semantic"])
    # Apply per-theme semantic overrides
    theme_semantic = palette.get(theme, {}).get("semantic", {})
    semantic.update(theme_semantic)
    return {role: resolve_color(palette, theme, color_name) for role, color_name in semantic.items()}
