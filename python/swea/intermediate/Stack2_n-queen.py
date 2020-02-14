# def Backtrack(y, x):
#     global N
#     qcnt = N
#     cnt = N*N

#     for i in range(N):
#         for j in range(N):
#             if i == y or j == x or i+j == x+y:
#                 counted[i][j] = 1
#     i = j = 0
#     while y+i < N and x+i < N:
#         counted[y+i][x+i] = 1
#         i += 1
#     while y-j >= 0 and x-j >= 0:
#         counted[y-j][x-j] = 1
#         j += 1
    
#     for m in range(N):
#         for n in range(N):
#             if not counted[m][n]:
#                 field[m][n] = 1
#                 counted[m][n] = 1
#                 Backtrack(m, n)
#             if field[m][n] == 1: qcnt - 1
#             if counted[m][n] == 1: cnt - 1
    
#     if qcnt == 0 and cnt == 0: return True
#     else: return False


# N = 4

# TF = False
# for i in range(N):
#     for j in range(N):
#         field = [[0 for i in range(N)] for j in range(N)]
#         counted = [[0 for i in range(N)] for j in range(N)]
#         field[i][j] = 1
#         counted[i][j] = 1
#         if Backtrack(i, j):
#             TF = True
#             break
#     if TF == True: break

# for _ in range(N):
#     print(field[_])


def Backtrack(y, x):
    global N
    for i in range(N):
        for j in range(N):
            if i == y or j == x or i+j == x+y:
                counted[y][x] = 1
    i = j = 0
    while x+i < N and y+i < N:
        counted[y+i][x+i] = 1
        i += 1
    while x-j >= 0 and y-j >= 0:
        counted[y-j][x-j] = 1
        j += 1
    



N = 4
field = [[0 for i in range(N)] for j in range(N)]

for n in range(N):
    counted = [[0 for i in range(N)] for j in range(N)]