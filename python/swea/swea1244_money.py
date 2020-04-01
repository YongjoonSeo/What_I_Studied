def Combi(start, r):
    for i in range(start, len(num)-r+1):
        if r == 1:
            yield [i]
        else:
            for j in Combi(i+1, r-1):
                yield [i] + j

def Pickchangeplace(start, n):
    for i in range(start, len(combi)-n+1):
        if n == 1:
            yield [combi[i]]
        else:
            for j in Pickchangeplace(i, n-1):
                yield [combi[i]] + j

T = int(input())
for t in range(1, T+1):
    num, k = input().split()
    num = list(num)
    combi = []
    result = -float('inf')
    for i in Combi(0, 2):
        combi.append(i)
    
    for case in Pickchangeplace(0, int(k)):
        for change in case:
            l, r = change
            num[l], num[r] = num[r], num[l]
        temp = ''
        for char in num: temp += char
        result = max(result, int(temp))
        for re in range(-1, -len(case)-1, -1):
            l, r = case[re]
            num[l], num[r] = num[r], num[l]
    
    print('#{0} {1}'.format(t, result))

    # Pickchangeplace(int(k))
    # print(num, k)