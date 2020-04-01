from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    deck = deque(lst)

    for i in range(M):
        idx, num = map(int, input().split())
        deck.insert(idx, num)

    print('#{0} {1}'.format(t, deck[L]))
