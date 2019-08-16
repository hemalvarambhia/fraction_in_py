import unittest
class Fraction:
   def __init__(self, numerator):
       pass

   def plus(self, augend):
       return 0

class AddingFractionsTest(unittest.TestCase):
    def testHookUp(self):
        assert 0 + 0 == 0

    def test_that_zero_plus_zero_equals_zero(self):
        addend = Fraction(0)
        augend = Fraction(0)
        sum = addend.plus(augend)
        assert sum == 0, 'Expected 0, got ' + str(sum)

if __name__ == "__main__":

    unittest.main() # run all tests
