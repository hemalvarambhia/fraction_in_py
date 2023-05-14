import unittest
import math
class Fraction:
   def __init__(self, numerator, denominator = 1):
       self.numerator = int(numerator)
       self.denominator = int(denominator)
       
   def __add__(self, augend):
       lcm = math.lcm(augend.denominator, self.denominator)  # lowest common multiple
       return Fraction(self.numerator * lcm / self.denominator + augend.numerator * lcm / augend.denominator,lcm)


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

    def test_that_1_on_3_plus_1_on_3_equals_2_on_3(self):
       addend = Fraction(1, 3)
       augend = Fraction(1, 3)

       sum = addend + augend

       self.assert_equals(sum, Fraction(2, 3))

    def test_that_2_on_3_plus_2_on_3_equals_4_on_3(self):
       addend = Fraction(2, 3)
       augend = Fraction(2, 3)

       sum = addend + augend

       self.assert_equals(sum.numerator, 4)
       self.assert_equals(sum.denominator, 3)
       self.assert_equals(sum, Fraction(4, 3))

    def test_that_2_on_5_plus_1_on_5_equals_3_on_5(self):
       addend = Fraction(2, 5)
       augend = Fraction(1, 5)
       sum = addend + augend
       self.assert_equals(sum.numerator, 3)
       self.assert_equals(sum.denominator, 5)

    def test_that_1_on_4_plus_1_on_3_equals_7_on_12(self):
       addend = Fraction(1, 4)
       augend = Fraction(1, 3)
       sum = addend + augend
       self.assert_equals(sum.numerator, 7)
       self.assert_equals(sum.denominator, 12)

       # This test fails ^^^
       # Next step is to add Fractions that do not have the same denominator

    def test_that_1_on_3_plus_1_on_5_equals_8_on_15(self):
        addend = Fraction(1, 3)
        augend = Fraction(1, 5)
        sum = addend + augend
        self.assert_equals(sum.numerator, 8)
        self.assert_equals(sum.denominator, 15)

    def test_that_1_on_2_plus_1_on_4_equals_3_on_4(self):
        addend = Fraction(1, 2)
        augend = Fraction(1, 4)
        sum = addend + augend
        self.assert_equals(sum.numerator, 3)
        self.assert_equals(sum.denominator, 4)

    def test_that_2_over_21_plus_1_over_6_is_11_over_42(self):
        addend = Fraction(2, 21)
        augend = Fraction(1, 6)
        sum = addend + augend
        self.assert_equals(sum.numerator, 11)
        self.assert_equals(sum.denominator, 42)

    def assert_equals(self, sum, expected):
        if isinstance(sum, int):
            assert sum == expected, 'Expected ' + str(expected) + ', got ' + str(sum)
        else:
            assert sum.numerator == expected.numerator, 'Numerator: expected: ' + str(expected) + ', but got ' + str(sum.numerator)
            assert sum.denominator == expected.denominator, 'Denominator: expected: ' + str(expected) + ', but got ' + str(sum.denominator)

if __name__ == "__main__":

    unittest.main() # run all tests
