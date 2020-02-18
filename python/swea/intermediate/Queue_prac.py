def BFS(n):
    queue = [n]

    while queue:
        v = queue.pop(0)

        if not visited[v]:
            visited[v] = 1
            result.append(v)
        
        for i in range(len(field)):
            if field[v][i] == 1 and not visited[i]:
                queue.append(i)

V, E = 7, 7
edges = [1, 2, 1, 3, 2, 5, 3, 5, 4, 6, 5, 6, 6, 7]
field = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]
result = []

for i in range(E):
    s, e = edges[i*2], edges[i*2+1]
    field[s][e] = 1
    field[e][s] = 1

BFS(1)
print(*result)