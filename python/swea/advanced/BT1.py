# 최소 교환횟수 - 교환 횟수가 구한 최소횟수보다 크면 가지치기.
# 1. 첫 번째 정류장에서 충전기를 끼운다 -> + 충전량 만큼 범위를 탐색할 수 있다.
# -> BT(s, s+충전량, 갈아끼운 횟수) -->>> BT(갈아끼운지점, 갈아끼운지점+충전량, 횟수)

def BT(s, e, val):
    global cnt, N
    if val >= cnt: return
    if e >= N-1:
        cnt = min(cnt, val)
        return
    for i in range(s+1, e+1):
        if i < len(bat):
            BT(i, i + bat[i], val+1)

T = int(input())
for t in range(1, T+1):
    inp = list(map(int, input().split()))
    N = inp[0]
    bat = inp[1:]
    cnt = float('inf')

    BT(0, bat[0], 0)

    print('#{0} {1}'.format(t, cnt))