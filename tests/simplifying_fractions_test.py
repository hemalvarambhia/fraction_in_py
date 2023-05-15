import unittest
import sys
import os
path = os.path.abspath("src")
sys.path.append(path)
from fraction import Fraction

class SimplifyingFractions(unittest.TestCase):
    def test_fraction_that_is_already_simplified(self):
        self.assert_equals(Fraction(3, 4), Fraction(3, 4))  # add assertion here

    def assert_equals(self, sum, expected):
        assert sum.numerator == expected.numerator, 'Numerator: expected: ' + str(expected) + ', but got ' + str(sum.numerator)
        assert sum.denominator == expected.denominator, 'Denominator: expected: ' + str(expected) + ', but got ' + str(sum.denominator)

if __name__ == '__main__':
    unittest.main()
