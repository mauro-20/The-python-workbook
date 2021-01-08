# Median of Three Values

# @param a the first value
# @param b the second value
# @param c the third value
# @return the median of values a,b and c
def median_of_three(a, b, c):
    if a > b > c or c > b > a:
        return b
    elif b > c > a or a > c > b:
        return c
    else:
        return a


def main():
    a = float(input('enter the first number: '))
    b = float(input('enter the second number: '))
    c = float(input('enter the third number: '))
    median = median_of_three(a, b, c)
    print(f"the median number is {median}")


if __name__ == '__main__':
    main()
