from sys import stdin
input = stdin.readline

def DFS(y, x):
    global N, M, icebergs
    visited = [[0 for i in range(M)] for j in range(N)]
    stack = [(y,x)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[y][x] = 1
    cnt = 1

    while stack:
        vy, vx = stack.pop()

        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and field[ny][nx] > 0:
                visited[ny][nx] = 1
                stack.append((ny,nx))
                cnt += 1
    
    return cnt
                
N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
result = 0
icebergs = []
cnt = 0
for i in range(N):
    for j in range(M):
        if field[i][j] > 0:
            icebergs.append((i,j))
            cnt += 1

while icebergs:
    if cnt != DFS(*icebergs[-1]):
        break
    
    melts = []
    for iceberg in icebergs:
        y, x = iceberg
        tempcnt = 0
        if y + 1 < N and field[y+1][x] <= 0: tempcnt += 1
        if x + 1 < M and field[y][x+1] <= 0: tempcnt += 1
        if 0 <= y - 1 and field[y-1][x] <= 0: tempcnt += 1
        if 0 <= x - 1 and field[y][x-1] <= 0: tempcnt += 1
        melts.append((y,x,tempcnt))
    
    for i in range(cnt-1, -1, -1):
        y, x, num = melts[i]
        field[y][x] -= num
        if field[y][x] <= 0: 
            icebergs.pop(i)
            cnt -= 1

    result += 1
else:
    result = 0

print(result)