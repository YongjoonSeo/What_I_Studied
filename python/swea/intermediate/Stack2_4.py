def BT(y, x, inp):
    global result, N
    tot = inp + field[y][x]

    if tot > result: return

    if y == N - 1:
        if result > tot:
            result = tot

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            BT(y+1, i, tot)
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [[i for i in list(map(int, input().split()))] for j in range(N)]
    visited = [0 for i in range(N)]
    result = 987654321

    for i in range(N):
        visited[i] = 1
        BT(0, i, 0)
        visited[i] = 0
    
    print('#{0} {1}'.format(t, result))