"""Generate yazi flavor TOML from the nepes palette."""


def generate_yazi(palette: dict, theme: str) -> str:
    """Generate a yazi flavor TOML for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"
    variant = "dark" if theme == "dark" else "light"
    return f"""# Nepes {name} — yazi flavor
# Copy to ~/.config/yazi/flavors/nepes-{variant}.yazi/flavor.toml

[flavor]
name = "nepes-{variant}"
author = "kayspark"
desc = "Nepes corporate colorscheme — {variant} variant"

[manager]
cwd = {{ fg = "{t['blue']}" }}
hovered = {{ bg = "{t['bg_hl']}" }}
preview_hovered = {{ bg = "{t['bg_alt']}" }}
find_keyword = {{ fg = "{t['green']}", bold = true }}
find_position = {{ fg = "{t['magenta']}", italic = true }}
marker_copied = {{ fg = "{t['green']}", bg = "{t['green']}" }}
marker_cut = {{ fg = "{t['red']}", bg = "{t['red']}" }}
marker_marked = {{ fg = "{t['blue']}", bg = "{t['blue']}" }}
marker_selected = {{ fg = "{t['orange']}", bg = "{t['orange']}" }}
tab_active = {{ fg = "{t['fg']}", bg = "{t['bg']}" }}
tab_inactive = {{ fg = "{t['fg_muted']}", bg = "{t['bg_dim']}" }}
count_copied = {{ fg = "{t['bg']}", bg = "{t['green']}" }}
count_cut = {{ fg = "{t['bg']}", bg = "{t['red']}" }}
count_selected = {{ fg = "{t['bg']}", bg = "{t['orange']}" }}
border_symbol = "|"
border_style = {{ fg = "{t['border']}" }}

[status]
separator_open = ""
separator_close = ""
separator_style = {{ fg = "{t['border']}", bg = "{t['border']}" }}
mode_normal = {{ fg = "{t['bg']}", bg = "{t['blue']}", bold = true }}
mode_select = {{ fg = "{t['bg']}", bg = "{t['green']}", bold = true }}
mode_unset = {{ fg = "{t['bg']}", bg = "{t['magenta']}", bold = true }}
progress_label = {{ fg = "{t['fg']}", bold = true }}
progress_normal = {{ fg = "{t['blue']}", bg = "{t['border']}" }}
progress_error = {{ fg = "{t['red']}", bg = "{t['border']}" }}
permissions_t = {{ fg = "{t['blue']}" }}
permissions_r = {{ fg = "{t['green']}" }}
permissions_w = {{ fg = "{t['red']}" }}
permissions_x = {{ fg = "{t['orange']}" }}
permissions_s = {{ fg = "{t['fg_muted']}" }}

[input]
border = {{ fg = "{t['blue']}" }}
title = {{ fg = "{t['fg']}" }}
value = {{ fg = "{t['fg']}" }}
selected = {{ bg = "{t['bg_hl']}" }}

[select]
border = {{ fg = "{t['blue']}" }}
active = {{ fg = "{t['green']}", bold = true }}
inactive = {{ fg = "{t['fg_dim']}" }}

[which]
cols = 3
mask = {{ bg = "{t['bg_alt']}" }}
cand = {{ fg = "{t['cyan']}" }}
rest = {{ fg = "{t['fg_muted']}" }}
desc = {{ fg = "{t['fg_dim']}" }}
separator = "  "
separator_style = {{ fg = "{t['border']}" }}

[completion]
border = {{ fg = "{t['blue']}" }}
active = {{ bg = "{t['bg_hl']}" }}
inactive = {{}}
icon_file = ""
icon_folder = ""
icon_command = ""
"""
