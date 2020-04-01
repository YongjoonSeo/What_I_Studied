from collections import deque

def BFS():
    global y, x, N, cnt, shark, sharkcnt
    q = deque()
    q.append((y,x))
    visited = [[0 for i in range(N)] for j in range(N)]
    visited[y][x] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    time = 0
    candi = []

    while q:
        time += 1
        for _ in range(len(q)):
            vy, vx = q.popleft()

            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]

                if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and field[ny][nx] <= shark:
                    if field[ny][nx] < shark and field[ny][nx] > 0:
                        candi.append((ny,nx))
                    visited[ny][nx] = 1
                    q.append((ny,nx))            

        # 골라낸 세대 중에서 먹을 수 있는 물고기 후보
        if candi:
            miny = min(candi, key=lambda k: k[0])
            final = []
            for fish in candi:
                if fish[0] == miny[0]:
                    final.append(fish)
            if final:
                finaly, finalx = min(final, key=lambda l: l[1])
                y, x = finaly, finalx
                field[y][x] = 0
                cnt += time
                sharkcnt += 1
                if sharkcnt == shark:
                    shark += 1
                    sharkcnt = 0
                return True
    else:
        return False

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
cnt = 0
shark = 2
sharkcnt = 0

x = y = 0
TF = False
for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            field[i][j] = 0
            x, y = j, i
            TF = True
            break
    if TF: break

while True:
    if not BFS(): break

print(cnt)


# for _ in range(len(field)):
#     print(field[_])