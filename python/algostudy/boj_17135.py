def Inrange(y, x, j, i, d):
    if abs(x-i) + (y-j) <= d:
        return True
    return False

def Totemp(n1, n2): # 중복 할당 방지
    if n1 == 1:
        if n2 == 1:
            return 0
        else:
            return 1
    return 0


N, M, D = map(int, input().split())

field = [[i for i in list(map(int, input().split()))] for j in range(5)]

# temp 만들기
wholearccom = []
wholearchers = [[0,5], [1,5], [2,5], [3,5], [4,5]]
for i in range(4):
    for j in range(i+1,5):
        temp = wholearchers.copy()
        temp.remove(wholearchers[i])
        temp.remove(wholearchers[j])
        wholearccom.append(temp)

tempset = [[0 for i in range(5)] for j in range(5)]


# print(wholearccom)
# for _ in range(len(field)):
#     print(field[_])


# N 행 바로 아래 성이 있다
# 궁수 3명
# 하나의 칸엔 하나의 궁수 -> 최대 적의 수니까 최적의 배치
# 하나의 칸엔 최대 하나의 적
# 모든 궁수 - 동시에 공격, 적 하나
# --> 공격 거리 D이하 -> 가장 가깝고 가장 왼쪽

# 궁수 공격 후 적 이동
# 궁수 배치 후 게임 진행은 정해져있다.