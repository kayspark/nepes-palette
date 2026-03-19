import subprocess
import tempfile
from pathlib import Path


def test_capture_dry_run_single_tool():
    """Dry-run capture of a single tool produces tape + README."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            ["uv", "run", "python", "-m", "nepes_palette", "capture",
             "bat", "--dry-run", "-o", tmpdir],
            capture_output=True, text=True,
            cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
        )
        assert result.returncode == 0
        assert "Capturing bat" in result.stdout

        bat_dir = Path(tmpdir) / "bat-nepes"
        assert (bat_dir / "docs" / "capture-dark.tape").exists()
        assert (bat_dir / "docs" / "capture-light.tape").exists()
        assert (bat_dir / "README.org").exists()

        readme = (bat_dir / "README.org").read_text()
        assert "#+title: bat-nepes" in readme
        assert "[[./docs/dark.png]]" in readme


def test_capture_dry_run_phase():
    """Dry-run with --phase=vhs captures all terminal tools."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            ["uv", "run", "python", "-m", "nepes_palette", "capture",
             "--phase", "vhs", "--dry-run", "-o", tmpdir],
            capture_output=True, text=True,
            cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
        )
        assert result.returncode == 0

        # Check a few tools exist
        for tool in ["bat", "nvim", "lazygit"]:
            docs = Path(tmpdir) / f"{tool}-nepes" / "docs"
            assert docs.exists(), f"{tool} docs dir missing"
            assert (docs / "capture-dark.tape").exists()


def test_capture_dry_run_all():
    """Dry-run with --all captures VHS tools and skips browser/gui."""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            ["uv", "run", "python", "-m", "nepes_palette", "capture",
             "--all", "--dry-run", "-o", tmpdir],
            capture_output=True, text=True,
            cwd="/Users/kaypark/workspace/colorscheme/nepes-palette",
        )
        assert result.returncode == 0
        assert "Skipping non-VHS" in result.stdout
