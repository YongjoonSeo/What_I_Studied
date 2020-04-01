from collections import deque 
# import sys

# sys.stdin = open('test.txt', 'r')

def BFS():
    global fire, person, w, h
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for i in range(w)] for j in range(h)]
    fireq = deque()
    fireq.extend(fire)
    pq = deque()
    pq.append(person)
    cnt = 0
    if person[0] == 0 or person[0] == h-1 or person[1] == 0 or person[1] == w-1:
        return 1

    while pq:
        cnt += 1
        for _ in range(len(fireq)):
            vy, vx = fireq.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if 0 <= ny < h and 0 <= nx < w and field[ny][nx] in ('.', '@'):
                    field[ny][nx] = '*'
                    fireq.append((ny,nx))
        
        for _ in range(len(pq)):
            vy, vx = pq.popleft()
            for i in range(4):
                ny = vy + dy[i]
                nx = vx + dx[i]
                if 0 <= ny < h and 0 <= nx < w and field[ny][nx] == '.':
                    if ny == 0 or ny == h-1 or nx == 0 or nx == w-1:
                        cnt += 1
                        return cnt
                    else:
                        field[ny][nx] = '@'
                        pq.append((ny, nx))
    else:
        return 'IMPOSSIBLE'

T = int(input())
for t in range(T):
    w, h = map(int, input().split())
    field = [list(input()) for j in range(h)]
    person = None
    fire = []

    for i in range(h):
        for j in range(w):
            if field[i][j] == '@': person = (i,j)
            elif field[i][j] == '*': fire.append((i,j))
    
    print(BFS())

    # for _ in range(len(field)):
    #     print(field[_])