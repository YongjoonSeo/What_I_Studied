for t in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    field = [[0 for i in range(V+1)] for j in range(V+1)]
    indeg = [0] * (V+1)
    visited = [0] * (V+1)
    result = []

    for i in range(E):
        s, e = edges[2*i], edges[2*i+1]
        field[s][e] = 1
        indeg[e] += 1

    while visited != [0] + [1] * V:
        for i in range(1, V+1):
            if indeg[i] == 0 and visited[i] == 0:
                result.append(i)
                visited[i] = 1
                for j in range(1, V+1):
                    if field[i][j] == 1:
                        indeg[j] -= 1
                break
    
    print('#{0}'.format(t), end=' ')
    print(*result)