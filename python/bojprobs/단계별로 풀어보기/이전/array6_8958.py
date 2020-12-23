N = int(input())
for _ in range(N):
    lst = list(input().split('X'))
    sum = 0
    for i in lst:
        if i != '':
            each = len(i) * (len(i) + 1) / 2
            sum += each
    print(int(sum))

