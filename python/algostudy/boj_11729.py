def hanoi(n, s, m, e):
    if n == 1:
        print('{0} {1}'.format(s, e))
        return
    hanoi(n-1, s, e, m)
    print('{0} {1}'.format(s, e))
    hanoi(n-1, m, s, e)

N = int(input())
print(2**N -1)
hanoi(N, 1, 2, 3)