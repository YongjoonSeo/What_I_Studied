import sys
sys.stdin = open('', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    k = r = c = 0
    for i in range(N):
        row = set()
        col = set()
        for j in range(N):
            if i == j: k += field[i][j]
            row.add(field[i][j])
            col.add(field[j][i])
        if len(row) != N: r += 1
        if len(col) != N: c += 1

    print('Case #{0}: {1} {2} {3}'.format(t, k, r, c))




    # for _ in range(len(field)):
    #     print(field[_])