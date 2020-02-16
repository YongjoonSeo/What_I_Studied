def Bt(y, x):
    global cnt, N
    ny = y+1
    
    for nx in range(N):
        if ny < N and not (ny in row or nx in col or ny+nx in diagplus or nx-ny in diagminus):
            row.append(ny)
            col.append(nx)
            diagplus.append(nx+ny)
            diagminus.append(nx-ny)
            Bt(ny, nx)
            row.pop()
            col.pop()
            diagplus.pop()
            diagminus.pop()
            if ny == N-1: cnt += 1

N = int(input())
cnt = 0
if N == 1:
    print(1)
else:
    for i in range(N):
        row = [0]
        col = [i]
        diagplus = [i]
        diagminus = [i]
        Bt(0, i)
    print(cnt)