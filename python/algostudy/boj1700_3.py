# 1. 콘센트에 있는 것 중 앞으로 등장하지 않는 것부터 뽑는다.
# 2. 콘센트에 있는 것 중엔 - 가장 나중에 시작하는 걸 뽑는다.
# if 콘센트에 있는 것 중 더 먼저 시작하는 걸 뽑을 때 최적해를 A라고 가정하고 가장 나중에 시작하는 걸 m이라고 칭한 후,
# A에서 m보다 먼저 등장하는 걸 l이라고 하자.
# l을 뽑았을 때 이미 최적해인데, l대신 m을 뽑는다고 해서 뽑는 횟수가 늘어나지 않는다.
# (콘센트에 있는 것들 중에서 뽑는 것이므로 m을 뽑기 전에 l이 들어온다고 뽑지 않는다.) 따라서 최적해가 된다.
# 남은 전기용품 중에 최소한으로 뽑으면 되므로 (남은 항목만 고려하면 되므로)
# 그리디 접근이 가능하다.

N, K = map(int, input().split())
lst = list(map(int, input().split()))
order = dict()
pluged = dict()
cnt = 0

for i in range(len(lst)):
    if not order.get(lst[i]):
        order[lst[i]] = [i]
    else:
        order[lst[i]].append(i)

for i in range(len(lst)):
    if len(pluged) < N:
        pluged[lst[i]] = 1
        order.get(lst[i]).pop(0)
    else:
        if lst[i] in pluged:
            order.get(lst[i]).pop(0)
            continue
        target = None
        priority = 0
        for j in pluged:
            if not order.get(j):
                target = j
                break
            else:
                val = order.get(j)[0]
                if priority < val:
                    priority = val
                    target = j
        pluged.pop(target)
        pluged[lst[i]] = 1
        order.get(lst[i]).pop(0)
        cnt += 1

print(cnt)