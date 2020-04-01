T = int(input())
for t in range(1, T+1):
    fee = list(map(int, input().split()))
    use = list(map(int, input().split()))
    use = [0] + use
    result = [0] + [fee[-1]] * 12
    
    for month in range(1, 13):
        if use[month]:
            result[month] = min(result[month-1]+ use[month]*fee[0], result[month-1]+ fee[1], result[month])
        else:
            result[month] = result[month-1]
        
        if month >= 3:
            result[month] = min(result[month], result[month-3] + fee[2])
    
    print('#{0} {1}'.format(t, result[-1]))