# Random License Plate

from random import randint


# this function generates a random plate number and it can be old style or new style
# the old style is 3 letters followed by 3 digits
# the new style is 4 digits followed by 3 letters
# @return a random plate number
def random_plate():
    plate = ''
    # randomly select a new or old style plate number
    style = randint(1, 2)
    # generate an old style plate number
    if style == 1:
        for i in range(3):
            plate += chr(randint(65, 90))
        for i in range(3):
            plate += str(randint(0, 9))
    # generate an new style plate number
    else:
        for i in range(4):
            plate += str(randint(0, 9))
        for i in range(3):
            plate += chr(randint(65, 90))
    return plate


# testing random_plate()
def main():
    print(random_plate())


if __name__ == '__main__':
    main()
