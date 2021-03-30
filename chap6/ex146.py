# Create a Bingo Card

from random import randrange


def generate(dic, key, start, stop):
    while len(dic[key]) < 5:
        num = randrange(start, stop)
        if num not in dic[key]:
            dic[key].append(num)


def card_generator():
    col = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}
    generate(col, 'B', 1, 15)
    generate(col, 'I', 16, 30)
    generate(col, 'N', 31, 45)
    generate(col, 'G', 46, 60)
    generate(col, 'O', 61, 75)
    return col


def display_card(card):
    print('  B', '  I', '  N', '  G', '  O')
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%3d " % card[letter][i], end="")
        print()


