#  2. Christmas tree 

# Ask user to enter the height of the tree 
# Then Print the tree: Ex. height == 3 
# The printout would be: 

#   * 
#  *** 
# ***** 

# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

height = int(input("please enter the height of the tree "))
i = 1
stars=1
for i in range(1,height+1):
    if height == 1:
        print("*")
    if i > 0:
        stars=i*2-1
        print(" " * (height-i) + "*" * stars)
