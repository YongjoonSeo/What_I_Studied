T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    num = A.count(B)
    print('#{0} {1}'.format(t, len(A)-(num*(len(B)-1))))