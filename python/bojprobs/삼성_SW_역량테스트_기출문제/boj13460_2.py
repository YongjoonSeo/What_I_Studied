# 바깥 행, 열은 모두 막혀있다. 보드에는 구멍 하나
# 왼쪽, 오른쪽, 위쪽, 아래쪽으로 기울이기
# 공은 동시에 움직임
# 모든 가장자리에는 벽이 있다
# 1. 빨간 구슬만 구멍에 빠지면 성공
# 2. 파란구슬이 구멍에 빠지면 실패
# 3. 빨간 구슬 파란 구슬 동시에 빠져도 실패
# a. 더이상 구슬이 움직이지 않으면 기울이는 것 스톱
# b. 10번 이하로 빨간 구슬 못 빼내면 -1 출력

# 출력: 최소 몇 번 만에 빨간 구슬 탈출하는지 - 조건 못맞추면 -1 출력

def Movepoint(dot1, dot2, direc): # dot1먼저, 그다음 dot2
    y, x = dot1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ny = y + dy[direc]
    nx = x + dx[direc]
    while dotfield[ny][nx] != '#' and (ny, nx) != dot2:
        if dotfield[ny][nx] == 'O':
            ny, nx = (-1, -1)
            break
        ny += dy[direc]
        nx += dx[direc]
    if (ny, nx) != (-1, -1):
        ny -= dy[direc]
        nx -= dx[direc]
    y2, x2 = dot2
    ny2 = y2 + dy[direc]
    nx2 = x2 + dx[direc]
    while dotfield[ny2][nx2] != '#' and (ny2, nx2) != (ny, nx):
        if dotfield[ny2][nx2] == 'O':
            ny2, nx2 = (-1, -1)
            break
        ny2 += dy[direc]
        nx2 += dx[direc]
    if (ny2, nx2) != (-1, -1):
        ny2 -= dy[direc]
        nx2 -= dx[direc]
    if (ny, nx) == (y, x):
        ny, nx = -2, -2
    if (ny2, nx2) == (y2, x2):
        ny2, nx2 = -2, -2
    return (ny, nx, ny2, nx2)

def BT(cnt, lst):
    global red, blue, result
    if cnt > 10 or cnt >= result: return
    for i in lst:
        if i == 0:
            if red[1] <= blue[1]:
                by, bx, ry, rx = Movepoint(blue, red, i)
            elif red[1] > blue[1]:
                ry, rx, by, bx = Movepoint(red, blue, i)
        elif i == 1:
            if red[0] <= blue[0]:
                by, bx, ry, rx = Movepoint(blue, red, i)
            elif red[0] > blue[0]:
                ry, rx, by, bx = Movepoint(red, blue, i)
        elif i == 2:
            if red[1] <= blue[1]:
                ry, rx, by, bx = Movepoint(red, blue, i)
            elif red[1] > blue[1]:
                by, bx, ry, rx = Movepoint(blue, red, i)
        elif i == 3:
            if red[0] <= blue[0]:
                ry, rx, by, bx = Movepoint(red, blue, i)
            elif red[0] > blue[0]:
                by, bx, ry, rx = Movepoint(blue, red, i)
        # print(ry, rx, by, bx)
        if ry == rx == by == bx == -2: continue
        if ry == -1:
            if by == -1:
                continue
            else:
                result = cnt
                return
        elif by == -1:
            continue
        tempblue = blue
        tempred = red
        if (by, bx) != (-2, -2):
            blue = (by, bx)
        if (ry, rx) != (-2, -2):
            red = (ry, rx)
        # print(red, blue)
        if i == 0 or i == 2:
            BT(cnt+1, [1,3])
        elif i == 1 or i == 3:
            BT(cnt+1, [0, 2])
        red = tempred
        blue = tempblue

N, M = map(int, input().split())
field = [list(input()) for j in range(N)]
dotfield = [[field[i][j] if field[i][j] not in ('R', 'B') else '.' for j in range(M)] for i in range(N)]
red = blue = None
result = 11

for i in range(N):
    for j in range(M):
        if field[i][j] == 'R': red = (i, j)
        elif field[i][j] == 'B': blue = (i, j)

BT(1, [0,1,2,3])
if result == 11: result = -1
print(result)

# for _ in range(len(dotfield)):
#     print(dotfield[_])