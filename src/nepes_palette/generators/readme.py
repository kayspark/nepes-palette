"""README.org generator for nepes-color sub-repos."""

from ..capture.runner import TOOL_REGISTRY

# Per-tool metadata for README generation
TOOL_METADATA: dict[str, dict] = {
    "bat": {
        "name": "bat",
        "description": "Syntax highlighting for cat replacement",
        "install": '1. Clone this repo\n2. Copy =nepes-dark.tmTheme= and =nepes-light.tmTheme= to =~/.config/bat/themes/=\n3. Run =bat cache --build=\n4. Set theme: =export BAT_THEME="Nepes Dark"=',
        "config": 'export BAT_THEME="Nepes Dark"  # or "Nepes Light"',
    },
    "delta": {
        "name": "delta",
        "description": "Syntax-highlighting pager for git diffs",
        "install": "1. Clone this repo\n2. Add to =~/.gitconfig=:\n#+begin_src gitconfig\n[include]\n    path = /path/to/nepes.gitconfig\n#+end_src",
        "config": None,
    },
    "lazygit": {
        "name": "lazygit",
        "description": "Terminal UI for git commands",
        "install": "1. Clone this repo\n2. Copy theme YAML to =~/.config/lazygit/=\n3. Set =LG_CONFIG_FILE= to the theme path",
        "config": "LG_CONFIG_FILE=~/.config/lazygit/nepes-dark.yml lazygit",
    },
    "fzf": {
        "name": "fzf",
        "description": "Command-line fuzzy finder",
        "install": "1. Clone this repo\n2. Source the theme in your shell RC:\n#+begin_src shell\nsource /path/to/fzf-nepes/nepes-dark.sh\n#+end_src",
        "config": None,
    },
    "lsd": {
        "name": "lsd",
        "description": "Modern ls replacement with colors and icons",
        "install": "1. Clone this repo\n2. Copy theme YAML to =~/.config/lsd/colors.yaml=",
        "config": None,
    },
    "fish": {
        "name": "fish",
        "description": "Fish shell color theme",
        "install": "1. Clone this repo\n2. Source the theme:\n#+begin_src shell\nsource /path/to/fish-nepes/nepes-dark.fish\n#+end_src",
        "config": None,
    },
    "kitty": {
        "name": "kitty",
        "description": "GPU-accelerated terminal emulator color theme",
        "install": "1. Clone this repo\n2. Include in =~/.config/kitty/kitty.conf=:\n#+begin_src conf\ninclude /path/to/kitty-nepes/nepes-dark.conf\n#+end_src",
        "config": None,
    },
    "yazi": {
        "name": "yazi",
        "description": "Terminal file manager color theme",
        "install": "1. Clone this repo\n2. Copy theme TOML to =~/.config/yazi/theme.toml=",
        "config": None,
    },
    "gitui": {
        "name": "gitui",
        "description": "Blazing fast terminal UI for git",
        "install": "1. Clone this repo\n2. Copy theme RON to =~/.config/gitui/theme.ron=",
        "config": None,
    },
    "starship": {
        "name": "starship",
        "description": "Cross-shell prompt palette",
        "install": "1. Clone this repo\n2. Add palette to =~/.config/starship.toml=",
        "config": None,
    },
    "tmux": {
        "name": "tmux",
        "description": "Terminal multiplexer theme (TPM plugin)",
        "install": "1. Add to =~/.config/tmux/tmux.conf=:\n#+begin_src conf\nset -g @plugin 'kayspark/tmux-nepes'\n#+end_src\n2. Install with =prefix + I=",
        "config": None,
    },
    "nvim": {
        "name": "Neovim",
        "description": "Neovim colorscheme with treesitter and LSP support",
        "install": "1. Add to lazy.nvim:\n#+begin_src lua\n{ 'kayspark/nvim-nepes', opts = { theme = 'dark' } }\n#+end_src",
        "config": 'vim.cmd("colorscheme nepes")',
    },
    "emacs": {
        "name": "Emacs",
        "description": "Emacs color theme built on modus-themes infrastructure",
        "install": "1. Clone this repo to =~/.config/emacs/themes/=\n2. Add to init:\n#+begin_src emacs-lisp\n(load-theme 'nepes-dark t)\n#+end_src",
        "config": None,
    },
    "wezterm": {
        "name": "WezTerm",
        "description": "GPU-accelerated terminal color scheme and status bar",
        "install": "1. Clone this repo\n2. Symlink to =~/.config/wezterm/colors/=\n3. Set in =wezterm.lua=:\n#+begin_src lua\nconfig.color_scheme = 'nepes-dark'\n#+end_src",
        "config": None,
    },
    "chrome": {
        "name": "Chrome",
        "description": "Chrome browser DevTools and new tab theme",
        "install": "1. Clone this repo\n2. Open =chrome://extensions=\n3. Enable Developer mode\n4. Load unpacked from =nepes-dark/= or =nepes-light/=",
        "config": None,
    },
    "raycast": {
        "name": "Raycast",
        "description": "Raycast launcher color theme",
        "install": "1. Clone this repo\n2. Import =nepes-dark.json= or =nepes-light.json= in Raycast preferences",
        "config": None,
    },
    "slack": {
        "name": "Slack",
        "description": "Slack sidebar custom theme",
        "install": "1. Open Slack > Preferences > Themes\n2. Paste the color values from =nepes-dark.txt= or =nepes-light.txt=",
        "config": None,
    },
    "css": {
        "name": "CSS",
        "description": "CSS custom properties (design tokens) and Safari user stylesheet",
        "install": "1. Clone this repo\n2. Import =nepes-tokens.css= in your project:\n#+begin_src css\n@import url('nepes-tokens.css');\n#+end_src",
        "config": None,
    },
    "safari": {
        "name": "Safari",
        "description": "Safari user stylesheet for dark/light browsing",
        "install": "1. Clone css-nepes repo\n2. In Safari > Settings > Advanced > Stylesheet, select =nepes-safari-dark.css=",
        "config": None,
    },
    "cmux": {
        "name": "cmux",
        "description": "Ghostty-based macOS terminal with vertical tabs for AI agents",
        "install": "1. Clone this repo\n2. Copy theme files to =~/.config/ghostty/themes/=:\n#+begin_src shell\ncp nepes-dark nepes-light ~/.config/ghostty/themes/\n#+end_src\n3. Set in =~/.config/ghostty/config=:\n#+begin_src conf\ntheme = nepes-dark\n#+end_src",
        "config": None,
    },
    "vhs": {
        "name": "VHS",
        "description": "Terminal recording themes for charmbracelet/vhs",
        "install": "1. Clone this repo\n2. Use in your =.tape= file:\n#+begin_src\nSet Theme " + '{"name":"Nepes Dark",...}' + "\n#+end_src\nOr copy the full JSON from =nepes-dark.json= / =nepes-light.json=.",
        "config": None,
    },
}


