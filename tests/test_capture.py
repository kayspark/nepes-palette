from pathlib import Path
from nepes_palette.capture.runner import TapeBuilder, generate_tape, TOOL_REGISTRY


def test_tape_builder_basic():
    """TapeBuilder produces valid VHS tape syntax."""
    tb = TapeBuilder(font_size=14)
    tb.type("echo hello")
    tb.enter()
    tb.sleep(1)
    tb.screenshot("out.png")
    tape = tb.build()
    assert "Set Width 1280" in tape
    assert "Set Height 720" in tape
    assert "Set FontSize 14" in tape
    assert 'Type "echo hello"' in tape
    assert "Enter" in tape
    assert "Sleep 1s" in tape
    assert 'Screenshot "out.png"' in tape


def test_tape_builder_output_gif():
    """TapeBuilder with output produces GIF recording."""
    tb = TapeBuilder(output="demo.gif")
    tb.type("ls")
    tb.enter()
    tape = tb.build()
    assert 'Output "demo.gif"' in tape


def test_generate_tape_unknown_tool():
    """generate_tape raises ValueError for unknown tool."""
    import pytest
    with pytest.raises(ValueError, match="Unknown tool"):
        generate_tape("nonexistent-tool", "dark", Path("/tmp"))


def test_tool_registry_has_terminal_tools():
    """Registry contains all 14 terminal tools."""
    terminal_tools = [
        "bat", "delta", "lazygit", "fzf", "lsd", "fish",
        "kitty", "yazi", "gitui", "starship", "tmux",
        "nvim", "emacs", "wezterm",
    ]
    for tool in terminal_tools:
        assert tool in TOOL_REGISTRY, f"{tool} not in registry"


def test_tool_registry_interactive_flag():
    """Interactive tools are flagged for GIF recording."""
    interactive = {"nvim", "emacs", "lazygit", "fzf", "gitui", "yazi"}
    for name, config in TOOL_REGISTRY.items():
        if name in interactive:
            assert config["interactive"] is True, f"{name} should be interactive"
        else:
            assert config["interactive"] is False, f"{name} should not be interactive"
