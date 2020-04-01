def Surveillance(y, x, val):
    global N, M
    right = []
    left = []
    up = []
    down = []

    i = j = n = m = 1
    while x+i < M and field[y][x+i] != 6:
        if field[y][x+i] not in (1, 2, 3, 4, 5, '#'):
            right.append((y, x+i))
        i += 1
    while x-j >= 0 and field[y][x-j] != 6:
        if field[y][x-j] not in (1, 2, 3, 4, 5, '#'):
            left.append((y, x-j))
        j += 1
    while y+n < N and field[y+n][x] != 6:
        if field[y+n][x] not in (1, 2, 3, 4, 5, '#'):
            down.append((y+n, x))
        n += 1
    while y-m >= 0 and field[y-m][x] != 6:
        if field[y-m][x] not in (1, 2, 3, 4, 5, '#'):
            up.append((y-m, x))
        m += 1

    if val == 1:
        return [right, left, up, down]
    elif val == 2:
        right.extend(left)
        up.extend(down)
        return [right, up]
    elif val == 3:
        lst1 = right[:]
        lst1.extend(up)
        right.extend(down)
        down.extend(left)
        left.extend(up)
        return [lst1, right, down, left]
    elif val == 4:
        lst1 = right[:]
        lst2 = left[:]
        lst1.extend(up)
        lst1.extend(down)
        lst2.extend(up)
        lst2.extend(down)
        down.extend(right)
        down.extend(left)
        up.extend(right)
        up.extend(left)
        return [lst1, down, lst2, up] 

def BT(depth):
    global result, N, M
    if depth == len(cctvs):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if field[i][j] == 0: cnt += 1
        result = min(cnt, result)
    else:
        y, x, val = cctvs[depth]
        for coordinates in Surveillance(y, x, val):
            if coordinates:
                for coordinate in coordinates:
                    sury, surx = coordinate
                    field[sury][surx] = '#'
                BT(depth + 1)
                for coordinate in coordinates:
                    sury, surx = coordinate
                    field[sury][surx] = 0
            else:
                BT(depth+1)

N, M = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
cctvs = []
result = float('inf')
fives = []

for i in range(N):
    for j in range(M):
        if field[i][j] >= 1 and field[i][j] <= 4:
            cctvs.append((i, j, field[i][j]))
        elif field[i][j] == 5:
            fives.append((i,j))

for five in fives:
    y, x = five
    i = j = n = m = 1
    while x+i < M and field[y][x+i] != 6:
        if field[y][x+i] not in (1, 2, 3, 4, 5):
            field[y][x+i] = '#'
        i += 1
    while x-j >= 0 and field[y][x-j] != 6:
        if field[y][x-j] not in (1, 2, 3, 4, 5):
            field[y][x-j] = '#'
        j += 1
    while y+n < N and field[y+n][x] != 6:
        if field[y+n][x] not in (1, 2, 3, 4, 5):
            field[y+n][x] = '#'
        n += 1
    while y-m >= 0 and field[y-m][x] != 6:
        if field[y-m][x] not in (1, 2, 3, 4, 5):
            field[y-m][x] = '#'
        m += 1
    

BT(0)

print(result)

# for _ in range(len(field)):
#     print(field[_])