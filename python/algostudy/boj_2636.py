import sys
sys.setrecursionlimit(1000001)

def IsSafe(y, x, ymax, xmax):
    if 0 <= y < ymax and 0 <= x < xmax: return True
    return False

def DFS(y, x, v, h):
    global field, visited, tempnum
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if IsSafe(ny, nx, v, h):
            if not visited[ny][nx]:
                if field[ny][nx] == 0:
                    visited[ny][nx] = 1
                    DFS(ny, nx, v, h)
                elif field[ny][nx] == 1:
                    tempnum += 1
                    field[ny][nx] = 0
                    visited[ny][nx] = 1

V, H = map(int, input().split())
field = [[i for i in list(map(int, input().split()))] for j in range(V)]
result = []

for i in range(min(V, H)):
    tempnum = 0
    visited = [[0 for i in range(H)] for j in range(V)]
    DFS(i, i, V, H)
    if tempnum == 0:
        break
    result.append(tempnum)

print(len(result))
print(result[-1])