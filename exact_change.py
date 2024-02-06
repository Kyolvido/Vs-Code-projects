import math

value = float(input('Enter dollar amount: '))
cents = int(value * 100)
#get dollars
dollar = cents // 100
cents = cents % 100
#get quarters
quarters = cents // 25
cents = cents % 25
#get dimes
dimes = cents // 10
cents = cents % 10
#get nickles 
nickles = cents // 5
cents = cents % 5

print(f"{dollar} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{cents} pennies")

