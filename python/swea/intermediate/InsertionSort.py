# from collections import deque

# llst = deque([69, 10, 30, 2, 16, 8, 31, 22])

# for i in range(1, len(llst)):
#     idx = i
#     while idx >= 0:
#         if idx == 0:
#             llst.appendleft(llst.pop(i))
#         elif llst[idx-1] <= llst[i]:
#             llst.insert(idx-1, llst.pop(i))
#             break
#         idx -= 1

# print(llst)

lst = [69, 10, 30, 2, 16, 8, 31, 22]

for i in range(1, len(lst)):
    idx = i
    while idx >= 0:
        if idx == 0:
            lst.insert(0, lst.pop(i))
        elif lst[idx-1] <= lst[i]:
            lst.insert(idx, lst.pop(i))
            break
        idx -= 1

print(lst)