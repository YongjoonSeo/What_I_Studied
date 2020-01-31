import random

g = ['a','b','c','d','e','f','g']
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

while len(g) > 0 and len(b) > 0:
    temp = []
    if len(g) >= 2:
        gtemp = random.sample(g,2)
        temp.extend(gtemp)
    elif len(g) == 1:
        temp.extend(g)
    
    if len(b) >= 3:
        btemp = random.sample(b,3)
        temp.extend(btemp)
    elif len(b) <= 1 :
        temp.extend(b)
    
    print(*temp)
