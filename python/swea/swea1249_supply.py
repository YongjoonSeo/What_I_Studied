def BT(y, x, total):
    global N, result
    if total >= result: return
    if y == N-1 and x == N-1:
        result = min(total, result)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
            visited[ny][nx] = 1
            BT(ny, nx, total + field[ny][nx])
            visited[ny][nx] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for j in range(N)]
    templ = tempr = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for i in range(1, N-1):
        templ += field[i][0]
        tempr += field[i][N-1]
    result = min(sum(field[0])+tempr, sum(field[N-1])+templ)

    visited[0][0] = 1
    BT(0, 0, 0)
    
    print('#{0} {1}'.format(t, result))



    # print(sum(field[0])+tempr, sum(field[N-1])+templ)
    # print(result)

    # # for _ in range(len(field)):
    # #     print(field[_])
    # # for _ in range(N):
    # #     print(visited[_])


# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     field = [list(map(int, input())) for j in range(N)]
#     candi = [float('inf') for i in range(N**2-1)]

#     print(candi)