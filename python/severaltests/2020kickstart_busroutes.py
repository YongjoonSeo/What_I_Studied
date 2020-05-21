# N bus routes (1 to N)
# ith bus route runs every Xi days
# she only take ith bus on day of multiples of Xi
# due date: D
# when is the latest day? -> print

# 뒤에서부터 찾는거?
# 숫자를 하나씩 줄여가면서 while문으로 버스 다 탈수 있는지 체크하면서 모든 숫자가 다 체크되는 순간을 답으로.

T = int(input())
for t in range(1, T+1):
    N, D = map(int, input().split())
    lst = list(map(int, input().split()))
    idx = len(lst) - 1
    isDone = False
    while True:
        while True:
            if idx == -1:
                isDone = True
                break
            elif D % lst[idx] == 0:
                idx -= 1
            else:
                break
        if isDone: break
        D -= 1
    print('Case #{0}: {1}'.format(t, D))



    # print(lst)