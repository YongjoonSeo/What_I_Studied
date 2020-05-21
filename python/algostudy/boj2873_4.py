# R, C 중에 홀수가 하나라도 있을 때 - 모두 돌면 됨 -->> 홀수 방향으로
# R, C 모두 짝수일때 - 시작, 끝 점을 제외하고 가장 값이 작은 한 군데만 피해서 가면 된다.
# 하나만 빠질 수 있는 부분 중에서 최소값인 부분을 제외하고 돌면 된다.
# (하나만 빠질 수 없는 부분에 최소값이 있다고 해도, 하나만 빠질 수 있는 부분에서도 하나 제외해야 하기 때문)
# i+j가 홀수인 부분이 하나만 빠질 수 있는 부분이다. (index 0 부터)
# 재귀 호출이 너무 많아서 메모리 초과가 나는 것 같다.
# 짝수일때 최소 부분을 찾는다면, 그 지점을 기점으로 임의로 경로를 구해보자.

R, C = map(int, input().split())
field = [list(map(int, input().split())) for i in range(R)]
result = ''

if R&1 or C&1:
    temp = ''
    toggle = 1
    if R&1:
        for i in range(R):
            if toggle == 1:
                temp += 'R' * (C-1)
            else:
                temp += 'L' * (C-1)
            toggle *= -1
            temp += 'D'
        result = temp[:-1]
    else:
        for i in range(C):
            if toggle == 1:
                temp += 'D'* (R-1)
            else:
                temp += 'U' * (R-1)
            toggle *= -1
            temp += 'R'
        result = temp[:-1]
else:
    minval = 1001
    ty, tx = 0, 0
    for i in range(R):
        for j in range(C):
            if (i+j)&1:
                if field[i][j] < minval:
                    ty, tx = i, j
                    minval = field[i][j]
    y, x = 0, 0
    temp = ''
    while 0 <= y < R and 0 <= x < C:
        if not ((y == ty-1 or y == ty) and not y&1):
            if x == 0:
                temp += 'R' * (C-1) + 'D'
                x = C-1
            else:
                temp += 'L' * (C-1) + 'D'
                x = 0
            y += 1
        elif x == tx:
            if x == C-2:
                temp += 'RDD'
                x += 1
                y += 2
            else:
                temp += 'RDRUR'
                x += 3
        elif x+1 == tx:
            if x == C-2:
                temp += 'DRD'
                x += 1
                y += 2
            else:
                temp += 'DRRUR'
                x += 3
        elif x == C-1:
            temp += 'DD'
            y += 2
        else:
            temp += 'DRUR'
            x += 2
    result = temp[:-1]

print(result)
# for _ in range(len(field)):
#     print(field[_])