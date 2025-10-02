import math
import sys


if __name__ == '__main__':
    x = float(input("Введите аргумент функции x:  "))

    e = 1e-10
    Sin, a = 0, x # a - член ряда
    n = 0

    while abs(a) > e:
        Sin += a
        n += 1
        a = ((-1) ** n) * (x ** (2 * n + 1)) / ((2 * n + 1) * math.factorial(2 * n + 1))

    print(f"Sin({x}) = {Sin}")
