"""Generate Safari user stylesheet from the nepes palette."""


def generate_safari(palette: dict, theme: str) -> str:
    """Generate a Safari user stylesheet for the given theme.

    The stylesheet customizes page appearance via Safari's user stylesheet
    setting (Preferences → Advanced → Style sheet).
    """
    t = palette[theme]
    name = "Dark" if theme == "dark" else "Light"
    scheme = "dark" if theme == "dark" else "light"

    return f"""\
/*
 * Nepes {name} — Safari User Stylesheet
 *
 * Install:
 *   1. Save this file as ~/Library/Safari/nepes-{theme}.css
 *   2. Open Safari → Settings → Advanced
 *   3. Under "Style sheet", select this file
 *
 * Note: Only one user stylesheet can be active at a time.
 */

/* ── Color Scheme ──────────────────────────────────────────── */

:root {{
  color-scheme: {scheme};
}}

/* ── Body ──────────────────────────────────────────────────── */

body {{
  background-color: {t["bg"]} !important;
  color: {t["fg"]} !important;
}}

/* ── Links ─────────────────────────────────────────────────── */

a:link {{
  color: {t["blue"]};
}}

a:visited {{
  color: {t["magenta"]};
}}

a:hover {{
  color: {t["cyan"]};
}}

/* ── Selection ─────────────────────────────────────────────── */

::selection {{
  background-color: {t["selection"]};
  color: {t["fg"]};
}}

/* ── Scrollbar ─────────────────────────────────────────────── */

::-webkit-scrollbar {{
  width: 12px;
  background-color: {t["bg_deep"]};
}}

::-webkit-scrollbar-thumb {{
  background-color: {t["border"]};
  border-radius: 6px;
  border: 2px solid {t["bg_deep"]};
}}

::-webkit-scrollbar-thumb:hover {{
  background-color: {t["bg_overlay"]};
}}

/* ── Form Controls ─────────────────────────────────────────── */

input,
textarea,
select {{
  background-color: {t["bg_dim"]} !important;
  color: {t["fg"]} !important;
  border: 1px solid {t["border"]} !important;
  border-radius: 4px;
}}

input:focus,
textarea:focus,
select:focus {{
  border-color: {t["blue"]} !important;
  outline: none;
}}

/* ── Buttons ───────────────────────────────────────────────── */

button,
input[type="button"],
input[type="submit"],
input[type="reset"] {{
  background-color: {t["bg_alt"]} !important;
  color: {t["fg"]} !important;
  border: 1px solid {t["border"]} !important;
  border-radius: 4px;
  cursor: pointer;
}}

button:hover,
input[type="button"]:hover,
input[type="submit"]:hover,
input[type="reset"]:hover {{
  background-color: {t["bg_hl"]} !important;
}}

/* ── Code Blocks ───────────────────────────────────────────── */

pre,
code {{
  background-color: {t["bg_dim"]} !important;
  color: {t["fg"]} !important;
  border-radius: 4px;
}}

pre {{
  padding: 1em;
  overflow-x: auto;
}}

code {{
  padding: 0.2em 0.4em;
}}
"""
