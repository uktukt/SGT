import camelcase
c = camelcase.CamelCase()
text = "hello world it's a test"
print(c.hump(text)) 

# create a function that returns a list of random dice throws
# it should have two parameters
# - number of dice in each throw, default 4
# - number of throws, default 100

# even better would be a another function to which you give the list of dice throws and it 
# plots the histogram
# this function would have two parameters
# - the list of dice throws - no default
# - the name of the file to save the plot to - default - empty string
# if the file name is empty string, the plot should be shown on the screen

# use the first function to create a list of 1000 dice throws with 6 dice in each throw
# pass the result to 2nd function to plot the histogram and save it to a file
# BONUS: file name should have current date and time in it

# ideally you would then run them from main guard
# which means this file would be a module, that can be imported


import random
import itertools
import matplotlib.pyplot as plt
import numpy as np

def dice_throws(nr_of_dice, nr_of_throws):
    number_of_dice = list(range(1,nr_of_dice+1))
    number_of_throws = list(range(1,nr_of_throws+1))
    # dice_nr = list(range(1,7))
    # comb = list(itertools.product(dice_nr))
    # comb_random = random.sample(comb, len(number_of_throws+number_of_dice))

    random_list = []
    for i in range(0, nr_of_dice + nr_of_throws):
        xx = random.randint(1, 6)
        random_list.append(xx)

    x = np.array([number_of_dice + number_of_throws])
    y = np.array([random_list])
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=1.0)
    plt.show()
    return random_list, number_of_dice + number_of_throws


print(dice_throws(2,2))
