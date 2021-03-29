# Shuffling a Deck of Cards

from random import randrange


# Construct a standard deck of cards with 4 suits and 13 values per suit
# @return a list of cards, with each card represented by two characters
def create_deck():
    deck = []
    fig = ['T', 'J', 'Q', 'K', 'A']
    suits = ['s', 'h', 'd', 'c']
    for s in suits:
        for i in range(2, 10):
            el = str(i)+s
            deck.append(el)
        for f in fig:
            el = f+s
            deck.append(el)
    return deck


# Shuffle a deck of cards by modifying the deck passed to the function
# @param cards the list of cards to shuffle
# @return (None)
def shuffle(deck):
    for i in range(len(deck)):
        r = randrange(len(deck))
        temp = deck[r]
        deck[r] = deck[i]
        deck[i] = temp


# Display a deck of cards before and after it has been shuffled
def main():
    deck = create_deck()
    print(deck)
    shuffle(deck)
    print(deck)


if __name__ == '__main__':
    main()
