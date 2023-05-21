import unittest
from fraction import Fraction

class SimplifyingFractions(unittest.TestCase):
    def test_fraction_that_is_already_simplified(self):
        sum1 = Fraction(3, 4)
        expected = Fraction(3, 4)
        self.assertEqual(sum1, expected)

    def test_simplifying_a_fraction_with_a_common_divisor(self):
        sum1 = Fraction(5, 10)
        expected = Fraction(1, 2)
        self.assertEqual(sum1, expected)

    def test_simplifying_a_fraction_with_a_negative_numerator(self):
        sum1 = Fraction(-5, 10)
        expected = Fraction(-1, 2)
        self.assertEqual(sum1, expected)

    def test_simplifying_a_fraction_with_a_negative_numerator(self):
        sum1 = Fraction(-2, -6)
        expected = Fraction(1, 3)
        self.assertEqual(sum1, expected)


if __name__ == '__main__':
    unittest.main()
