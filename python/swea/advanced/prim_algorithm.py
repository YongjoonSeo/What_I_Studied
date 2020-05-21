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

for key in sorted(graph.keys()):
    print(key, graph[key])
print('--------Graph--------')
# 그래프의 인접리스트 표현

N = len(graph.keys()) # N은 정점의 개수

def MST_PRIM(G, s): # G: 그래프, s: 시작 정점
    minWeight = [float('inf') for i in range(N)] # 가중치를 무한대로 초기화
    parents = [None for i in range(N)] # 트리에서 연결될 부모 정점 초기화.
    # 각 정점이 실제 어떤 간선을 통해 트리와 연결되었는지를 확인하기 위해 사용한다.
    visited = [0 for i in range(N)] # 정점 방문 여부 초기화
    minWeight[s] = 0 # 시작 정점의 가중치를 0으로 설정한다.
    # 또한, 이 설정은 시작 정점을 방문하겠다고 표시하기 위한 장치가 된다.

    for i in range(N): # 정점의 개수 만큼 반복 (모든 정점을 방문할 때까지)
        minidx, minval = -1, float('inf') # 최소 가중치 정점을 찾기 위한 초기화
        # 여기서부터 방문하지 않은 정점 중 최소 가중치 정점 찾기
        for j in range(N): # 새로 추가할 정점 찾기
            if not visited[j] and minWeight[j] < minval:
                minval = minWeight[j]
                minidx = j
        visited[minidx] = 1 # 최소 가중치 정점 방문 표시
        # 여기서부터 추가한 정점에 인접한 간선에 대해 minWeight 갱신과정
        for v, val in G[minidx]: # 새로 추가한 정점 인근의 간선 정보 갱신
            if not visited[v] and val < minWeight[v]:
                minWeight[v] = val
                parents[v] = minidx

        print(minidx, minval) # 새로 추가할 정점과 그 가중치
        print(visited, minWeight, parents) # 정점의 방문 정보, 갱신한 가중치 정보, MST
        print('----------------')

    return parents, sum(minWeight)

print(MST_PRIM(graph, 0))