class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __add__(self, augend):
        lcm = math.lcm(augend.denominator, self.denominator)  # lowest common multiple
        return Fraction(self.numerator * lcm / self.denominator + augend.numerator * lcm / augend.denominator, lcm)
