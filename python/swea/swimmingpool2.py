def mini(month, total):
    global result
    if month >= 12: 
        result = min(result, total)
        return
    if not use[month]:
        mini(month+1, total)
    else:
        cnt = 0
        m3, per_month = fee[2], min(fee[1], use[month]*fee[0])
        mini(month+1, total+per_month)
        if month + 1 < 12 and use[month+1]:
            per_month += min(fee[1], fee[0] * use[month+1])
            cnt += 1
            mini(month+2, total+per_month)
        if month + 2 < 12 and use[month+2]:
            per_month += min(fee[1], fee[0] * use[month+2])
            cnt += 2
        minval = min(m3, per_month)
        if m3 == minval:
            mini(month+3, total + minval)
        if per_month == minval:
            if cnt == 0:
                mini(month+1, total + minval)
            elif cnt == 1:
                mini(month+2, total + minval)
            else:
                mini(month+3, total + minval)

T = int(input())
for t in range(1, T+1):
    fee = list(map(int, input().split()))
    use = list(map(int, input().split()))
    result = fee[-1]
    mini(0, 0)
    print('#{0} {1}'.format(t, result))
