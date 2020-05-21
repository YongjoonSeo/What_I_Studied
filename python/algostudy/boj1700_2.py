# 매 순간 선택할 때, 만약 플러그를 뽑아야 하는 경우가 생기면
# 1. 그 순간부터 N개의 원소가 생기는 집합을 찾는다 (N개의 원소가 되거나 lst의 끝에 다다르거나)
# --> 이 부분이 전체적인 해를 고려하지 못하게 한 것 같다.
# 2. 기존에 있는 곳에서 겹치는 걸 후보군에서 제외한다.
# 3. 겹치지 않는 것 중에 뽑는다.

# 만약 겹치는 것에서 뽑는 경우의 최적해가 있다고 하면
# 겹치지 않는 것 중에 뽑는다고 해도 그 최적해에 영향을 주지 않는다.
# (겹치는 부분은 그냥 뽑지않고 넘어갈 것이므로 최소 횟수에 영향을 주지 않는다)
# 그리고 남은 전기용품에 대해 최소 횟수를 구한다. (오직 고려해야할 대상은 남은 전기용품이다)

N, K = map(int, input().split())
lst = list(map(int, input().split()))
pluged = dict()
cnt = 0

for i in range(len(lst)):
    if len(pluged) < N:
        pluged[lst[i]] = 1
    else:
        if lst[i] in pluged:
            continue
        compare = dict()
        idx = i
        while len(compare) < N and idx < len(lst):
            compare[lst[idx]] = 1
            idx += 1
        target = None
        for k in pluged:
            if not compare.get(k):
                target = k
                break
        print(lst[i], target, end='---\n')
        pluged.pop(target)
        pluged[lst[i]] = 1
        cnt += 1

print(cnt)
