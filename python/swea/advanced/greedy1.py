# N개의 컨테이너를 M대의 트럭으로 운반
# 편도로 운반 - 트럭 하나당 하나의 컨테이너
# 적재용량 초과하는 컨테이너(화물)는 운반 불가
# 화물의 총 중량이 최대가 될 때 전체 옮긴 화물의 무게 구하기.

# 출력: 옮겨진 화물의 전체 무게 (하나도 못 옮기면 0을 출력)

# 그리디 접근이 가능한가?
# 만약 트럭 적재용량이 큰 순, 컨테이너가 큰 순으로 해서 가장 적재용량이 큰 것이 가장 무거운것을 나른다고 하자.
# 트럭은 한 번씩 밖에 못가니까 가장 큰 것을 옮긴 때보다 더 무거운 짐을 옮길 수 없다 -> 탐욕적 선택 속성
# 남은 트럭들은 실을 수 있는 것 중에 가장 적재용량이 큰 것을 실어야 한다 -> 최적 부분 구조
# 그리디 접근 가능.

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    clst = list(map(int, input().split()))
    tlst = list(map(int, input().split()))
    clst.sort()
    tlst.sort()
    result = 0

    isempty = False
    for tidx in range(M):
        truck = tlst.pop()
        container = clst.pop()
        # cidx = len(clst)-1
        # container = clst[cidx]
        while container > truck:
            if clst: container = clst.pop()
            else:
                isempty = True
                break
        if truck >= container:
            result += container
        if isempty or not clst: break

    print('#{0} {1}'.format(t, result))