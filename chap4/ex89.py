# Convert an Integer to Its Ordinal Number

def int_to_ordinal(int):
    if int == 1:
        return 'first'
    elif int == 2:
        return 'second'
    elif int == 3:
        return 'third'
    elif int == 4:
        return 'fourth'
    elif int == 5:
        return 'fifth'
    elif int == 6:
        return 'sixth'
    elif int == 7:
        return 'seventh'
    elif int == 8:
        return 'eighth'
    elif int == 9:
        return 'ninth'
    elif int == 10:
        return 'tenth'
    elif int == 11:
        return 'eleventh'
    elif int == 12:
        return 'twelfth'
    else:
        return ''


def main():
    for i in range(1, 13):
        print(f"{i} = {int_to_ordinal(i)}")


if __name__ == '__main__':
    main()
