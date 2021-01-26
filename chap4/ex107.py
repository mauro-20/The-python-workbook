# Reduce a Fraction to Lowest Terms

# Compute the greatest common divisor of two integers
# @param num1 the first integer under consideration
# @param num2 the second integer under consideration
# @return the greatest common divisor of the integers
def gcd(num1, num2):
    divisor = min(num1, num2)
    while num1 % divisor or num2 % divisor:
        divisor -= 1
    return divisor


# Reduce a fraction to lowest terms
# @param numerator the integer numerator of the fraction
# @param denominator the integer denominator of the fraction (must be non-zero)
# @return the numerator and denominator of the reduced fraction
def fraction_lowest_terms(numerator: int, denominator: int):
    divisor = gcd(numerator, denominator)
    numerator = numerator/divisor
    denominator = denominator/divisor
    return numerator, denominator


# user test
def main():
    numerator = int(input('enter the numerator: '))
    denominator = int(input('enter the denominator: '))
    lowest_terms = fraction_lowest_terms(numerator, denominator)
    print('the lowest term of the fraction is {:g}/{:g}'.format(lowest_terms[0], lowest_terms[1]))


if __name__ == '__main__':
    main()
