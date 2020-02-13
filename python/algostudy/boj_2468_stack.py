def DFS(y, x, h):
    global N
    stack = [(y,x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while stack:
        vy, vx = stack[-1]
        visited[vy][vx] = 1

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if field[ny][nx] > h and not visited[ny][nx]:
                    stack.append((ny, nx))
                    break
        else:
            stack.pop()

N = int(input())
field = [[i for i in list(map(int, input().split()))] for j in range(N)]
result = 0

for h in range(1, 101):
    visited = [[0 for i in range(N)] for j in range(N)]
    tempcnt = 0
    for i in range(N):
        for j in range(N):
            if field[i][j] > h and not visited[i][j]:
                DFS(i, j, h)
                tempcnt += 1
    if result < tempcnt:
        result = tempcnt
            
print(result)
# for _ in range(len(field)):
#     print(field[_])