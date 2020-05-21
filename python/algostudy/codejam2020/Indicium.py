import sys
sys.setrecursionlimit(10000)

def BT(y, x):
    global N, result, resultmsg
    isdid = False
    for i in range(1, N+1):
        isnot = False
        for j in range(N):
            if i == field[y][j] or i == field[j][x]:
                isnot = True
                break
        if isnot: continue
        field[y][x] = i
        isdid = True
        if y == N-1 and x == N-1:
            for n in range(N):
                for m in range(N):
                    result[n][m] = field[n][m]
            return
        elif x == N-1:
            BT(y+1, 0)
        else:
            BT(y, x+1)
        field[y][x] = 0

T= int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    field = [[0 for i in range(N)] for j in range(N)]
    result = [[0 for i in range(N)] for j in range(N)]
    resultmsg = 'POSSIBLE'
    # tempsum = 0
    # for i in range(1,N+1):
    #     tempsum += i
    # if K % N == 0 or K == tempsum:
    #     if K == tempsum:
    #         for i in range(N):
    #             field[i][i] = i
    #     else:
    #         n = K//N
    #         for i in range(N):
    #             field[i][i] = n
    # else:
    #     resultmsg = 'IMPOSSIBLE'
    BT(0, 0)
    tempsum = 0
    for i in range(N):
        tempsum += field[i][i]
    if K == tempsum: resultmsg = 'POSSIBLE'
    else: resultmsg = 'IMPOSSIBLE'

    print('Case #{0}: {1}'.format(t, resultmsg))
    if resultmsg == 'POSSIBLE':
        for _ in range(len(result)):
            print(*result[_])
    # for _ in range(len(result)):
    #     print(*result[_])