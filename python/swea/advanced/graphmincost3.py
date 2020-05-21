# 다익스트라
# 0번 지점에서 N번 지점까지 이동
def Dijkstra(G, s, N):
    visited = [0 for i in range(N)]
    mindist = [float('inf') for i in range(N)]
    mindist[s] = 0

    for i in range(N):
        minidx, minval = -1, float('inf')
        for j in range(N):
            if not visited[j] and minval > mindist[j]:
                minval = mindist[j]
                minidx = j
        visited[minidx] = 1
        if G.get(minidx):
            for e, val in G.get(minidx):
                if not visited[e] and mindist[e] > val + mindist[minidx]:
                    mindist[e] = val + mindist[minidx]

    return mindist[-1]

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

    print('#{0} {1}'.format(t, Dijkstra(graph, 0, V+1)))

