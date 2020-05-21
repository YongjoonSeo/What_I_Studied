def Dijkstra(G, s, N): # G: 그래프, s: 시작 정점, N: 정점의 개수
    visited = [0 for i in range(N+1)] # 정점 방문 여부 초기화
    dist = [float('inf') for i in range(N+1)] # 경로 길이를 무한대로 초기화
    parents = [None for i in range(N+1)] # 트리에서 연결될 부모 정점 초기화.
    # 각 정점이 실제 어떤 간선을 통해 트리와 연결되었는지를 확인하기 위해 사용한다.
    dist[s] = 0 # 시작 정점의 경로 길이를 0으로 설정한다.
    # 또한, 이 설정은 시작 정점을 방문하겠다고 표시하기 위한 장치가 된다.

    for i in range(1, N+1): # 정점의 개수 만큼 반복 (모든 정점을 방문할 때까지)
        minidx, minval = -1, float('inf') # 최소 경로 정점을 찾기 위한 초기화
        # 여기서부터 방문하지 않은 정점 중 최소 경로 정점 찾기
        for j in range(1, N+1): # 새로 추가할 정점 찾기
            if not visited[j] and dist[j] < minval:
                minval = dist[j]
                minidx = j
        visited[minidx] = 1 # 최소 경로 정점 방문 표시
        # 여기서부터 추가한 정점에 인접한 간선에 대해 dist 갱신과정
        if G.get(minidx): # 인접 정점이 있는 경우만 최단 경로 정보 갱신
            for v, val in G.get(minidx): # 새로 추가한 정점 인근의 최단 경로 정보 갱신
                if not visited[v] and dist[minidx] + val < dist[v]:
            # 현재 정점(minidx) 까지의 최단 경로 길이 + 해당 정점(v)와의 거리 <val>의 합이
            # 해당 정점에 저장된 최단 경로 길이 <dist[v]>보다 작으면 dist[v]를 더 작은 값으로 갱신한다.
                    dist[v] = dist[minidx] + val
                    parents[v] = minidx

        print(minidx, minval)  # 새로 추가할 정점과 그 최단 경로 길이
        print(visited[1:], dist[1:], parents[1:])  # 정점의 방문 정보, 갱신한 최단 경로 길이 정보, 최단 경로 트리
        print('----------------')

    return parents[1:] # 시작점 s에서의 최단 경로 트리


edges = [(1, 2, 3), (1, 3, 5), (2, 3, 1), (3, 2, 1), (2, 4, 6), (3, 4, 3), (3, 5, 6), (4, 5, 2), (5, 4, 3), (4, 6, 3), (5, 6, 6)]
graph = dict()
for edge in edges:
    s, e, val = edge
    if graph.get(s):
        graph[s].append((e, val))
    else:
        graph[s] = [(e, val)]

for key in graph.keys():
    print(key, graph[key])
print('--------Graph--------')
# 그래프의 인접리스트 표현 (유향 그래프)

print(Dijkstra(graph, 1, 6))