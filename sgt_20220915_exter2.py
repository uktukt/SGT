# 2. Almost Hangman
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places,
# all other letters remain asterisks.
# Example:
# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***
# In principle, this is a good start to the game of hangman.
# https://en.wikipedia.org/wiki/Hangman_(game)

import string
text1 = input("enter text ")
text2 = text1.replace(text1, '*'*len(text1))
print(text2)
symbol = input("enter the symbol ")
replace_letter = text1.find(symbol)
index_letter = text1.index(symbol)

for i in text2:
    if index_letter == True:
        text3 = text2.replace('*', index_letter)
        print(text3)
