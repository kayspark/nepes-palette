"""Generate Emacs Modus-derivative theme files."""


# Diff/subtle/nuanced backgrounds must differ between dark and light themes.
# Dark: low-luminance tinted backgrounds on warm brown base.
# Light: high-luminance pastel tints on white base.
_BG_DARK = {
    "bg-added":          "#1E2E1E",
    "bg-added-faint":    "#192619",
    "bg-added-refine":   "#2A4A2A",
    "bg-removed":        "#2E1E1E",
    "bg-removed-faint":  "#261919",
    "bg-removed-refine": "#4A2A2A",
    "bg-changed":        "#2E2E1E",
    "bg-changed-faint":  "#262619",
    "bg-changed-refine": "#4A4A2A",
    "bg-red-subtle":     "#3A1C1C",
    "bg-green-subtle":   "#1C2E1C",
    "bg-yellow-subtle":  "#2E2A1C",
    "bg-blue-subtle":    "#1C2040",
    "bg-magenta-subtle": "#2E1C30",
    "bg-cyan-subtle":    "#1C2E30",
    "bg-red-nuanced":     "#2C1414",
    "bg-green-nuanced":   "#142214",
    "bg-yellow-nuanced":  "#221E14",
    "bg-blue-nuanced":    "#141828",
    "bg-magenta-nuanced": "#221422",
    "bg-cyan-nuanced":    "#142222",
    # Graph backgrounds
    "bg-graph-red-0":     "#B52C2C",
    "bg-graph-red-1":     "#702020",
    "bg-graph-green-0":   "#0FED00",
    "bg-graph-green-1":   "#007800",
    "bg-graph-yellow-0":  "#F1E00A",
    "bg-graph-yellow-1":  "#B08940",
    "bg-graph-blue-0":    "#2FAFEF",
    "bg-graph-blue-1":    "#1F2F8F",
    "bg-graph-magenta-0": "#BF94FE",
    "bg-graph-magenta-1": "#5F509F",
}

_BG_LIGHT = {
    "bg-added":          "#E8F5E8",
    "bg-added-faint":    "#F0FAF0",
    "bg-added-refine":   "#C8E8C8",
    "bg-removed":        "#F5E8E8",
    "bg-removed-faint":  "#FAF0F0",
    "bg-removed-refine": "#E8C8C8",
    "bg-changed":        "#F5F0E0",
    "bg-changed-faint":  "#FAF8F0",
    "bg-changed-refine": "#E8E0C0",
    "bg-red-subtle":     "#F5E0E0",
    "bg-green-subtle":   "#E0F0E0",
    "bg-yellow-subtle":  "#F0ECD0",
    "bg-blue-subtle":    "#E0E4F0",
    "bg-magenta-subtle": "#EDE0F0",
    "bg-cyan-subtle":    "#E0F0F0",
    "bg-red-nuanced":     "#FAF0F0",
    "bg-green-nuanced":   "#F0FAF0",
    "bg-yellow-nuanced":  "#FAF8F0",
    "bg-blue-nuanced":    "#F0F2FA",
    "bg-magenta-nuanced": "#F5F0FA",
    "bg-cyan-nuanced":    "#F0FAFA",
    # Graph backgrounds
    "bg-graph-red-0":     "#EF7969",
    "bg-graph-red-1":     "#FFAAB4",
    "bg-graph-green-0":   "#2CC22C",
    "bg-graph-green-1":   "#60E060",
    "bg-graph-yellow-0":  "#F0D000",
    "bg-graph-yellow-1":  "#F5E870",
    "bg-graph-blue-0":    "#2FAFEF",
    "bg-graph-blue-1":    "#79B8FF",
    "bg-graph-magenta-0": "#BF94FE",
    "bg-graph-magenta-1": "#E0B0FF",
}


