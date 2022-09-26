p0 = 1000
perc = 10
delta = 5
target_p = 5000
years = 10

sum1 = p0 * (1 + perc*0.01)**years + delta * (1 + perc*0.01)**(years-1)
sum2 = delta * (years -1)
print(sum1)
print(sum2)
