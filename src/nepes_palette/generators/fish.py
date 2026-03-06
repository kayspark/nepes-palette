"""Generate fish shell color theme from the nepes palette."""


def _strip(hex_color: str) -> str:
    """Strip the leading '#' from a hex color (fish uses bare hex)."""
    return hex_color.lstrip("#")


def generate_fish(palette: dict, theme: str) -> str:
    """Generate a fish shell script that sets fish color variables."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"

    fg = _strip(t["fg"])
    fg_dim = _strip(t["fg_dim"])
    blue = _strip(t["blue"])
    cyan = _strip(t["cyan"])
    green = _strip(t["green"])
    red = _strip(t["red"])
    yellow = _strip(t["yellow"])
    magenta = _strip(t["magenta"])
    orange = _strip(t["orange"])
    comment = _strip(t["comment"])
    bg_hl = _strip(t["bg_hl"])
    selection = _strip(t["selection"])
    bg = _strip(t["bg"])

    return f"""\
#!/usr/bin/env fish
# Nepes {name} — fish shell color theme
# Source this file: source nepes-{theme}.fish

# Syntax highlighting
set -U fish_color_normal {fg}
set -U fish_color_command {cyan}
set -U fish_color_keyword {blue}
set -U fish_color_quote {green}
set -U fish_color_redirection {fg_dim}
set -U fish_color_end {orange}
set -U fish_color_error {red}
set -U fish_color_param {magenta}
set -U fish_color_comment {comment}
set -U fish_color_selection --background={bg_hl}
set -U fish_color_search_match --background={selection}
set -U fish_color_operator {yellow}
set -U fish_color_escape {orange}
set -U fish_color_autosuggestion {comment}
set -U fish_color_cancel {red}
set -U fish_color_cwd {blue}
set -U fish_color_user {green}
set -U fish_color_host {cyan}
set -U fish_color_valid_path --underline

# Pager
set -U fish_pager_color_progress {fg_dim}
set -U fish_pager_color_prefix {cyan} --bold
set -U fish_pager_color_completion {fg}
set -U fish_pager_color_description {comment}
set -U fish_pager_color_selected_background --background={bg_hl}
"""
