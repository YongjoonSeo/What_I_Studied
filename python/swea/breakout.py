def Brokenbricks(y, x, num, arr):
    if num == 0: return set()
    if num == 1: return {(y, x, num)}
    tempset = {(y, x, num)}
    arr[y][x] = 1
    l = r = u = d = 1
    while x-l >= 0 and l < num:
        if field[y][x-l] and not arr[y][x-l]:
            arr[y][x-l] = 1
            tempset.update(Brokenbricks(y, x-l, field[y][x-l], arr))
        l += 1
    while x+r < W and r < num:
        if field[y][x+r] and not arr[y][x+r]:
            arr[y][x+r] = 1
            tempset.update(Brokenbricks(y, x+r, field[y][x+r], arr))
        r += 1
    while y-u >= 0 and u < num:
        if field[y-u][x] and not arr[y-u][x]:
            arr[y-u][x] = 1
            tempset.update(Brokenbricks(y-u, x, field[y-u][x], arr))
        u += 1
    while y+d < H and d < num:
        if field[y+d][x] and not arr[y+d][x]:
            arr[y+d][x] = 1
            tempset.update(Brokenbricks(y+d, x, field[y+d][x], arr))
        d += 1
    return tempset

def BT(times):
    global W, H, result
    if times == 0: 
        cnt = 0
        for i in range(H):
            for j in range(W):
                if field[i][j] > 0: cnt += 1
        result = min(result, cnt)
        return
    for i in range(W):
        start = 0
        while start < H and not field[start][i] : start += 1
        if start == H: continue
        visited = [[0 for i in range(W)] for j in range(H)]
        bricks = Brokenbricks(start, i, field[start][i], visited)
        for brick in bricks:
            y, x, num = brick
            field[y][x] = 0
            
        temp = 0
        for row in field:
            temp += sum(row)
        if temp == 0: 
            result = 0
            return
        
        rest = set()
        for m in range(W):
            idx = H-1
            for n in range(-1,-H-1,-1):
                if field[n][m] > 0:
                    rest.add((n, m, field[n][m]))
                    field[n][m], field[idx][m] = field[idx][m], field[n][m]
                    idx -= 1
        BT(times-1)
        for brick in rest:
            y, x, num = brick
            field[y][x] = num
        for brick in bricks:
            y, x, num = brick
            field[y][x] = num

T = int(input())
for t in range(1, T+1):
    N, W, H = map(int, input().split())
    field = [list(map(int, input().split())) for j in range(H)]
    result = 200

    BT(N)
    print('#{0} {1}'.format(t, result))

    # visited = [[0 for i in range(W)] for j in range(H)]
    # print(sorted(list(Brokenbricks(2,2,field[2][2], visited))))


    # for _ in range(len(field)):
    #     print(field[_])