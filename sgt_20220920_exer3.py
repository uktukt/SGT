# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.

# sentence = input("enter a sentence ")
import string

sentence = "Alus kauss mans"
separated = sentence.lower().split()
sentence_reversed = []
for i in separated: 
    sentence_reversed.append(i[::-1])

sentence_again = " ". join(sentence_reversed)
print(sentence_again)