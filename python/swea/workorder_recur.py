def DFS(n):
    global field, visited
    for i in range(1, V+1):
        if field[n][i] == 1:
            indeg[i] -= 1
            if indeg[i] == 0 and not visited[i]:
                visited[i] = 1
                result.append(i)
                DFS(i)

for t in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    field = [[0 for i in range(V+1)] for j in range(V+1)]
    visited = [0 for i in range(V+1)]
    indeg = [0 for i in range(V+1)]
    result = []

    for i in range(E):
        s, e = edges[2*i], edges[2*i+1]
        field[s][e] = 1
        indeg[e] += 1
    
    for i in range(1, V+1):
        if indeg[i] == 0 and not visited[i]:
            visited[i] = 1
            result.append(i)
            DFS(i)
    
    print('#{0}'.format(t), end=' ')
    print(*result)
