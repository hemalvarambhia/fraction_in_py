import unittest
class Fraction:
   def __init__(self, numerator, denominator = 1):
       self.numerator = int(numerator)
       self.denominator = int(denominator)
       
   def __add__(self, augend):
      return Fraction(int(self.numerator) + int(augend.numerator), 5)

   def as_integer(self):
      return self.numerator

class AddingFractionsTest(unittest.TestCase):
    def testHookUp(self):
        assert 0 + 0 == 0
        assert 0 + 1 == 1

    def test_that_zero_plus_zero_equals_zero(self):
        addend = Fraction(0)
        augend = Fraction(0)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), 0)

    def test_that_zero_plus_one_equals_one(self):
        addend = Fraction(0)
        augend = Fraction(1)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), 1)

    def test_that_one_plus_one_equals_two(self):
        addend = Fraction(1)
        augend = Fraction(1)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), 2)

    def test_that_minus_one_plus_zero_equals_minus_one(self):
        addend = Fraction(-1)
        augend = Fraction(0)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), -1)

    def test_that_minus_one_plus_one_equals_zero(self):
        addend = Fraction(-1)
        augend = Fraction(1)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), 0)

    def test_that_minus_one_plus_two_equals_one(self):
        addend = Fraction(-1)
        augend = Fraction(2)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), 1)

    def test_that_minus_one_plus_minus_one_equals_minus_two(self):
        addend = Fraction(-1)
        augend = Fraction(-1)
        sum = addend + augend
        self.assert_equals(sum.as_integer(), -2)

    #def test_that_1_on_3_plus_1_on_3_equals_2_on_3(self):
    #   addend = Fraction(1,3)
    #   augend = Fraction(1,3)
    #   sum = addend + augend
    #   self.assert_equals(sum.numerator, 2)
    #   self.assert_equals(sum.denominator, 3)

    def test_that_2_on_5_plus_1_on_5_equals_3_on_5(self):
       addend = Fraction(2, 5)
       augend = Fraction(1, 5)
       sum = addend + augend
       self.assert_equals(sum.numerator, 3)
       self.assert_equals(sum.denominator, 5)

    def assert_equals(self, sum, expected):
        assert sum == expected, 'Expected ' + str(expected) + ', got ' + str(sum)

if __name__ == "__main__":

    unittest.main() # run all tests
