T = int(input())
for t in range(1, T+1):
    W, H, N = map(int, input().split())
    result = 0
    sx, sy = map(int, input().split())
    for i in range(N-1):
        x, y = map(int, input().split())
        if (x > sx and y > sy) or (x < sx and y < sy):
            if abs(x - sx) > abs(y - sy): result += abs(x - sx)
            else: result += abs(y - sy)
        else:
            result += abs(x - sx) + abs(y - sy)
        sx, sy = x, y
    print('#{0} {1}'.format(t, result))