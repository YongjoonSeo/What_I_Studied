# 방향 그래프의 최단 경로를 구하라.

# 출력: i번 정점으로의 최단경로값을 출력한다.
    # 시작점은 0, 경로 없으면 INF

# 체크할 조건
# 1 <= V <= 20000
    # 1부터 시작
# 1 <= E <= 300000
# 시작점 자신도 출력, 경로 없으면 INF 출력

# 다익스트라 알고리즘을 사용하여 모든 정점으로의 값을 출력한다.

# import sys
# input = sys.stdin.readline

# def djikstra(graph, s, V):
#     visited = [0] * (V+1)
#     dist = [float('inf')] * (V+1)
#     dist[s] = 0
    
#     for i in range(1, V+1):
#         mi, mv = 0, float('inf')
#         for j in range(1, V+1):
#             if not visited[j] and mv > dist[j]:
#                 mi, mv = j, dist[j]
#         visited[mi] = 1
#         if mi in graph:
#             for e, val in graph.get(mi):
#                 if not visited[e] and dist[e] > dist[mi] + val:
#                     dist[e] = dist[mi] + val
    
#     return dist[1:]

# def solution(V, E):
#     start = int(input())
#     graph = dict()
#     for i in range(E):
#         s, e, val = map(int, input().split())
#         if s in graph: graph[s].append((e, val))
#         else: graph[s] = [(e, val)]
#     for res in djikstra(graph, start, V):
#         if res == float('inf'): print('INF')
#         else: print(res)    

# if __name__ == '__main__':
#     solution(*map(int, input().split()))

# >> 시간 초과
# V^2 == 400000000 정도라 초과되는듯
# 우선순위 큐를 사용하여 구현해보자.

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

def djikstra(graph, s, V):
    dist = [float('inf')] * (V+1)
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        mv, mi = heappop(pq)
        if dist[mi] < mv: continue
        if mi in graph:
            for val, e in graph.get(mi):
                if dist[e] > dist[mi] + val:
                    dist[e] = dist[mi] + val
                    heappush(pq, (dist[e], e))
    return dist[1:]

def solution(V, E):
    start = int(input())
    graph = dict()
    for i in range(E):
        s, e, val = map(int, input().split())
        if s in graph: graph[s].append((val, e))
        else: graph[s] = [(val, e)]
    for res in djikstra(graph, start, V):
        if res == float('inf'): print('INF')
        else: print(res)    

if __name__ == '__main__':
    solution(*map(int, input().split()))