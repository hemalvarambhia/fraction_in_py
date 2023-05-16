import unittest

import pytest
from fraction import Fraction

class SimplifyingFractions(unittest.TestCase):
    def test_fraction_that_is_already_simplified(self):
        self.assert_equals(Fraction(3, 4), Fraction(3, 4))  # add assertion here

    def test_simplifying_a_fraction_with_a_common_divisor(self):
        self.assert_equals(Fraction(5, 10), Fraction(1, 2))

    def test_simplifying_a_fraction_with_a_negative_numerator(self):
        self.assert_equals(Fraction(-5, 10), Fraction(-1, 2))

    def assert_equals(self, sum, expected):
        assert sum.numerator == expected.numerator, 'Numerator: expected: ' + str(expected) + ', but got ' + str(sum.numerator)
        assert sum.denominator == expected.denominator, 'Denominator: expected: ' + str(expected) + ', but got ' + str(sum.denominator)

if __name__ == '__main__':
    unittest.main()
