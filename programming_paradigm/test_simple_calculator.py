# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # Addition
    def test_add_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_floats(self):
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)

    # Subtraction
    def test_subtract_integers(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(self.calc.subtract(4, 10), -6)

    # Multiplication
    def test_multiply_integers(self):
        self.assertEqual(self.calc.multiply(7, 6), 42)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(12345, 0), 0)

    # Division
    def test_divide_normal(self):
        self.assertEqual(self.calc.divide(7, 2), 3.5)

    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-9, 3), -3.0)

    def test_divide_zero_numerator(self):
        self.assertEqual(self.calc.divide(0, 5), 0.0)

    def test_divide_by_zero_raises(self):
        # Expect the standard ZeroDivisionError
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()