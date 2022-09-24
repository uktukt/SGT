# # 1. FizzBuzz 

# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz 

# So if number divided by 5 then Fizz If divided by 7 then Buzz,
#  If divided by 5 AND 7 then FizzBuzz otherwise the same number

#  Note: such a task became popular as the first task to ask to determine 
#  whether a person knows about programming at all smile

range_end = 100
div1 = 3
div2 = 2
for i in range(1,range_end+1):
    #print(i)
    if  i % div1 == div1 and i % div2 == 0:
        print("FizzBuzz", end=",")
    elif i % div1 == 0:
        print("Fizz", end=",")
    elif i % div2 == 0:
        print("Buzz", end=",")
    elif i % div1 != div1 and i % div2 != 0:
        print(i, end=",")