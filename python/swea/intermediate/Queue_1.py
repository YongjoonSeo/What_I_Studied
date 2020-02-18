from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    q = deque(list(input().split()))
    q.rotate(-M)
    print('#{0} {1}'.format(t, q.popleft()))