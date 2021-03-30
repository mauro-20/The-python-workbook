# Two Dice Simulation
from random import randint


# returns the total of a 2 dice roll
def dice_roll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    return dice1 + dice2


def main():
    expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36,
                11: 2/36, 12: 1/36}
    count = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    # roll the dice
    for i in range(1000):
        total = dice_roll()
        if total in count:
            count[total] += 1
   
    print('Total Simulated  Expected')
    for k in count:
        print('{:5d}{:10.2f}{:10.2f}'.format(k, count[k]/10, expected[k]*100))


main()
