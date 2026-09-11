# Personal Homepage Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the homepage so it presents a higher-level personal identity — finding structure in complexity and leaving room for emergence — while keeping software engineering as quiet background context.

**Architecture:** Keep the site as a single static `index.html` with semantic HTML, inline CSS, and one meaningful inline SVG composition. Add a small stdlib-only Python contract test so content and structural regressions are detectable without introducing a frontend toolchain.

**Tech Stack:** HTML5, CSS, inline SVG, Python 3 stdlib `unittest`.

**Spec:** `docs/superpowers/specs/2026-09-11-personal-homepage-redesign.md`

## Global Constraints

- No CASE, CSC, workplace names, internal systems, mascots, characters, project stories, or organization-specific language may appear.
- Software engineering is background context, not the organizing principle.
- Theme is `Structured Core, Living Edge`.
- Primary idea: `I like finding structure in complexity — then seeing what can grow from it.`
- Preserve `relationships over inventory` as a personal principle.
- Keep warm off-white / graphite foundation and use copper/orange only as a living signal for connection, change, curiosity, or emergence.
- Avoid dashboard cards, floating pills, badge walls, résumé layout, timelines, particle fields, parallax, scroll-jacking, and framework dependencies.
- Use semantic HTML, accessible SVG title/description, responsive layout, and `prefers-reduced-motion` support.
- External dependencies remain zero unless a specific visual behavior proves impossible with CSS/SVG.

---

### Task 1: Homepage contract and identity rewrite

**Files:**
- Create: `tests/test_homepage.py`
- Modify: `index.html`

**Interfaces:**
- Consumes: the current one-page site and redesign spec.
- Produces: a page whose public copy expresses identity before occupation and whose sections are `hero`, `ways-of-seeing`, `between-things`, and `public-edge`.

- [ ] **Step 1: Write the failing contract tests**

Create `tests/test_homepage.py` with stdlib tests that assert:

```python
from pathlib import Path
import unittest

HTML = Path(__file__).parents[1].joinpath("index.html").read_text(encoding="utf-8")


class HomepageContractTest(unittest.TestCase):
    def test_identity_before_occupation(self):
        self.assertIn("finding structure in complexity", HTML.lower())
        self.assertIn("seeing what can grow from it", HTML.lower())
        self.assertIn("background is in software engineering", HTML.lower())

    def test_work_history_strip_is_removed(self):
        self.assertNotIn("traditional applications", HTML.lower())
        self.assertNotIn("application platforms", HTML.lower())
        self.assertNotIn("platform engineering", HTML.lower())

    def test_four_lenses_exist(self):
        for lens in ("structure", "relationships", "boundaries", "emergence"):
            self.assertIn(f'data-lens="{lens}"', HTML)

    def test_personal_principle_is_present(self):
        self.assertIn("relationships over inventory", HTML.lower())

    def test_work_specific_identity_is_absent(self):
        for forbidden in ("case2", "csc", "kubernetes", "gitops", "ci/cd", "openapi"):
            self.assertNotIn(forbidden, HTML.lower())


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify RED**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: failures for the new identity copy, four lens markers, and removal of the old work-history/technology content.

- [ ] **Step 3: Rewrite semantic page structure and copy**

Replace the current job-history-first content with:

- Hero eyebrow: `structured core / living edge`
- Hero statement: `I like finding structure in complexity — then seeing what can grow from it.`
- Supporting copy: `My background is in software engineering, but I tend to be drawn to relationships, boundaries, and the ways ideas and systems become coherent enough to evolve.`
- Ways-of-seeing section with four lens groups marked `data-lens="structure"`, `relationships`, `boundaries`, and `emergence`.
- Between-things heading: `The interesting part is usually between things.`
- Between-things prose: `I’m usually less interested in collecting more pieces than in understanding how they fit together. Once the relationships make sense, the whole becomes easier to explain, change, and sometimes turn into something unexpected.`
- Closing principle: `relationships over inventory`
- Public-edge note: `This is a small public edge of a much larger set of things I explore, build, and think about.`

Keep the GitHub link and `f3tknco` identity visible.

- [ ] **Step 4: Run tests to verify GREEN**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add index.html tests/test_homepage.py
git commit -m "feat: reframe homepage around personal identity"
```

---

### Task 2: Structured Core, Living Edge visual system

