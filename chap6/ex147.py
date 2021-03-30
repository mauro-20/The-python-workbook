# Checking for a Winning Card

from ex146 import display_card


def is_winning(card):
    # check rows
    for i in range(5):
        check = 0
        for k in card:
            check += card[k][i]
        if check == 0:
            return True
    # check columns
    for k in card:
        if sum(card[k]) == 0:
            return True
    # check diagonal 1
    check = 0
    i = 0
    for k in card:
        check += card[k][i]
        i += 1
    if check == 0:
        return True
    # check diagonal 2
    check = 0
    i = 4
    for k in card:
        check += card[k][i]
        i -= 1
    if check == 0:
        return True
    return False


# Testing
if __name__ == '__main__':
    card1 = {'B': [5, 1, 0, 8, 0], 'I': [23, 0, 20, 0, 19], 'N': [0, 0, 42, 40, 0], 'G': [51, 0, 58, 53, 47], 'O': [0, 0, 66, 74, 64]}
    card2 = {'B': [0, 0, 0, 0, 0], 'I': [18, 28, 16, 19, 24], 'N': [41, 33, 35, 34, 37], 'G': [58, 52, 46, 50, 55], 'O': [62, 72, 70, 74, 65]}
    card3 = {'B': [5, 0, 12, 8, 6], 'I': [23, 0, 20, 27, 19], 'N': [32, 0, 42, 40, 43], 'G': [51, 0, 58, 53, 47], 'O': [62, 0, 66, 74, 64]}
    card4 = {'B': [0, 1, 12, 8, 6], 'I': [23, 0, 20, 27, 19], 'N': [32, 39, 0, 40, 43], 'G': [51, 50, 58, 0, 47], 'O': [62, 61, 66, 74, 0]}
    display_card(card1)
    print(is_winning(card1))
    print()
    display_card(card2)
    print(is_winning(card2))
    print()
    display_card(card3)
    print(is_winning(card3))
    print()
    display_card(card4)
    print(is_winning(card4))
