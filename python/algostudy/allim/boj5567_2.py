from collections import deque

def BFS(N):
    global n
    q = deque([N])
    cnt = 2
    while q and cnt:
        cnt -= 1
        for i in range(len(q)):
            v = q.popleft()
            for j in range(1, n+1):
                if not visited[j] and field[v][j]:
                    visited[j] = 1
                    q.append(j)


n = int(input())
m = int(input())
field = [[0 for i in range(n+1)] for j in range(n+1)]
visited = [0 for i in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

visited[1] = 1
BFS(1)
print(sum(visited) - 1)

# for _ in range(len(field)):
#     print(field[_])