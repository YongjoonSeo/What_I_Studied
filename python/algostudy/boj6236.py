# N일 동안 사용할 금액 계산 (1부터)
# M번만 통장에서 돈 뺌 < 정확히 M번을 맞춤
# M번을 맞추기 위해 남은 금액을 통장에 집어넣고 K원 인출 가능.
# 즉 M == N이라면 매일 빼서 써야할 것 같고 그 경우라면 제일 작은 경우에 맞추면 될듯하다.
# N일 동안에 M번 뽑아야하는데 그 중에 가장 작은 금액 K로 모두 커버할 수 있으려면?
# 출력: 최소금액 인출금 K원
# 다시 해봐야할듯

def returnK(inplst, m, maxidx, maxval, prevmax):
    if len(inplst) <= m:
        inplst.sort(reverse=True)
        result = len(inplst)
        i = 0
        while result <= m:
            if result == m:
                return max(inplst[i], prevmax)
            i += 1
            result += 1

    newlst = []
    newmaxidx = maxidx
    newmaxval = maxval
    i = 0
    while i < len(inplst):
        if i == maxidx or i+1 == len(inplst) or i+1 == maxidx:
            if newmaxval == inplst[i]:
                newmaxidx = len(newlst)
            newlst.append(inplst[i])
            i += 1
        else:
            if newmaxval >= inplst[i] + inplst[i+1]:
                newlst.append(inplst[i] + inplst[i+1])
            else:
                newmaxval = inplst[i] + inplst[i+1]
                newmaxidx = len(newlst)
                newlst.append(newmaxval)
            i += 2

    # for i in range(0, len(inplst), 2):
    #     if i+1 < len(inplst):
    #         newlst.append(inplst[i] + inplst[i+1])
    #         newmaxval = max(newmaxval, inplst[i], inplst[i+1])
    #     else:
    #         newlst.append(inplst[i])
    #         newmaxval = max(newmaxval, inplst[i])
    return returnK(newlst, m, newmaxidx, newmaxval, maxval)


N, M = map(int, input().split())
lst = []
maxval = maxidx = 0
for i in range(N):
    inp = int(input())
    lst.append(inp)
    if maxval < inp:
        maxval = inp
        maxidx = i

print(returnK(lst, M, maxidx, maxval, maxval))