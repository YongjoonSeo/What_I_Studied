from collections import deque

def Pickplace(start, r):
    if r == 0: return
    for i in range(start, len(chickenplace)-r+1):
        if r == 1:
            yield [i]
        else:
            for j in Pickplace(i+1, r-1):
                yield [i] + j

def BFS(y, x, hidx):
    global N
    visited = [[0 for i in range(N)] for j in range(N)]
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ckidx = 0
    cnt = 0

    while q:
        cnt += 1
        for k in range(len(q)):
            vy, vx = q.popleft()

            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]

                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                    if field[ny][nx] == 2:
                        visited[ny][nx] = 1
                        distance[hidx][ckplaceidx.get((ny,nx))] = cnt
                        ckidx += 1
                    visited[ny][nx] = 1
                    q.append((ny,nx))

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
houses = []
chickenplace = []
result = float('inf')

for i in range(N):
    for j in range(N):
        if field[i][j] == 2: chickenplace.append((i,j))
        elif field[i][j] == 1: houses.append((i,j))

distance = [[0 for i in range(len(chickenplace))] for j in range(len(houses))]
ckplaceidx = dict()
for i in range(len(chickenplace)):
    ckplaceidx[chickenplace[i]] = i

for houseidx in range(len(houses)):
    hy, hx = houses[houseidx][0], houses[houseidx][1]
    BFS(hy, hx, houseidx)

for pick in Pickplace(0, M):
    tempresult = 0
    for house in range(len(distance)):
        temphcnt = float('inf')
        for ckplace in pick:
            temphcnt = min(temphcnt, distance[house][ckplace])
        tempresult += temphcnt
        if tempresult >= result: break
    else:
        result = min(tempresult, result)

print(result)

# for _ in range(len(distance)):
#     print(distance[_])

# for _ in range(len(field)):
#     print(field[_])