# Next Prime

from ex98 import is_prime


def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


def main():
    num = int(input('enter a number: '))
    print(f"the first prime number greater than {num} is {next_prime(num)}")


if __name__ == '__main__':
    main()
