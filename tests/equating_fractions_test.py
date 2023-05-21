import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_reflexivity(self):
        f = Fraction(1, 2)

        self.assertEqual(f, f)

    def test_symmetry(self):
        f = Fraction(3, 7)
        g = Fraction(3, 7)

        self.assertEqual(f, g)
        self.assertEqual(g, f)

    def test_fractions_with_different_numerators_are_unequal(self):
        f = Fraction(4, 5)
        g = Fraction(3, 5)

        self.assertNotEqual(f, g)

    def test_fractions_with_different_denominators_are_unequal(self):
        f = Fraction(8, 13)
        g = Fraction(8, 99)

        self.assertNotEqual(f, g, "Expected {} not to equal {}".format(f, g))

    def test_fractions_are_not_equal_to_objects_of_a_different_type(self):
        self.assertNotEqual(Fraction(8, 5), "string")


if __name__ == "__main__":
    unittest.main()
