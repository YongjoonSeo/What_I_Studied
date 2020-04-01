from collections import deque

def BFS(greenlst, redlst):
    global result, N, M
    cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    greenq = deque()
    greenq.extend(greenlst)
    redq = deque()
    redq.extend(redlst)
    for coor in greenq:
        visited[coor[0]][coor[1]] = 1
    for coor in redq:
        visited[coor[0]][coor[1]] = 1
    
    while greenq or redq:
        greenset = set()
        redset = set()
        tempgreen = []

        for _ in range(len(greenq)):
            vgy, vgx = greenq.popleft()

            for i in range(4):
                ngy = vgy + dy[i]
                ngx = vgx + dx[i]

                if 0 <= ngy < N and 0 <= ngx < M and not visited[ngy][ngx] and field[ngy][ngx]:
                    visited[ngy][ngx] = 2
                    tempgreen.append((ngy, ngx))
                    greenset.add((ngy, ngx))
                    greenq.append((ngy, ngx))
        
        for _ in range(len(redq)):
            vry, vrx = redq.popleft()

            for i in range(4):
                nry = vry + dy[i]
                nrx = vrx + dx[i]

                if 0 <= nry < N and 0 <= nrx < M and field[nry][nrx]:
                    if not visited[nry][nrx] or visited[nry][nrx] == 2:
                        visited[nry][nrx] = 1
                        redset.add((nry, nrx))
                        redq.append((nry, nrx))

        for temp in tempgreen:
            visited[temp[0]][temp[1]] = 1

        for coor in greenset&redset:
            cnt += 1
            greenq.remove(coor)
            redq.remove(coor)
        
    result = max(cnt, result)

def combi(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combi(arr, i+1, r-1):
                yield [arr[i]] + j

N, M, G, R = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
possible = []
result = -1

for i in range(N):
    for j in range(M):
        if field[i][j] == 2:
            possible.append((i,j))

for green in combi(possible, 0, G):
    redcandi = possible[:]
    for coor in green:
        redcandi.remove(coor)
    for red in combi(redcandi, 0, R):
        visited = [[0 for i in range(M)] for j in range(N)]
        BFS(green, red)

print(result)

# for test in combi([1,2,3,4,5], 0, 3):
#     print(test)

# for _ in range(len(field)):
#     print(field[_])