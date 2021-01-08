# The Twelve Days of Christmas
from ex89 import int_to_ordinal


def verse(num):
    print(f"On the {int_to_ordinal(num)} day of Christmas\nmy true love sent to me:")
    if num >= 12:
        print('Twelve drummers drumming')
    if num >= 11:
        print('Eleven pipers piping')
    if num >= 10:
        print('Ten lords a-leaping')
    if num >= 9:
        print('Nine ladies dancing')
    if num >= 8:
        print('Eight maids a-milking')
    if num >= 7:
        print('Seven swans a-swimming')
    if num >= 6:
        print('Six geese a-laying')
    if num >= 5:
        print('Five gold rings')
    if num >= 4:
        print('Four calling birds')
    if num >= 3:
        print('Three french hens')
    if num >= 2:
        print('Two turtle doves')
    if num >= 1:
        if num > 1:
            print('And a', end=' ')
        else:
            print('A', end=' ')
        print('partridge in a pear tree.\n')


def the_twelve_days_of_christmas():
    for i in range(1, 13):
        verse(i)


the_twelve_days_of_christmas()
