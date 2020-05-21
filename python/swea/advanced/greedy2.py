# 24시간
# 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록

# 출력: 최대 몇 대의 화물차가 이용하는지

# 완료시간이 빠른 순으로 정렬하면
# 탐욕적 선택 속성 - 가장 빨리 끝나는 화물차를 선택할 때, 전체 문제의 최적 해에서 가장 빨리 끝나는 화물차가 있다고 하면
# 만약 그 둘이 다르다면 바꿔 넣더라도 최적 해의 다른 화물차와는 겹치지 않는다 -> 그리디 접근의 최적해가 반드시 존재한다
# 최적 부분 구조 - 가장 빨리 끝나는 화물차를 선택한 후에, 겹치는 걸 걸러낸 나머지 중에서 가장 빨리 끝나는 것을 선택해야 한다.
# (남은 트럭만이 고려 대상이 남은 유일한 남은 집합이다)
# 그리디 접근 가능.

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = []
    for n in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort(key=lambda x:x[1], reverse=True)

    result = [lst.pop()]
    while lst:
        next = lst.pop()
        if result[-1][1] <= next[0]:
            result.append(next)

    print('#{0} {1}'.format(t, len(result)))
