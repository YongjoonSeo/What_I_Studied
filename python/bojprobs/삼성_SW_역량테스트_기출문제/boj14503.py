def BT(y, x, direc):
    global result, N, M
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    stack = []
    visited[y][x] = 1
    result += 1
    stack.append((y, x, direc, 0))

    while stack:
        vy, vx, vd, t = stack.pop()
        d = (vd + 3) % 4
        ny = vy + dy[d]
        nx = vx + dx[d]
        if 0 <= ny < N and 0 <= nx < M and not field[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = 1
            stack.append((ny, nx, d, 0))
            result += 1
        else:
            if t == 3:
                tempy = vy - dy[d]
                tempx = vx - dx[d]
                if field[tempy][tempx]: return
                else: stack.append((tempy, tempx, d, 0))
            else:
                stack.append((vy, vx, d, t+1))

N, M = map(int, input().split())
r, c, d = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
visited = [[0 for i in range(M)] for j in range(N)]
result = 0
BT(r, c, d)

print(result)
# for _ in range(len(visited)):
#     print(visited[_])