from collections import deque

def BFS(y, x):
    global N
    q = deque()
    q.append([y, x])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = -1

    while q:
        result += 1
        for i in range(len(q)):
            vy, vx = q.popleft()
        
            if not visited[vy][vx]:
                visited[vy][vx] = 1

            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if 0 <= nx < N and 0 <= ny < N:
                    if not visited[ny][nx]:
                        if field[ny][nx] == 3:
                            return result
                        elif field[ny][nx] == 0:
                            visited[ny][nx] = 1
                            q.append([ny, nx])
    return 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [[i for i in list(map(int, input()))] for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            if field[i][j] == 2:
                x, y = j, i

    print('#{0} {1}'.format(t, BFS(y,x)))

    # for _ in range(len(field)):
    #     print(field[_])