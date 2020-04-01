R, C, T = map(int, input().split())
field = [list(map(int, input().split())) for j in range(R)]
dusts = []
purifier = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(R):
    for j in range(C):
        if field[i][j] > 0:
            dusts.append((i, j, field[i][j]))
f = 0
for i in range(R):
    if field[i][0] == -1:
        purifier.append((i, 0))
        f += 1
    if f == 2: break
up = purifier[0]
down = purifier[1]

while T:
    notinrange = set()
    # print(dusts)
    # print(set(dusts))
    # print(len(dusts))
    # print(len(set(dusts)))
    for dust in dusts:
        y, x, A = dust
        cnt = 0
        if y != 0 and y != R-1 and y != up[0] and y != down[0] and x != 0 and x != C-1:
            notinrange.add((y,x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and field[ny][nx] != -1:
                if field[ny][nx] == 0 and ny != 0 and ny != R-1 and ny != up[0] and ny != down[0] and nx != 0 and nx != C-1: 
                    notinrange.add((ny, nx))
                field[ny][nx] += A//5
                cnt += 1
        field[y][x] -= (A//5) * cnt
    
    if T == 1:
        for _ in range(len(field)):
            print(field[_])
    # print(up[0])
    # print(down[0])
    print(notinrange)

    x1 = x2 = y1 = y2 = 0
    if up[0] == 0: 
        field[0][1] = 0
        y1, x1 = 0, 1
    else: 
        field[up[0]-1][0] = 0
        y1, x1 = up[0]-1, 0
    if down[0] == R-1: 
        field[R-1][1] = 0
        y2, x2 = R-1, 0
    else: 
        field[down[0]+1][0] = 0 
        y2, x2 = down[0]+1, 0
    
    idx1 = idx2 = 0
    dusts = []
    while field[y1][x1] != -1:
        py, px = y1, x1
        if py == 0 and 0 <= px < C-1: idx1 = 0
        elif 0 <= py < up[0] and px == C-1: idx1 = 1
        elif 0 < px <= C-1 and py == up[0]: idx1 = 2
        else: idx1 = 3
        y1 = py + dy[idx1]
        x1 = px + dx[idx1]
        if field[y1][x1] != -1:
            field[py][px] = field[y1][x1]
            if field[py][px] > 0: dusts.append((py, px, field[py][px]))
        else:
            field[py][px] = 0
    
    while field[y2][x2] != -1:
        py, px = y2, x2
        if px == 0 and down[0] <= py < R-1: idx2 = 1
        elif 0 <= px < C-1 and py == R-1: idx2 = 0
        elif px == C-1 and down[0] < py <= R-1: idx2 = 3
        else: idx2 = 2        
        y2 = py + dy[idx2]
        x2 = px + dx[idx2]
        if field[y2][x2] != -1:
            field[py][px] = field[y2][x2]
            if field[py][px] > 0: dusts.append((py, px, field[py][px]))
        else:
            field[py][px] = 0
    
    # print(dusts)
    for new in notinrange:
        y, x = new
        if field[y][x] > 0: dusts.append((y, x, field[y][x]))
    
    # print(cnt)
    # print(tempt-T)
    
    # visited = [[0 for i in range(C)] for j in range(R)]
    # for dust in dusts:
    #     y, x, a = dust
    #     visited[y][x] = a
    # for _ in range(len(visited)):
    # #     print(visited[_])
    if T == 1:
        print('/////////')
        for _ in range(len(field)):
            print(field[_])
    # print('--------')
    T -= 1

cnt = 0
for i in range(R):
    for j in range(C):
        cnt += field[i][j]

print(cnt+2)

# for _ in range(len(field)):
#     print(field[_])