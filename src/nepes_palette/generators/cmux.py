"""Generate cmux (Ghostty) color theme from the nepes palette."""


def generate_cmux(palette: dict, theme: str) -> str:
    """Generate a Ghostty-format theme file for cmux."""
    t = palette[theme]
    a = t["ansi"]
    name = "Dark" if theme == "dark" else "Light"
    return f"""\
# Nepes {name} — cmux / Ghostty color theme
# Place in ~/.config/ghostty/themes/nepes-{theme}
# Then set: theme = nepes-{theme}

background = {t['bg']}
foreground = {t['fg']}
cursor-color = {t['cursor']}
cursor-text = {t['bg']}
selection-background = {t['selection']}
selection-foreground = {t['fg']}

palette = 0={a['black']}
palette = 1={a['red']}
palette = 2={a['green']}
palette = 3={a['yellow']}
palette = 4={a['blue']}
palette = 5={a['magenta']}
palette = 6={a['cyan']}
palette = 7={a['white']}
palette = 8={a['bright_black']}
palette = 9={a['bright_red']}
palette = 10={a['bright_green']}
palette = 11={a['bright_yellow']}
palette = 12={a['bright_blue']}
palette = 13={a['bright_magenta']}
palette = 14={a['bright_cyan']}
palette = 15={a['bright_white']}
"""
