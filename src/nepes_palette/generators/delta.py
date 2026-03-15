"""Generate delta gitconfig include from the nepes palette."""

from nepes_palette.colors import hex_to_rgb
from nepes_palette.palette import get_semantic_colors


def _blend(fg_hex: str, bg_hex: str, alpha: float) -> str:
    """Blend fg into bg at alpha (0-1), return #RRGGBB."""
    fg = hex_to_rgb(fg_hex)
    bg = hex_to_rgb(bg_hex)
    r = int(fg[0] * alpha + bg[0] * (1 - alpha))
    g = int(fg[1] * alpha + bg[1] * (1 - alpha))
    b = int(fg[2] * alpha + bg[2] * (1 - alpha))
    return f"#{r:02X}{g:02X}{b:02X}"


def generate_delta(palette: dict) -> str:
    """Generate a gitconfig include fragment for delta with dark-theme colors."""
    dark = palette["dark"]
    sem = get_semantic_colors(palette, "dark")
    bg = dark["bg"]

    # Subtle tinted backgrounds matching editor diff aesthetics (nvim/emacs)
    add_bg = _blend(dark["green"], bg, 0.12)
    del_bg = _blend(dark["red"], bg, 0.12)
    add_emph_bg = _blend(dark["green"], bg, 0.25)
    del_emph_bg = _blend(dark["red"], bg, 0.25)

    return f"""\
# Nepes Dark — delta color theme
# Include in ~/.gitconfig:  [include] path = ~/workspace/colorscheme/delta-nepes/nepes.gitconfig

[delta "nepes-dark"]
    syntax-theme = nepes-dark
    dark = true
    minus-style = syntax "{del_bg}"
    minus-emph-style = syntax "{del_emph_bg}"
    plus-style = syntax "{add_bg}"
    plus-emph-style = syntax "{add_emph_bg}"
    inline-hint-style = "{dark["fg_muted"]}"
    line-numbers-minus-style = "{sem["removed"]}"
    line-numbers-plus-style = "{sem["added"]}"
    line-numbers-zero-style = "{dark["fg_muted"]}"
    commit-decoration-style = "{dark["blue"]}" ol
    file-style = "{dark["fg"]}" bold
    file-decoration-style = "{dark["blue"]}" ul
    hunk-header-decoration-style = "{dark["cyan"]}" box
    hunk-header-style = file line-number "{dark["fg_dim"]}"

[color "diff"]
    meta = "bold {dark["blue"]}"
    frag = "bold {dark["cyan"]}"
    old = "{sem["removed"]}"
    new = "{sem["added"]}"
    commit = "bold {dark["blue"]}"
    whitespace = "reverse {sem["removed"]}"
"""
