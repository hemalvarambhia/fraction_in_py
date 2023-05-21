import unittest
from fraction import Fraction

class SimplifyingFractions(unittest.TestCase):
    def test_fraction_that_is_already_simplified(self):
        self.assert_equals(Fraction(3, 4), Fraction(3, 4))  # add assertion here

    def test_simplifying_a_fraction_with_a_common_divisor(self):
        self.assert_equals(Fraction(5, 10), Fraction(1, 2))

    def test_simplifying_a_fraction_with_a_negative_numerator(self):
        self.assert_equals(Fraction(-5, 10), Fraction(-1, 2))

    def test_simplifying_a_fraction_with_a_negative_numerator(self):
        self.assert_equals(Fraction(-2, -6), Fraction(1, 3))

    def assert_equals(self, sum, expected):
        self.assertEqual(sum, expected)

if __name__ == '__main__':
    unittest.main()
