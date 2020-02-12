def DFS(y, x):
    global field, visited, result
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if not visited[ny][nx]:
            if field[ny][nx] == 0:
                visited[ny][nx] = 1
                DFS(ny, nx)
            elif field[ny][nx] == 3:
                result = 1
                return

for t in range(1, 11):
    T = int(input())
    field = [[i for i in list(map(int, input()))] for j in range(16)]
    visited = [[0 for i in range(16)] for j in range(16)]
    x = y = 0
    result = 0

    TF = False
    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                x, y = j, i
    
    visited[y][x] = 1
    DFS(y,x)

    print('#{0} {1}'.format(t,result))