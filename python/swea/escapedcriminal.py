from collections import deque

def Tunnel(n): # x, y
    lst = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if n == 1: return lst
    elif n == 2: return [lst[1], lst[3]]
    elif n == 3: return [lst[0], lst[2]]
    elif n == 4: return [lst[3], lst[0]]
    elif n == 5: return lst[:2]
    elif n == 6: return lst[1:3]
    else: return lst[2:]

def BFS(y, x, num):
    global N, M
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    cnt = 1
    limit = num - 1

    while q and limit:
        limit -= 1

        for _ in range(len(q)):
            vy, vx = q.popleft()

            for i in Tunnel(field[vy][vx]):
                ny = vy + i[1]
                nx = vx + i[0]

                if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and field[ny][nx]:
                    if i[0] == 1:
                        if field[ny][nx] in [2, 4, 5]: continue
                    elif i[0] == -1:
                        if field[ny][nx] in [2, 6, 7]: continue
                    elif i[1] == 1:
                        if field[ny][nx] in [3, 5, 6]: continue
                    elif i[1] == -1:
                        if field[ny][nx] in [3, 4, 7]: continue                    
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                    cnt += 1

    return cnt

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    field = [list(map(int, input().split())) for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]
    result = BFS(R, C, L)
    
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(field)):
    #     print(field[_])
    # for _ in range(len(visited)):
    #     print(visited[_])