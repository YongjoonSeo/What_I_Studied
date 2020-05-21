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

N = len(graph)
minWeight = [float('inf') for i in range(N)]
parents = [None for i in range(N)]
visited = [0 for i in range(N)]
minWeight[0] = 0

for i in range(N):
    minidx = -1
    minval = float('inf')
    for j in range(N):
        if not visited[j] and minval > minWeight[j]:
            minval = minWeight[j]
            minidx = j
    visited[minidx] = 1
    for v, val in graph.get(minidx):
        if not visited[v] and minWeight[v] > val:
            minWeight[v] = val
            parents[v] = minidx

    print(minidx, minval)  # 새로 추가할 정점과 그 가중치
    print(visited, minWeight, parents)  # 정점의 방문 정보, 갱신한 가중치 정보, MST
    print('----------------')

print(parents)
print(sum(minWeight))

for _ in range(len(graph)):
    print(_, graph[_])