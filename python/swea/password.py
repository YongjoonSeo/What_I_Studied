for t in range(1, 11):
    T = int(input())
    numlst = list(map(int, input().split()))
    idx = 0

    while numlst[-1] != 0:
        subtract = idx + 1
        numlst[0] = numlst[0] - subtract
        if numlst[0] < 0: numlst[0] = 0
        temp = [0] * 8
        for i in range(8):
            temp[i] = numlst[(i+1) % 8]
        numlst = temp
        idx = (idx + 1) % 5
    
    print('#{0}'.format(t), end=' ')
    print(*numlst)