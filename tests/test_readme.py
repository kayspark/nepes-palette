from nepes_palette.generators.readme import generate_readme, TOOL_METADATA


def test_generate_readme_bat():
    result = generate_readme("bat")
    assert "#+title: bat-nepes" in result
    assert "[[./docs/dark.png]]" in result
    assert "[[./docs/light.png]]" in result
    assert "Installation" in result


def test_generate_readme_nvim():
    result = generate_readme("nvim")
    assert "#+title: nvim-nepes" in result
    assert "[[./docs/dark.gif]]" in result  # interactive -> has GIF
    assert "lazy.nvim" in result.lower() or "Lazy" in result


def test_generate_readme_has_dark_light_table():
    result = generate_readme("kitty")
    assert "Dark" in result
    assert "Light" in result


def test_all_tools_have_metadata():
    """Every tool in the registry should have README metadata."""
    from nepes_palette.capture.runner import TOOL_REGISTRY
    for tool in TOOL_REGISTRY:
        assert tool in TOOL_METADATA, f"{tool} missing from TOOL_METADATA"


def test_readme_is_org_format():
    result = generate_readme("delta")
    assert result.startswith("#+")
    assert "#+title:" in result


def test_readme_image_links_no_file_prefix():
    """Org image links must use ./docs/ not file:docs/ for GitHub rendering."""
    from nepes_palette.capture.runner import TOOL_REGISTRY
    for tool in TOOL_REGISTRY:
        result = generate_readme(tool)
        assert "[[file:" not in result, f"{tool} README uses file: prefix"


def test_generate_readme_cmux():
    result = generate_readme("cmux")
    assert "#+title: cmux-nepes" in result
    assert "ghostty" in result.lower()
    assert "[[./docs/dark.png]]" in result
