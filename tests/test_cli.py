import subprocess
import sys


def test_cli_validate():
    result = subprocess.run(
        [sys.executable, "-m", "nepes_palette.cli", "validate"],
        capture_output=True, text=True,
        cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
    )
    # validate may exit 1 if there are WCAG failures, but it should still produce output
    assert "WCAG" in result.stdout or "contrast" in result.stdout.lower()


def test_cli_help():
    result = subprocess.run(
        [sys.executable, "-m", "nepes_palette.cli", "--help"],
        capture_output=True, text=True,
        cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
    )
    assert result.returncode == 0
    assert "validate" in result.stdout
    assert "generate" in result.stdout
