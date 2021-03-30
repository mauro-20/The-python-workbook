# Play Bingo

from random import shuffle
from ex146 import card_generator, display_card
from ex147 import is_winning


def game():
    # generate the Bingo calls and shuffle them
    count = 1
    step = 15
    bingo = 'BINGO'
    calls = []
    for ch in bingo:
        for i in range(count, count + step):
            calls.append(ch + str(i))
        count += step
    shuffle(calls)

    # generate a Bingo card
    card = card_generator()
    # display_card(card)

    # check with how many tries the card is winning
    tries = 0
    for c_el in calls:
        for k in card:
            if c_el[0] == k:
                slice_c_el = int(c_el[1:])
                for i in range(len(card[k])):
                    if card[k][i] == slice_c_el:
                        card[k][i] = 0
                tries += 1
                if is_winning(card):
                    # display_card(card)
                    return tries


# display data of 1000 Bingo cards
def main():
    count = {}
    tries = []
    average_attempts = 0
    average_times = 0
    for i in range(1000):
        attempts = game()
        if attempts in count:
            count[attempts] += 1
        else:
            count[attempts] = 1

    for k in count:
        tries.append(k)
        if count[k] > average_times:
            average_attempts = k
            average_times = count[k]

    print('Number of calls on 1000 tries:\nMinimum: {}\nMaximum: {}\nAverage: {}'.format(min(tries), max(tries),
                                                                                         average_attempts))


if __name__ == '__main__':
    main()
