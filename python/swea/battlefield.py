def move(direc):
    global H, W, y, x
    if direc == 'U':
        if y - 1 >= 0 and field[y-1][x] not in ('-', '*', '#'):
            field[y-1][x] = '^'
            field[y][x] = '.'
            y = y - 1
        else:
            field[y][x] = '^'
    elif direc == 'D':
        if y + 1 < H and field[y+1][x] not in ('-', '*', '#'):
            field[y+1][x] = 'v'
            field[y][x] = '.'
            y = y + 1
        else:
            field[y][x] = 'v'
    elif direc == 'L':
        if x - 1 >= 0 and field[y][x-1] not in ('-', '*', '#'):
            field[y][x-1] = '<'
            field[y][x] = '.'
            x = x - 1
        else:
            field[y][x] = '<'
    else:
        if x + 1 < W and field[y][x+1] not in ('-', '*', '#'):
            field[y][x+1] = '>'
            field[y][x] = '.'
            x = x + 1
        else:
            field[y][x] = '>'

def shoot():
    global H, W, y, x
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    for i in range(4):
        if ('>', 'v', '<', '^')[i] == field[y][x]:
            idx = i
            break
    nx, ny = x + dx[idx], y + dy[idx]
    while 0 <= nx < W and 0 <= ny < H:
        if field[ny][nx] == '*': 
            field[ny][nx] = '.'
            break
        elif field[ny][nx] == '#': break
        nx += dx[idx]
        ny += dy[idx]

T = int(input())
for t in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for j in range(H)]
    N = int(input())
    lst = list(input())

    x = y = 0
    TF = False
    for i in range(H):
        for j in range(W):
            if field[i][j] in ('^', 'v', '<', '>'):
                x, y = j, i
                TF = True
                break
        if TF: break

    for order in lst:
        if order == 'S':
            shoot()
        else:
            move(order)

    print('#{0}'.format(t), end=' ')
    for _ in range(len(field)):
        print(''.join(field[_]))
    # print(lst)