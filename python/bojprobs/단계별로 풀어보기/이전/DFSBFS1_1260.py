def DFS(n):
    stack = [n]
    resultDFS.append(n)
    visited[n] = 1
    while stack:
        v = stack[-1]
        
        for i in range(1, N+1):
            if field[v][i] and not visited[i]:
                stack.append(i)
                resultDFS.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

def BFS(n):
    q = [n]
    resultBFS.append(n)
    visited[n] = 1
    while q:
        v = q.pop(0)
        for i in range(1, N+1):
            if field[v][i] and not visited[i]:
                q.append(i)
                resultBFS.append(i)
                visited[i] = 1

N, M, V = map(int, input().split())
field = [[0 for i in range(N+1)] for j in range(N+1)]
visited = [0 for i in range(N+1)]
resultDFS = []
resultBFS = []

for i in range(M):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

DFS(V)
visited = [0 for i in range(N+1)]
BFS(V)
print(*resultDFS)
print(*resultBFS)