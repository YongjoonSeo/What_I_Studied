T = int(input())
for i in range(1,T+1):
    N = int(input())
    lst = [[1]*(N+2) for i in range(N+2)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    x0 = 1
    y0 = 1
    d = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            lst[i][j] = 0

    for j in range(1, N*N+1):
        lst[y0][x0] = j
        if lst[y0+dy[d]][x0+dx[d]] > 0:
            d = (d + 1) % 4
        x0 += dx[d]
        y0 += dy[d]

    print('#{0}'.format(i))
    for k in range(1, N+1):
        for l in range(1, N+1):
            print(lst[k][l], end=' ')
        print()
