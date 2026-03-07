"""Generate kitty terminal color scheme from the nepes palette."""


def generate_kitty(palette: dict, theme: str) -> str:
    """Generate a kitty .conf color scheme for the given theme."""
    t = palette[theme]
    a = t["ansi"]
    name = "Dark" if theme == "dark" else "Light"
    return f"""# Nepes {name} — kitty color scheme
# Copy to ~/.config/kitty/nepes-{theme}.conf and add:
#   include nepes-{theme}.conf

foreground {t['fg']}
background {t['bg']}
cursor {t['cursor']}
cursor_text_color {t['bg']}
selection_foreground {t['fg']}
selection_background {t['selection']}
url_color {t['cyan']}
active_border_color {t['blue']}
inactive_border_color {t['border']}
bell_border_color {t['orange']}
active_tab_foreground {t['fg']}
active_tab_background {t['bg']}
inactive_tab_foreground {t['fg_muted']}
inactive_tab_background {t['bg_dim']}
tab_bar_background {t['bg_deep']}

# ANSI colors
color0  {a['black']}
color1  {a['red']}
color2  {a['green']}
color3  {a['yellow']}
color4  {a['blue']}
color5  {a['magenta']}
color6  {a['cyan']}
color7  {a['white']}
color8  {a['bright_black']}
color9  {a['bright_red']}
color10 {a['bright_green']}
color11 {a['bright_yellow']}
color12 {a['bright_blue']}
color13 {a['bright_magenta']}
color14 {a['bright_cyan']}
color15 {a['bright_white']}
"""
