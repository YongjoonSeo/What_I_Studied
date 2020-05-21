# R, C 중에 홀수가 하나라도 있을 때 - 모두 돌면 됨 -->> 홀수 방향으로
# R, C 모두 짝수일때 - 4가지 경우 중 하나.
# 첫 시작점의 오른쪽, 아래, 마지막점의 위쪽, 왼쪽 4개 중에 값이 가장 작은 경우가 정답이다.
# --->>>>>> 이 부분이 틀렸다..!
# 가장 작은 경우를 피해가야한다.

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
    case = 0
    minval = 1001
    lst = [field[0][1], field[1][0], field[R-1][C-2], field[R-2][C-1]]
    for i in range(4):
        if lst[i] <= minval:
            minval = lst[i]
            case = i
    if case == 2 or case == 3:
        y, x = 0, 0
        while not (y == R-1 and x == C-1):
            if y == R-2 and x == C-2:
                if case == 2: result += 'RD'
                else: result += 'DR'
                break
            elif y == R-2:
                result += 'DRUR'
                x += 2
            else:
                result += 'R' * (C-1) + 'D' + 'L' * (C-1) + 'D'
                y += 2
    else:
        y, x = 0, 0
        temp = ''
        if case == 0:
            while x < C:
                if x < 2:
                    if y == R-2:
                        temp += 'DRR'
                        x += 2
                    else:
                        temp += 'DRDL'
                        y += 2
                else:
                    temp += 'U' * (R-1) + 'R' + 'D' * (R-1) + 'R'
                    x += 2
        else:
            while y < R:
                if y < 2:
                    if x == C-2:
                        temp += 'RDD'
                        y += 2
                    else:
                        temp += 'RDRU'
                        x += 2
                else:
                    temp += 'L' * (R-1) + 'D' + 'R' * (R-1) + 'D'
                    y += 2
        result = temp[:-1]

print(result)
# for _ in range(len(field)):
#     print(field[_])