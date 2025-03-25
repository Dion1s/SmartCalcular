import unittest
from src.calculator_logic import (
    calculate_factorial, calculate_sin, calculate_cos, calculate_tan,
    calculate_cot, calculate_square_root, calculate_third_root,
    change_sign, calculate_percent, calculate_expression
)

class TestCalculatorLogic(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(calculate_factorial("5"), "120")
        self.assertEqual(calculate_factorial("0"), "1")

    def test_trigonometric_functions(self):
        self.assertAlmostEqual(float(calculate_sin("90")), 1.0, places=5)
        self.assertAlmostEqual(float(calculate_cos("0")), 1.0, places=5)
        self.assertAlmostEqual(float(calculate_tan("45")), 1.0, places=5)
        self.assertAlmostEqual(float(calculate_cot("45")), 1.0, places=5)

    def test_square_root(self):
        self.assertEqual(calculate_square_root("4"), "2.0")
        self.assertEqual(calculate_square_root("-4"), "ERROR")

    def test_third_root(self):
        self.assertEqual(calculate_third_root("8"), "2.0")
        self.assertEqual(calculate_third_root("-8"), "ERROR")

    def test_sign_change(self):
        self.assertEqual(change_sign("5"), "-5")
        self.assertEqual(change_sign("-5"), "5")

    def test_percent(self):
        self.assertEqual(calculate_percent("50"), "0.5")

    def test_expression(self):
        self.assertEqual(calculate_expression("2+2"), "4")
        self.assertEqual(calculate_expression("10/2"), "5.0")

if __name__ == '__main__':
    unittest.main() 