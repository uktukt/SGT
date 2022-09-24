# 1. Confusion
# The user enters a name.
# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ",
# then the first name of the user name then "?"
# Example:
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

import string

name = input("enter your name ")
name_reversed = name[::-1]
name_cap = name_reversed.capitalize()
add_text = ",a thorough mess is it not "
print(name_cap + add_text + name[0] + "?")