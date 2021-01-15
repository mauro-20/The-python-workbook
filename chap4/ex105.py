# Arbitrary Base Conversions

from ex104 import int_to_hex, hex_to_int


# Convert a number from base 10 to base new base
# @param number the base 10 number to convert
# @param new_base the base to convert to
# @return the string of digits in new base
def decimal_to_n(decimal: int, new_base: int):
    out = ''
    while decimal > 0:
        out = str(int_to_hex(decimal % new_base)) + out
        decimal = decimal // new_base
    return out


# Convert a number from base 'base' to base 10
# @param number the base 'base' number, stored in a string
# @param base the base of the number to convert
# @return the base 10 number
def n_to_decimal(number: str, base: int):
    decimal = 0
    for i in range(len(number)):
        decimal = decimal * base
        decimal = decimal + hex_to_int(number[i])
    return decimal


# Convert a number between two arbitrary bases
def main():
    number = input('enter a number: ')
    base = int(input('and its base: '))
    new_base = int(input('enter the base you want to convert to: '))
    if base == 10:
        new_number = decimal_to_n(int(number), new_base)
        print('the converted number in base {} is {}'.format(new_base, new_number))
    else:
        new_number = decimal_to_n(n_to_decimal(number, base), new_base)
        print('the converted number in base {} is {}'.format(new_base, new_number))


if __name__ == '__main__':
    main()
