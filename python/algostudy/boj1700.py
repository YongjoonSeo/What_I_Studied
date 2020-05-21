# 1. 플러그가 비어있을 때 - 순서대로 끼운다
# 2. 가득 차 있을 때 - 앞으로 끼울 것중 가장 사용 빈도가 낮은거(0포함) 먼저 뺀다?
# 사용 빈도가 가장 낮은 걸(A) 빼는 게 아닌 최소 횟수 최적해가 있다고 가정하자.
# 앞으로 빼게 될 것을 생각하면 A보다 사용 빈도가 낮은 건 없다.
# 만약 A를 빼지 않는 최소 횟수 최적해가 있다고 하면 그때 빼는 플러그를 B라고 하자.
# 앞으로의 B 사용량보다 A의 사용량이 적으므로 B보다 A를 더 적게 뽑을 것이다.
# (B대신 A를 뽑는다고 다른 것을 뽑을 경우에 영향을 주진 않는다 - B를 뽑을 만큼 A를 뽑으면 되니까)
# 따라서 A를 뽑는게 최소 횟수이다.
# 그리고 남은 전기용품 중에 최소 횟수로만 뽑아야 한다. (고려해야할 대상은 오직 이것이다.)
# 틀린거같은데

# 1. 문제의 답을 만드는 과정을 여러 조각으로 나눈다.
# 2. 각 조각마다 어떤 우선순위로 선택해야 할지 결정한다.
# 3. 탐욕적 선택 속성과 최적 부분 구조를 증명한다.

# 만약 남은 횟수가 같다면 가장 마지막에 쓰는거 먼저 뽑는다.

N, K = map(int, input().split())
lst = list(map(int, input().split()))
numcnt = [0 for i in range(K+1)]
pluged = dict()
cnt = 0

for i in lst:
    numcnt[i] += 1

for i in lst:
    if len(pluged) < N:
        pluged[i] = 1
        numcnt[i] -= 1
    else:
        if i in pluged:
            numcnt[i] -= 1
            continue
        targetval = 1000
        target = None
        temp = dict()
        for j in pluged:
            if numcnt[j] < targetval:
                targetval = numcnt[j]
                target = j
        print(target)
        pluged.pop(target)
        pluged[i] = 1
        numcnt[i] -= 1
        cnt += 1

print(cnt)


