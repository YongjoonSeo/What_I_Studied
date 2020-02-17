def DFS(y, x):
    global N, result
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= ny < N and 0 <= nx < N:
            if field[ny][nx] == 3:
                result = 1
                return
            if field[ny][nx] == 0 and not visited[ny][nx]:
                DFS(ny, nx)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [[i for i in list(map(int, input()))] for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if field[i][j] == 2:
                x, y = j, i
    
    DFS(y,x)
    print('#{0} {1}'.format(t, result))