# Find and output the first 20 
# (even better option to choose how many first primes we want) 
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...
# so remember we already know how to find a single prime number 
# from previous exercise:
# # for i in range(2, n): # so n-1 is clearly sufficient but can we do better?
# for i in range(2, int(n**0.5)+1): # so we check only up to and including square root of n
#     if n % i == 0:
#         print(f"{n} is not a prime number.")
#         print(f"Sorry {n} is not a prime number because it divides by {i}")
#         break
# else: # this is executed if the for loop is not broken out of with break
#     print(f"I am sure that {n} is a prime number!")


nr = int(input("how many prime numbers do you want? "))
prime_nr = []
range_end = 1000_000
    
for c in range(2, range_end):
    for i in range(2, int(range_end**0.5)+1): # so we check only up to and including square root of n /int(nr**0.5)+1
        if c % i == 0:
            break
        else:
            prime_nr.append(c)
            break
first_primes = prime_nr[:nr]
print(first_primes)




