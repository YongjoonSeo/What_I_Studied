T = int(input())
hexchar = '0123456789ABCDEF'
hexmap = dict()
for i in range(16):
    hexmap[hexchar[i]] = i
for t in range(1, T+1):
    n, hexnum = input().split()
    n = int(n)
    decnum = 0
    idx = 1
    for i in range(-1, -n-1, -1):
        decnum += idx * hexmap.get(hexnum[i])
        idx *= 16

    result = ''
    while decnum:
        result = str(decnum % 2) + result
        decnum //= 2
    add = '0' * (n*4 - len(result))
    result = add + result

    print('#{0} {1}'.format(t, result))