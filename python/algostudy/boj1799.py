# 비숍 - 대각선으로 움직인다
# 비숍이 놓일 수 없는 곳이 있을 때, 서로가 서로를 잡을 수 없도록 비숍을 넣는다.
# (비숍이 놓일 수 없는 곳을 지나갈 수는 있다) 비숍을 놓을 수 있는 곳 - 1
# 출력 : 놓을 수 있는 비숍의 최대 개수

# if 놓일 수 있는 곳이면 놓는다.
# 비숍 하나 놓을 때마다 대각선 '빈 곳'을 채워둔다. 이 좌표들을 잠깐 저장하고, 백트래킹할 때 원상복귀한다.
# -> 카운트도 원상복귀한다
# 맵의 빈 곳을 카운트해둔다. 빈 곳이 없다면 그때 max(그때의 비숍 개수, result).
# (빈 곳이란, 비숍이 들어갈 수 있는 곳이다)
# 홀수칸 짝수칸 나눌 수 있다......!!

def tempchange(y, x):
    global field, spacecnt
    field[y][x] = 0
    spacecnt -= 1
    return (y, x)

def route(i, j):
    global field, N
    m = n = a = b = 1
    while 0 <= i+m < N and 0 <= j+m < N:
        if field[i+m][j+m]:
            yield tempchange(i+m, j+m)
        m += 1
    while 0 <= i-n < N and 0 <= j-n < N:
        if field[i - n][j - n]:
            yield tempchange(i-n, j-n)
        n += 1
    while 0 <= i+a < N and 0 <= j-a < N:
        if field[i + a][j - a]:
            yield tempchange(i+a, j-a)
        a += 1
    while 0 <= i-b < N and 0 <= j+b < N:
        if field[i - b][j + b]:
            yield tempchange(i-b, j+b)
        b += 1

def BT(rest, bishop=0):
    global spacecnt, N, result
    if spacecnt + bishop <= result: return
    if spacecnt == 0: result = max(result, bishop)
    savecoors = []
    istart = rest // N
    for i in range(istart, N):
        for j in range(N):
            if field[i][j]:
                savecoors.append((i,j))
                field[i][j] = 0
                spacecnt -= 1
                for m, n in route(i, j):
                    savecoors.append((m,n))
                BT(i*N+j, bishop+1)
                # if spacecnt: return
                spacecnt += len(savecoors)
                for coor in savecoors:
                    field[coor[0]][coor[1]] = 1


N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
bishopcnt = 0
spacecnt = 0
result = -1
for i in range(N):
    for j in range(N):
        if field[i][j]:
            spacecnt += 1

BT(0, 0)
print(result)

# for i in range(N):
#     for j in range(N):
#         if field[i][j]:
#             tempsave = []
#             tempsave.append((i,j))
#             field[i][j] = 0
#             spacecnt -= 1
#             for m, n in route(i, j):
#                 tempsave.append((m,n))
#             BT(i, j)
#             spacecnt += len(tempsave)
#             for y, x in tempsave:
#                 field[y][x] = 1

# for _ in range(len(field)):
#     print(field[_])