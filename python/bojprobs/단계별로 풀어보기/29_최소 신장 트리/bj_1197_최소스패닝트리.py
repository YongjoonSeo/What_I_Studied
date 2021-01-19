# 출력: 최소 스패닝 트리의 가중치

# 체크할 조건
# 1 <= V <= 10000
# 1 <= E <= 100000

# 1. 크루스칼

# import sys
# input = sys.stdin.readline

# def find(x, parents):
#     if parents[x] == x: return x
#     parents[x] = find(parents[x], parents)
#     return parents[x]

# def union(x, y, parents, ranks):
#     xr = find(x, parents)
#     yr = find(y, parents)
#     if ranks[xr] >= ranks[yr]:
#         parents[yr] = xr
#     else:
#         parents[xr] = yr
#     if ranks[xr] == ranks[yr]:
#         ranks[xr] += 1

# def kruskal(edges, parents, ranks, V):
#     cost = 0
#     for val, s, e in edges:
#         if find(s, parents) != find(e, parents):
#             union(s, e, parents, ranks)
#             cost += val
#             V -= 1
#             if V - 1 == 0: return cost

# def solution(V, E):
#     parents = [i for i in range(V+1)]
#     ranks = [0] * (V+1)
#     edges = []
#     for i in range(E):
#         s, e, val = map(int, input().split())
#         edges.append([val, s, e])
#     edges.sort()
#     print(kruskal(edges, parents, ranks, V))

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# 2. 프림

import sys
input = sys.stdin.readline

def prim(graph, V):
    visited = [0] * (V+1)
    weight = [float('inf')] * (V+1)
    weight[1] = 0

    for i in range(1, V+1):
        mi, mv = 0, float('inf')
        for j in range(1, V+1):
            if not visited[j] and mv > weight[j]:
                mv = weight[j]
                mi = j
        visited[mi] = 1
        for e, val in graph.get(mi):
            if not visited[e] and weight[e] > val:
                weight[e] = val
    
    return sum(weight[1:])

def solution(V, E):
    graph = dict()
    for i in range(E):
        s, e, val = map(int, input().split())
        if s in graph: graph[s].append((e, val))
        else: graph[s] = [(e, val)]
        if e in graph: graph[e].append((s, val))
        else: graph[e] = [(s, val)]
    print(prim(graph, V))

if __name__ == '__main__':
    solution(*map(int, input().split()))