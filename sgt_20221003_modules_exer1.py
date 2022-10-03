
# 1. The Shuffle
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.

# you can use a loop or use something from the library

# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html

import random
import itertools

def get_shuffled_cards():
    var1 = ["A", "Jack", "Queen","King"] + list(range(2,11))
    var2 = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    cards = list(itertools.product(var1, var2))
    cards_random = random.sample(cards, len(var1)*len(var2))
    return cards_random

print(get_shuffled_cards())