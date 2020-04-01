# from collections import deque

# def BFS(y, x):
#     global N, result, startpoint
#     q = deque()
#     q.append((y,x))
#     visited[y][x] = 1
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     cnt = 0

#     while q:
#         cnt += 1

#         for _ in range(len(q)):
#             vy, vx = q.popleft()

#             for i in range(4):
#                 ny = vy + dy[i]
#                 nx = vx + dx[i]

#                 if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and field[ny][nx] - field[vy][vx] == 1:

def DFS(y, x, cnt, start):
    global N, result, startpoint
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < N and 0 <= nx < N and field[ny][nx] - field[y][x] == 1:
            DFS(ny, nx, cnt+1, start)
    else:
        if cnt == result:
            startpoint = min(startpoint, start)
        elif cnt > result:
            result = cnt
            startpoint = start

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    startpoint = N*N+1
    result = 0

    for i in range(N):
        for j in range(N):
            DFS(i, j, 1, field[i][j])
    
    print('#{0} {1} {2}'.format(t, startpoint, result))

    # for _ in range(len(field)):
    #     print(field[_])