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

    def test_visual_system_hooks_exist(self):
        self.assertIn('class="structured-field"', HTML)
        self.assertIn('class="living-signal"', HTML)
        self.assertIn('class="possibility-branch"', HTML)
        self.assertIn('class="structure-grid"', HTML)

    def test_accessible_meaningful_svg_exists(self):
        self.assertIn('role="img"', HTML)
        self.assertIn('<title id="field-title">', HTML)
        self.assertIn('<desc id="field-desc">', HTML)

    def test_static_dependency_free_page(self):
        self.assertNotIn("<script src=", HTML.lower())
        self.assertNotIn("<link rel=\"stylesheet\" href=", HTML.lower())

    def test_reduced_motion_support_exists(self):
        self.assertIn("prefers-reduced-motion", HTML)

    def test_mobile_breakpoint_exists(self):
        self.assertRegex(HTML, r"@media\s*\(max-width:\s*7[0-9]{2}px\)")


if __name__ == "__main__":
    unittest.main()
