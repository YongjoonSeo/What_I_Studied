# 섬들이 연결되는 게 한 섬을 찾았다고 그 섬에서 출발할 필요가 없다.
# 한 섬에 여러 섬이 연결될 수 있다.

def DFS(y, x):
    global N, M, islands, island
    island.clear()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = [(y,x)]
    fieldvisited[y][x] = 1
    island.append((y, x))
    field[y][x] = len(visited)
    while stack:
        vy, vx = stack[-1]
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx] > 0 and not fieldvisited[ny][nx]:
                fieldvisited[ny][nx] = 1
                island.append((ny, nx))
                stack.append((ny, nx))
                field[ny][nx] = len(visited)
                break
        else:
            stack.pop()
    islands.append(island[:])

def BT(cnt, idx): #idx: idx of islands
    global result, N, M, testfield
    if cnt >= result: return
    visited[idx] = 1
    for i in range(1, len(visited)):
        if not visited[i]: break
    else:
        result = min(cnt, result)
        visited[idx] = 0
        return
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for coor in islands[idx]:
        vy, vx = coor
        for direc in range(4):
            tempcnt = 0
            i = j = 1
            if direc == 0 or direc == 2:
                while True:
                    nx = vx + i * dx[direc]
                    if nx == -1 or nx == M or field[vy][nx] == idx:
                        break
                    elif field[vy][nx] > 0:
                        if visited[field[vy][nx]] and visited[idx]:
                            break
                        elif tempcnt < 2: break
                        # if tempcnt < 2: break
                        else:
                            BT(cnt+tempcnt, field[vy][nx])
                            break
                    tempcnt += 1
                    i += 1
            elif direc == 1 or direc == 3:
                while True:
                    ny = vy + j * dy[direc]
                    if ny == -1 or ny == N or field[ny][vx] == idx:
                        break
                    elif field[ny][vx] > 0:
                        if visited[field[ny][vx]] and visited[idx]:
                            break
                        elif tempcnt < 2: break
                        # if tempcnt < 2: break
                        else:
                            BT(cnt+tempcnt, field[ny][vx])
                            break
                    tempcnt += 1
                    j += 1
    visited[idx] = 0

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
visited = [0]
result = 1000
islands = [0]
island = []

fieldvisited = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        if field[i][j] > 0 and not fieldvisited[i][j]:
            DFS(i, j)
            visited.append(0)

BT(0, 1)
if result == 1000: result = -1
print(result)
# print(visited)
# for _ in range(len(field)):
#     print(field[_])
# print(islands)
# print(visited)