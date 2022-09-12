year_of_service = input("how many years are you working here? ")
year_of_service = float(year_of_service)
if year_of_service > 2:
    salary = input("what is your montly salary? ")
    salary = float(salary)
    b = int((year_of_service - 2) * salary * 0.15)
    print("your bonus is", b)
else:
    print("no bonus")