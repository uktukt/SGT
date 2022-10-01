# 3. Is there a pangram?

# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')

# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise


# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram

# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a

import string

def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    text_cleaned = text.lower().replace(" ", "")
    if set(text_cleaned) == set(alphabet):
        return print("it is pangram")
    return print("it is not a pangram")
    
is_pangram("Abcdef ghijklmnopqrstuvwxy")