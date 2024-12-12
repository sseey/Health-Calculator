import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        # Teste un cas valide
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr_male(self):
        # Teste un cas valide pour un homme
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'male'), 1695.67, places=2)

    def test_calculate_bmr_female(self):
        # Teste un cas valide pour une femme
        self.assertAlmostEqual(calculate_bmr(175, 70, 30, 'female'), 1507.13, places=2)

if __name__ == '__main__':
    unittest.main()
