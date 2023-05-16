import math
class Fraction:
    def __init__(self, numerator, denominator=1):
        divisor = math.gcd(int(numerator), int(denominator))
        multiplier = -1 if denominator < 0 else 1
        self.numerator = multiplier * int(numerator / divisor)
        self.denominator = multiplier * int(denominator / divisor)

    def __add__(self, augend):
        lcm = math.lcm(augend.denominator, self.denominator)  # lowest common multiple
        return Fraction(self.numerator * lcm / self.denominator + augend.numerator * lcm / augend.denominator, lcm)
