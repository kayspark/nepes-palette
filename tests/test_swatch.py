import tempfile
from pathlib import Path
from nepes_palette.palette import load_palette
from nepes_palette.swatch import render_swatch

PALETTE_PATH = Path(__file__).parent.parent / "palette.toml"


def test_render_swatch_creates_png():
    palette = load_palette(PALETTE_PATH)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        output = f.name
    render_swatch(palette, output)
    p = Path(output)
    assert p.exists()
    assert p.stat().st_size > 1000
    p.unlink()
