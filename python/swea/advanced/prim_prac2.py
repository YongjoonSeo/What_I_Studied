edges = [(0, 1, 32), (0, 2, 31), (0, 6, 51), (0, 5, 60), (1, 2, 21), (2, 4, 46), (6, 2, 25), (6, 4, 51), (3, 4, 34), (3, 5, 18), (5, 4, 40)]
graph = dict()
for edge in edges:
    s, e, val = edge
    if graph.get(s):
        graph[s].append((e, val))
    else:
        graph[s] = [(e, val)]
    if graph.get(e):
        graph[e].append((s, val))
    else:
        graph[e] = [(s, val)]

def Prim(G, s):
    N = len(G)
    visited = [0 for i in range(N)]
    minWeight = [float('inf') for i in range(N)]
    parents = [None for i in range(N)]
    minWeight[s] = 0

    for i in range(N):
        minidx = -1
        minval = float('inf')
        for j in range(N):
            if not visited[j] and minWeight[j] < minval:
                minval = minWeight[j]
                minidx = j
        visited[minidx] = 1
        for v, val in G.get(minidx):
            if not visited[v] and val < minWeight[v]:
                minWeight[v] = val
                parents[v] = minidx

    return (parents, sum(minWeight))

print(Prim(graph, 3))