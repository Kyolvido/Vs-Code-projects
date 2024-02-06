import math
import sys
import random
#diameter and cost
SMALL_PIZZA = [12,11.00] 
MEDIUM_PIZZA = [14,14.00]
LARGE_PIZZA = [18,18.00]

pizza_size = input('What size pizza do you want? (S,M,L): ')
#base Cost
cost = 0.0
if pizza_size == 'S':
    radius = SMALL_PIZZA [0]/2
    cost = SMALL_PIZZA [1]
elif pizza_size == 'M':
    radius = MEDIUM_PIZZA [0]/2
    cost = MEDIUM_PIZZA [1]
elif pizza_size == 'L':
    radius = LARGE_PIZZA [0]/2
    cost = LARGE_PIZZA [1]
else:
    print('Invalid pizza size')

print(cost)

area = math.pi * (radius * radius)# (radius ** 2) or math.pow(radius,2)

print(f'Cost per sq in: {(cost/area):2f}')

num_topping = float(input('Enter number of toppings: '))
dice_roll = random.randrange(1,21)

if dice_roll == 1:
    rate = 2.0
    topping_price = 1.50*(rate)**num_topping
elif dice_roll < 10:
    topp_price = .87*num_topping
else: 
    topping_price = 5


#f(x) = $0.87(r)^n
##rate = 1.5
##topping_price = 1.50*(rate)**num_topping
total_cost = cost + topping_price

print(f'Total Cost: ${total_cost: .2f}')

method = input('How would you like to pay ("cash" or "card")')

if method == "cash":
   
    paid = float(input('Enter dollar amount: '))
    
    if paid < total_cost:
        print('You owe me money punk')
        sys.exit()
    value = paid - total_cost   
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
    print('Here is your change')
    print(f"{dollar} dollars")
    print(f"{quarters} quarters")
    print(f"{dimes} dimes")
    print(f"{cents} pennies")
else:
    
  print(f'Charged{total_cost:.2f}')  
    
print('Thankyou for your bidness')  

#while paid > 0:
    
    
   # 50 %