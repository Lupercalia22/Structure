import math

class MyFunc:
    def __init__(self, numerator: int, denominator: int):
        g = math.gcd(numerator, denominator)

        self.numerator = numerator // g
        self.denominator = denominator // g

    @staticmethod
    def gcd(a, b):
        return b if not b else gcd(b, a % b)

my_func = MyFunc(9, 9)
print("Числитель:", my_func.numerator)
print("Знаменатель:", my_func.denominator, end='\n\n')

from fractions import Fraction as F

num = F("0/9")
print(f"Числитель: {num.numerator}", f"Знаменатель: {num.denominator}", sep='\n')