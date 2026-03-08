"""Generate nepes-tokens.css — CSS custom properties for web projects."""


def generate_css(palette: dict) -> str:
    """Generate a CSS file with design tokens as CSS custom properties."""
    brand = palette["brand"]
    dark = palette["dark"]
    light = palette["light"]
    motion = palette["motion"]

    # Key mapping: palette key -> CSS var name
    theme_vars = {
        "bg": "--bg-primary",
        "bg_dim": "--bg-secondary",
        "bg_alt": "--bg-card",
        "bg_deep": "--bg-deep",
        "bg_hl": "--bg-highlight",
        "bg_overlay": "--bg-overlay",
        "fg": "--text-primary",
        "fg_dim": "--text-secondary",
        "fg_muted": "--text-muted",
        "border": "--border-color",
        "border_subtle": "--border-subtle",
        "bg_glass": "--bg-glass",
        "selection": "--selection-bg",
        "comment": "--comment",
        "cursor": "--cursor",
        "green": "--success",
        "red": "--error",
        "orange": "--warning",
        "blue": "--info",
    }

    lines = []
    lines.append("/* Nepes Design Tokens — generated, do not edit */")
    lines.append("")
    lines.append(":root {")

    # Brand colors (constant across themes)
    lines.append("  /* Brand */")
    for name, value in brand.items():
        css_name = name.replace("_", "-")
        lines.append(f"  --nepes-{css_name}: {value};")
    lines.append("")

    # Dark theme as default
    lines.append("  /* Theme (dark default) */")
    for key, var_name in theme_vars.items():
        lines.append(f"  {var_name}: {dark[key]};")
    lines.append("")

    # Accent
    lines.append("  /* Accent */")
    lines.append("  --accent: var(--nepes-orange);")
    lines.append("  --link-color: var(--accent);")
    lines.append("")

    # Chart series
    chart = dark["chart"]
    lines.append("  /* Chart */")
    for i, color in enumerate(chart["series"], start=1):
        lines.append(f"  --chart-{i}: {color};")

    # Chart step/recipe backgrounds
    step_bg = chart.get("step_bg", "")
    recipe_bg = chart.get("recipe_bg", "")
    lines.append(f"  --chart-step-0: {step_bg};")
    lines.append(f"  --chart-step-1: {recipe_bg};")
    lines.append("")

    # Motion tokens
    lines.append("  /* Motion */")
    for key, value in motion.items():
        css_name = key.replace("_", "-")
        lines.append(f"  --{css_name}: {value};")

    lines.append("}")
    lines.append("")

    # Light theme overrides
    lines.append('[data-theme="light"] {')
    for key, var_name in theme_vars.items():
        lines.append(f"  {var_name}: {light[key]};")
    lines.append("")

    # Light accent
    lines.append("  --accent: var(--nepes-blue);")
    lines.append("")

    # Light chart
    light_chart = light["chart"]
    for i, color in enumerate(light_chart["series"], start=1):
        lines.append(f"  --chart-{i}: {color};")
    light_step_bg = light_chart.get("step_bg", "")
    light_recipe_bg = light_chart.get("recipe_bg", "")
    lines.append(f"  --chart-step-0: {light_step_bg};")
    lines.append(f"  --chart-step-1: {light_recipe_bg};")

    lines.append("}")
    lines.append("")

    return "\n".join(lines)