def generate_readme(tool: str) -> str:
    """Generate README.org content for a tool's sub-repo."""
    meta = TOOL_METADATA[tool]
    is_interactive = TOOL_REGISTRY.get(tool, {}).get("interactive", False)
    repo_name = f"{tool}-nepes"

    lines = [
        f"#+title: {repo_name}",
        f"#+description: Nepes color theme for {meta['name']}",
        "",
        f"{meta['description']}.",
        "",
        "Part of the [[https://github.com/kayspark][Nepes Colorscheme]] suite.",
        "",
        "* Screenshots",
        "",
        "| Dark | Light |",
        "|------+-------|",
        "| [[./docs/dark.png]] | [[./docs/light.png]] |",
        "",
    ]

    # Add GIF section for interactive tools
    if is_interactive:
        lines.extend([
            "** Demo",
            "",
            "| Dark | Light |",
            "|------+-------|",
            "| [[./docs/dark.gif]] | [[./docs/light.gif]] |",
            "",
        ])

    lines.extend([
        "* Installation",
        "",
        meta["install"],
        "",
    ])

    if meta.get("config"):
        lines.extend([
            "* Configuration",
            "",
            "#+begin_src shell",
            meta["config"],
            "#+end_src",
            "",
        ])

    lines.extend([
        "* Credits",
        "",
        "Generated by [[https://github.com/kayspark/nepes-palette][nepes-palette]].",
        "",
    ])

    return "\n".join(lines)
