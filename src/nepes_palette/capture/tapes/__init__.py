"""VHS tape definitions for all terminal tools.

Importing this package registers all tape builders.
"""
from . import (  # noqa: F401
    bat, delta, lsd, fzf, fish, kitty, starship, tmux,
    lazygit, gitui, yazi, nvim, emacs, wezterm,
)
