import unittest
from scripts.validate_skills import ROOT, validate_skill

class ValidationTests(unittest.TestCase):
    def test_all_skills_validate(self):
        errors=[]
        for path in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()): errors.extend(validate_skill(path))
        self.assertEqual(errors, [])
    def test_expected_skill_count(self):
        self.assertEqual(len([p for p in (ROOT / "skills").iterdir() if p.is_dir()]), 30)

if __name__ == "__main__": unittest.main()
