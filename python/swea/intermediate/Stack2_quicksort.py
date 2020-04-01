# def Quick(inplst):
#     a = inplst[:]
#     pivot = len(a)//2
#     left = []
#     right = []
    
#     if pivot == 0: return a
#     if pivot == 1:
#         if len(a) & 1:
#             for i in range(-1, 2, 2):
#                 if a[i] > a[pivot]: right.append(a[i])
#                 else: left.append(a[i])
#             if not left: right = Quick(right)
#             elif not right: left = Quick(left) 
#         else:
#             if a[0] > a[pivot]: a[0], a[pivot] = a[pivot], a[0]
#             return a

#     left = Quick(a[:pivot])
#     right = Quick(a[pivot+1:])
        
#     return left + [a[pivot]] + right

#     # left = a[:pivot]
#     # right = a[pivot+1:]

#     # if len(a) // 2 == 1:
#     #     return left + [pivot] + right
#     # else:
#     #     left = Quick(left[:], begin, pivot-1)
#     #     right = Quick(right[:], pivot+1, end)

# def Quick(inplst):
#     lst = inplst[:]
#     pivot = lst[0]
#     left = []
#     right = []
#     pivots = []

#     for char in lst:
#         if char < pivot: left.append(char)
#         elif char == pivot: pivots.append(char)
#         else: right.append(char)
    
#     if len(inplst) == 2:
#         return left + pivots + right
#     elif len(inplst) == 3:
#         if len(left) == 2: return Quick(left) + pivots
#         elif len(right) == 2: return pivots + Quick(right)
    
#     if len(left) == 1: return left + pivots + Quick(right)
#     elif len(right) == 1: return Quick(left) + pivots + right

#     return Quick(left) + pivots + Quick(right)

# # target = [3, 5, 8, 1, 2, 9, 4, 7, 6]
# target = [1, 1, 2, 1]
# print(Quick(target))
        
def Quick(inplst):
    lst = inplst[:]
    pivot = lst[0]
    left = []
    right = []
    pivots = []

    for char in lst:
        if char < pivot: left.append(char)
        elif char == pivot: pivots.append(char)
        else: right.append(char)
    
    if len(inplst) <= 2:
        return left + pivots + right
    
    if not left and not right:
        return pivots
    elif not left:
        return pivots + Quick(right)
    elif not right:
        return Quick(left) + pivots

    return Quick(left) + pivots + Quick(right)

target = [3, 5, 8, 1, 2, 9, 4, 7, 6]
print(Quick(target))