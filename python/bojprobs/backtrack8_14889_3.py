from itertools import combinations

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
result = float('inf')

for case in combinations(range(N), N//2):
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