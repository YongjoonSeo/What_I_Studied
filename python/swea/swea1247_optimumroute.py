def BT(x, y, dist):
    global result, N, house

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            nx, ny = clients[i]
            BT(nx, ny, dist + abs(x-nx) + abs(y-ny))
            visited[i] = 0
    else:
        for k in visited:
            if not k: return
        hx, hy = house
        tempresult = dist + abs(x-hx) + abs(y-hy)
        result = min(tempresult, result)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    visited = [0 for i in range(N)]
    company = house = 0
    clients = []
    result = float('inf')

    for i in range(0, len(lst), 2):
        x, y = lst[i], lst[i+1]
        if i == 0: company = (x,y)
        elif i == 2: house = (x,y)
        else: clients.append((x,y))
    
    cx, cy = company
    BT(cx, cy, 0)
    print('#{0} {1}'.format(t, result))