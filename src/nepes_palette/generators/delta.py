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
# Nepes Dark — delta configuration
# Include in ~/.gitconfig:  [include] path = nepes.gitconfig

[delta]
    syntax-theme = nepes-dark
    line-numbers = true
    side-by-side = true
    minus-style = syntax "{del_bg}"
    minus-emph-style = syntax "{del_emph_bg}"
    plus-style = syntax "{add_bg}"
    plus-emph-style = syntax "{add_emph_bg}"
    line-numbers-minus-style = "{sem["removed"]}"
    line-numbers-plus-style = "{sem["added"]}"
    line-numbers-zero-style = "{dark["fg_muted"]}"
    line-numbers-left-format = "{{nm:>4}} "
    line-numbers-right-format = "{{np:>4}} "

[delta "decorations"]
    commit-decoration-style = "{sem["keyword"]}" ol
    file-style = "{dark["fg"]}" bold
    file-decoration-style = "{dark["blue"]}" ul
    hunk-header-decoration-style = "{dark["cyan"]}" box
    hunk-header-style = file line-number "{dark["fg_dim"]}"
"""
