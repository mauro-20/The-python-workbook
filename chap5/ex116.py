# Perfect Numbers

from ex115 import divisor


def is_perfect(n):
    div = divisor(n)
    if sum(div) == n:
        return True
    return False


def main():
    for num in range(10000):
        if is_perfect(num):
            print(num)


if __name__ == '__main__':
    main()
