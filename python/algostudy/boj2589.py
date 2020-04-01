from collections import deque

# def Issafe(y, x):
#     global V, H
#     if 0 <= y < V and 0 <= x < H: return True
#     return False

def BFS(y, x):
    global V, H
    cnt = -1
    q = deque([(y, x)])

    if not visited[y][x]:
        visited[y][x] = 1

    while q:
        cnt += 1
        for _ in range(len(q)):
            vy, vx = q.popleft()
            
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]

                if 0 <= ny < V and 0 <= nx < H and not visited[ny][nx]:
                    if field[ny][nx] == 'L':
                        q.append((ny, nx))
                    visited[ny][nx] = 1
    # if cnt > result:
    #     result = cnt
    return cnt

V, H = map(int, input().split())
field = [[i for i in input()] for j in range(V)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = 0

for i in range(V):
    for j in range(H):
        if field[i][j] == 'L':
            visited = [[0 for i in range(H)] for j in range(V)]
            result = max(result, BFS(i, j))

print(result)

# for _ in range(len(field)):
#     print(field[_])