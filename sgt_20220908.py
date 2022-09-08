# Write a program that asks for and saves a username
username = input("what is your name? ")
# Ask a question about the user's age, using the username in the question.
age_now = input(f"what is {username} age " )
age_now = float(age_now)
# Shows in how many years the user will be 100 years old smile
age_after = print(f"{username} will be 100 years old after", round(100-age_now), "years")
# BONUS: 
# then you will need two additional lines:
# import datetime # let's talk about imports separately

import datetime
current_year = datetime.datetime.now().year

# currentYear = datetime.datetime.now (). yearLet the program also show the year when the user will be 100 years old.
print(f"{username} will be 100 years old in", current_year + round(100-age_now))
# It could use a variable with the current year.
# It would be even better to get the current year automatically