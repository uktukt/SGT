p0 = 1000
perc = 2
delta = -50
target_p = 5000
years = 100

sum1 = p0 * (1 + perc*0.01)**years + delta * (1 + perc*0.01)**(years-1)
sum2 = delta * (years -1)
print(sum1)
print(sum2)
