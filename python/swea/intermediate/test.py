def Quick(inplst):
    if not inplst: return []
    lst = inplst[:]
    pivot = lst[0]
    left = []
    right = []
    pivots = []

    for char in lst:
        if char < pivot: left.append(char)
        elif char == pivot: pivots.append(char)
        else: right.append(char)
    
    if len(inplst) == 2:
        return left + pivots + right
    elif len(inplst) == 3:
        if len(left) == 2: return Quick(left) + pivots
        elif len(right) == 2: return pivots + Quick(right)
    
    if len(left) == 1: return left + pivots + Quick(right)
    elif len(right) == 1: return Quick(left) + pivots + right

    return Quick(left) + pivots + Quick(right)

target = [69, 10, 30, 2, 16, 8, 31, 22]
print(Quick(target))
