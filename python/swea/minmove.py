from collections import deque

def BFS(y, x, fy, fx):
    global result, W, H
    dx = [1, 0, -1, 0, 1, -1]
    dy = [0, 1, 0, -1, 1, -1]
    checked = []
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    checked.append((y,x))
    cnt = 0
    isFound = False

    while q:
        cnt += 1

        for _ in range(len(q)):
            vx, vy = q.popleft()

            for i in range(6):
                ny = vy + dy[i]
                nx = vx + dx[i]

                if 0 <= ny < H and 0 <= nx < W and not visited[ny][nx]:
                    if ny == fy and nx == fx:
                        isFound = True
                        break
                    visited[ny][nx] = 1
                    checked.append((ny, nx))
                    q.append((ny, nx))
            if isFound: break
        if isFound: break

    for coor in checked:
        visited[coor[0]][coor[1]] = 0
    result += cnt

T = int(input())
for t in range(1, T+1):
    W, H, N = map(int, input().split())
    visited = [[0 for i in range(W)] for j in range(H)]
    result = 0
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1
    for i in range(N-1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        BFS(sy, sx, y, x)
        sx, sy = x, y
    
    print('#{0} {1}'.format(t, result))

