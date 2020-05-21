T = int(input())
for t in range(1, T+1):
    n, num = input().split()
    zeros = ''
    n = int(n)
    convert_int = int(num, 16)
    binarynum = bin(convert_int)[2:]
    if len(binarynum) != 4 * n:
        zeros += '0' * (4*n - len(binarynum))
    print('#{0} {1}'.format(t, zeros+binarynum))