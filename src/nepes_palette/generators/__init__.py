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

    generators = {
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
    }

    for repo_name, files in generators.items():
        repo_dir = output_dir / repo_name
        repo_dir.mkdir(parents=True, exist_ok=True)
        for filename, gen_func in files:
            path = repo_dir / filename
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(gen_func())
            print(f"  Generated {path}")
