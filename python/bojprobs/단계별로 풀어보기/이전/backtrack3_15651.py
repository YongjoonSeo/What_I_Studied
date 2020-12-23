def BT(arr, start, r):
    for i in range(len(arr)):
        if start == r-1:
            yield [arr[i]]
        else:
            for j in BT(arr, start+1, r):
                yield [arr[i]] + j

N, M = map(int, input().split())
for i in BT(list(range(1, N+1)), 0, M):
    print(*i)

# def BT(arr, start, r):
#     for i in range(start, len(arr)):
#         arr[i], arr[start] = arr[start], arr[i]
#         if start == r-1:
#             yield [arr[start]]
#         else:
#             for j in BT(arr, start+1, r):
#                 yield [arr[start]] + j
#         arr[i], arr[start] = arr[start], arr[i]