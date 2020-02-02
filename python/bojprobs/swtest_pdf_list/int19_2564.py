# def clock(currentseq, xmax, ymax): # 시계 방향 기준, current: seq
#     idx = currentseq
#     if idx in [[ymax, i] for i in range(xmax)]: # 2
#         return [0, -1]
#     elif idx in [[i, 0] for i in range(ymax)]: # 3
#         return [-1, 0]
#     elif idx in [[0, i] for i in range(xmax)]: # 1
#         return [0, 1]
#     else: # 4
#         return [1, 0]    

# w, h = map(int, input().split())
# field = [[0 for i in range(w+1)] for j in range(h+1)]
# num = int(input())

# for i in range(1,num+1):
#     loc, dist = map(int, input().split())
#     if loc == 1:
#         field[0][dist] = i
#     elif loc == 2:
#         field[h][dist] = i
#     elif loc == 3:
#         field[dist][0] = i
#     else:
#         field[dist][w] = i

# loc, dist = list(map(int, input().split()))
# if loc == 1:
#     cur = [0,dist]
# elif loc == 2:
#     cur = [h,dist]
# elif loc == 3:
#     cur = [dist,0]
# else:
#     cur = [dist,w]

# result = 0
# for j in range(1, num+1):
#     mcnt1 = mcnt2 = 0
#     mintemp = [mcnt1, mcnt2]
#     for k in range(2):
#         now = cur
#         while field[now[0]][now[1]] != j:
#             now[0] += clock(now, w+1, h+1)[0] * ((-1) ** k)
#             now[1] += clock(now, w+1, h+1)[1] * ((-1) ** k)
#             mintemp[k] += 1
#     result += min(mintemp)

# print(result)



# for _ in range(len(field)):
#     print(field[_])
# print(cur)

def clock(currentseq, xmax, ymax): # 시계 방향 기준, current: seq
    idx = currentseq
    if idx in [[ymax, i] for i in range(1, xmax+1)]: # 2
        return [0, -1]
    elif idx in [[i, 0] for i in range(1, ymax+1)]: # 3
        return [-1, 0]
    elif idx in [[0, i] for i in range(xmax)]: # 1
        return [0, 1]
    else: # 4
        return [1, 0]

def cntclock(currentseq, xmax, ymax): # 시계 방향 기준, current: seq
    idx = currentseq
    if idx in [[ymax, i] for i in range(xmax)]: # 2
        return [0, 1]
    elif idx in [[i, 0] for i in range(ymax)]: # 3
        return [1, 0]
    elif idx in [[0, i] for i in range(1, xmax+1)]: # 1
        return [0, -1]
    else: # 4
        return [-1, 0]

def loc(lst, xmax, ymax):
    if lst[0] == 1:
        return [0, lst[1]]
    elif lst[0] == 2:
        return [ymax, lst[1]]
    elif lst[0] == 3:
        return [lst[1], 0]
    else:
        return [lst[1], xmax]

def move(lst1, lst2):
    return [lst1[0] + lst2[0], lst1[1] + lst2[1]]


w, h = map(int, input().split())
field = [[0 for i in range(w+1)] for j in range(h+1)]

shopnum = int(input())
shops = []
for i in range(1, shopnum+1):
    shop = list(map(int, input().split()))
    shoploc = loc(shop, w, h)
    shops.append(shoploc)

dong = list(map(int, input().split()))
dloc = loc(dong, w, h)

result = 0

for j in shops:
    temp1 = temp2 = 0
    cur = dloc
    field[j[0]][j[1]] = 1
    while cur != j:
        cur = move(cur, clock(cur, w, h))
        temp1 += 1
    
    cur = dloc
    while cur != j:
        cur = move(cur, cntclock(cur, w, h))
        temp2 += 1

    field[j[0]][j[1]] = 0
    result += min(temp1, temp2)

print(result)



# 시작 인덱스와 끝 인덱스가 어떤 동작이냐에 따라서도 달라진다. (clock, cntclock)


# for i in range(len(field)):
#     print(field[i])