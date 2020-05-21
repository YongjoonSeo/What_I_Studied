# 1. N*N 격자가 아닌 대각선의 집합으로 보는 것
# 2. 홀수판 짝수판 따로따로 보는 것.

def BT(idx, bishop, rest):
    global N, tempresult, diff
    if rest == 2*N-1-diff:
        if not N&1:
            tempresult = max(tempresult, bishop)
            return
    elif rest == 2*N-2-diff:
        if N&1:
            if idx == 1:
                tempresult = max(tempresult, bishop)
                return
    elif rest == 2*N-diff:
        if N&1:
            if idx == 0:
                tempresult = max(tempresult, bishop)
                return
    for i in range(N):
        for j in range(N):
            if field[i][j] and idxfield[i][j] == idx and diag1[i-j] and diag2[i+j]:
                field[i][j] = 0
                diag1[i-j] = 0
                diag2[i+j] = 0
                BT(idx, bishop+1, rest-2)
                field[i][j] = 1
                diag1[i-j] = 1
                diag2[i+j] = 1


N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
idxfield = [0 if i&1 else 1 for i in range(N**2)]
idxfield = [idxfield[i:i+N] for i in range(0, N**2, N)]
if not N&1:
    for i in range(1, N, 2):
        for j in range(N):
            if idxfield[i][j]: idxfield[i][j] = 0
            else: idxfield[i][j] = 1
diag1 = [1 for i in range(2*N-1)] # 우하
diag2 = [1 for i in range(2*N-1)] # 우상

d1lst = [[N-1, i] for i in range(N-1,-1,-1)] + [[j, N-1] for j in range(N-1)]
d2lst = [[0, i] for i in range(N)] + [[j, N-1] for j in range(1, N)]
for i in range(9):
    d1 = -4
    d1 += i
    d2 = i
    yd1, xd1 = d1lst[i]
    yd2, xd2 = d2lst[i]
    m = n = 0
    while yd1-m >= 0 and xd1-m >= 0:
        if field[yd1-m][xd1-m]: break
        m += 1
    else:
        diag1[yd1 - xd1] = 0
    while yd2+n < N and xd2-n >= 0:
        if field[yd2+n][xd2-n]: break
        n += 1
    else:
        diag2[yd2 + xd2] = 0

print(diag1)
print(diag2)
#
# print(d1lst)
# print(d2lst)

diff = (2*N-1) * 2 - (sum(diag1)+sum(diag2))
print(diff)
tempresult = 0
BT(1, 0, (sum(diag1)+sum(diag2)))
result = tempresult
# tempresult = 0
# BT(0, 0, (sum(diag1)+sum(diag2)))
# result = tempresult

print(result)
# print(sum(diag1)+sum(diag2))
# print(diag1)
# print(diag2)

# for _ in range(len(idxfield)):
#     print(idxfield[_])