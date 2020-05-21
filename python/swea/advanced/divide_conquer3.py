# 조건 1 - A에 들어있다
# 조건 2 - 탐색 과정에서 양쪽 구간을 번갈아 선택한다

def binsearch(arr, val, s, e, region):
    if s == e:
        if val == arr[s]: return True
        else: return False
    mid = (s+e) // 2
    if arr[mid] > val:
        if region == 1:
            return False
        else:
            return binsearch(arr, val, s, mid-1, 1)
    elif arr[mid] == val:
        return True
    else:
        if region == 2:
            return False
        else:
            return binsearch(arr, val, mid+1, e, 2)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for num in B:
        if binsearch(A, num, 0, N-1, 0): cnt += 1

    print('#{0} {1}'.format(t, cnt))