**Files:**
- Modify: `index.html`
- Modify: `tests/test_homepage.py`

**Interfaces:**
- Consumes: Task 1 semantic structure.
- Produces: a single coherent visual field where structure gradually gives way to branching possibility, with copper used as the living signal.

- [ ] **Step 1: Extend tests for visual-system hooks**

Add tests that assert the page contains:

```python
    def test_visual_system_hooks_exist(self):
        self.assertIn('class="structured-field"', HTML)
        self.assertIn('class="living-signal"', HTML)
        self.assertIn('class="possibility-branch"', HTML)
        self.assertIn('class="structure-grid"', HTML)

    def test_accessible_meaningful_svg_exists(self):
        self.assertIn('role="img"', HTML)
        self.assertIn('<title id="field-title">', HTML)
        self.assertIn('<desc id="field-desc">', HTML)
```

- [ ] **Step 2: Run tests to verify RED**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: the new visual hook tests fail.

- [ ] **Step 3: Implement the main visual composition**

In `index.html`:

- Use a two-column desktop hero with a restrained abstract SVG on the expressive side.
- Build a `structured-field` SVG or SVG-backed field that starts with aligned rules/nodes and then introduces one or two asymmetric branch paths near `Emergence`.
- Represent the four lenses as parts of one field, not four cards and not a linear process.
- Use `structure-grid` only in the structured side/region and fade it with mask/gradient or local opacity rather than covering the whole page uniformly.
- Use `living-signal` for the copper path and node accents.
- Use `possibility-branch` for a secondary path that departs from the main structure without implying required workflow.
- Preserve generous negative space and editorial typography; avoid bordered containers around each lens.
- Keep monospace annotations small and sparse.

- [ ] **Step 4: Add subtle native motion**

Add one optional CSS animation to the living signal, such as a slow dash drift or pulse with a cycle of at least 5 seconds. Do not animate large page regions.

Add a `@media (prefers-reduced-motion: reduce)` block that disables the motion and keeps every element visible.

- [ ] **Step 5: Run tests to verify GREEN**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add index.html tests/test_homepage.py
git commit -m "feat: add structured living visual system"
```

---

### Task 3: Responsive, accessibility, and final verification

**Files:**
- Modify: `index.html`
- Modify: `tests/test_homepage.py`

**Interfaces:**
- Consumes: the completed redesign.
- Produces: a responsive and accessible static page suitable for GitHub Pages.

- [ ] **Step 1: Add regression tests for implementation boundaries**

Extend the contract tests with:

```python
    def test_static_dependency_free_page(self):
        self.assertNotIn("<script src=", HTML.lower())
        self.assertNotIn("<link rel=\"stylesheet\" href=", HTML.lower())

    def test_reduced_motion_support_exists(self):
        self.assertIn("prefers-reduced-motion", HTML)

    def test_mobile_breakpoint_exists(self):
        self.assertRegex(HTML, r"@media\s*\(max-width:\s*7[0-9]{2}px\)")
```

- [ ] **Step 2: Run tests to verify RED if any boundary is missing**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: any missing dependency, reduced-motion, or mobile contract fails before final adjustments.

- [ ] **Step 3: Finish responsive and accessibility behavior**

Ensure:

- Desktop composition remains balanced at approximately 1120px max width.
- At widths below roughly 760px, the hero and field stack cleanly and text sizes remain readable.
- Meaningful SVG has title/description; decorative paths are hidden from assistive tech where appropriate.
- Focus-visible states exist for GitHub and identity links.
- Contrast stays readable on the warm-paper background.
- Motion disabling does not hide content.

- [ ] **Step 4: Run full contract tests**

Run: `python -m unittest tests/test_homepage.py -v`

Expected: all tests pass with zero failures.

- [ ] **Step 5: Parse and render the page locally**

Run a stdlib HTML parse check and render the page to an image or PDF using an available headless browser. Inspect at least one desktop and one narrow/mobile viewport. If a browser is unavailable, record that limitation explicitly rather than claiming visual verification.

- [ ] **Step 6: Compare branch against master**

Confirm the branch contains only the spec, plan, test, and homepage redesign changes expected for this work.

- [ ] **Step 7: Commit final polish**

```bash
git add index.html tests/test_homepage.py
git commit -m "test: verify responsive homepage redesign"
```
