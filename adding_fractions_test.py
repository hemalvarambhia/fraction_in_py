import unittest
class Fraction:
   def __init__(self, numerator):
       self.numerator = int(numerator)
       pass

   def __add__(self, augend):
      return int(self.numerator) + int(augend.numerator)

class AddingFractionsTest(unittest.TestCase):
    def testHookUp(self):
        assert 0 + 0 == 0
        assert 0 + 1 == 1

    def test_that_zero_plus_zero_equals_zero(self):
        addend = Fraction(0)
        augend = Fraction(0)
        sum = addend + augend
        expected = 0
        self.assert_equals(sum, expected)

    def test_that_zero_plus_one_equals_one(self):
        addend = Fraction(0)
        augend = Fraction(1)
        sum = addend + augend
        expected = 1
        self.assert_equals(sum, expected)

    def test_that_one_plus_one_equals_two(self):
        addend = Fraction(1)
        augend = Fraction(1)
        sum = addend + augend
        expected = 2
        self.assert_equals(sum, expected)

    def test_that_minus_one_plus_zero_equals_minus_one(self):
        addend = Fraction(-1)
        augend = Fraction(0)
        sum = addend + augend
        assert sum == -1, ' Expected -1, got ' + str(sum)

    def test_that_minus_one_plus_one_equals_zero(self):
        addend = Fraction(-1)
        augend = Fraction(1)
        sum = addend + augend
        assert sum == 0, ' Expected 0, got ' + str(sum)

    def test_that_minus_one_plus_two_equals_one(self):
        addend = Fraction(-1)
        augend = Fraction(2)
        sum = addend + augend
        assert sum == 1, ' Expected 1, got ' + str(sum)

    def test_that_minus_one_plus_minus_one_equals_minus_two(self):
        addend = Fraction(-1)
        augend = Fraction(-1)
        sum = addend + augend
        assert sum == -2, ' Expected -2, got ' + str(sum)

    def assert_equals(self, sum, expected):
        assert sum == expected, 'Expected ' + str(expected) + ', got ' + str(sum)

if __name__ == "__main__":

    unittest.main() # run all tests
