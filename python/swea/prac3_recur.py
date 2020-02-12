# 7 8
# 1 2 1 3 2 5 2 4 3 5 4 6 5 6 6 7
# 시작점 1

def DFS(n):
    global field, visited, result
    if not visited[n]:
        visited[n] = 1
        result.append(n)
    for i in range(len(field)):
        if field[n][i] == 1 and not visited[i]:
            DFS(i)

V, E = 7, 8
edges = [1, 2, 1, 3, 2, 5, 2, 4, 3, 5, 4, 6, 5, 6, 6, 7]
field = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for i in range(V+1)]
result = []

for i in range(E):
    s, e = edges[i*2], edges[i*2+1]
    field[s][e] = 1
    field[e][s] = 1

DFS(1)
print(*result)

# for _ in range(len(field)):
#     print(field[_])
# print(edges)
