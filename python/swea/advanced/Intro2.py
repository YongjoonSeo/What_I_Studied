T = int(input())
for t in range(1, T+1):
    N = float(input())
    divider = 1/2
    binnum = ''
    while N:
        if divider <= N:
            N -= divider
            binnum += '1'
        else:
            binnum += '0'
        divider /= 2
        if len(binnum) >= 13:
            binnum = 'overflow'
            break
    print('#{0} {1}'.format(t, binnum))
