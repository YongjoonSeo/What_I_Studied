T = int(input())
for j in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    howmany = [0] * 10
    for i in range(10):
        howmany[i] = numbers.count(i)
    maximum = max(howmany)
    maxidx = 9- howmany[::-1].index(maximum)
    print('#{0} {1} {2}'.format(j, maxidx, maximum))