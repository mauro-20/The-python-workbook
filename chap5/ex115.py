# List of Proper Divisors

# provides a list of the proper divisors of an integer
# @param n the number you want to find the divisors
# @return a list of the proper divisor
def divisor(n):
    div = []
    for d in range(1, n):
        if n % d == 0:
            div.append(d)
    return div


# test with input from user
def main():
    num = int(input('enter an integer: '))
    div = divisor(num)
    print('the divisor of {} are {}'.format(num, div))


if __name__ == '__main__':
    main()
