import unittest
class Fraction:
   def __init__(self, numerator):
       self.numerator = int(numerator)
       pass
       
   def plus(self, augend):
       return int(self.numerator) + int(augend.numerator)

   def __add__(self, augend):
      return self.plus(augend) 

class AddingFractionsTest(unittest.TestCase):
    def testHookUp(self):
        assert 0 + 0 == 0
        assert 0 + 1 == 1

    def test_that_zero_plus_zero_equals_zero(self):
        addend = Fraction(0)
        augend = Fraction(0)
        sum = addend + augend
        assert sum == 0, 'Expected 0, got ' + str(sum)

    def test_that_zero_plus_one_equals_one(self):
        addend = Fraction(0)
        augend = Fraction(1)
        sum = addend + augend
        assert sum == 1, 'Expected 1, got ' + str(sum)

    def test_that_one_plus_one_equals_two(self):
        addend = Fraction(1)
        augend = Fraction(1)
        sum = addend + augend
        assert sum == 2, 'Expected 1, got ' + str(sum)

    def test_that_minus_one_plus_zero_equals_minus_one(self): 
        addend = Fraction(-1)
        augend = Fraction(0)
        sum = addend + augend
        assert sum == -1, ' Expected -1, got ' + str(sum)
      

      

if __name__ == "__main__":

    unittest.main() # run all tests
