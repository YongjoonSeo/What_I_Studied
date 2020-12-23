N, M = map(int, input().split())
result = 0
cards = list(map(int, input().split()))

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            temp = cards[i] + cards[j] + cards[k]
            if temp > result and temp <= M:
                result = temp

print(result)