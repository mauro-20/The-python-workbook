# Is It a Valid Triangle?

# from 3 side length this function will compute if a triangle can be formed, returning a boolean value
# @param a first side
# @param b second side
# @param c third side
# @return boolean value
def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False


# function to test isTriangle()
def main():
    a = float(input('enter the first side: '))
    b = float(input('enter the second side: '))
    c = float(input('enter the third side: '))
    if is_triangle(a, b, c):
        print('is a triangle')
    else:
        print('is not a triangle')


if __name__ == '__main__':
    main()
