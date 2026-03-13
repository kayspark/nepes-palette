"""Generate bat/sublime tmTheme XML from the nepes palette."""

from nepes_palette.colors import lighten
from nepes_palette.palette import get_semantic_colors, resolve_color


def _xml_escape(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _scope_entry(scope: str, foreground: str, *, font_style: str = "") -> str:
    lines = [
        "        <dict>",
        "            <key>scope</key>",
        f"            <string>{_xml_escape(scope)}</string>",
        "            <key>settings</key>",
        "            <dict>",
        "                <key>foreground</key>",
        f"                <string>{foreground}</string>",
    ]
    if font_style:
        lines.append("                <key>fontStyle</key>")
        lines.append(f"                <string>{font_style}</string>")
    lines.append("            </dict>")
    lines.append("        </dict>")
    return "\n".join(lines)


def generate_bat(palette: dict, theme: str) -> str:
    """Generate a tmTheme XML string for bat syntax highlighting."""
    t = palette[theme]
    sem = get_semantic_colors(palette, theme)
    theme_name = f"Nepes {'Dark' if theme == 'dark' else 'Light'}"

    # Brighten blue-family colors for dark theme — bat renders inside
    # translucent terminals (WezTerm 90% opacity) where standard blue
    # lacks contrast against the effectively lighter background.
    if theme == "dark":
        sem = dict(sem)  # shallow copy to avoid mutating shared dict
        sem["keyword"] = lighten(sem["keyword"], 0.08)
        sem["builtin"] = lighten(sem["builtin"], 0.08)
        sem["info"] = lighten(sem["info"], 0.08)

    # Global settings (no background — inherit terminal's translucent bg)
    global_settings = {
        "foreground": t["fg"],
        "caret": t["cursor"],
        "selection": t["selection"],
        "lineHighlight": t["bg_hl"],
        "gutterForeground": t["fg_muted"],
        "findHighlight": resolve_color(palette, theme, "orange"),
        "invisibles": t["fg_muted"],
    }

    # Build scope entries
    scopes = [
        # Comment
        _scope_entry("comment, comment.line, comment.block", sem["comment"], font_style="italic"),
        # String
        _scope_entry("string, string.quoted", sem["string"]),
        # Number
        _scope_entry("constant.numeric", sem["number"]),
        # Constant
        _scope_entry("constant, constant.language, constant.character", sem["constant"]),
        # Keyword
        _scope_entry("keyword, keyword.control, storage.type, storage.modifier", sem["keyword"]),
        # Builtin
        _scope_entry("support.function, support.class, support.type", sem["builtin"]),
        # Function
        _scope_entry("entity.name.function, meta.function-call", sem["function"]),
        # Type
        _scope_entry("entity.name.type, entity.name.class, entity.name.struct", sem["type"]),
        # Variable
        _scope_entry("variable, variable.other", sem["variable"]),
        # Parameter
        _scope_entry("variable.parameter", sem["parameter"]),
        # Operator
        _scope_entry("keyword.operator", sem["operator"]),
        # Tag
        _scope_entry("entity.name.tag", sem["keyword"]),
        # Attribute
        _scope_entry("entity.other.attribute-name", sem["function"]),
        # Heading — use fg for maximum readability, stand out by bold weight
        _scope_entry("markup.heading, entity.name.section, punctuation.definition.heading", t["fg"], font_style="bold"),
        # Bold
        _scope_entry("markup.bold", t["fg"], font_style="bold"),
        # Italic
        _scope_entry("markup.italic", t["fg"], font_style="italic"),
        # Link
        _scope_entry("markup.underline.link, string.other.link", sem["info"], font_style="underline"),
        # Inserted
        _scope_entry("markup.inserted", sem["added"]),
        # Deleted
        _scope_entry("markup.deleted", sem["removed"]),
        # Changed
        _scope_entry("markup.changed", sem["changed"]),
        # Error
        _scope_entry("invalid, invalid.illegal", sem["error"]),
        # Preprocessor
        _scope_entry("meta.preprocessor, keyword.control.import", sem["keyword"]),
        # Escape
        _scope_entry("constant.character.escape", sem["constant"], font_style="bold"),
        # Regex
        _scope_entry("string.regexp", sem["function"]),
        # Punctuation
        _scope_entry("punctuation", t["fg_subtle"]),
    ]

    # Assemble XML
    global_dict_lines = []
    for key, value in global_settings.items():
        global_dict_lines.append(f"                <key>{key}</key>")
        global_dict_lines.append(f"                <string>{value}</string>")
    global_dict_str = "\n".join(global_dict_lines)
    scopes_str = "\n".join(scopes)

    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>name</key>
    <string>{theme_name}</string>
    <key>settings</key>
    <array>
        <dict>
            <key>settings</key>
            <dict>
{global_dict_str}
            </dict>
        </dict>
{scopes_str}
    </array>
</dict>
</plist>
"""
