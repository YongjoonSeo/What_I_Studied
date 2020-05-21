def BT(y, x, val):
    global result, N
    if y == N-1 and x == N-1:
        result = min(result, val)
        # for _ in range(len(visited)):
        #     print(visited[_])
        # print('----')
        return
    dx = [1, 0]
    dy = [0, 1]
    for i in range(2):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < N and nx < N and not visited[ny][nx]:
            if val+field[ny][nx] >= result: continue
            visited[ny][nx] = 1
            BT(ny, nx, val+field[ny][nx])
            visited[ny][nx] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    result = float('inf')
    BT(0, 0, field[0][0])
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(visited)):
    #     print(visited[_])