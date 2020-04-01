from collections import deque

def Pickremoveplace(start, r):
    if r == 0: return
    for i in range(start, len(chickenplace)-r+1):
        if r == 1:
            yield [chickenplace[i]]
        else:
            for j in Pickremoveplace(i+1, r-1):
                yield [chickenplace[i]] + j

def BFS(y, x):
    global N
    visited = [[0 for i in range(N)] for j in range(N)]
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
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
                        return cnt
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

if len(chickenplace) - M:
    for places in Pickremoveplace(0, len(chickenplace) - M):
        tempresult = 0
        for place in places:
            py, px = place
            field[py][px] = 0

        for house in houses:
            hy, hx = house
            tempresult += BFS(hy, hx)
            if tempresult >= result: break
        else:
            result = min(result, tempresult)            

        for place in places:
            py, px = place
            field[py][px] = 2
else:
    result = 0
    for house in houses:
        hy, hx = house
        result += BFS(hy, hx)

print(result)

# for _ in range(len(field)):
#     print(field[_])