"""VHS tape generation and execution for colorscheme captures."""

import subprocess
import shutil
from pathlib import Path


def vhs_theme_for(theme: str) -> str:
    """Return VHS theme JSON (single-line) for dark or light variant."""
    from ..generators.vhs import generate_vhs
    from ..palette_data import PALETTE
    import json
    obj = json.loads(generate_vhs(PALETTE, theme))
    return json.dumps(obj)


class TapeBuilder:
    """Builds VHS .tape file content programmatically."""

    def __init__(self, width: int = 1280, height: int = 720,
                 font_size: int = 14, output: str | None = None):
        self._lines: list[str] = []
        self._width = width
        self._height = height
        self._font_size = font_size
        self._output = output

    def type(self, text: str) -> "TapeBuilder":
        self._lines.append(f'Type "{text}"')
        return self

    def enter(self) -> "TapeBuilder":
        self._lines.append("Enter")
        return self

    def sleep(self, seconds: int | float) -> "TapeBuilder":
        self._lines.append(f"Sleep {seconds}s")
        return self

    def screenshot(self, path: str) -> "TapeBuilder":
        self._lines.append(f'Screenshot "{path}"')
        return self

    def ctrl(self, key: str) -> "TapeBuilder":
        self._lines.append(f"Ctrl+{key}")
        return self

    def escape(self) -> "TapeBuilder":
        self._lines.append("Escape")
        return self

    def hide(self) -> "TapeBuilder":
        self._lines.append("Hide")
        return self

    def show(self) -> "TapeBuilder":
        self._lines.append("Show")
        return self

    def set(self, key: str, value: str) -> "TapeBuilder":
        self._lines.append(f"Set {key} {value}")
        return self

    def source(self, path: str) -> "TapeBuilder":
        self._lines.append(f"Source {path}")
        return self

    def build(self) -> str:
        header = []
        if self._output:
            header.append(f'Output "{self._output}"')
        header.extend([
            f"Set Width {self._width}",
            f"Set Height {self._height}",
            f"Set FontSize {self._font_size}",
            "",
        ])
        return "\n".join(header + self._lines) + "\n"


# Tool registry — defines capture behavior for each terminal tool
TOOL_REGISTRY: dict[str, dict] = {
    "bat":      {"interactive": False, "phase": "vhs"},
    "delta":    {"interactive": False, "phase": "vhs"},
    "lazygit":  {"interactive": True,  "phase": "vhs"},
    "fzf":      {"interactive": True,  "phase": "vhs"},
    "lsd":      {"interactive": False, "phase": "vhs"},
    "fish":     {"interactive": False, "phase": "vhs"},
    "kitty":    {"interactive": False, "phase": "vhs"},
    "yazi":     {"interactive": True,  "phase": "vhs"},
    "gitui":    {"interactive": True,  "phase": "vhs"},
    "starship": {"interactive": False, "phase": "vhs"},
    "tmux":     {"interactive": False, "phase": "vhs"},
    "nvim":     {"interactive": True,  "phase": "vhs"},
    "emacs":    {"interactive": True,  "phase": "vhs"},
    "wezterm":  {"interactive": False, "phase": "vhs"},
    "vhs":      {"interactive": False, "phase": "config"},
    "chrome":   {"interactive": False, "phase": "browser"},
    "css":      {"interactive": False, "phase": "browser"},
    "safari":   {"interactive": False, "phase": "browser"},
    "raycast":  {"interactive": False, "phase": "gui"},
    "slack":    {"interactive": False, "phase": "gui"},
}

# Maps tool name → function that builds a TapeBuilder for that tool
_tape_builders: dict[str, "callable"] = {}


def register_tape(tool_name: str):
    """Decorator to register a tape builder function for a tool."""
    def decorator(func):
        _tape_builders[tool_name] = func
        return func
    return decorator


def generate_tape(tool: str, theme: str, output_dir: Path) -> str:
    """Generate VHS tape content for a given tool and theme.

    Args:
        tool: Tool name (e.g., "bat", "nvim")
        theme: "dark" or "light"
        output_dir: Directory for output screenshots/gifs

    Returns:
        VHS tape file content as string

    Raises:
        ValueError: If tool is not in registry or has no tape builder
    """
    if tool not in TOOL_REGISTRY:
        raise ValueError(f"Unknown tool: {tool}")

    if tool not in _tape_builders:
        raise ValueError(f"No tape builder registered for: {tool}")

    builder_func = _tape_builders[tool]
    return builder_func(theme, output_dir)


def run_tape(tape_content: str, tape_path: Path) -> subprocess.CompletedProcess:
    """Write tape content to file and execute with VHS."""
    if not shutil.which("vhs"):
        raise FileNotFoundError(
            "VHS not found. Install: sudo port install vhs || "
            "go install github.com/charmbracelet/vhs@latest"
        )

    tape_path.write_text(tape_content)
    return subprocess.run(
        ["vhs", str(tape_path)],
        capture_output=True, text=True, check=True,
    )


def get_tools_by_phase(phase: str) -> list[str]:
    """Return tool names for a given capture phase."""
    return [name for name, cfg in TOOL_REGISTRY.items() if cfg["phase"] == phase]
