def BT(month, total):
    global result
    if total > result: return
    if month >= 12: 
        result = min(result, total)
        return
    for i in range(3):
        if use[month]:
            if i == 0:
                BT(month+3, total+fee[2])
            elif i == 1:
                BT(month+1, total+fee[1])
            else:
                BT(month+1, total+fee[0]*use[month])
        else:
            BT(month+1, total)

T = int(input())
for t in range(1, T+1):
    fee = list(map(int, input().split()))
    use = list(map(int, input().split()))
    result = fee[-1]
    BT(0, 0)
    print('#{0} {1}'.format(t, result))