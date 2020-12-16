# Binary to Decimal

binary = input('enter a binary number: ')

decimal = 0
exp = len(binary)-1
for i in binary:
    decimal += int(i)*2**exp
    exp -= 1

print('the equivalent decimal number is', decimal)
