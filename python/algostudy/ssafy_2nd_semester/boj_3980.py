# 백트래킹 해서 11명 다 돌았을 때 최댓값을 찾으면 괜찮을 듯.
# 100이 최대이니까 최댓값 도달 못한다면 제끼기.
# --> (nth+1) * 100 최대 1100, 
# ㅡㅡ 제낄 필요도 없는 거였는데 문제도 잘 안 읽고 풀어서 나가리됨 ㅡㅡ^

def BT(nth, val):
    global result
    if nth == 11:
        result = max(result, val)
        return

    for i in range(11):
        if field[nth][i] and not position[i]:
            position[i] = 1
            BT(nth + 1, val + field[nth][i])
            position[i] = 0


T = int(input())
for t in range(T):
    field = [list(map(int, input().split())) for i in range(11)]
    position = [0 for i in range(11)]
    result = -1

    BT(0, 0)
    print(result)


    # for _ in range(len(field)):
    #     print(field[_])