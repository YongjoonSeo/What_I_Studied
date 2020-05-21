# 맨 위에서부터 훑으니까 갈 수 없는 길이면 다시 안 가게 해두는 건 어떨까?
# (왜냐면 더 위쪽으로는 갈 길이 없는 경우에 backtrack으로 돌아오는 거니까 그 가지는 모두 잘라내는 것)

def BT(y, x):
    global C, cnt, isfound
    if x == C:
        cnt += 1
        isfound = True
        return
    dy = [-1, 0, 1]

    for i in range(3):
        ny = y + dy[i]
        if 0 <= ny < R and field[ny][x] == '.':
            field[ny][x] = 'x'
            BT(ny, x+1)
            if isfound: return


R, C = map(int, input().split())
field = [list(input()) for j in range(R)]
dy = [-1, 0, 1]
cnt = 0

for i in range(R):
    isfound = False
    BT(i, 1)

print(cnt)