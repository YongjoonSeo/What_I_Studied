def DFS(y, x, edge):
    global V, H
    stack = [(y,x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0

    while stack:
        vy, vx = stack[-1]

        if not visited[vy][vx]:
            visited[vy][vx] = 1

        for i in range(4):
            nx = vx + dx[i]
            ny = vy + dy[i]

            if edge <= nx < H-edge and edge <= ny < V-edge:
                if not visited[ny][nx]:
                    if field[ny][nx] == 0:
                        stack.append((ny, nx))
                        break
                    else:
                        cnt += 1
                        field[ny][nx] = 0
                        visited[ny][nx] = 1
        else:
            stack.pop()                       
    if cnt == 0: return False
    return cnt

V, H = map(int, input().split())
field = [[i for i in list(map(int, input().split()))] for j in range(V)]
result = []

for i in range(min(V//2, H//2)):
    visited = [[0 for i in range(H)] for j in range(V)]
    temp = DFS(i, i, i)
    if not temp: break
    result.append(temp)

print(len(result))
print(result[-1])

# for i in range(len(field)):
#     print(field[i])