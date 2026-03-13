"""Generate Neovim color palette in Lua format."""


def generate_nvim(palette: dict) -> str:
    """Generate lua/nepes/palette.lua containing both dark and light themes."""
    lines = ["local M = {}", ""]

    for theme in ["dark", "light"]:
        t = palette[theme]
        lines.append(f"M.{theme} = {{")
        # Add basic colors
        for key, value in t.items():
            if key in ["ansi", "semantic", "chart", "surface", "bg_glass", "border_subtle"]:
                continue
            lines.append(f'  {key:12} = "{value}",')

        # Add semantic mappings resolved to hex
        from ..palette import get_semantic_colors
        semantic = get_semantic_colors(palette, theme)
        lines.append("  -- Semantic tokens")
        for role, hex_val in semantic.items():
            lines.append(f'  {role:12} = "{hex_val}",')

        lines.append('  none         = "NONE",')
        lines.append("}")
        lines.append("")

    lines.append("return M")
    return "\n".join(lines) + "\n"
