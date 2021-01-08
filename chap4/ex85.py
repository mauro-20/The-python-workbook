# Compute the Hypotenuse

import math


def hypotenuse(a, b):
    c = math.sqrt(a ** 2 + b ** 2)
    return c


def main():
    a = float(input('enter the first cachet: '))
    b = float(input('enter the second cachet: '))
    return print(hypotenuse(a, b))


if __name__ == "__main__":
    main()
