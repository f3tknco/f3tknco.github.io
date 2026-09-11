from pathlib import Path
import re
import unittest

HTML = Path(__file__).parents[1].joinpath('index.html').read_text(encoding='utf-8')
LOWER = HTML.lower()
TEXT = re.sub(r'<[^>]+>', '', LOWER)


class HomepageContractTest(unittest.TestCase):
    def test_uses_established_public_concepts(self):
        for concept in ('software engineering', 'systems thinking', 'visual thinking', 'continuous learning'):
            self.assertIn(concept, LOWER)

    def test_hero_is_plain_language(self):
        self.assertIn('i like making complex ideas easier to understand', TEXT)

    def test_custom_framework_language_is_removed(self):
        for phrase in (
            'structured core',
            'living edge',
            'ways of seeing',
            'relationships over inventory',
            'public edge',
        ):
            self.assertNotIn(phrase, LOWER)

    def test_old_four_lens_framework_is_removed(self):
        self.assertNotIn('data-lens=', LOWER)
        self.assertNotIn('emergence', LOWER)

    def test_work_specific_identity_is_absent(self):
        for forbidden in ('case2', 'csc', 'kubernetes', 'gitops', 'ci/cd', 'openapi'):
            self.assertNotIn(forbidden, LOWER)

    def test_visual_remains_dependency_free_and_accessible(self):
        self.assertIn('class="systems-visual"', HTML)
        self.assertIn('role="img"', HTML)
        self.assertIn('<title id="visual-title">', HTML)
        self.assertIn('<desc id="visual-desc">', HTML)
        self.assertNotIn('<script src=', LOWER)
        self.assertNotIn('<link rel="stylesheet" href=', LOWER)

    def test_reduced_motion_support_exists(self):
        self.assertIn('prefers-reduced-motion', LOWER)

    def test_mobile_breakpoint_exists(self):
        self.assertRegex(HTML, r'@media\s*\(max-width:\s*7[0-9]{2}px\)')


if __name__ == '__main__':
    unittest.main()
