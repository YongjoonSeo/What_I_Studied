def Dirnum(field, inpy, inpx):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    x, y = inpx, inpy
    cnt = 0

    for i in range(4):
        if field[y+dy[idx]][x+dx[idx]] == 0:
            cnt += 1
        idx = (idx + 1) % 4
    
    return cnt

def Search(field, inpy, inpx):
    global visited
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    idx = 0
    x, y = inpx, inpy
    stack = []

    while True:
        field[y][x] = 9
        dirnum = Dirnum(field, y, x)

        for i in range(4):
            if field[y+dy[i]][x+dx[i]] == 0:
                idx = i
                break
            elif field[y+dy[i]][x+dx[i]] == 3:
                return 1
        
        if dirnum >= 2:
            visited[y][x] = 1
            stack.append((y,x))

        # if dirnum == 1:
        #     y,x = stack.pop()
        #     stack.append((y+dy[idx], x+dx[idx]))
        # elif dirnum > 1:
        #     stack.append((y+dy[idx], x+dx[idx]))
        # else:
        #     if stack:
        #         y,x = stack.pop()
        #         continue
        #     else:
        #         return 0
        # x, y = x+dx[idx], y+dy[idx]

        if dirnum == 1:
            if visited[y][x]: y, x = stack.pop()
        elif dirnum == 0:
            if stack:
                y, x = stack[-1]
                continue
            else:
                return 0
        x, y = x + dx[idx], y + dy[idx]
    
for t in range(1,11):
    T = int(input())
    maze = []
    startx = starty = 0
    for i in range(16):
        tempstr = input()
        templst = []
        for j in range(len(tempstr)):
            templst.append(int(tempstr[j]))
            if int(tempstr[j]) == 2:
                startx, starty = i, j
        maze.append(templst)
    visited = [[0 for i in range(16)] for j in range(16)]
    
    result = Search(maze, starty, startx)
    print('#{0} {1}'.format(T, result))
    



    # for _ in range(len(maze)):
    #     print(*maze[_], sep=' ')