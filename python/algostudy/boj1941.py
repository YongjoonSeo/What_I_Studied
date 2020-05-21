# 5*5 정사각형 격자 자리배치
# 7명, 가로나 세로로 인접, 이다솜파가 4명 이상이어야 한다.('S')
# 전체 맵을 돌면서 각 지점에서 모든 경우의 수를 다 찾고 나면 visited 하고 경우의 수 찾기
# Y가 4개이상 되는 순간부터 자르고, 7명에서 가능하면 카운트
# -->> 일렬로만 가는 게 아니다!

# def BT(y,x,num,idx):
#     global cnt
#     if num >= 4 or idx < 1: return
#     if idx == 1:
#         cnt += 1
#         return
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#     lst = []
#
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
#             possible[ny][nx] = 1
#             lst.append((ny,nx))
#
#     for coor in lst:
#         i, j = coor
#         visited[i][j] = 1
#         if field[i][j] == 'Y':
#             BT(i, j, num + 1, idx - 1)
#         else:
#             BT(i, j, num, idx - 1)
#         visited[i][j] = 0

    # for i in range(5):
    #     for j in range(5):
    #         if possible[i][j]:
    #             possible[i][j] = 0
    #             visited[i][j] = 1
    #             if field[i][j] == 'Y':
    #                 BT(i, j, num+1, idx-1)
    #             else:
    #                 BT(i, j, num, idx-1)
    #             possible[i][j] = 1
    #             visited[i][j] = 0

#     for coor in lst:
#         i, j = coor
#         possible[i][j] = 0
#
# field = [list(input()) for j in range(5)]
# visited = [[0 for i in range(5)] for j in range(5)]
# cnt = 0
# possible = [[0 for i in range(5)] for j in range(5)]
#
# for i in range(5):
#     for j in range(5):
#         visited[i][j] = 1
#         if field[i][j] == 'Y':
#             BT(i,j,1,7)
#         else:
#             BT(i,j,0,7)
#
# print(cnt)
# for i in range(len(field)):
#     print(field[i])

# 인접해있는지 체크하며 조합으로 세어보자.
def DFS(dot, lst):
    y, x = dot
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5 and possible[ny][nx]:
            possible[ny][nx] = 0
            lst.remove((ny, nx))
            DFS((ny,nx), lst)

def combi(arr, start, r):
    if r < 1 or not arr: return [[]]
    for i in range(start, len(arr)-r+1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combi(arr, i+1, r-1):
                yield [arr[i]] + j


field = [list(input()) for j in range(5)]
possible = [[0 for i in range(5)] for j in range(5)]
Y = []
S = []
sl = yl = None
cnt = 0
for i in range(5):
    for j in range(5):
        if field[i][j] == 'Y': Y.append((i,j))
        else: S.append((i,j))
if len(S) > 7:
    sl = 7
else:
    sl = len(S)
if len(Y) > 3:
    yl = 3
else:
    yl = len(Y)
if len(S) <= 3:
    print(0)
else:
    for i in range(7-sl, 1+yl):
        j = 7-i
        for scoor in combi(S, 0, j):
            if i == 0:
                check = scoor[:]
                for c in check:
                    possible[c[0]][c[1]] = 1
                DFS(check[0], check)
                if not check:
                    cnt += 1
                for c in check:
                    possible[c[0]][c[1]] = 0
            else:
                for ycoor in combi(Y, 0, i):
                    check = scoor[:]
                    check.extend(ycoor)
                    for c in check:
                        possible[c[0]][c[1]] = 1
                    DFS(check[0], check)
                    if not check:
                        cnt += 1
                    for c in check:
                        possible[c[0]][c[1]] = 0
    print(cnt)