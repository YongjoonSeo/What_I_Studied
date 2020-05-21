# 시작 칸에 말 "4개"
# 말은 게임판의 화살표 방향 대로만 이동
# -> 파란색 칸에서 이동 시작하면 파란 화살표를 타야하고 이외엔 빨간 화살표를 탄다.
# 도착칸에 도착하면 주사위 상관없이 마친다
# 게임은 총 10개의 턴
# 매 턴 1~5 주사위를 굴리고 도착 칸에 없는 말을 골라 주사위 만큼 이동
# 말이 이동을 마치는 칸에 다른 말이 있으면 그건 못고름 (이동 마치는 칸이 도착칸이면 가능)
# -> 그니까 가려는 목적지에 다른 말이 있으면 못간다는 말인듯
# 칸에 적힌 수가 점수에 추가된다
# 주사위에서 나올 수 10개를 알고있다 (순서대로)

# 출력: 얻을 수 있는 점수의 최댓값

# 제약 조건: 말이 못 가는 경우
# - 가려는 목적지에 말이 있는 경우 (도착 제외)
# - 화살표에서 벗어나는 루트
# - 주사위는 1~5
# 선호 조건: 발판 숫자 증감폭
# - 증감폭이 가장 큰 순서대로 선호
# - 25 -> 40: 5
# - 10 -> 25: 3
# - 시작 -> 10, 10 -> 20, 20 -> 30, 30 -> 40: 2
# - 20 -> 25: 2, 2, 1
# - 30 -> 25: -2, -1, -1, -1

def Move(dot, step):
    s, loc = dot
    if s == 10:
        if step == 1 or step == 2 or step == 3: return (step * 3, 'cross')
        elif step == 4: return (15, 'cross')
        else: return (20, 'cross')
    elif s == 20:
        if step == 1 or step == 2: return (2 * step, 'cross')
        elif step == 3: return (5, 'cross')
        elif step == 4: return (10, 'cross')
        else: return (15, 'cross')
    elif s == 30 and loc == 'circle':
        if step == 1: return (-2, 'cross')
        elif step == 2 or step == 3 or step == 4: return ((-1) * step - 1, 'cross')
        else: return (0, 'cross')
    else:
        if loc == 'cross':
            temps = s
            while step:
                if s == 13 or s == 16: s += 3
                elif s == 19: s += 6
                elif s == 22: s += 2
                elif s == 24: s += 1
                elif s == 28 or s == 27 or s == 26: s -= 1
                elif s == 25 or s == 30 or s == 35 or s == 40: s += 5
                step -= 1
                if s > 40: return 'arrive'
            return (s - temps, 'cross')
        else:
            if s + step*2 > 40: return 'arrive'
            elif s + step*2 == 40: return (step*2, 'cross')
            return (step*2, 'circle')

def BT(idx, cnt):
    global result
    if idx == 10:
        result = max(result, cnt)
        # if cnt > 211:
        #     print(cnt)
        #     print(horse)
        return
    for i in range(4):
        if horse[i][0] != 'arrive':
            step = Move(horse[i], dice[idx])
            temp = horse[i][:]
            if step == 'arrive':
                horse[i][0] = 'arrive'
                BT(idx+1, cnt)
                horse[i][0] = temp[0]
            else:
                val, loc = step
                horse[i] = [horse[i][0]+val, loc]
                isoverlap = False
                for j in range(4):
                    if i == j: continue
                    elif horse[i] == horse[j]:
                        horse[i] = temp
                        isoverlap = True
                        break
                if isoverlap: continue
                BT(idx+1, cnt+horse[i][0])
                horse[i] = temp
        else:
            continue

dice = list(map(int, input().split()))
result = -1
horse = [[0, 'circle'], [0, 'circle'], [0, 'circle'], [0, 'circle']]

BT(0, 0)
print(result)

# for j in range(0, 42, 2):
#     tempval = [j, 'circle']
#     print(tempval)
#     for i in range(7):
#         step = Move(tempval, 1)
#         if step != 'arrive':
#             val, loc = step
#             tempval[0] += val
#             if loc == 'cross':
#                 tempval[1] = 'cross'
#             print(tempval, end=' ')
#         else:
#             print(step)
#             break
#     print()

# for j in [13, 16, 19, 25, 22, 24, 26, 27, 28, 30, 35, 40]:
#     tempval = [j, 'cross']
#     print(tempval)
#     for i in range(7):
#         step = Move(tempval, 5)
#         if step != 'arrive':
#             val, loc = step
#             tempval[0] += val
#             if loc == 'cross':
#                 tempval[1] = 'cross'
#             print(tempval[0], end=' ')
#         else:
#             print(step)
#             break
#     print()


# tempval = [12, 'circle']
# for i in range(7):
#     step = Move(tempval, 1)
#     if step != 'arrive':
#         val, loc = step
#         tempval[0] += val
#         if loc == 'cross':
#             tempval[1] = 'cross'
#         print(tempval[0])
#     else:
#         print(step)
#         break