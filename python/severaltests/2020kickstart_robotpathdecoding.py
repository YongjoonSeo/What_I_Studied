# 10^9 * 10^9 square (the rover begins with (1,1))
# 2 <= X <= 9

# 움직이는 함수 만들기 - 양 끝에서 넘어가는 거 구현 필요 -> 하나씩 움직이지 말고 한번에 움직이자 (곱하기 넣어서, 각각이 얼마나 가는지)
# -> (N, S, E, W) 각각 움직인 숫자 -> return 좌표
# 중첩 명령 해석해서 리스트에 집어넣기 [N, S, E, W] -> 괄호 넣을 스택, 숫자 넣을 스택
# field만들지 말고 숫자로 좌표 이동하기

def move(direclist):
    N, S, E, W = direclist
    sx, sy = 1, 1
    sx += E - W
    sy += S - N
    if sx < 1: sx += 10 ** 9
    elif sx > 10 ** 9: sx -= 10 ** 9
    if sy < 1: sy += 10 ** 9
    elif sy > 10 ** 9: sy -= 10 ** 9
    return (sx, sy)

T = int(input())
for t in range(1, T+1):
    lst = list(input())
    direc = [0 for i in range(4)]
    tempdir = [0 for i in range(4)]
    num = []
    sumnum = []
    for char in lst:
        if not sumnum:
            if char == 'N': direc[0] += 1
            elif char == 'S': direc[1] += 1
            elif char == 'E': direc[2] += 1
            elif char == 'W': direc[3] += 1
            elif char == '(':
                sumnum.append([0 for i in range(4)])
            else: num.append(char)
        else:
            if char == ')':
                popnum = int(num.pop())
                popsumnum = sumnum.pop()
                if not sumnum:
                    for i in range(4):
                        direc[i] += popnum * popsumnum[i]
                else:
                    for i in range(4):
                        sumnum[-1][i] += popnum * popsumnum[i]
            elif char == '(':
                sumnum.append([0 for i in range(4)])
            elif char == 'N': sumnum[-1][0] += 1
            elif char == 'S': sumnum[-1][1] += 1
            elif char == 'E': sumnum[-1][2] += 1
            elif char == 'W': sumnum[-1][3] += 1
            else: num.append(char)

    result = move(direc)
    print('Case #{0}: '.format(t), end='')
    print(*result)

# print(direc)

