def search(start, depth):
    if depth <= 0 : return
    global cnt
    for i in range(start, n+1):
        if field[start][i] and not visited[i]:
            visited[i] = 1
            if not counted[i]:
                counted[i] = 1
            search(i, depth-1)
            visited[i] = 0

n = int(input())
m = int(input())
field = [[0 for i in range(n+1)] for j in range(n+1)]
visited = [0 for i in range(n+1)]
counted = [0 for i in range(n+1)]
result = 0

for i in range(m):
    s, e = map(int, input().split())
    field[s][e] = 1
    field[e][s] = 1

visited[1] = 1
search(1, 2)

if counted[1]:
    result = sum(counted) - 1
else:
    result = sum(counted)

print(result)
# for _ in range(len(field)):
#     print(field[_])