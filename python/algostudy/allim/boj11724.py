import sys
sys.setrecursionlimit(10000)

def connect(start):
    for i in range(1, N+1):
        if not visited[i] and field[start][i]:
            visited[i] = 1
            connect(i)

N, M = map(int, input().split())
field = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1
visited = [0 for i in range(N+1)]
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        visited[i] = 1
        msg = connect(i)
        cnt += 1

print(cnt)

# for _ in range(len(field)):
#     print(field[_])