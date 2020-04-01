from collections import deque

def Issafe(y, x):
    global N, M
    if 0 <= x < M and 0 <= y < N: return True
    return False

def DFS(y, x, idx):
    global qcheck
    stack = [(y,x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while stack:
        vy, vx = stack[-1]

        if visited[vy][vx] == idx and field[vy][vx] > 0:
            visited[vy][vx] += 1
            qcheck.append((vy, vx))
            iceberg.append((vy, vx))

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if Issafe(ny, nx) and visited[ny][nx] == idx:
                if field[ny][nx] > 0:
                    stack.append((ny,nx))
                    qcheck.append((ny, nx))
                    iceberg.append((ny, nx))
                    visited[ny][nx] += 1
                    break
        else:
            stack.pop()

def BFS():
    qreduceidx = qcheck.copy()
    reduceval = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while qcheck:
        vy, vx = qcheck.popleft()
        
        tempcnt = 0
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if Issafe(ny, nx) and field[ny][nx] == 0:
                tempcnt += 1
        else:
            reduceval.append(tempcnt)
    
    while qreduceidx:
        vy, vx = qreduceidx.popleft()
        field[vy][vx] -= reduceval.popleft()
        if field[vy][vx] < 0: field[vy][vx] = 0

N, M = map(int, input().split())
field = [[i for i in list(map(int, input().split()))] for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
result = 0
iceberg = deque()
qcheck = deque()

TF = False
for i in range(N):
    for j in range(M):
        if field[i][j] > 0:
            DFS(i, j, 0)
            BFS()
            TF = True
            break
    if TF: break

idx = 1
while True:
    stack = [iceberg.popleft()]
    sy, sx = stack[-1]
    icebergvisited = [[0 for i in range(M)] for j in range(N)]
    while stack:
        tempy, tempx = stack[-1]
        if not icebergvisited[tempy][tempx]: icebergvisited[tempy][tempx] = 1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = tempx + dx[i]
            ny = tempy + dy[i]
            if Issafe(ny, nx) and not icebergvisited[ny][nx] and visited[ny][nx] == idx:
                stack.append((ny, nx))
                icebergvisited[ny][nx] = 1
                if (ny, nx) == iceberg[0]:
                    iceberg.popleft()
                break
        else:
            stack.pop()
    if iceberg: break
    DFS(sy, sx, idx)
    if qcheck:
        BFS()
    else:
        TF = False
        for col in range(N):
            for row in range(M):
                if field[col][row]:
                    TF = True
                    break
            if TF: break
        if TF: break
        else:
            result = 0
            break
    result += 1
    idx += 1

print(result)

# for _ in range(len(field)):
#     print(field[_])
# for _ in range(len(visited)):
#     print(visited[_])