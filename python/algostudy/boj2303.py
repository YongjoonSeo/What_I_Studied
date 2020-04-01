def MaxUnits(lst):
    result = 0
    for i in range(len(lst)-2):
        for j in range(i+1, len(lst)-1):
            for k in range(j+1, len(lst)):
                temp = lst[i] + lst[j] + lst[k]
                temp %= 10
                if temp > result:
                    result = temp
    return result

N = int(input())
result = (0, 0)
for i in range(1, N+1):
    cards = list(map(int, input().split()))
    val = MaxUnits(cards)
    if result[1] <= val:
        result = (i, val)
print(result[0])