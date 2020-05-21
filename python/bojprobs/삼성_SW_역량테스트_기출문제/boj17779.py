# N x N 격자, r행 c열 (r,c)
# 5개의 선거구로 나눠야하고, 각 구역(격자의 각 칸)은 5개 선거구 중 하나에 포함되어야 한다.
# 5개 선거구는 적어도 하나의 구역 포함, 한 선거구의 구역은 모두 연결
# 경계선 - 마름모의 왼쪽 꼭지점이 (x,y) (1부터 시작 -> 1이라도 맨 첫번째 칸도 포함해서 시작)
## ----->>>>>>>>>>>> 마름모의 위쪽 꼭지점이 시작점이다.. 그림의 x, y는 사실 행, 열을 나타낸다.
# 인구가 가장 많은 선거구와 가장 적은 선거구 인구 차이의 최솟값?

# def x,y,d1,d2 조합 가능한지
# def x,y,d1,d2 입력 -> 그에 맞는 선거구 좌표들 쭉 뽑아서 총 인구를 구해주는 함수
# -> 5번 선거구 테두리를 골라서 모두 바꿔주고 안에서는 DFS로 좌표 구하기 -> 원래 값은 되돌려주기
# def 선거구 최대인구, 최소인구 backtrack (x,y,d1,d2 조합해가면서) -> result보다 구한 값이 크면 걸러내기, 조합 불가능하면 걸러내기
from collections import deque

def is_possible(x, y, d1, d2):
    if x >= 0 and x+d1+d2 < N and y-d1 >= 0 and y + d2 < N: return True
    return False

def populations(x, y, d1, d2):
    global N
    lst = [(x,y,field[y][x])]
    field[y][x] = 0
    i = j = 1
    while i != d1:
        lst.append((x+i, y-i, field[y-i][x+i]))
        field[y-i][x+i] = 0
        i += 1
    while j != d2:
        lst.append((x+j, y+j, field[y+j][x+j]))
        field[y+j][x+j] = 0
        j += 1
    ux, uy, dx, dy = x+d1, y-d1, x+d2, y+d2
    lst.append((ux, uy, field[uy][ux]))
    lst.append((dx, dy, field[dy][dx]))

    field[uy][ux] = 0
    field[dy][dx] = 0
    i = j = 1
    while i != d2+1:
        lst.append((ux+i, uy+i, field[uy+i][ux+i]))
        field[uy+i][ux+i] = 0
        i += 1
    while j != d1:
        lst.append((dx+j, dy-j, field[dy-j][dx+j]))
        field[dy-j][dx+j] = 0
        j += 1
    temp = []
    tempprint = [[] for i in range(5)]
    regions = [0] * 5
    for i in range(N):
        for j in range(N):
            if field[i][j]:
                if 1 <= i < N - 1 and 1 <= j < N - 1 and field[i - 1][j] == 0 and field[i + 1][j] == 0 and field[i][j - 1] == 0 and field[i][j + 1] == 0:
                    regions[4] += field[i][j]
                    tempprint[4].append((i,j))
                    temp.append((i,j))
                elif i < x + d1 and j <= y:
                    regions[0] += field[i][j]
                    tempprint[0].append((i,j))
                elif i <= x + d2 and y < j:
                    regions[1] += field[i][j]
                    tempprint[1].append((i,j))
                elif x + d1 <= i and j < y - d1 + d2:
                    regions[2] += field[i][j]
                    tempprint[2].append((i,j))
                elif x + d2 < i and y - d1 + d2 <= j:
                    regions[3] += field[i][j]
                    tempprint[3].append((i,j))
    if (y,x+1) not in temp:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        q = deque()
        q.append((y, x+1))
        lst.append((x+1, y, field[y][x+1]))
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if field[ny][nx]:
                    q.append((ny, nx))
                    lst.append((nx, ny, field[ny][nx]))
                    field[ny][nx] = 0

    for dot in lst:
        x, y, val = dot
        regions[4] += val
        tempprint[4].append((y,x))
        # field[y][x] = val
    if max(regions) - min(regions) == 15:
        for i in range(5):
            print(tempprint[i])
        print('----------tempprint')
        for i in range(N):
            print(field[i])
        print(temp, end='---\n')
    for dot in lst:
        x, y, val = dot
        field[y][x] = val
    return max(regions) - min(regions)

def BT():
    global N
    result = float('inf')
    for i in range(1, N-1):
        for j in range(N-2):
            for d1 in range(1, N-1):
                for d2 in range(1, N-1):
                    if is_possible(j, i, d1, d2):
                        if populations(j, i, d1, d2) == 15:
                            print(populations(j, i, d1, d2), end='---///-\n')
                        result = min(result, populations(j, i, d1, d2))
    return result

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
print(BT())


# print(populations(1, 4, 3, 2))