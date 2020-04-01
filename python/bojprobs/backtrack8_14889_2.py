def Combinations(arr, start, r):
    for i in range(start, len(arr) -r + 1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in Combinations(arr, i+1, r-1):
                yield [arr[i]] + j

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
result = float('inf')

for case in Combinations(range(N), 0, N//2):
    rest = set(range(N)) - set(case)
    startteam = linkteam = 0
    for i in case:
        for j in case:
            startteam += field[i][j]
    for i in rest:
        for j in rest:
            linkteam += field[i][j]
    result = min(result, abs(startteam-linkteam))

print(result)


# for _ in range(len(field)):
#     print(field[_])

# for case in Combinations(range(6), 0, 3):
#     print(case, end=' ')