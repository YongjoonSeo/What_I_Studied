def DFS(y, x):
    global field, visited, result
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = [(y,x)]

    TF = False
    while stack:
        vy, vx = stack[-1]

        if not visited[vy][vx]:
            visited[vy][vx] = 1
        
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if not visited[ny][nx]:
                if field[ny][nx] == 0:
                    stack.append((ny, nx))
                    break
                elif field[ny][nx] == 3:
                    result = 1
                    TF = True
                    return
        else:
            stack.pop()

for t in range(1, 11):
    T = int(input())
    field = [[i for i in list(map(int, input()))] for j in range(16)]
    visited = [[0 for i in range(16)] for j in range(16)]
    x = y = 0
    result = 0

    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                x, y = j, i
    
    DFS(y, x)
    print('#{0} {1}'.format(T, result))