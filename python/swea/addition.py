T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    print('#{0} {1}'.format(t, A+B))