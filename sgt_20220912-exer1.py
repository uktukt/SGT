temp = input("what is your temperature? ")
temp = float(temp)
if temp < 35:
    print("not too cold")
elif 35 <= temp <= 37:
    print("all right")
else:
    print("possible fever")