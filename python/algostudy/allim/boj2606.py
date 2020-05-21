# 1번 컴퓨터 그래프탐색
from collections import deque

def BFS(n):
    global N
    q = deque([n])
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if not visited[i] and field[v][i]:
                q.append(i)
                visited[i] = 1

N = int(input())
E = int(input())
field = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for i in range(N+1)]
for i in range(E):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

visited[1] = 1
BFS(1)

print(sum(visited)-1)
# for _ in range(len(field)):
#     print(field[_])