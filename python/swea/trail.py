def DFS(y, x, count, num):
    global result, N
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = count + 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and field[ny][nx] < num:
            DFS(ny, nx, cnt, field[ny][nx])
    else:
        result = max(result, cnt)
    
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(map(int, input().split())) for j in range(N)]
    starts = []
    result = 0

    ref = field[0][0]
    for i in range(N):
        for j in range(N):
            if ref == field[i][j]: starts.append((i,j))
            elif ref < field[i][j]:
                starts.clear()
                ref = field[i][j]
                starts.append((i,j))

    for i in range(N):
        for j in range(N):
            for k in range(K+1):
                for start in starts:
                    sy, sx = start
                    field[i][j] -= k
                    DFS(sy, sx, 0, field[sy][sx])
                    field[i][j] += k
    
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(field)):
    #     print(field[_])