def Search(y, x, idx, string):
    if idx == 7:
        result.add(string)
        return
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            Search(ny, nx, idx+1, string+str(field[ny][nx]))

T = int(input())
for t in range(1, T+1):
    field = [list(map(int, input().split())) for i in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            Search(i, j, 1, str(field[i][j]))
    
    print('#{0} {1}'.format(t, len(result)))