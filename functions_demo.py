


x = [4, 5, 2, 4, 5, 1, 2, 7, 8, 4, 7]
y = ['a', 'a', 'b', 'c' , 'b']
def getMode(myList):
     counter = {}
     for num in myList:
        print(num)
     if num in counter:
         counter[num] += 1 
     else:
         counter[num] = 1
         

myMax = 0
letter = ''
for key, val in counter.items:
    if val > myMax:
        letter = key
        myMax = val
    



#     for i in range(0,10):
#         print(i
#               )
    
    # for num in myList:
    # print(num)
    # print(f'{num}C is {toFahrenheit(num)}F')
    
    # l = len(myList)
    # count = 0
    # print(l)
    # while count <= l - 1:
    #         print(myList[count])
    #         count += 1


# getMode(x)

#myDictionary = {'Player1': 'a'}
# #returs key
# for what in myDictionary:
# #returns key and value
# for what,whatt in myDictionary.items():
# returns value
#x,y = y,x
#swaps variables


# for what in myDictionary.values():
#     print(what)
    