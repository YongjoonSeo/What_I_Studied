def DFS(num, depth):
    if depth <= 0: return
    global n
    for i in range(1, n+1):
        if field[num][i] and not visited[i]:
            visited[i] = 1
            counted[i] = 1
            DFS(i, depth-1)
            visited[i] = 0


n = int(input())
m = int(input())
field = [[0 for i in range(n+1)] for j in range(n+1)]
visited = [0 for i in range(n+1)]
counted = [0 for i in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

visited[1] = 1
counted[1] = 1
DFS(1, 2)

print(sum(counted)-1)
# print(counted)
# for _ in range(len(field)):
#     print(field[_])