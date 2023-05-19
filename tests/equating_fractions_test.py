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

        assert f != g


if __name__ == '__main__':
    unittest.main()
