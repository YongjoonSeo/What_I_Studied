def binarycount(s, e, aim):
    middle = int((s + e) / 2)
    start = s
    end = e
    count = 0
    while middle != aim:
        middle = int((start + end) / 2)
        if aim < middle:
            end = middle
            count += 1
        else:
            start = middle
            count += 1
    return count

T = int(input())
for i in range(1, T+1):
    P, A, B = map(int, input().split())
    start = 1
    A_count = binarycount(1, P, A)
    B_count = binarycount(1, P, B)
    if A_count > B_count:
        print('#{0} B'.format(i))
    elif A_count == B_count:
        print('#{0} 0'.format(i))
    else:
        print('#{0} A'.format(i))