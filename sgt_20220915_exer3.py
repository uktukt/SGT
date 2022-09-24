# 3. Text conversion

# Write a program for text conversion

# Save user input

# Print the entered text without changes
# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good
# Examples:
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good 
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator.
# Also slice syntax will be useful.
# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?

import string

# text = input("enter a text here ")
text = "he is not good"
term1 = "not"
term2 = "so"


if text.find(term1):
    text_good = text.replace("not bad", "good")
    if text_good.find(term2):
         text_good_so = text_good.replace("not so bad", "good")
         print(text_good_so)
    else:
        print(text_good)
else:
    print(text)
