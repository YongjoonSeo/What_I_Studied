def Dragon(lst, k):
    global dots
    if k == 0: 
        dots = lst[:]
        return
    mat = [0, -1, 1, 0]
    refx, refy = lst[-1]
    newdots = lst[:-1]
    for i in range(-1, -len(lst)-1, -1):
        x, y = lst[i]
        nx, ny = x-refx, y-refy
        turnx, turny = mat[0]*nx + mat[1]*ny, mat[2]*nx + mat[3]*ny
        resx, resy = turnx+refx, turny+refy
        newdots.append((resx, resy))
    Dragon(newdots[:], k-1)

N = int(input())
field = [[0 for i in range(101)] for j in range(101)]
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dots = []
    curve = [(x,y)]
    if d == 0:
        curve.append((x+1, y))
    elif d == 1:
        curve.append((x, y-1))
    elif d == 2:
        curve.append((x-1, y))
    else:
        curve.append((x, y+1))
    Dragon(curve, g)
    for dot in dots:
        x, y = dot
        field[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        for n in range(2):
            TF = False
            for m in range(2):
                if not field[i+n][j+m]:
                    TF = True
                    break
            if TF: break
        else: cnt += 1

print(cnt)