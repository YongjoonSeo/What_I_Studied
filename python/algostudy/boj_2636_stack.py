def DFS(y, x):
    global V, H, tempcnt
    stack = [(y, x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while stack:
        vy, vx = stack[-1]
        if not visited[vy][vx]:
            visited[vy][vx] = 1
        
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if 0+x <= nx < H and 0+y <= ny < V:
                if not visited[ny][nx]:
                    if field[ny][nx] == 0:
                        stack.append((ny, nx))
                        break
                    else:
                        field[ny][nx] = 0
                        visited[ny][nx] = 1
                        tempcnt += 1
        else:
            stack.pop()

V, H = map(int, input().split())
field = [[i for i in list(map(int, input().split()))] for j in range(V)]
result = []

for i in range(min(V, H) // 2):
    tempcnt = 0
    visited = [[0 for i in range(H)] for j in range(V)]
    DFS(i, i)
    if tempcnt == 0:
        break
    result.append(tempcnt)

print(len(result))
print(result[-1])
# for _ in range(len(field)):
#     print(field[_])