# def BT_permutation(times, inp):

#     if times == inp:
#         result.append(stack.copy())
#         return
    
#     for i in range(inp):
#         stack.append(targetcopy.pop(0))
#         BT_permutation(times + 1, inp)
#         targetcopy.append(stack.pop())

# target = [1, 2, 3]
# targetcopy = target.copy()
# stack = []
# N = len(target)
# result = []
# BT_permutation(0, N)

# print(result)

def BT_permutation(t, inp):
    times = inp - t

    if t == 0:
        result.append(stack.copy())
        return 
    
    for i in range(inp):
        if target[i] not in stack:
            stack.append(target[i])
            BT_permutation(t - 1, inp)
            stack.remove(target[i])


target = [1, 2, 3, 4]
n = len(target)
stack = []

result = []
BT_permutation(2, n) 
# nPr, n개(4개) 중에서 r개(2개)를 뽑아 순서를 고려하여 늘어놓는 경우의 수
print(result)

result = []
BT_permutation(4, n) 
# n!, n개(4개)를 순서를 고려하여 늘어놓는 경우의 수
print(result)