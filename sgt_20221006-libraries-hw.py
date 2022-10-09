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
import datetime

def dice_throws(nr_of_dice, nr_of_throws):
    number_of_dice = list(range(1,nr_of_dice+1))
    number_of_throws = list(range(1,nr_of_throws+1))

    current_date = datetime.datetime.now()
    random_list = []
    r_sum_list = []

    for j in range(0,nr_of_throws):
        for i in range(0, nr_of_dice):
            xx = random.randint(1, 6)
            random_list.append(xx)
         
    my_list = random_list
    start = 0
    end = nr_of_throws*nr_of_dice
    step = nr_of_dice
    random_sum = 0
    for v in range(start, end, step):
        x = v
        new = my_list[x:x+step]
        r_sum = sum(new)
        # print(new)
        # print(r_sum)
        r_sum_list.append(r_sum)

    fig, ax = plt.subplots()
    x = np.array(number_of_throws)
    x2 = np.arange(len(x))
    y = np.array(r_sum_list)
    ax.bar(x2, y, width=1)
    ax.set_xlabel('number of throws')
    ax.set_ylabel('sum of dices')
    fig.suptitle(current_date)
    plt.savefig('dice_throws.png')
    plt.show()
    # return random_list, number_of_throws, r_sum_list


print(dice_throws(2,100))

