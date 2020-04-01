# from collections import deque

# def Search(y, x):
#     visitedh = [0 for i in range(10)]
#     visitedv = [0 for i in range(10)]
#     visitedsq = [0 for i in range(10)]
#     for i in range(9):
#         visitedh[field[y][i]] += 1
#         visitedv[field[i][x]] += 1
    
#     i = j = 0
#     while not (i*3 <= y <(i+1)*3): i += 1
#     while not (j*3 <= x < (j+1)*3): j += 1
#     for n in range(i*3, (i+1)*3):
#         for m in range(j*3, (j+1)*3):
#             visitedsq[field[n][m]] += 1
    
#     lst = list(range(10))
#     if visitedh[0] == 1:
#         for num in range(1, 10):
#             if visitedh[num]: lst.remove(num)
#         field[y][x] = lst.pop()
#         return True
#     elif visitedv[0] == 1:
#         for num in range(1, 10):
#             if visitedv[num]: lst.remove(num)
#         field[y][x] = lst.pop()
#         return True
#     elif visitedsq[0] == 1:
#         for num in range(1, 10):
#             if visitedsq[num]: lst.remove(num)
#         field[y][x] = lst.pop()
#         return True
#     return False

# field = [[i for i in list(map(int, input().split()))] for j in range(9)]
# q = deque()

# for i in range(9):
#     for j in range(9):
#         if field[i][j] == 0:
#             q.append((i,j))

# while q:
#     y, x = q.popleft()
#     if not Search(y,x):
#         q.append((y,x))

# for _ in range(len(field)):
#     print(field[_])

from collections import deque

def Sudoku():
    global q
    if not q: return
    y, x = q.popleft()
    i = j = 0
    while not (i <= y < i+3): i += 3
    while not (j <= x < j+3): j += 3

    for k in range(1, 10):
        TF = False
        for n in range(i, i+3):
            for m in range(j, j+3):
                if field[n][m] == k:
                    TF = True
                    break
            if TF: break
        if TF: continue
        
        TF = False
        for idx in range(9):
            if field[y][idx] == k:
                TF = True
                break
            if field[idx][x] == k:
                TF = True
                break
        if TF: continue

        field[y][x] = k
        if not Sudoku():
            if not q: return
            field[y][x] = 0
    else:
        if field[y][x]: return True
        q.appendleft((y,x))
        return False

field = [[i for i in list(map(int, input().split()))] for j in range(9)]
q = deque()

for i in range(9):
    for j in range(9):
        if field[i][j] == 0:
            q.append((i,j))
while q:
    Sudoku()

for _ in range(len(field)):
    print(*field[_])