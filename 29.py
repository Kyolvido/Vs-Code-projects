import math
#taking in a number
def isEven(num):
    #checks if it is a int type
    if not isinstance(num,int):
        print(f'isEven only accepts int types,youpass: {type(num)}')
        return
    
    if num % 2 == 0:
        return True
    else:
        return False
        
def isOdd(num):
   if isEven(num) == True:
       return False
   else:
       return True
   
def areaTriangle(base, height):
    area = (base * height) / 2
    return area



# x = int(input("Enter number: "))
# print(isOdd(x))

user_base = float(input('Enter base:'))
user_height = float(input('Enter height:'))
user_area = areaTriangle(user_base, user_height)
print(user_area)


def toCelsius(fahrenheight):
    c = (fahrenheight - 32) * (5/9)
    return c

def toFarenheight (celsius):
    f = (celsius / (5/9))
    return

print(toCelsius(32))
print(toFarenheight(0))
