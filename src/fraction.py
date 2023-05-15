import math
class Fraction:
    def __init__(self, numerator, denominator=1):
        divisor = math.gcd(int(numerator), int(denominator))
        self.numerator = int(numerator / divisor)
        self.denominator = int(denominator / divisor)

    def __add__(self, augend):
        lcm = math.lcm(augend.denominator, self.denominator)  # lowest common multiple
        return Fraction(self.numerator * lcm / self.denominator + augend.numerator * lcm / augend.denominator, lcm)
