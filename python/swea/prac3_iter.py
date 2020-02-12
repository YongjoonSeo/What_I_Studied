def DFS(n):
    global field, visited
    stack = [n]

    while stack:
        v = stack[-1]
        
        if not visited[v]:
            visited[v] = 1
            result.append(v)
        
        for i in range(len(field)):
            if field[v][i] == 1 and not visited[i]:
                stack.append(i)
                break
        else:
            stack.pop()

V, E = 7, 8
edges = [1, 2, 1, 3, 2, 5, 2, 4, 3, 5, 4, 6, 5, 6, 6, 7]
field = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]
result = []

for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    field[s][e] = 1
    field[e][s] = 1

DFS(1)
print(*result)