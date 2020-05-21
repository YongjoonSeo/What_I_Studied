# starts from 1 (1 to N)
# N checkpoints, i-th checkpoint - height of Hi
# peak - 1. not 1st and Nth 2. height > immediately before & height > immediately after
# print # of peaks

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        if lst[i] > lst[i-1] and lst[i] > lst[i+1]:
            cnt += 1
    print('Case #{0}: {1}'.format(t, cnt))