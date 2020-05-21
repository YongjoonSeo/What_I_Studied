from collections import deque

def BFS(start):
    q = deque([start])
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if not visited[i] and field[v][i]:
                visited[i] = 1
                q.append(i)

N, M = map(int, input().split())
field = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for i in range(N+1)]
cnt = 0
for i in range(M):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        BFS(i)
        cnt += 1

print(cnt)