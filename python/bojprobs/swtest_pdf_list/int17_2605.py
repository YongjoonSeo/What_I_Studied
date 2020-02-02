N = int(input())
pick = list(map(int, input().split()))
result = []
for i in range(N):
    result.insert(len(result) - pick[i], i+1)
print(*result)