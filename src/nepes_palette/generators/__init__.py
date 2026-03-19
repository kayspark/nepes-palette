from pathlib import Path


def generate_all(palette: dict, output_dir: Path):
    from .bat import generate_bat
    from .delta import generate_delta
    from .lazygit import generate_lazygit
    from .fzf import generate_fzf
    from .lsd import generate_lsd
    from .fish import generate_fish
    from .chrome import generate_chrome
    from .raycast import generate_raycast
    from .kitty import generate_kitty
    from .yazi import generate_yazi
    from .gitui import generate_gitui
    from .slack import generate_slack
    from .css import generate_css
    from .safari import generate_safari
    from .vhs import generate_vhs
    from .nvim import generate_nvim
    from .emacs import generate_emacs_theme
    from .claude_code import generate_claude_code
    from .mplstyle import generate_mplstyle
    from .cmux import generate_cmux

    generators = {
        "nvim-nepes": [
            ("lua/nepes/palette.lua", lambda: generate_nvim(palette)),
        ],
        "emacs-nepes": [
            ("nepes-dark-theme.el", lambda: generate_emacs_theme(palette, "dark")),
            ("nepes-light-theme.el", lambda: generate_emacs_theme(palette, "light")),
        ],
        "bat-nepes": [
            ("nepes-dark.tmTheme", lambda: generate_bat(palette, "dark")),
            ("nepes-light.tmTheme", lambda: generate_bat(palette, "light")),
        ],
        "delta-nepes": [
            ("nepes.gitconfig", lambda: generate_delta(palette)),
        ],
        "lazygit-nepes": [
            ("nepes-dark.yml", lambda: generate_lazygit(palette, "dark")),
            ("nepes-light.yml", lambda: generate_lazygit(palette, "light")),
        ],
        "fzf-nepes": [
            ("nepes-dark.sh", lambda: generate_fzf(palette, "dark")),
            ("nepes-light.sh", lambda: generate_fzf(palette, "light")),
        ],
        "lsd-nepes": [
            ("nepes-dark.yaml", lambda: generate_lsd(palette, "dark")),
            ("nepes-light.yaml", lambda: generate_lsd(palette, "light")),
        ],
        "fish-nepes": [
            ("nepes-dark.fish", lambda: generate_fish(palette, "dark")),
            ("nepes-light.fish", lambda: generate_fish(palette, "light")),
        ],
        "chrome-nepes": [
            ("nepes-dark/manifest.json", lambda: generate_chrome(palette, "dark")),
            ("nepes-light/manifest.json", lambda: generate_chrome(palette, "light")),
        ],
        "raycast-nepes": [
            ("nepes-dark.json", lambda: generate_raycast(palette, "dark")),
            ("nepes-light.json", lambda: generate_raycast(palette, "light")),
        ],
        "kitty-nepes": [
            ("nepes-dark.conf", lambda: generate_kitty(palette, "dark")),
            ("nepes-light.conf", lambda: generate_kitty(palette, "light")),
        ],
        "yazi-nepes": [
            ("nepes-dark.toml", lambda: generate_yazi(palette, "dark")),
            ("nepes-light.toml", lambda: generate_yazi(palette, "light")),
        ],
        "gitui-nepes": [
            ("nepes-dark.ron", lambda: generate_gitui(palette, "dark")),
            ("nepes-light.ron", lambda: generate_gitui(palette, "light")),
        ],
        "slack-nepes": [
            ("nepes-dark.txt", lambda: generate_slack(palette, "dark")),
            ("nepes-light.txt", lambda: generate_slack(palette, "light")),
        ],
        "css-nepes": [
            ("nepes-tokens.css", lambda: generate_css(palette)),
            ("nepes-safari-dark.css", lambda: generate_safari(palette, "dark")),
            ("nepes-safari-light.css", lambda: generate_safari(palette, "light")),
        ],
        "vhs-nepes": [
            ("nepes-dark.json", lambda: generate_vhs(palette, "dark")),
            ("nepes-light.json", lambda: generate_vhs(palette, "light")),
        ],
        "claude-code-nepes": [
            ("nepes-dark.json", lambda: generate_claude_code(palette, "dark")),
            ("nepes-light.json", lambda: generate_claude_code(palette, "light")),
        ],
        "mplstyle-nepes": [
            ("nepes-light.mplstyle", lambda: generate_mplstyle(palette, "light")),
            ("nepes-dark.mplstyle", lambda: generate_mplstyle(palette, "dark")),
        ],
        "cmux-nepes": [
            ("nepes-dark", lambda: generate_cmux(palette, "dark")),
            ("nepes-light", lambda: generate_cmux(palette, "light")),
        ],
    }

    for repo_name, files in generators.items():
        repo_dir = output_dir / repo_name
        repo_dir.mkdir(parents=True, exist_ok=True)
        for filename, gen_func in files:
            path = repo_dir / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(gen_func())
            print(f"  Generated {path}")
