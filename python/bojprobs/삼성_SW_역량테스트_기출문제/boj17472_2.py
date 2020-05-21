def DFS(y, x):
    global N, M, islands, island
    island.clear()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    stack = [(y,x)]
    fieldvisited[y][x] = 1
    island.append((y, x))
    field[y][x] = len(islands)
    while stack:
        vy, vx = stack[-1]
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx] > 0 and not fieldvisited[ny][nx]:
                fieldvisited[ny][nx] = 1
                island.append((ny, nx))
                stack.append((ny, nx))
                field[ny][nx] = len(islands)
                break
        else:
            stack.pop()
    islands.append(island[:])

def cases(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in cases(arr, i+1, r-1):
                yield [arr[i]] + j

def min_distance(islands, obj):
    global N, M
    returnval = 1000
    islandval = field[islands[0][0]][islands[0][1]]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for island in islands:
        vy, vx = island
        for direc in range(4):
            cnt = 0
            i = j = 1
            if direc == 0 or direc == 2:
                while True:
                    nx = vx + i * dx[direc]
                    if nx == -1 or nx == M or field[vy][nx] == islandval:
                        break
                    elif field[vy][nx] > 0:
                        if cnt < 2: break
                        elif field[vy][nx] != obj: break
                        else:
                            returnval = min(returnval, cnt)
                    cnt += 1
                    i += 1
            elif direc == 1 or direc == 3:
                while True:
                    ny = vy + j * dy[direc]
                    if ny == -1 or ny == N or field[ny][vx] == islandval:
                        break
                    elif field[ny][vx] > 0:
                        if cnt < 2: break
                        elif field[ny][vx] != obj: break
                        else:
                            returnval = min(returnval, cnt)
                    cnt += 1
                    j += 1
    if returnval == 1000: return -1
    return returnval

def isvalid(arr, s, visited):
    q = [s]
    while q:
        v = q.pop(0)
        for i in range(1, len(arr)):
            if arr[v][i] and not visited[i]:
                visited[i] = 1
                q.append(i)
    for j in range(1, len(visited)):
        if not visited[j]: return False
    return True

def BT():
    result = 1000
    edges = []
    for edgecase in cases(range(1, len(islands)), 0, 2):
        edges.append(edgecase)
    # print(edges)
    for caseset in cases(edges, 0, len(islands)-2):
        arr = [[0 for i in range(len(islands))] for j in range(len(islands))]
        for case in caseset:
            s, e = case
            arr[s][e] = 1
            arr[e][s] = 1
        visited = [0 for i in range(len(islands))]
        visited[1] = 1
        if not isvalid(arr, 1, visited): continue

        tempval = 0
        for case in caseset:
            vidx, fidx = case # idx of island
            fval = field[islands[fidx][0][0]][islands[fidx][0][1]]
            distance = min_distance(islands[vidx], fval)
            if distance == -1: break
            else:
                tempval += distance
                if tempval >= result: break
        else:
            # print(result)
            # print(caseset)
            result = min(tempval, result)

    if result == 1000: return -1
    return result

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
islands = [0]
island = []

fieldvisited = [[0 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        if field[i][j] > 0 and not fieldvisited[i][j]:
            DFS(i, j)

# print('======')
print(BT())
# print('======')
# BT()
# test=[]
# for case in cases(range(1,6), 0, 2):
#     test.append(case)
# print(test)
# print(min_distance(islands[3], 5))
# for _ in range(len(field)):
#     print(field[_])

# for case in cases([1,2,3,4,5], 0, 2):
#     print(case)