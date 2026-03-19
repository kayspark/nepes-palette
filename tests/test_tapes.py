from pathlib import Path
from nepes_palette.capture.runner import generate_tape, TOOL_REGISTRY

# Import tapes to trigger registration
import nepes_palette.capture.tapes  # noqa: F401


def test_all_vhs_tools_have_tape_builders():
    """Every VHS-phase tool must have a registered tape builder."""
    vhs_tools = [name for name, cfg in TOOL_REGISTRY.items() if cfg["phase"] == "vhs"]
    for tool in vhs_tools:
        # Should not raise
        tape = generate_tape(tool, "dark", Path("/tmp/test"))
        assert "Set Width" in tape
        assert "Screenshot" in tape


def test_bat_tape_dark():
    tape = generate_tape("bat", "dark", Path("/tmp/test"))
    assert "bat" in tape.lower() or "BAT" in tape
    assert "showcase.py" in tape
    assert "Screenshot" in tape


def test_bat_tape_light():
    tape = generate_tape("bat", "light", Path("/tmp/test"))
    assert "Screenshot" in tape


def test_nvim_tape_has_gif():
    """Interactive tools should produce GIF output."""
    tape = generate_tape("nvim", "dark", Path("/tmp/test"))
    assert "Output" in tape
    assert ".gif" in tape


def test_lsd_tape_no_gif():
    """Non-interactive tools should not produce GIF."""
    tape = generate_tape("lsd", "dark", Path("/tmp/test"))
    assert "Output" not in tape or ".gif" not in tape


def test_terminal_tapes_use_paging_never():
    """Terminal emulator tapes must use --paging=never to avoid pager errors."""
    terminal_tools = ["cmux", "kitty", "wezterm"]
    for tool in terminal_tools:
        tape = generate_tape(tool, "dark", Path("/tmp/test"))
        assert "--paging=never" in tape, f"{tool} tape missing --paging=never"


def test_cmux_tape_dark():
    tape = generate_tape("cmux", "dark", Path("/tmp/test"))
    assert "showcase.py" in tape
    assert "Screenshot" in tape
    assert "--paging=never" in tape
