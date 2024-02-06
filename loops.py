# selection = ''
# while selection != 'q':
#     selection = input()
#     print("|")
#     print(" |")
#     print("  |")
#     print(" |")
#     print("|")


# for i in range (0,10):


# myList =['jon','kyle','ryan']

# for name in myList:
#     print(name)
    
    
# mydic = {'Name':'John'}
# print(mydic)

# for name in mydic:
#     print(name)
    
validation={
    'hour':{'min': 0,'max': 23, 'default':12, 'units':'HH'},
    'minuet': {'min': 0,'max': 59,'default':12, 'units':'MM'},
    'direction': {'min': 0,'max': 359,'default':0, 'units':'degrees'}    
}
    
user_data = [('hour',49),('hour',20),('direction',300),('cost',100)]

TypeSets = set(['hour','hour','direction','cost'])

AllowedTypees = set(validation.keys())

not_allowed = AllowedTypees

    
    