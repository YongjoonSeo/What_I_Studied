# def Permu(arr, start, r):
#     for i in range(start, len(arr)):
#         arr[start], arr[i] = arr[i], arr[start]
#         if r-1 == 0:
#             yield [arr[start]]
#         else:
#             for j in Permu(arr, start+1, r-1):
#                 yield [arr[start]] + j
#         arr[start], arr[i] = arr[i], arr[start]

def BT(n, inp, k, temp):
    if inp == k: 
        result.append(temp)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            temp.append(i)
            BT(n, inp, k+1, temp[:])
            visited[i] = 0
            temp.remove(i)

N, M = map(int, input().split())
result = []
visited = [0 for i in range(N+1)]
BT(N, M, 0, [])
for i in result:
    print(*i)

