import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_reflexivity(self):
        f = Fraction(1, 2)

        self.assertEqual(f, f)
    def test_symmetry(self):
        f = Fraction(3, 7)
        g = Fraction(3, 7)

        self.assertEquals(f, g)
        self.assertEquals(g, f)


if __name__ == '__main__':
    unittest.main()
