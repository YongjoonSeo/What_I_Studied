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

def BT(rest, bishop, idx):
    global spacecnt, N, tempresult
    if spacecnt + bishop <= tempresult: return
    if spacecnt == 0: tempresult = max(tempresult, bishop)
    savecoors = []
    istart = rest // N
    for i in range(istart, N):
        for j in range(N):
            if field[i][j] and idxfield[i][j] == idx:
                savecoors.append((i,j))
                field[i][j] = 0
                spacecnt -= 1
                for m, n in route(i, j):
                    savecoors.append((m,n))
                BT(i*N+j, bishop+1, idx)
                # if spacecnt: return
                spacecnt += len(savecoors)
                for coor in savecoors:
                    field[coor[0]][coor[1]] = 1


N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
idxfield = [0 if i&1 else 1 for i in range(N**2)]
idxfield = [idxfield[i:i+N] for i in range(0,N**2,N)]
bishopcnt = 0
spacecnt = 0
firstcnt = 0
tempresult = -1
for i in range(N):
    for j in range(N):
        if field[i][j]:
            if idxfield[i][j]:
                firstcnt += 1
            spacecnt += 1
secondcnt = spacecnt - firstcnt
spacecnt = firstcnt
BT(0, 0, 1)
result = tempresult
tempresult = -1
spacecnt = secondcnt
BT(0, 0, 0)
result += tempresult
print(result)