# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     lst.sort()
#     result = []

#     for i in range(1 << N):
#         temp = 0
#         for j in range(N):
#             if i & (1 << j):
#                 temp += lst[j]
#         if temp not in set(result): result.append(temp)

#     print('#{0} {1}'.format(t, len(result)))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    result = set()
    result.add(0)
    for num in lst:
        temp = list(result)
        for i in temp:
            result.add(i+num)
    print('#{0} {1}'.format(t, len(result)))
