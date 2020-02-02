T = int(input())
for i in range(1, T+1):
    N = int(input())
    field = [[1 for i in range(N+2)] for j in range(N+2)]
    for j in range(1,N+1):
        for k in range(1, N+1):
            field[j][k] = 0
    
    x, y = 1, 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    for j in range(1, N**2+1):
        field[y][x] = j
        if field[y+dy[idx]][x+dx[idx]] != 0:
            idx = (idx + 1) % 4
        x, y = x+dx[idx], y+dy[idx]

    
    print('#{0}'.format(i))
    for i in range(1, N+1):
        print(*field[i][1:N+1])


    # for _ in range(len(field)):
    #     print(field[_])