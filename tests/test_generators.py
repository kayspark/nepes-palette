from nepes_palette.palette import load_palette
from nepes_palette.generators.bat import generate_bat
from nepes_palette.generators.delta import generate_delta
from nepes_palette.generators.lazygit import generate_lazygit
from nepes_palette.generators.fzf import generate_fzf
from nepes_palette.generators.lsd import generate_lsd
from nepes_palette.generators.fish import generate_fish
from nepes_palette.generators.chrome import generate_chrome
from nepes_palette.generators.raycast import generate_raycast
from nepes_palette.generators.kitty import generate_kitty
from nepes_palette.generators.yazi import generate_yazi
from nepes_palette.generators.gitui import generate_gitui
from nepes_palette.generators.slack import generate_slack

def test_generate_bat_dark():
    palette = load_palette()
    result = generate_bat(palette, "dark")
    assert '<?xml version="1.0"' in result
    assert "Nepes Dark" in result
    assert "#1E1C1A" in result
    assert "comment" in result.lower()
    assert "keyword" in result.lower()

def test_generate_bat_light():
    palette = load_palette()
    result = generate_bat(palette, "light")
    assert "Nepes Light" in result
    assert "#F8F8F8" in result

def test_generate_delta():
    palette = load_palette()
    result = generate_delta(palette)
    assert "[delta" in result
    assert "syntax-theme" in result
    assert "plus-style" in result
    assert "minus-style" in result

def test_generate_lazygit_dark():
    palette = load_palette()
    result = generate_lazygit(palette, "dark")
    assert "activeBorderColor" in result
    assert "selectedLineBgColor" in result

def test_generate_lazygit_light():
    palette = load_palette()
    result = generate_lazygit(palette, "light")
    assert "Nepes Light" in result

def test_generate_fzf_dark():
    palette = load_palette()
    result = generate_fzf(palette, "dark")
    assert "--color=" in result
    assert "export" in result

def test_generate_fzf_light():
    palette = load_palette()
    result = generate_fzf(palette, "light")
    assert "Nepes Light" in result

def test_generate_lsd_dark():
    palette = load_palette()
    result = generate_lsd(palette, "dark")
    assert "permission" in result
    assert "file-type" in result
    assert "directory" in result

def test_generate_lsd_light():
    palette = load_palette()
    result = generate_lsd(palette, "light")
    assert "Nepes Light" in result

def test_generate_fish_dark():
    palette = load_palette()
    result = generate_fish(palette, "dark")
    assert "fish_color_normal" in result
    assert "fish_color_command" in result
    assert "fish_pager_color" in result

def test_generate_fish_light():
    palette = load_palette()
    result = generate_fish(palette, "light")
    assert "Nepes Light" in result

def test_generate_chrome_dark():
    palette = load_palette()
    result = generate_chrome(palette, "dark")
    import json
    manifest = json.loads(result)
    assert manifest["manifest_version"] == 3
    assert manifest["name"] == "Nepes Dark"
    assert "frame" in manifest["theme"]["colors"]
    assert "toolbar" in manifest["theme"]["colors"]
    assert manifest["theme"]["colors"]["tab_text"] == [220, 216, 212]  # #DCD8D4

def test_generate_chrome_light():
    palette = load_palette()
    result = generate_chrome(palette, "light")
    import json
    manifest = json.loads(result)
    assert manifest["name"] == "Nepes Light"
    assert manifest["theme"]["colors"]["tab_text"] == [28, 28, 30]  # #1C1C1E

def test_generate_raycast_dark():
    palette = load_palette()
    result = generate_raycast(palette, "dark")
    import json
    theme = json.loads(result)
    assert theme["name"] == "Nepes Dark"
    assert theme["appearance"] == "dark"
    assert theme["colors"]["background"] == "#1E1C1A"
    assert theme["colors"]["text"] == "#DCD8D4"
    assert theme["colors"]["tint"] == "#6A84CA"

def test_generate_raycast_light():
    palette = load_palette()
    result = generate_raycast(palette, "light")
    import json
    theme = json.loads(result)
    assert theme["name"] == "Nepes Light"
    assert theme["appearance"] == "light"
    assert theme["colors"]["background"] == "#F8F8F8"

def test_generate_kitty_dark():
    palette = load_palette()
    result = generate_kitty(palette, "dark")
    assert "foreground" in result
    assert "background" in result
    assert "color0" in result
    assert "color15" in result
    assert "tab_bar_margin_color" in result
    assert "mark1_background" in result
    assert "macos_titlebar_color" in result
    assert "#23438E" in result  # blue_dim for active tab

def test_generate_kitty_light():
    palette = load_palette()
    result = generate_kitty(palette, "light")
    assert "Nepes Light" in result

def test_generate_yazi_dark():
    palette = load_palette()
    result = generate_yazi(palette, "dark")
    assert "[manager]" in result
    assert "[status]" in result
    assert "marker_copied" in result
    assert "mode_normal" in result

def test_generate_yazi_light():
    palette = load_palette()
    result = generate_yazi(palette, "light")
    assert "Nepes Light" in result

def test_generate_gitui_dark():
    palette = load_palette()
    result = generate_gitui(palette, "dark")
    assert "selected_tab" in result
    assert "diff_line_add" in result
    assert "Rgb(" in result

def test_generate_gitui_light():
    palette = load_palette()
    result = generate_gitui(palette, "light")
    assert "Nepes Light" in result

def test_generate_slack_dark():
    palette = load_palette()
    result = generate_slack(palette, "dark")
    assert "Slack" in result
    # Should have 8 comma-separated hex values on the last non-empty line
    lines = [l for l in result.strip().splitlines() if not l.startswith("#")]
    assert len(lines) == 1
    values = lines[0].split(",")
    assert len(values) == 8

def test_generate_slack_light():
    palette = load_palette()
    result = generate_slack(palette, "light")
    assert "Nepes Light" in result
