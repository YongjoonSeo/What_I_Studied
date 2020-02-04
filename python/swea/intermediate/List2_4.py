T = int(input())
for i in range(1, T+1):
    int(input())
    result = []
    raw = list(map(int, input().split()))
    raw.sort()
    for _ in range(5):
        result.append(raw.pop())
        result.append(raw.pop(0))
    
    print('#{0}'.format(i), end=' ')
    print(*result)