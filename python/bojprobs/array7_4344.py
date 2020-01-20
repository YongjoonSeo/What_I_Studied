C = int(input())
for _ in range(C):
    case = list(map(int, input().split()))
    wholenum = case[0]
    sum = ave = 0
    for i in range(1, wholenum + 1):
        sum += case[i]
    ave = sum / wholenum

    howmany = 0
    for j in range(1, wholenum + 1):
        if case[j] > ave:
            howmany += 1
    print('{0:0.3f}%'.format(howmany / wholenum * 100))