import unittest
from fraction import Fraction


class AddingFractionsTest(unittest.TestCase):
    def testHookUp(self):
        assert 0 + 0 == 0
        assert 0 + 1 == 1

    def test_that_zero_plus_zero_equals_zero(self):
        addend = Fraction(0)
        augend = Fraction(0)

        sum = addend + augend

        self.assert_equals(sum, Fraction(0))

    def test_that_zero_plus_one_equals_one(self):
        addend = Fraction(0)
        augend = Fraction(1)

        sum = addend + augend

        self.assert_equals(sum, Fraction(1))

    def test_that_one_plus_one_equals_two(self):
        addend = Fraction(1)
        augend = Fraction(1)

        sum = addend + augend

        self.assert_equals(sum, Fraction(2))

    def test_that_minus_one_plus_zero_equals_minus_one(self):
        addend = Fraction(-1)
        augend = Fraction(0)

        sum = addend + augend

        self.assert_equals(sum, Fraction(-1))

    def test_that_minus_one_plus_one_equals_zero(self):
        addend = Fraction(-1)
        augend = Fraction(1)

        sum = addend + augend

        self.assert_equals(sum, Fraction(0))

    def test_that_minus_one_plus_two_equals_one(self):
        addend = Fraction(-1)
        augend = Fraction(2)

        sum = addend + augend

        self.assert_equals(sum, Fraction(1))

    def test_that_minus_one_plus_minus_one_equals_minus_two(self):
        addend = Fraction(-1)
        augend = Fraction(-1)

        sum = addend + augend

        self.assert_equals(sum, Fraction(-2))

    def test_that_1_on_3_plus_1_on_3_equals_2_on_3(self):
        addend = Fraction(1, 3)
        augend = Fraction(1, 3)

        sum = addend + augend

        self.assert_equals(sum, Fraction(2, 3))

    def test_that_2_on_3_plus_2_on_3_equals_4_on_3(self):
        addend = Fraction(2, 3)
        augend = Fraction(2, 3)

        sum = addend + augend

        self.assert_equals(sum, Fraction(4, 3))

    def test_that_2_on_5_plus_1_on_5_equals_3_on_5(self):
        addend = Fraction(2, 5)
        augend = Fraction(1, 5)

        sum = addend + augend

        self.assert_equals(sum, Fraction(3, 5))

    def test_that_1_on_4_plus_1_on_3_equals_7_on_12(self):
        addend = Fraction(1, 4)
        augend = Fraction(1, 3)

        sum = addend + augend

        self.assert_equals(sum, Fraction(7, 12))

    def test_that_1_on_3_plus_1_on_5_equals_8_on_15(self):
        addend = Fraction(1, 3)
        augend = Fraction(1, 5)

        sum = addend + augend

        self.assert_equals(sum, Fraction(8, 15))

    def test_that_1_on_2_plus_1_on_4_equals_3_on_4(self):
        addend = Fraction(1, 2)
        augend = Fraction(1, 4)

        sum = addend + augend

        self.assert_equals(sum, Fraction(3, 4))

    def test_that_2_over_21_plus_1_over_6_is_11_over_42(self):
        addend = Fraction(2, 21)
        augend = Fraction(1, 6)

        sum = addend + augend

        self.assert_equals(sum, Fraction(11, 42))

    def assert_equals(self, sum, expected):
       self.assertEqual(sum, expected)


if __name__ == "__main__":
    unittest.main()  # run all tests
