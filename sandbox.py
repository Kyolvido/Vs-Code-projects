import sys 

import math

# chr()


# ord()


#stacking functions
# math.sqrt(math.pow(math.ceil(5.7), 2 * 1/2 (math.pi)))

# ((x and y) and (not ))

# lots of loop questions on test
# write each iteration for loops


# num_elements = int(input())
# myList = []

# for i in  range(num_elements):
#     print(i)
#     myList.append(i)
    
# print(myList)
# ' ','\n','\t'

# def doSomething(var1, var2): #parameters
#     return (var1,var2) #arguments

# x , _ = doSomething(5,2)

ball = (0,100)
for x,y in enumerate(ball):
    def get_scores():
    left_scorerange = (0,600)
    right_scorerange = (800,600)
    
    for x,y in enumerate(ball):
        if left_scorerange[0] <= ball[0,1] <= left_scorerange[1]:
             player1_score += 1
        else:
            player1_score = 0
        
        if right_scorerange[0] <= ball[0,1] <= right_scorerange[1]:
            player1_score += 1
        else:
            player2_score = 0
    
    #im thinking if the ball passes within the range on left or right the player score will update depending what side it passes
    """Return the current scores of player1 and player2 as a tuple.
    
    TODO: CHANGE THIS FUNCTION TO RETURN SCORES FROM YOUR IMPLEMENTATION.
    THEN UPDATE THIS DOCSTRING TO REFLECT YOUR IMPLEMENTATION."""
    return (player1_score, player2_score)
