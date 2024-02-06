stroke = int(input())
par = int(input())
difference = stroke - par
score_type = ''
valid_par = [3,4,5]
if par not in valid_par:
    score_type = 'Error'
    print(f'Par {par} in {stroke} strokes is {score_type}')
elif difference == -2:
    score_type = 'Eagle'
    print(f'Par {par} in {stroke} strokes is {score_type}')
elif difference == -1:
    score_type = 'Birdie'
    print(f'Par {par} in {stroke} strokes is {score_type}')
elif difference == 0:
    score_type = 'Par'
    print(f'Par {par} in {stroke} strokes is {score_type}')
elif difference == +1:
    score_type = 'Bogey'
    print(f'Par {par} in {stroke} strokes is {score_type}')
else:
    score_type = 'Error'
    print(f'Par {par} in {stroke} strokes is {score_type}')
    #hello
    