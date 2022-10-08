# 2. Deck - probably for homework, see how far you get

# write a class Deck with the following attributes(variables)
# available - contains list of card tuples that can be used
# spent - contains list of card tuples that have been used
# there should be following methods:

# constructor (__init__) method
# initializes available with full 52 card list of tuples
# initializes spent with empty list
# shuffle(self):
# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class

import random
import itertools
import string

def get_shuffled_cards():
    var1 = ["A", "Jack", "Queen","King"] + list(range(2,11))
    var2 = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    cards = list(itertools.product(var1, var2))
    cards_random = random.sample(cards, len(cards))
    return cards_random

# print(get_shuffled_cards())

class Deck:
    var1 = ["A", "Jack", "Queen","King"] + list(range(2,11))
    var2 = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]

    def __init__(self):
        self.available = list(itertools.product(self.var1, self.var2))
        self.shuffle()
        self.spent = []

    def __str__(self):
        return f"Available cards: {self.available}\nSpent cards: {self.spent}"

    def shuffle(self):
        self.available = random.sample(self.available, len(self.available))
        return self

    def get_cards(self, count=1):
        cards = self.available[:count]
        self.spent.extend(cards)
        self.available = self.available[count:]
        return cards


if __name__ == "__main__":
    print(get_shuffled_cards())
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck)
    # print(my_deck.get_cards(5))
    print(my_deck.get_cards(1))
    print(my_deck)