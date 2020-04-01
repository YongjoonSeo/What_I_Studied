def Collect(u, v, Y, X):
    global field, leng
    dx = [-1, 0]
    dy = [0, -1]
    for i in range(2):
        nx = X + dx[i]
        ny = Y + dy[i]
        if 0 <= nx < leng and 0 <= ny < leng:
            if field[ny][nx]: return []
    
    htop = vleft = hbot = vright = 0
    while Edge(Y, X+htop, leng-1, leng-1) and field[Y][X+htop]: htop += 1
    while Edge(Y+vleft, X, leng-1, leng-1) and field[Y+vleft][X]: vleft += 1
    while Edge(Y+vleft-1, X+hbot, leng-1, leng-1) and field[Y+vleft-1][X+hbot]: hbot += 1
    while Edge(Y+vright, X+htop-1, leng-1, leng-1) and field[Y+vright][X+htop-1]: vright += 1
    if htop == u:
        if Y + vleft - 1 + v < leng:
            if not (field[Y + vleft - 1 + v][X] and field[Y + vleft - 1 + v][X+u-1]): 
                tempfield = [[field[i][j] for j in range(X, X+u)] for i in range(Y, Y+vleft)]
                yield (tempfield, 0)
    if vleft == u:
        if X + htop - 1 + v < leng:
            if not (field[Y][X + htop - 1 + v] and field[Y+u-1][X + htop - 1 + v]): 
                tempfield = [[field[i][j] for j in range(X, X+htop)] for i in range(Y, Y+u)]
                yield (tempfield, 1)
    if hbot == u:
        if Y - v >= 0:
            if not (field[Y - v][X] and field[Y - v][X+u-1]): 
                tempfield = [[field[i][j] for j in range(X, X+u)] for i in range(Y, Y+vleft)]
                yield (tempfield, 2)
    if vright == u:
        if X - v >= 0:
            if not (field[Y][X - v] and field[Y+u-1][X - v]):
                tempfield = [[field[i][j] for j in range(X, X+htop)] for i in range(Y, Y+u)]
                yield (tempfield, 3)

def Edge(y, x, maxy, maxx):
    if 0 <= y <= maxy and 0 <= x <= maxx: return True
    return False

def Check(arr, idx, w, x, y):
    wcheck = xcheck = ycheck = 0
    lastv = len(arr)-1
    lasth = len(arr[0])-1
    if idx == 0:
        while Edge(lastv, wcheck, lastv, lasth) and arr[lastv][wcheck]: wcheck += 1
        while Edge(lastv, wcheck+ycheck, lastv, lasth) and not arr[lastv][wcheck+ycheck]: ycheck += 1
        while Edge(lastv-xcheck, wcheck, lastv, lasth) and not arr[lastv-xcheck][wcheck]: xcheck += 1
        for i in range(lastv - xcheck + 1, lastv + 1):
            for j in range(wcheck, wcheck + ycheck):
                if arr[i][j]: return False
    elif idx == 1:
        while Edge(lastv-wcheck, lasth, lastv, lasth) and arr[lastv-wcheck][lasth]: wcheck += 1
        while Edge(lastv-wcheck-ycheck, lasth, lastv, lasth) and not arr[lastv-wcheck-ycheck][lasth]: ycheck += 1
        while Edge(lastv-wcheck, lasth-xcheck, lastv, lasth) and not arr[lastv-wcheck][lasth-xcheck]: xcheck += 1
        for i in range(lastv - wcheck, lastv-wcheck-ycheck, -1):
            for j in range(lasth, lasth-xcheck, -1):
                if arr[i][j]: return False
    elif idx == 2:
        while Edge(0, lasth-wcheck, lastv, lasth) and arr[0][lasth-wcheck]: wcheck += 1
        while Edge(0, lasth-wcheck-ycheck, lastv, lasth) and not arr[0][lasth-wcheck-ycheck]: ycheck += 1
        while Edge(xcheck, lasth-wcheck, lastv, lasth) and not arr[xcheck][lasth-wcheck]: xcheck += 1
        for i in range(xcheck):
            for j in range(lasth - wcheck, lasth - wcheck - ycheck, -1):
                if arr[i][j]: return False
    else:
        while Edge(wcheck, 0, lastv, lasth) and arr[wcheck][0]: wcheck += 1
        while Edge(wcheck+ycheck, 0, lastv, lasth) and not arr[wcheck+ycheck][0]: ycheck += 1
        while Edge(wcheck, xcheck, lastv, lasth) and not arr[wcheck][xcheck]: xcheck += 1
        for i in range(wcheck, wcheck + ycheck):
            for j in range(xcheck):
                if arr[i][j]: return False
    if wcheck == w and xcheck == x and ycheck == y:
        return True
    return False

leng = int(input())
u, v, w, x, y = map(int, input().split())
field = [[i for i in list(map(int, input().split()))] for j in range(leng)]
cnt = 0
result =[]

for i in range(leng):
    for j in range(leng):
        if field[i][j] == 1:
            temp = (i+1, j+1)
            for sample in Collect(u, v, i, j):
                if sample:
                    if Check(sample[0], sample[1], w, x, y):
                        result.append(temp)
                        cnt += 1
print(cnt)
for i in result:
    print(*i)

# for temp in Collect(u, v, 12, 4):
#     for _ in range(len(temp[0])):
#         print(temp[0][_])
#     print(Check(temp[0], temp[1], w, x, y))

# for _ in range(len(tempfield)):
#     print(tempfield[_])
# for _ in range(len(field)):
#     print(field[_])