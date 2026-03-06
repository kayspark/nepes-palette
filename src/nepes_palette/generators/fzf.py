"""Generate fzf color configuration from the nepes palette."""


def generate_fzf(palette: dict, theme: str) -> str:
    """Generate a shell script that sets FZF_DEFAULT_OPTS colors."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"
    return f"""#!/bin/sh
# Nepes {name} — fzf color configuration
# Source this file or copy the export line to your shell rc

export FZF_DEFAULT_OPTS="$FZF_DEFAULT_OPTS \\
  --color=fg:{t['fg']},bg:{t['bg']},hl:{t['green']} \\
  --color=fg+:{t['fg']},bg+:{t['bg_hl']},hl+:{t['green_bright']} \\
  --color=prompt:{t['blue']},pointer:{t['blue']},marker:{t['orange']} \\
  --color=spinner:{t['magenta']},info:{t['fg_muted']},header:{t['fg_dim']} \\
  --color=border:{t['border']},label:{t['fg_dim']},separator:{t['border']} \\
  --color=gutter:{t['bg']}"
"""
