"""Generate lsd color theme YAML from the nepes palette."""


def _hex_to_ansi256(hex_color: str) -> int:
    """Approximate a hex color to the nearest ANSI 256 color code."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    # Grayscale ramp (colors 232-255)
    if r == g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round((r - 8) / 247 * 24) + 232
    # 6x6x6 color cube (colors 16-231)
    ri = round(r / 255 * 5)
    gi = round(g / 255 * 5)
    bi = round(b / 255 * 5)
    return 16 + 36 * ri + 6 * gi + bi


def generate_lsd(palette: dict, theme: str) -> str:
    """Generate an lsd color theme YAML string."""
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"

    fg = _hex_to_ansi256(t["fg"])
    fg_dim = _hex_to_ansi256(t["fg_dim"])
    fg_subtle = _hex_to_ansi256(t["fg_subtle"])
    fg_muted = _hex_to_ansi256(t["fg_muted"])
    blue = _hex_to_ansi256(t["blue"])
    cyan = _hex_to_ansi256(t["cyan"])
    green = _hex_to_ansi256(t["green"])
    red = _hex_to_ansi256(t["red"])
    yellow = _hex_to_ansi256(t["yellow"])
    magenta = _hex_to_ansi256(t["magenta"])
    orange = _hex_to_ansi256(t["orange"])
    border = _hex_to_ansi256(t["border"])

    return f"""\
# Nepes {name} — lsd color theme
# Place in ~/.config/lsd/colors.yaml

user: {green}
group: {yellow}

permission:
  read: {green}
  write: {yellow}
  exec: {red}
  exec-sticky: {magenta}
  no-access: {fg_muted}

date:
  hour-old: {cyan}
  day-old: {fg_dim}
  older: {fg_subtle}

size:
  none: {fg_muted}
  small: {green}
  medium: {yellow}
  large: {red}

inode:
  valid: {fg_dim}
  invalid: {fg_muted}

links:
  normal: {fg_dim}
  multi: {orange}

tree-edge: {border}

file-type:
  directory: {blue}
  file: {fg}
  symlink: {cyan}
  fifo: {orange}
  socket: {magenta}
  char-device: {yellow}
  block-device: {yellow}
  special: {orange}
  executable: {red}
  uid-bit: {magenta}
  gid-bit: {yellow}
"""
