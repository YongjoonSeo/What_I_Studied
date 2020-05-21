# 크기 N x N 격자
# (r, c) == r행 c열 (1부터 시작) (본문의 x가 y(행)이고 y가 x(열)이다)
# 5개 선거구로 나눈다
# -> 각 선거구는 적어도 하나의 구역을 포함, 각 구역은 5개의 선거구 중 하나에 포함
# 선거구 나누는 방법 - 기준점과 경계의 길이를 정해서 마름모꼴로 만든다.
# -> 마름모의 윗쪽 꼭지점이 시작점.
# 선거구의 인구는 선거구 구역의 인구를 모두 합한 값
# 출력 -> 인구가 가장 많은 선거구와 가장 적은 선거구의 "인구 차이의 최솟값" 출력
# def 조건을 만족하는지 (y, x, d1, d2) 입력 -> T, F 출력
# def (y, x, d1, d2) 입력 -> 선거구 인구 차이의 최솟값 출력
# def 경우의 수 순회하면서 모든 경우 탐색 (입력 X) -> 최솟값의 최솟값 result 출력
from collections import deque

def ispossible(y, x, d1, d2):
    if y+d1+d2 < N and x-d1 >= 0 and x+d2 < N: return True
    return False

def population(y, x, d1, d2):
    global N
    lst = [(y, x, field[y][x])]
    field[y][x] = 0
    i = j = 1
    while i != d1:
        lst.append((y+i, x-i, field[y+i][x-i]))
        field[y+i][x-i] = 0
        i += 1
    while j != d2:
        lst.append((y+j, x+j, field[y+j][x+j]))
        field[y + j][x + j] = 0
        j += 1
    ly, lx, ry, rx = y+i, x-i, y+j, x+j
    lst.append((ly, lx, field[ly][lx]))
    field[ly][lx] = 0
    lst.append((ry, rx, field[ry][rx]))
    field[ry][rx] = 0
    i = j = 1
    while i != d2+1:
        lst.append((ly+i, lx+i, field[ly+i][lx+i]))
        field[ly+i][lx+i] = 0
        i += 1
    while j != d1:
        lst.append((ry+j, rx-j, field[ry+j][rx-j]))
        field[ry + j][rx - j] = 0
        j += 1
    if field[y+1][x] and field[y+2][x]:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        q = deque()
        q.append((y+1, x))
        lst.append((y + 1, x, field[y + 1][x]))
        field[y+1][x] = 0
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if field[ny][nx]:
                    lst.append((ny, nx, field[ny][nx]))
                    field[ny][nx] = 0
                    q.append((ny, nx))

    regions = [0 for i in range(5)]
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                if 1 <= i < N-1 and 1 <= j < N-1 and not field[i - 1][j] and not field[i + 1][j] and not field[i][j - 1] and not field[i][j + 1]:
                    regions[4] += field[i][j]
                elif i < y+d1 and j <= x: regions[0] += field[i][j]
                elif i <= y+d2 and x < j: regions[1] += field[i][j]
                elif y+d1 <= i and j < x-d1+d2: regions[2] += field[i][j]
                elif y+d2 < i and j >= x-d1+d2: regions[3] += field[i][j]

    for dot in lst:
        y, x, val = dot
        regions[4] += val
        field[y][x] = val

    # if max(regions) - min(regions) == 20:
    #     print('----after district 5----')
    #     for _ in range(len(field)):
    #         print(field[_])

    # for dot in lst:
    #     y, x, val = dot
    #     field[y][x] = val

    # if max(regions) - min(regions) == 20:
    #     print('----after all----')
    #     for _ in range(len(field)):
    #         print(field[_])
    #     print(lst)
    #     print('--case ended--')

    return max(regions) - min(regions)

def BT():
    global N
    result = float('inf')
    for i in range(N-2):
        for j in range(1, N-1):
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    if ispossible(i, j, d1, d2):
                        result = min(result, population(i, j, d1, d2))
    return result

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
print(BT())

# for _ in range(len(field)):
#     print(field[_])