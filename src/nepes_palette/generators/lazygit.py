"""Generate lazygit theme YAML from the nepes palette."""


def generate_lazygit(palette: dict, theme: str) -> str:
    """Generate a lazygit theme YAML snippet for the given theme."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"
    return f"""# Nepes {name} — lazygit theme
# Copy to ~/.config/lazygit/config.yml under gui.theme

gui:
  theme:
    activeBorderColor:
      - "{t['blue']}"
      - bold
    inactiveBorderColor:
      - "{t['fg_muted']}"
    optionsTextColor:
      - "{t['blue']}"
    selectedLineBgColor:
      - "{t['bg_hl']}"
    selectedRangeBgColor:
      - "{t['bg_hl']}"
    cherryPickedCommitBgColor:
      - "{t['cyan_dim']}"
    cherryPickedCommitFgColor:
      - "{t['cyan']}"
    unstagedChangesColor:
      - "{t['red']}"
    defaultFgColor:
      - "{t['fg']}"
"""
