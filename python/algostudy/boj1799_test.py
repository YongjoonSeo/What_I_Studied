from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
chess = [list(map(int,input().rsplit())) for _ in range(n)]

che_1 = [[0] * n for _ in range(n)] ; che_1[0][n-1] = 1
che_2 = [[0] * n for _ in range(n)] ; che_2[n-1][n-1] = 1

for i in [0,n-1],[n-1,n-1]:

    if not i[0]:
        che_ = che_1
    else:
        che_ = che_2

    temp = deque([i])
    while temp:
        x, y = temp.popleft()
        for i, j in [1,0],[0,1],[-1,0],[0,-1]:
            nx, ny = x + i, y + j
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if che_[nx][ny]:
                continue
            che_[nx][ny] = che_[x][y] + 1
            temp.append((nx,ny))

graph = {} ; t = 0
for i in range(n):
    for j in range(n):
        if chess[i][j]:
            if not che_1[i][j] in graph:
                graph[che_1[i][j]] = [che_2[i][j]]
                continue
            graph[che_1[i][j]].append(che_2[i][j])

print(graph)

for _ in range(5):
    print(che_1[_])
for _ in range(5):
    print(che_2[_])