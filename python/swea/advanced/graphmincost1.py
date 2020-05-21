def prim(G, s, N):
    visited = [0 for i in range(N)]
    minWeight = [float('inf') for i in range(N)]
    minWeight[s] = 0

    for i in range(N):
        minidx, minval = -1, float('inf')
        for j in range(N):
            if not visited[j] and minval > minWeight[j]:
                minval = minWeight[j]
                minidx = j
        visited[minidx] = 1
        for e, val in G.get(minidx):
            if not visited[e] and minWeight[e] > val:
                minWeight[e] = val
    return sum(minWeight)

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = dict()
    for i in range(E):
        s, e, val = map(int, input().split())
        if graph.get(s):
            graph[s].append((e, val))
        else:
            graph[s] = [(e, val)]
        if graph.get(e):
            graph[e].append((s, val))
        else:
            graph[e] = [(s, val)]

    print('#{0} {1}'.format(t, prim(graph, 0, V+1)))

    # for _ in range(len(graph)):
    #     print(_, graph[_])
