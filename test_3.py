# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year
# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year 

p0 = 1000
perc = 2
delta = 50
target_p = 1200
years = 2


sum = p0 * (1 + perc*0.01)**years + delta * (1 + perc*0.01)**(years-1) + delta * (years -1)
print(sum)