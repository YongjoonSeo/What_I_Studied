for _ in range(4):
    temp = list(map(int, input().split()))
    a_rec = temp[:4]
    b_rec = temp[4:]
    ax, ay, ap, aq = a_rec
    bx, by, bp, bq = b_rec

    if bx < ax - (bp - bx) or bx > ap:
        print('d')
    elif bx == ax - (bp - bx) or bx == ap:
        if by == ay - (bq - by) or by == aq:
            print('c')
        elif ay - (bq - by) < by < aq:
            print('b')
        else:
            print('d')
    else:
        if by == ay - (bq - by) or by == aq:
            print('b')
        elif ay - (bq - by) < by < aq:
            print('a')
        else:
            print('d')