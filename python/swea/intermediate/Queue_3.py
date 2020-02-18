T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    chz = list(enumerate(list(map(int, input().split()))))
    pot = chz[:N]
    rest = chz[N:]

    while len(rest) != 1:
