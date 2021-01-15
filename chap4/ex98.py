# Is a Number Prime?

# this function determine if a number is prime
# @param num is the number to be checked
# @return True if the number is prime, False otherwise
def is_prime(num: int):
    # check that the number is greater than 1
    if num <= 1:
        return False

    for i in range(2, num):
        # check if the number is divisible by other numbers
        if num % i == 0:
            return False
    return True


# test is_prime()
def main():
    num = int(input('enter a number: '))
    if is_prime(num):
        print("it's a prime number!")
    else:
        print("sorry that's not a prime number")


if __name__ == '__main__':
    main()
