# # 2. Cubes
# The user enters the beginning (integer) and end number.
# The output is the entered numbers and their cubes
# For example: inputs 2 and 5 (two inputs)

# Output
# 2 cubed: 8
# 3 cubed: 27
# 4 cubed: 64
# 5 cubed: 125

# All cubes: [8,27,64,125]

# PS could theoretically do without a list, but with a list it will be more convenient

cube1 = int(input("enter 1st number "))
cube2 = int(input("enter 2nd number "))

cubes = []
for i in range(cube1, cube2+1,1):
    cubes.append(i**3)
    print(str(i) + " cubed: " + str(i**3))

print("All cubes:",cubes)