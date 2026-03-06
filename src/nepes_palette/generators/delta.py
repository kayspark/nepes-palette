"""Generate delta gitconfig include from the nepes palette."""

from nepes_palette.palette import get_semantic_colors


def generate_delta(palette: dict) -> str:
    """Generate a gitconfig include fragment for delta with dark-theme colors."""
    dark = palette["dark"]
    sem = get_semantic_colors(palette, "dark")

    return f"""\
# Nepes Dark — delta configuration
# Include in ~/.gitconfig:  [include] path = nepes.gitconfig

[delta]
    syntax-theme = nepes-dark
    line-numbers = true
    side-by-side = true
    minus-style = syntax "{dark["red_dim"]}"
    minus-emph-style = syntax "{dark["red"]}"
    plus-style = syntax "{dark["green_dim"]}"
    plus-emph-style = syntax "{dark["green"]}"
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
