T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    raw = list(map(int, input().split()))
    chz = [[raw[i], i+1] for i in range(len(raw))]
    pot = chz[:N]
    rest = chz[N:]
    
    idx = 0
    while rest:
        for i in range(len(pot)):
            pot[i][0] //= 2
            if pot[i][0] == 0: 
                pot.pop(i)
                pot.insert(i, rest.pop(0))
                idx = i
                if not rest: break
    
    idx = (idx + 1) % len(pot)
    while len(pot) != 1:
        pot[idx][0] //= 2
        if pot[idx][0] == 0:
            if idx == len(pot) - 1:
                pot.pop(idx)
                idx = 0
            else:
                pot.pop(idx)
        else:
            idx = (idx + 1) % len(pot)
    
    print('#{0} {1}'.format(t, pot.pop()[1]))

    # while len(rest) != 1:
