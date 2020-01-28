T = int(input())
for i in range(1, T+1):
    N = int(input())
    red = set()
    blue = set()
    for j in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        temp = tuple((x,y) for x in range(x1, x2+1) for y in range(y1, y2+1))
        if color == 1:
            red.update(temp)
        else:
            blue.update(temp)
    result = len(red & blue)
    print('#{0} {1}'.format(i, result))