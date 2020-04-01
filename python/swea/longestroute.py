def DFS(cnt, start):
    global N, result
    for j in range(1, N+1):
        if not v[j] and field[start][j]:
            v[j] = 1
            DFS(cnt+1, j)
            v[j] = 0
    else:
        result = max(result, cnt)                    

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    field = [[0 for i in range(N+1)] for j in range(N+1)]
    v = [0 for i in range(N+1)]
    result = -1

    for i in range(M):
        s, e = map(int, input().split())
        field[s][e] = 1
        field[e][s] = 1
    
    for j in range(1, N+1):
        v[j] = 1
        DFS(1, j)
        v[j] = 0

    print('#{0} {1}'.format(t, result))