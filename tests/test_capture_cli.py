import subprocess


def test_capture_help():
    """capture subcommand shows help."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "nepes_palette", "capture", "--help"],
        capture_output=True, text=True,
        cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
    )
    assert result.returncode == 0
    assert "capture" in result.stdout.lower()
    assert "--phase" in result.stdout
    assert "--all" in result.stdout


def test_capture_unknown_tool():
    """capture with unknown tool exits with error."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "nepes_palette", "capture", "nonexistent"],
        capture_output=True, text=True,
        cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
    )
    assert result.returncode != 0
