# Dealing Hands of Cards

from ex125 import create_deck, shuffle


# deals a certain number of cards per hand of a certain deck
# @param num_hands is the number of hands we want to play
# @param num_card_per_hand is the number of cards per hand
# @param deck is the deck to use
# @return a list that contains lists of all the hands that were dealt
def deal(num_hands, num_card_per_hand, deck):
    hands = []
    hand = []
    for i in range(num_hands):
        n = 0
        while n < num_card_per_hand:
            hand.append(deck.pop(0))
            n += 1
        hands.append(hand)
        hand = []
    return hands


# display the cards of 5 hands with 5 cards per hand and the rest of the deck
def main():
    deck = create_deck()
    shuffle(deck)
    print(deal(5, 5, deck))
    print(deck)


if __name__ == '__main__':
    main()