def generate_emacs_theme(palette: dict, theme: str) -> str:
    """Generate nepes-dark-theme.el or nepes-light-theme.el."""
    name = "dark" if theme == "dark" else "light"
    t = palette[theme]
    bg = _BG_DARK if theme == "dark" else _BG_LIGHT

    if theme == "dark":
        desc = "Nepes corporate dark theme — warm brownish backgrounds with brand colors."
        paren_bg = "#504848"
        # Dark: keyword uses blue-cooler (brand blue #23438E — authoritative)
        keyword_mapping = "blue-cooler"
        # Dark: intense diff uses brighter variants
        added_intense = "green-warmer"
        removed_intense = "red-warmer"
    else:
        desc = "Nepes corporate light theme — clean light background with brand colors."
        paren_bg = "#D8D7D7"
        # Light: keyword uses blue (primary #23438E — best contrast at 8.73:1)
        keyword_mapping = "blue"
        # Light: intense diff uses dimmer/cooler variants for contrast on light bg
        added_intense = "green-cooler"
        removed_intense = "red-cooler"

    # Extended named colors for custom face support
    rust = t["orange_dim"]
    gold = t["yellow_dim"]
    olive = t["comment"]

    # Build bg-* lines
    bg_lines = []
    bg_lines.append("")
    bg_lines.append("     ;; Diff backgrounds")
    for key in ["bg-added", "bg-added-faint", "bg-added-refine",
                "bg-removed", "bg-removed-faint", "bg-removed-refine",
                "bg-changed", "bg-changed-faint", "bg-changed-refine"]:
        bg_lines.append(f'     ({key:24} "{bg[key]}")')
    bg_lines.append("")
    bg_lines.append("     ;; Subtle backgrounds for regions, prompts")
    for color in ["red", "green", "yellow", "blue", "magenta", "cyan"]:
        key = f"bg-{color}-subtle"
        bg_lines.append(f'     ({key:24} "{bg[key]}")')
    bg_lines.append("")
    bg_lines.append("     ;; Nuanced backgrounds (lighter tint)")
    for color in ["red", "green", "yellow", "blue", "magenta", "cyan"]:
        key = f"bg-{color}-nuanced"
        bg_lines.append(f'     ({key:24} "{bg[key]}")')
    bg_lines.append("")
    bg_lines.append("     ;; Intense backgrounds")
    bg_lines.append(f'     (bg-red-intense     "{t["red_dim"]}")')
    bg_lines.append(f'     (bg-green-intense   "{t["green_dim"]}")')
    bg_lines.append(f'     (bg-yellow-intense  "{t["orange_dim"]}")')
    bg_lines.append(f'     (bg-blue-intense    "{t["blue_dim"]}")')
    bg_lines.append(f'     (bg-magenta-intense "{t["magenta_dim"]}")')
    bg_lines.append(f'     (bg-cyan-intense    "{t["cyan_dim"]}")')
    bg_lines.append("")
    bg_lines.append("     ;; Graphs")
    for key in sorted(k for k in bg if k.startswith("bg-graph-")):
        bg_lines.append(f'     ({key:24} "{bg[key]}")')

    bg_block = "\n".join(bg_lines)

    return f""";;; nepes-{name}-theme.el --- Nepes {name} theme (modus derivative) -*- lexical-binding: t; -*-

;; Author: kaypark
;; URL: https://github.com/kayspark/emacs-nepes

;;; Commentary:

;; {name.capitalize()} variant of the Nepes corporate colorscheme.
;; Built on modus-themes infrastructure for 200+ face coverage.
;; Requires `nepes-themes' for shared infrastructure.

;;; Code:

(require 'nepes-themes)

;;; Layer 1: Core palette (named colors)

(defvar nepes-{name}-palette
  (modus-themes-generate-palette
   '(;; Backgrounds
     (bg-main  "{t["bg"]}")
     (bg-dim   "{t["bg_dim"]}")
     (bg-active "{t["bg_hl"]}")
     (bg-inactive "{t["bg_alt"]}")
     (border  "{t["border"]}")

     ;; Foregrounds
     (fg-main  "{t["fg"]}")
     (fg-dim   "{t["fg_dim"]}")
     (fg-alt   "{t["fg_subtle"]}")

     ;; Core hues — WCAG-refined
     (blue          "{t["blue"]}")
     (blue-warmer   "{t["blue_bright"]}")
     (blue-cooler   "{t["blue_dim"]}")
     (blue-faint    "{t["ansi"]["bright_blue"]}")
     (blue-intense  "{t["blue_dim"]}")

     (red           "{t["red"]}")
     (red-warmer    "{t["red_bright"]}")
     (red-cooler    "{t["red_dim"]}")
     (red-faint     "{t["ansi"]["bright_red"]}")
     (red-intense   "{t["red_dim"]}")

     (green         "{t["green"]}")
     (green-warmer  "{t["green_bright"]}")
     (green-cooler  "{t["green_dim"]}")
     (green-faint   "{t["ansi"]["bright_green"]}")
     (green-intense "{t["green_dim"]}")

     (yellow        "{t["yellow"]}")
     (yellow-warmer "{t["orange"]}")
     (yellow-cooler "{t["yellow_dim"]}")
     (yellow-faint  "{t["ansi"]["bright_yellow"]}")
     (yellow-intense "{t["yellow_bright"]}")

     (magenta       "{t["magenta"]}")
     (magenta-warmer "{t["magenta_bright"]}")
     (magenta-cooler "{t["magenta_dim"]}")
     (magenta-faint "{t["ansi"]["bright_magenta"]}")
     (magenta-intense "{t["magenta_dim"]}")

     (cyan          "{t["cyan"]}")
     (cyan-warmer   "{t["cyan_bright"]}")
     (cyan-cooler   "{t["cyan_dim"]}")
     (cyan-faint    "{t["ansi"]["bright_cyan"]}")
     (cyan-intense  "{t["cyan_dim"]}")

     ;; Extended named colors
     (rust  "{rust}")
     (gold  "{gold}")
     (olive "{olive}")

     ;; Special
     (bg-completion "{t["selection"]}")
     (bg-hover      "{t["bg_hl"]}")
     (bg-hover-secondary "{t["bg_alt"]}")
     (bg-hl-line    "{t["bg_dim"]}")
{bg_block})
   'warm)
  "Core palette for `nepes-{name}'.")

;;; Layer 2: User palette (empty, for user overrides)

(defvar nepes-{name}-palette-user nil
  "User overrides for `nepes-{name}' palette.")

;;; Layer 3: Semantic overrides (mappings)

(defvar nepes-{name}-palette-overrides
  `(;; Syntax
    (keyword {keyword_mapping})
    (builtin blue-warmer)
    (fnname cyan)
    (string green)
    (type magenta)
    (constant yellow-cooler)
    (variable fg-main)
    (comment fg-alt)
    (docstring green-faint)
    (docmarkup green-faint)

    ;; Operators and delimiters
    (bracket fg-alt)
    (delimiter fg-alt)
    (operator fg-alt)
    (number yellow-cooler)
    (punctuation fg-alt)

    ;; Headings (rainbow)
    (fg-heading-1 blue)
    (fg-heading-2 magenta)
    (fg-heading-3 cyan)
    (fg-heading-4 green)
    (fg-heading-5 yellow)
    (fg-heading-6 red)
    (fg-heading-7 fg-alt)
    (fg-heading-8 blue-warmer)

    ;; Status
    (err red)
    (warning yellow-warmer)
    (info blue)

    ;; Diff/VC
    (fg-added green)
    (fg-added-intense {added_intense})
    (fg-changed yellow-warmer)
    (fg-changed-intense yellow-intense)
    (fg-removed red)
    (fg-removed-intense {removed_intense})

    ;; Line numbers
    (fg-line-number-inactive fg-alt)
    (fg-line-number-active fg-dim)
    (bg-line-number-inactive bg-main)
    (bg-line-number-active bg-dim)

    ;; Prompts
    (fg-prompt blue)

    ;; Completion
    (fg-completion-match-0 blue)
    (fg-completion-match-1 magenta)
    (fg-completion-match-2 cyan)
    (fg-completion-match-3 green)

    ;; Paren match
    (fg-paren-match blue)
    (bg-paren-match "{paren_bg}")

    ;; Links
    (underline-link blue)
    (underline-link-visited magenta)

    ;; Region
    (bg-region "{t["selection"]}")

    ;; Prose
    (prose-todo red)
    (prose-done green))
  "Semantic palette overrides for `nepes-{name}'.")

;;; Theme declaration

(modus-themes-theme 'nepes-{name}
  'nepes
  "{desc}"
  '{name}
  'nepes-{name}-palette
  'nepes-{name}-palette-user
  'nepes-{name}-palette-overrides)

(provide-theme 'nepes-{name})
;;; nepes-{name}-theme.el ends here
"""
