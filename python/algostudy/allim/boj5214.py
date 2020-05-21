# 하이퍼튜브 하나는 역 K개를 연결한다.
# 1번 역에서 N번 역으로 가는데 방문하는 최소 역의 수?
# bfs로 N번역까지 최소거리 구하자.
# 모든 간선을 연결하면 메모리가 터진다? -> 1
from collections import deque
import sys

def combi(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combi(arr, i+1, r-1):
                yield [arr[i]] + j

def BFS():
    global N
    q = deque([1])
    cnt = 1
    visited = [0 for i in range(N+1)]
    visited[1] = 1
    isfound = False
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            for i in graph[v]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = 1
                    if i == N:
                        isfound = True
                        break
            if isfound: break
        if isfound: break
    else:
        cnt = -1
    return cnt


N, K, M = map(int, input().split())
graph = dict()
temp = []
for i in range(M):
    for s, e in combi(list(map(int, input().split())), 0, 2):
        temp.append((s,e))
        if not graph.get(s):
            graph[s] = set()
        graph[s].add(e)
        if not graph.get(e):
            graph[e] = set()
        graph[e].add(s)

field = [[0 for i in range(N+1)] for j in range(N+1)]
for s, e in temp:
    field[s][e] = 1
    field[e][s] = 1

result = BFS()
print(result)

print(sys.getsizeof(graph))
print(sys.getsizeof((field)))
# print(graph)

