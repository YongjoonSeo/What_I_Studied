# for i in range(1, 11):
for i in range(1, 2):
    T = int(input())
    # field = [input() for i in range(16)]
    field = [list(map(int, input())) for _ in range(16)]
    visited = [[False for i in range(16)] for j in range(16)]
    TF = False
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    result = 0
    x = y = 0

    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                x, y = j, i
                TF = True
                break
        if TF == True:
            break
    
    stack = [(y,x)]
    visited[y][x] == True
    TF = False


    while stack:
        v = stack[-1]
        y, x = v[0], v[1]

        for i in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if visited[ny][nx] == False and field[ny][nx] == 0:
                stack.append((ny, nx))
                visited[ny][nx] == True
                break
            elif field[ny][nx] == 3:
                result = 1
                TF = True
                break
        
        else:
            stack.pop()
    for _ in range(16):
        print(field[_])
    for _ in range(16):
        print(visited[_])
    
    print('#{0} {1}'.format(T, result))

             



    
