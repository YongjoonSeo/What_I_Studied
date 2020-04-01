from collections import deque

def BFS(arr):
    global result, N, M
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.extend(arr)
    changed = []

    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not field[ny][nx]:
                field[ny][nx] = 2
                changed.append((ny, nx))
                q.append((ny, nx))
    
    result = max(result, len(empty) - 3 - len(changed))
    for coor in changed:
        field[coor[0]][coor[1]] = 0

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
empty = []
virus = []
result = -1

for i in range(N):
    for j in range(M):
        if field[i][j] == 0: empty.append((i,j))
        elif field[i][j] == 2: virus.append((i,j))

for i in range(len(empty)-2):
    y1, x1 = empty[i]
    field[y1][x1] = 1
    for j in range(i+1, len(empty)-1):
        y2, x2 = empty[j]
        field[y2][x2] = 1 
        for k in range(j+1, len(empty)):
            y3, x3 = empty[k]
            field[y3][x3] = 1
            BFS(virus)
            field[y3][x3] = 0
        field[y2][x2] = 0
    field[y1][x1] = 0

print(result)



# for _ in range(len(field)):
#     print(field[_])