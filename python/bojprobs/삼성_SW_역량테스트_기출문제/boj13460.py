def findcoor(y, x, direc):
    global N, M
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ny = y + dy[direc]
    nx = x + dx[direc]
    if 0 <= ny < N and 0 <= nx < M and field[ny][nx] != '#' and field[ny][nx] != 'R' and field[ny][nx] != 'B':
        while 0 <= ny < N and 0 <= nx < M and field[ny][nx] != '#' and field[ny][nx] != 'R' and field[ny][nx] != 'B':
            if field[ny][nx] == 'O':
                return (ny, nx, field[ny][nx])
            ny += dy[direc]
            nx += dx[direc]
        ny -= dy[direc]
        nx -= dx[direc]
        return (ny, nx, field[ny][nx])
    else:
        return (y, x, field[y][x])

def BT(ry, rx, by, bx, times, prev):
    global result
    if times > 10 or times >= result: return
    for i in range(4):
        if abs(i-prev) == 2: continue
        if i == 0:
            if rx > bx:
                rry, rrx, rr = findcoor(ry, rx, i)
                if rr == 'O':
                    field[ry][rx] = '.'
                    rby, rbx, rb = findcoor(by, bx, i)
                    field[ry][rx] = 'R'
                    if rb == 'O':
                        result = -1
                        return
                    else:
                        result = times
                        return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                rby, rbx, rb = findcoor(by, bx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
            else:
                rby, rbx, rb = findcoor(by, bx, i)
                if rb == 'O':
                    result = -1
                    return
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                rry, rrx, rr = findcoor(ry, rx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                if rr == 'O':
                    result = times
                    return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
        elif i == 1:
            if ry > by:
                rry, rrx, rr = findcoor(ry, rx, i)
                if rr == 'O':
                    field[ry][rx] = '.'
                    rby, rbx, rb = findcoor(by, bx, i)
                    field[ry][rx] = 'R'
                    if rb == 'O':
                        result = -1
                        return
                    else:
                        result = times
                        return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                rby, rbx, rb = findcoor(by, bx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
            else:
                rby, rbx, rb = findcoor(by, bx, i)
                if rb == 'O':
                    result = -1
                    return
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                rry, rrx, rr = findcoor(ry, rx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                if rr == 'O':
                    result = times
                    return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
        elif i == 2:
            if rx < bx:
                rry, rrx, rr = findcoor(ry, rx, i)
                if rr == 'O':
                    field[ry][rx] = '.'
                    rby, rbx, rb = findcoor(by, bx, i)
                    field[ry][rx] = 'R'
                    if rb == 'O':
                        result = -1
                        return
                    else:
                        result = times
                        return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                rby, rbx, rb = findcoor(by, bx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
            else:
                rby, rbx, rb = findcoor(by, bx, i)
                if rb == 'O':
                    result = -1
                    return
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                rry, rrx, rr = findcoor(ry, rx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                if rr == 'O':
                    result = times
                    return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
        elif i == 3:
            if ry < by:
                rry, rrx, rr = findcoor(ry, rx, i)
                if rr == 'O':
                    field[ry][rx] = '.'
                    rby, rbx, rb = findcoor(by, bx, i)
                    field[ry][rx] = 'R'
                    if rb == 'O':
                        result = -1
                        return
                    else:
                        result = times
                        return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                rby, rbx, rb = findcoor(by, bx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
            else:
                rby, rbx, rb = findcoor(by, bx, i)
                if rb == 'O':
                    result = -1
                    return
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]
                rry, rrx, rr = findcoor(ry, rx, i)
                if ry == rry and rx == rrx and by == rby and bx == rbx:
                    continue
                if rr == 'O':
                    result = times
                    return
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                BT(rry, rrx, rby, rbx, times+1, i)
                field[ry][rx], field[rry][rrx] = field[rry][rrx], field[ry][rx]
                field[by][bx], field[rby][rbx] = field[rby][rbx], field[by][bx]

N, M = map(int, input().split())
field = [list(input()) for j in range(N)]
result = 11
blue = None
red = None

for i in range(N):
    for j in range(M):
        if field[i][j] == 'B': blue = [i, j]
        elif field[i][j] == 'R': red = [i, j]
        if blue and red: break
    if blue and red: break

BT(red[0], red[1], blue[0], blue[1], 1, 7)

if result == 11: result = -1

print(result)
# for _ in range(len(field)):
#     print(field[_])