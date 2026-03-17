# Chart Palette Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add chart-specific color palettes to nepes-palette, generate an R package (ggnepes) and matplotlib style files (mplstyle-nepes).

**Architecture:** Chart colors are separate overrides in `palette_data.py` (don't change terminal/editor ANSI colors). Two new generators produce output for two new repos. R package is CRAN-ready. matplotlib style files are drop-in.

**Tech Stack:** Python (generators), R (ggnepes package, ggplot2, testthat, roxygen2), matplotlib (.mplstyle format)

**Validated colors:** `docs/chart-palette-validated.md`

---

## Chunk 1: Core Palette — Chart Colors

### Task 1: Add chart_bases and SPC palette to palette_data.py

**Files:**
- Modify: `src/nepes_palette/palette_data.py` (chart section, lines 188-216)

- [ ] **Step 1: Add chart_bases with validated colors**

In `palette_data.py`, replace the current `_dark_chart_bases` / `_light_chart_bases` with separate chart-specific colors. Add after the existing chart section (~line 216):

```python
# ── Chart-Specific Colors (WCAG AA + colorblind validated) ──
_light["chart_bases"] = [
    "#23438E",  # blue (unchanged)
    "#C25609",  # orange (darkened for AA on white)
    "#017939",  # green (hue-shifted for colorblind safety)
    "#C4181F",  # red (unchanged)
    "#2D7A82",  # teal (unchanged)
    "#873D8E",  # purple (hue-shifted from blue)
]

_light["chart_midtones"] = [
    "#6278AB",  # blue midtone
    "#A7693E",  # orange midtone
    "#017939",  # green (no midtone — use base for fills too)
    "#B75B5F",  # red midtone
    "#56898E",  # teal midtone
    "#96699A",  # purple midtone
]

_dark["chart_bases"] = [
    _dark["blue"],      # #5C8CFF
    _dark["orange"],    # #FEA413
    _dark["green"],     # #3DDC84
    _dark["red"],       # #FF5C5C
    _dark["cyan"],      # #3A9BA5
    _dark["magenta"],   # #A274C3
]

_dark["chart_midtones"] = [
    _dark["blue_bright"],     # #6B8AD8
    _dark["orange_bright"],   # #FFBD4A
    _dark["green_bright"],    # #6BCF70
    _dark["red_bright"],      # #E85B61
    _dark["cyan_bright"],     # #5CBDC7
    _dark["magenta_bright"],  # #BB8EDA
]

# SPC semantic palette
_light["spc"] = {
    "center_line":   "#23438E",
    "data_points":   "#5A7EB0",
    "control_limit": "#6A6A6A",
    "spec_limit":    "#C25609",
    "violation":     "#C4181F",
}

_dark["spc"] = {
    "center_line":   "#5C8CFF",
    "data_points":   "#6B8AD8",
    "control_limit": "#8A9199",
    "spec_limit":    "#FEA413",
    "violation":     "#FF5C5C",
}
```

Keep the existing `_dark_chart_bases` / `chart_series()` code unchanged — it's used by existing generators.

- [ ] **Step 2: Run validation**

Run: `uv run python -m nepes_palette.cli validate`
Expected: all existing checks still pass (chart_bases are additive, no existing colors changed)

- [ ] **Step 3: Run existing tests**

Run: `uv run pytest tests/ -v`
Expected: 77 tests pass (no regressions)

- [ ] **Step 4: Commit**

```bash
git add src/nepes_palette/palette_data.py
git commit -m "feat: add chart_bases, chart_midtones, SPC palette to palette_data"
```

---

## Chunk 2: matplotlib Style Generator + Repo

### Task 2: Create mplstyle generator

**Files:**
- Create: `src/nepes_palette/generators/mplstyle.py`
- Modify: `src/nepes_palette/generators/__init__.py`

- [ ] **Step 1: Write test for mplstyle generator**

Create `tests/test_generators.py` additions (append to existing file):

```python
def test_generate_mplstyle_light():
    palette = load_palette()
    from nepes_palette.generators.mplstyle import generate_mplstyle
    result = generate_mplstyle(palette, "light")
    assert "axes.prop_cycle" in result
    assert "#23438E" in result  # blue chart base
    assert "axes.facecolor: white" in result

def test_generate_mplstyle_dark():
    palette = load_palette()
    from nepes_palette.generators.mplstyle import generate_mplstyle
    result = generate_mplstyle(palette, "dark")
    assert "axes.prop_cycle" in result
    assert "#1E1C1A" in result  # dark bg
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run pytest tests/test_generators.py::test_generate_mplstyle_light -v`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement mplstyle generator**

Create `src/nepes_palette/generators/mplstyle.py`:

```python
"""Generate matplotlib style files from the nepes palette."""


def generate_mplstyle(palette: dict, theme: str) -> str:
    """Generate a .mplstyle file for matplotlib."""
    t = palette[theme]
    bases = t["chart_bases"]
    midtones = t["chart_midtones"]
    # 12-color cycle: 6 bases then 6 midtones
    cycle = bases + midtones
    cycle_str = ", ".join(f"'{c}'" for c in cycle)

    if theme == "dark":
        return f"""\
# Nepes Dark — matplotlib style
# Install: cp to ~/.config/matplotlib/stylelib/nepes-dark.mplstyle
# Use: plt.style.use('nepes-dark')

axes.prop_cycle: cycler('color', [{cycle_str}])
axes.facecolor: {t["bg"]}
axes.edgecolor: {t["fg_muted"]}
axes.labelcolor: {t["fg"]}
axes.grid: True

figure.facecolor: {t["bg"]}
figure.edgecolor: {t["bg"]}

text.color: {t["fg"]}

xtick.color: {t["fg_dim"]}
ytick.color: {t["fg_dim"]}

grid.color: {t["bg_hl"]}
grid.alpha: 0.8
grid.linestyle: --

legend.facecolor: {t["bg_alt"]}
legend.edgecolor: {t["border"]}
legend.framealpha: 0.9

savefig.facecolor: {t["bg"]}
savefig.edgecolor: {t["bg"]}
"""
    else:
        return f"""\
# Nepes Light — matplotlib style
# Install: cp to ~/.config/matplotlib/stylelib/nepes-light.mplstyle
# Use: plt.style.use('nepes-light')

axes.prop_cycle: cycler('color', [{cycle_str}])
axes.facecolor: white
axes.edgecolor: {t["fg_subtle"]}
axes.labelcolor: {t["fg"]}
axes.grid: True

figure.facecolor: white
figure.edgecolor: white

text.color: {t["fg"]}

xtick.color: {t["fg_dim"]}
ytick.color: {t["fg_dim"]}

grid.color: {t["bg_alt"]}
grid.alpha: 0.8
grid.linestyle: --

legend.facecolor: white
legend.edgecolor: {t["border"]}
legend.framealpha: 0.9

savefig.facecolor: white
savefig.edgecolor: white
"""
```

- [ ] **Step 4: Register in __init__.py**

Add to imports and generators dict in `generators/__init__.py`:

```python
from .mplstyle import generate_mplstyle

# In generators dict:
"mplstyle-nepes": [
    ("nepes-light.mplstyle", lambda: generate_mplstyle(palette, "light")),
    ("nepes-dark.mplstyle", lambda: generate_mplstyle(palette, "dark")),
],
```

- [ ] **Step 5: Run tests**

Run: `uv run pytest tests/test_generators.py -v`
Expected: all pass including new mplstyle tests

- [ ] **Step 6: Commit**

```bash
git add src/nepes_palette/generators/mplstyle.py src/nepes_palette/generators/__init__.py tests/test_generators.py
git commit -m "feat: add matplotlib style generator"
```

### Task 3: Create mplstyle-nepes repo

**Files:**
- Create: `~/workspace/colorscheme/mplstyle-nepes/` (new repo)

- [ ] **Step 1: Generate mplstyle files**

Run: `uv run python -m nepes_palette.cli generate`
Verify: `mplstyle-nepes/nepes-light.mplstyle` and `nepes-dark.mplstyle` created

- [ ] **Step 2: Init repo and push**

```bash
cd ~/workspace/colorscheme/mplstyle-nepes
git init && git branch -m main
git add nepes-light.mplstyle nepes-dark.mplstyle README.org
git commit -m "feat: nepes matplotlib style files (light + dark)"
gh repo create kayspark/mplstyle-nepes --private --source=. --push \
  --description "Nepes colorscheme for matplotlib"
```

- [ ] **Step 3: Install to dotfiles**

```bash
mkdir -p ~/.config/matplotlib/stylelib
cp nepes-light.mplstyle nepes-dark.mplstyle ~/.config/matplotlib/stylelib/
```

- [ ] **Step 4: Commit**

```bash
git push origin HEAD:main
```

---

## Chunk 3: ggnepes R Package

### Task 4: Create ggnepes R package structure

**Files:**
- Create: `~/workspace/colorscheme/ggnepes/DESCRIPTION`
- Create: `~/workspace/colorscheme/ggnepes/R/palettes.R`
- Create: `~/workspace/colorscheme/ggnepes/R/scales.R`
- Create: `~/workspace/colorscheme/ggnepes/R/themes.R`
- Create: `~/workspace/colorscheme/ggnepes/tests/testthat/test-palettes.R`
- Create: `~/workspace/colorscheme/ggnepes/tests/testthat.R`
- Create: `~/workspace/colorscheme/ggnepes/.Rbuildignore`
- Create: `~/workspace/colorscheme/ggnepes/LICENSE`

- [ ] **Step 1: Install R dev dependencies**

```r
R --vanilla -e "install.packages(c('ggplot2', 'testthat', 'roxygen2', 'devtools'), repos='https://cran.r-project.org')"
```

- [ ] **Step 2: Create DESCRIPTION**

```
Package: ggnepes
Title: Nepes Corporate Color Palette for 'ggplot2'
Version: 0.1.0
Authors@R: person("Kay", "Park", email = "kspark@nepes.co.kr", role = c("aut", "cre"))
Description: Provides color palettes and themes derived from the Nepes
    corporate identity for use with 'ggplot2'. Includes discrete color
    scales, SPC (Statistical Process Control) semantic palettes, and
    complete 'ggplot2' themes for light and dark backgrounds.
License: MIT + file LICENSE
Imports: ggplot2 (>= 3.0.0)
Suggests: testthat (>= 3.0.0)
Config/testthat/edition: 3
Encoding: UTF-8
Roxygen: list(markdown = TRUE)
RoxygenNote: 7.3.2
```

- [ ] **Step 3: Create R/palettes.R with validated hex values**

This file is the generator target. Contains hardcoded hex values from `chart-palette-validated.md`:

```r
#' Nepes Color Palette
#'
#' Returns a character vector of hex colors from the Nepes corporate palette.
#'
#' @param theme Character. Either "light" (default) or "dark".
#' @param n Integer. Number of colors to return (default: 12).
#' @return A character vector of hex color strings.
#' @export
#' @examples
#' nepes_pal()
#' nepes_pal("dark", n = 6)
nepes_pal <- function(theme = "light", n = 12) {
  pal <- if (theme == "dark") .nepes_dark_12 else .nepes_light_12
  if (n > length(pal)) n <- length(pal)
  pal[seq_len(n)]
}

#' Nepes SPC Palette
#'
#' Returns a named character vector of colors for SPC (Statistical Process
#' Control) charts: center line, data points, control limits, spec limits,
#' and violations.
#'
#' @param theme Character. Either "light" (default) or "dark".
#' @return A named character vector.
#' @export
#' @examples
#' nepes_spc()
#' nepes_spc("dark")
nepes_spc <- function(theme = "light") {
  if (theme == "dark") .nepes_spc_dark else .nepes_spc_light
}

# ── Light theme (12 colors: 6 bases + 6 midtones) ──
.nepes_light_12 <- c(
  "#23438E", "#C25609", "#017939", "#C4181F", "#2D7A82", "#873D8E",
  "#6278AB", "#A7693E", "#017939", "#B75B5F", "#56898E", "#96699A"
)

# ── Dark theme (12 colors: 6 bases + 6 midtones) ──
.nepes_dark_12 <- c(
  "#5C8CFF", "#FEA413", "#3DDC84", "#FF5C5C", "#3A9BA5", "#A274C3",
  "#6B8AD8", "#FFBD4A", "#6BCF70", "#E85B61", "#5CBDC7", "#BB8EDA"
)

# ── SPC palettes ──
.nepes_spc_light <- c(
  center_line   = "#23438E",
  data_points   = "#5A7EB0",
  control_limit = "#6A6A6A",
  spec_limit    = "#C25609",
  violation     = "#C4181F"
)

.nepes_spc_dark <- c(
  center_line   = "#5C8CFF",
  data_points   = "#6B8AD8",
  control_limit = "#8A9199",
  spec_limit    = "#FEA413",
  violation     = "#FF5C5C"
)
```

- [ ] **Step 4: Create R/scales.R**

```r
#' Nepes Discrete Color Scale
#'
#' @param theme Character. "light" (default) or "dark".
#' @param ... Additional arguments passed to
#'   \code{\link[ggplot2]{discrete_scale}}.
#' @return A ggplot2 scale.
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(iris, aes(Sepal.Length, Sepal.Width, color = Species)) +
#'   geom_point() +
#'   scale_color_nepes()
scale_color_nepes <- function(theme = "light", ...) {
  pal <- nepes_pal(theme)
  ggplot2::discrete_scale("colour", "nepes",
    function(n) pal[seq_len(n)], ...)
}

#' @rdname scale_color_nepes
#' @export
scale_colour_nepes <- scale_color_nepes

#' Nepes Discrete Fill Scale
#'
#' @inheritParams scale_color_nepes
#' @export
scale_fill_nepes <- function(theme = "light", ...) {
  pal <- nepes_pal(theme)
  ggplot2::discrete_scale("fill", "nepes",
    function(n) pal[seq_len(n)], ...)
}
```

- [ ] **Step 5: Create R/themes.R**

```r
#' Nepes Light Theme for ggplot2
#'
#' A clean, minimal theme with white background using Nepes palette colors.
#'
#' @param base_size Base font size (default: 11).
#' @param base_family Font family (default: system sans-serif).
#' @return A ggplot2 theme.
#' @export
theme_nepes_light <- function(base_size = 11, base_family = "") {
  ggplot2::theme_minimal(base_size = base_size, base_family = base_family) +
    ggplot2::theme(
      plot.background    = ggplot2::element_rect(fill = "white", color = NA),
      panel.background   = ggplot2::element_rect(fill = "white", color = NA),
      panel.grid.major   = ggplot2::element_line(color = "#E7E6E6"),
      panel.grid.minor   = ggplot2::element_blank(),
      axis.text          = ggplot2::element_text(color = "#3A3A3E"),
      axis.title         = ggplot2::element_text(color = "#1C1C1E"),
      plot.title         = ggplot2::element_text(color = "#1C1C1E", face = "bold"),
      plot.subtitle      = ggplot2::element_text(color = "#5A5A64"),
      legend.background  = ggplot2::element_rect(fill = "white", color = NA),
      legend.key         = ggplot2::element_rect(fill = "white", color = NA),
      strip.background   = ggplot2::element_rect(fill = "#F0F0F0", color = NA),
      strip.text         = ggplot2::element_text(color = "#1C1C1E")
    )
}

#' Nepes Dark Theme for ggplot2
#'
#' A minimal theme with warm dark background using Nepes palette colors.
#'
#' @inheritParams theme_nepes_light
#' @export
theme_nepes_dark <- function(base_size = 11, base_family = "") {
  ggplot2::theme_minimal(base_size = base_size, base_family = base_family) +
    ggplot2::theme(
      plot.background    = ggplot2::element_rect(fill = "#1E1C1A", color = NA),
      panel.background   = ggplot2::element_rect(fill = "#1E1C1A", color = NA),
      panel.grid.major   = ggplot2::element_line(color = "#3E3A38"),
      panel.grid.minor   = ggplot2::element_blank(),
      axis.text          = ggplot2::element_text(color = "#B6B0AC"),
      axis.title         = ggplot2::element_text(color = "#DCD8D4"),
      plot.title         = ggplot2::element_text(color = "#DCD8D4", face = "bold"),
      plot.subtitle      = ggplot2::element_text(color = "#8A9199"),
      legend.background  = ggplot2::element_rect(fill = "#2E2C2A", color = NA),
      legend.key         = ggplot2::element_rect(fill = "#2E2C2A", color = NA),
      strip.background   = ggplot2::element_rect(fill = "#2E2C2A", color = NA),
      strip.text         = ggplot2::element_text(color = "#DCD8D4")
    )
}
```

- [ ] **Step 6: Create tests/testthat.R**

```r
library(testthat)
library(ggnepes)
test_check("ggnepes")
```

- [ ] **Step 7: Create tests/testthat/test-palettes.R**

```r
test_that("nepes_pal returns 12 colors by default", {
  pal <- nepes_pal()
  expect_length(pal, 12)
})

test_that("nepes_pal returns valid hex colors", {
  pal <- nepes_pal()
  expect_true(all(grepl("^#[0-9A-Fa-f]{6}$", pal)))
})

test_that("nepes_pal n parameter works", {
  expect_length(nepes_pal(n = 6), 6)
  expect_length(nepes_pal(n = 3), 3)
})

test_that("nepes_pal dark theme works", {
  pal <- nepes_pal("dark")
  expect_length(pal, 12)
  expect_true(all(grepl("^#[0-9A-Fa-f]{6}$", pal)))
})

test_that("nepes_spc returns named vector", {
  spc <- nepes_spc()
  expect_length(spc, 5)
  expect_named(spc, c("center_line", "data_points", "control_limit",
                       "spec_limit", "violation"))
})

test_that("scale_color_nepes returns a ggplot2 scale", {
  s <- scale_color_nepes()
  expect_s3_class(s, "Scale")
})

test_that("theme_nepes_light returns a ggplot2 theme", {
  th <- theme_nepes_light()
  expect_s3_class(th, "theme")
})

test_that("theme_nepes_dark returns a ggplot2 theme", {
  th <- theme_nepes_dark()
  expect_s3_class(th, "theme")
})
```

- [ ] **Step 8: Create remaining package files**

`.Rbuildignore`:
```
^.*\.Rproj$
^\.Rproj\.user$
^docs$
```

`LICENSE`:
```
MIT License

Copyright (c) 2026 Kay Park / Nepes Co., Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
...
```

`tests/testthat.R` (already in step 6)

- [ ] **Step 9: Generate NAMESPACE with roxygen2**

```bash
cd ~/workspace/colorscheme/ggnepes
R --vanilla -e "roxygen2::roxygenise()"
```

- [ ] **Step 10: Run R CMD check**

```bash
R CMD build .
R CMD check ggnepes_0.1.0.tar.gz --as-cran
```

Expected: 0 errors, 0 warnings, possibly 1-2 notes (new submission, no vignette)

- [ ] **Step 11: Init repo and push**

```bash
git init && git branch -m main
git add -A
git commit -m "feat: ggnepes R package — nepes color palette for ggplot2"
gh repo create kayspark/ggnepes --private --source=. --push \
  --description "Nepes corporate color palette for ggplot2 (CRAN-ready)"
```

---

## Chunk 4: ggplot2 Generator in nepes-palette

### Task 5: Create ggplot2 generator

**Files:**
- Create: `src/nepes_palette/generators/ggplot2.py`
- Modify: `src/nepes_palette/generators/__init__.py`

- [ ] **Step 1: Write test**

Add to `tests/test_generators.py`:

```python
def test_generate_ggplot2():
    palette = load_palette()
    from nepes_palette.generators.ggplot2 import generate_ggplot2
    result = generate_ggplot2(palette)
    assert "nepes_pal" in result
    assert "#23438E" in result
    assert "nepes_spc" in result
    assert ".nepes_light_12" in result
```

- [ ] **Step 2: Implement generator**

Create `src/nepes_palette/generators/ggplot2.py`:

```python
"""Generate R/palettes.R for the ggnepes package."""


def generate_ggplot2(palette: dict) -> str:
    """Generate R/palettes.R with hardcoded hex vectors from palette."""
    lt = palette["light"]
    dk = palette["dark"]

    def _r_vec(colors):
        inner = ", ".join(f'"{c}"' for c in colors)
        return f"c(\n  {inner}\n)"

    def _r_named_vec(d):
        inner = ",\n  ".join(f'{k:15} = "{v}"' for k, v in d.items())
        return f"c(\n  {inner}\n)"

    return f'''\
# Generated by nepes-palette — do not edit manually.
# Regenerate: uv run python -m nepes_palette.cli generate

.nepes_light_12 <- {_r_vec(lt["chart_bases"] + lt["chart_midtones"])}

.nepes_dark_12 <- {_r_vec(dk["chart_bases"] + dk["chart_midtones"])}

.nepes_spc_light <- {_r_named_vec(lt["spc"])}

.nepes_spc_dark <- {_r_named_vec(dk["spc"])}
'''
```

- [ ] **Step 3: Register in __init__.py**

```python
from .ggplot2 import generate_ggplot2

"ggnepes": [
    ("R/palettes-generated.R", lambda: generate_ggplot2(palette)),
],
```

Note: generates to `R/palettes-generated.R` (not `palettes.R`) since the R package has manually maintained roxygen docs in `palettes.R` that source the generated values.

- [ ] **Step 4: Run tests**

Run: `uv run pytest tests/ -v`
Expected: all pass

- [ ] **Step 5: Commit and push**

```bash
git add src/nepes_palette/generators/ggplot2.py src/nepes_palette/generators/__init__.py tests/test_generators.py
git commit -m "feat: add ggplot2 palettes.R generator"
git push origin HEAD:master
```

---

## Chunk 5: Final Integration

### Task 6: Update memory and docs

- [ ] **Step 1: Update MEMORY.md** — add ggnepes and mplstyle-nepes to sub-repos table (23 total)
- [ ] **Step 2: Update spec** — mark as implemented, note any deviations
- [ ] **Step 3: Commit dotfiles** — memory, matplotlib stylelib install

```bash
cd ~/.dotfiles && git add -A && git commit -m "chore: add ggnepes, mplstyle-nepes to memory + install mplstyle"
git push
```
