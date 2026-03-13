"""Generate Neovim color palette in Lua format."""

# Lua reserved keywords — must use ["key"] bracket syntax
_LUA_RESERVED = frozenset({
    "and", "break", "do", "else", "elseif", "end", "false", "for",
    "function", "goto", "if", "in", "local", "nil", "not", "or",
    "repeat", "return", "then", "true", "until", "while",
})


def _lua_key(key: str, width: int = 12) -> str:
    """Format a Lua table key, using bracket syntax for reserved words."""
    if key in _LUA_RESERVED:
        return f'["{key}"]' + " " * max(0, width - len(key) - 4)
    return f"{key:{width}}"


def generate_nvim(palette: dict) -> str:
    """Generate lua/nepes/palette.lua containing both dark and light themes."""
    from ..palette import get_semantic_colors

    lines = ["local M = {}", ""]

    for theme in ["dark", "light"]:
        t = palette[theme]
        lines.append(f"M.{theme} = {{")

        # Base color tokens
        base_keys = set()
        for key, value in t.items():
            if key in ("ansi", "semantic", "chart", "surface", "bg_glass", "border_subtle"):
                continue
            base_keys.add(key)
            lines.append(f"  {_lua_key(key)} = \"{value}\",")

        # Semantic tokens (skip if already emitted as a base key)
        semantic = get_semantic_colors(palette, theme)
        lines.append("  -- Semantic tokens")
        for role, hex_val in semantic.items():
            if role in base_keys:
                continue
            lines.append(f"  {_lua_key(role)} = \"{hex_val}\",")

        lines.append('  none         = "NONE",')
        lines.append("}")
        lines.append("")

    lines.append("return M")
    return "\n".join(lines) + "\n"
