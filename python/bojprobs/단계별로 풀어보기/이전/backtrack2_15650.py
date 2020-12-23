def BT(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r-1 == 0:
            yield [arr[i]]
        else:
            for j in BT(arr, i+1, r-1):
                yield [arr[i]] + j

N, M = map(int, input().split())
for i in BT(list(range(1, N+1)), 0, M):
    print(*i)