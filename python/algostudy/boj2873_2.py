# R, C 중에 홀수가 하나라도 있을 때 - 모두 돌면 됨 -->> 홀수 방향으로
# R, C 모두 짝수일때 - 시작, 끝 점을 제외하고 가장 값이 작은 한 군데만 피해서 가면 된다.
# 하나만 빠질 수 있는 부분 중에서 최소값인 부분을 제외하고 돌면 된다.
# (하나만 빠질 수 없는 부분에 최소값이 있다고 해도, 하나만 빠질 수 있는 부분에서도 하나 제외해야 하기 때문)
# i+j가 홀수인 부분이 하나만 빠질 수 있는 부분이다. (index 0 부터)

import sys
sys.setrecursionlimit(2000000)

def BT(y, x, ty, tx, cnt):
    global R, C, isfound, ry, rx
    if cnt == 1:
        isfound = True
        ry, rx = y, x
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and (ny, nx) != (ty, tx) and (ny, nx) != (R - 1, C - 1) and field[ny][nx]:
            field[ny][nx] = 0
            resultstack.append(i)
            BT(ny, nx, ty, tx, cnt-1)
            if isfound: return
            field[ny][nx] = 1
            resultstack.pop()


R, C = map(int, input().split())
field = [list(map(int, input().split())) for i in range(R)]
result = ''

if R&1 or C&1:
    temp = ''
    toggle = 1
    if R&1:
        for i in range(R):
            if toggle == 1:
                temp += 'R' * (C-1)
            else:
                temp += 'L' * (C-1)
            toggle *= -1
            temp += 'D'
        result = temp[:-1]
    else:
        for i in range(C):
            if toggle == 1:
                temp += 'D'* (R-1)
            else:
                temp += 'U' * (R-1)
            toggle *= -1
            temp += 'R'
        result = temp[:-1]
else:
    case = 0
    minval = 1001
    ty, tx = 0, 0
    for i in range(R):
        for j in range(C):
            if (i+j)&1:
                if field[i][j] < minval:
                    ty, tx = i, j
                    minval = field[i][j]

    field[0][0] = 0
    ry, rx = 0, 0
    dx = [0, 1, -1, 0]
    dy = [-1, 0, 0, 1]
    stack = [(0,0)]
    resultstack = []
    cnt = R*C-2
    isfound = False
    BT(0, 0, ty, tx, cnt)

    for i in resultstack:
        if i == 0:
            result += 'U'
        elif i == 1:
            result += 'R'
        elif i == 2:
            result += 'L'
        else:
            result += 'D'

    if (ry, rx) == (R-1, C-2):
        result += 'R'
    else:
        result += 'D'

print(result)
# for _ in range(len(field)):
#     print(field[_])