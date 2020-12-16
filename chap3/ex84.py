# Coin Flip Simulation

import random

flip_average = 0

# repeat 10 times
for i in range(10):

    # initialization
    cons_H = 0
    cons_T = 0
    flip_count = 0

    # flipping the coin for 3 consecutive times
    while cons_H < 3 and cons_T < 3:
        coin = random.randint(1, 2)
        if coin == 1:
            print('H', end='')
            cons_H += 1
            if cons_T != 0:
                cons_T = 0
        else:
            print('T', end='')
            cons_T += 1
            if cons_H != 0:
                cons_H = 0
        flip_count += 1
    flip_average += flip_count
    print(' ({} flips)'.format(flip_count))

flip_average = flip_average/10
print('on average {} flips were needed'.format(flip_average))
