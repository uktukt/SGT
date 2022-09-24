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

        


# text=input("First player, please enter a text ")
# space = " "
# asterisk="*"
# new_text=""

# for c in text:
#     if c == space:
#         new_text += space  
#     else: 
#         new_text += asterisk 

# print(new_text)

# while asterisk in new_text:
#     letter=input("Second player, please enter a letter ")
#    # letter="a"
#     for i, c in enumerate(text): # so enumarate returns index and value
#         if c == letter:
#            new_text=new_text[:i]+letter+new_text[i+1:]
#     print(new_text)

# #NOT WORKING
# print("GAME OVER")
# print(new_text)