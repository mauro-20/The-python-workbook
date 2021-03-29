# Random Lottery Numbers

from random import randint


# generates a list of 6 lottery numbers (from 1 to 49)
def rdm_lottery_numbers():
    res = []
    while len(res) < 6:
        num = randint(1, 49)
        if num not in res:
            res.append(num)
    res.sort()
    return res


print(rdm_lottery_numbers())
