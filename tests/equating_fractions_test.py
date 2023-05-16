import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_reflexivity(self):
        f = Fraction(1, 2)

        self.assertEqual(f, f)


if __name__ == '__main__':
    unittest.main()
