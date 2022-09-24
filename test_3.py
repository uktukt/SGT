n = 1000000 #how to define positive infinity?
input_primes=int(input("How many prime numbers do you want to find? Please enter a positive number. "))
primes = []
for i in range(2, n):
	for j in range(2, int(i ** 0.5) + 1): 
 		if i%j == 0:
 			break
	else:
		primes.append(i)

print(f"Here are first {input_primes} prime numbers",primes[:input_primes])