def BT(tempsum, start, end):
    global result, B
    if tempsum >= result: return
    if start == end:
        if B <= tempsum < result:
            result = tempsum
        return
    else:
        BT(tempsum + lst[start], start+1, end)
        BT(tempsum, start+1, end)

T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    result = 200001
    BT(0, 0, N)

    print('#{0} {1}'.format(t, result - B))