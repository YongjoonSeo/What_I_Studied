# N x N 체스판, 사용 말의 개수 K개
# 하나의 말 위에 다른 말 올릴 수 있다
# 체스판의 각 칸은 흰색, 빨간색, 파란색 세 가지 중 하나로 색칠
# 체스판 위에 말 K개를 놓고 시작, 1번부터 K번까지 번호, 이동 방향도 미리 정해져있다. (위, 아래, 왼쪽, 오른쪽)
# 턴 한 번: 1번 말 ~ K번 말까지 '순서대로' 이동시키는 것 (위에 올려져 있는 말도 함께 이동)
# 말의 이동 방향에 있는 칸에 따라 말의 이동이 다르다
# 턴이 진행되는 중에 말이 4개 이상 쌓이면 종료
# 이동방향: 1-오른쪽, 2-왼쪽, 3-위쪽, 4-아래쪽

# 이동하려는 칸에 따라서
# 1. 흰색: 그 칸으로 이동 // A번 말이 이동하려는 칸에 말이 있으면 그 가장 위에 A번 말을 올려놓는다
# (이미 A번 말 위에 다른 말이 있으면 함께 쌓는다)
# 2. 빨간색: 이동한 후에 '이동하는 말'의 쌓여있는 순서를 반대로 바꾼다.
# 3. 파란색: A번 말의 이동 방향을 반대로 하고 한 칸 이동. & 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색이면 이동 X
# 체스판을 벗어나는 경우 - 파란색처럼

# 흰색, 빨간색, 파란색 밑 가장자리일 때의 움직임
# ->> 한 개의 말에 대해서만 정보바꾸기
# 말이 겹쳐지는 것
# -> 말의 정보를 스택처럼 저장해두는 맵을 하나 더 만들어서 조작해보자.
# -> info에 있는 모든 말들에 대해 수행

# 출력: 게임이 종료되는 턴의 번호를 출력, 그 값이 1000보다 크거나 게임이 종료되지 않는다면 -1을 출력
def white(y, x, ny, nx, idx):
    temp = info[y][x][idx:]
    info[ny][nx].extend(temp)
    info[y][x] = info[y][x][:idx]
    return len(info[ny][nx])

def red(y, x, ny, nx, idx):
    temp = info[y][x][idx:]
    temp.reverse()
    info[ny][nx].extend(temp)
    info[y][x] = info[y][x][:idx]
    return len(info[ny][nx])

N, K = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
info = [[[] for i in range(N)] for j in range(N)]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
cnt = 0
stacked = -1
lst = []
for k in range(K):
    r, c, d = map(int, input().split())
    lst.append([r-1, c-1, d-1])
    info[r-1][c-1].append(k)

while cnt <= 1000:
    cnt += 1
    for i in range(K):
        y, x, d = lst[i]
        idx = info[y][x].index(i)
        ny = y + dy[d]
        nx = x + dx[d]
        p = 0
        if ny < 0 or ny >= N or nx < 0 or nx >= N or field[ny][nx] == 2:
            if d == 1 or d == 3: d -= 1
            else: d += 1
            ny = y + dy[d]
            nx = x + dx[d]
            if ny < 0 or ny >= N or nx < 0 or nx >= N or field[ny][nx] == 2:
                lst[i][2] = d
                continue
            p = 1
        if field[ny][nx] == 0:
            for k in info[y][x][idx:]:
                lst[k][0] = ny
                lst[k][1] = nx
            stacked = white(y, x, ny, nx, idx)
        elif field[ny][nx] == 1:
            for k in info[y][x][idx:]:
                lst[k][0] = ny
                lst[k][1] = nx
            stacked = red(y, x, ny, nx, idx)
        if p: lst[i][2] = d
        if stacked >= 4: break
    if stacked >= 4: break
if cnt > 1000: cnt = -1

print(cnt)

# print(lst)
