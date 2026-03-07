"""Generate gitui theme (RON format) from the nepes palette."""


def _hex_to_ron_rgb(hex_color: str) -> str:
    """Convert '#AABBCC' to 'Rgb(170, 187, 204)'."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"Rgb({r}, {g}, {b})"


def generate_gitui(palette: dict, theme: str) -> str:
    """Generate a gitui theme file in RON format for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"

    def fg(color: str) -> str:
        return f"Some(Style(fg: Some({_hex_to_ron_rgb(t[color])})))"

    def bg(color: str) -> str:
        return f"Some(Style(bg: Some({_hex_to_ron_rgb(t[color])})))"

    def fg_bold(color: str) -> str:
        return f"Some(Style(fg: Some({_hex_to_ron_rgb(t[color])}), modifiers: (bits: 1)))"

    return f"""\
// Nepes {name} — gitui theme
(
    selected_tab: {fg_bold('blue')},
    command_fg: {fg('fg')},
    selection_bg: {bg('bg_hl')},
    selection_fg: {fg('fg')},
    cmdbar_bg: {bg('bg')},
    cmdbar_extra_lines_bg: {bg('bg_dim')},
    disabled_fg: {fg('fg_muted')},
    diff_line_add: {fg('green')},
    diff_line_delete: {fg('red')},
    diff_file_added: {fg('green')},
    diff_file_removed: {fg('red')},
    diff_file_moved: {fg('magenta')},
    diff_file_modified: {fg('orange')},
    commit_hash: {fg('magenta')},
    commit_time: {fg('comment')},
    commit_author: {fg('cyan')},
    danger_fg: {fg('red')},
    push_gauge_bg: {bg('blue')},
    push_gauge_fg: {fg('bg')},
    tag_fg: {fg('yellow')},
    branch_fg: {fg('cyan')},
)
"""
