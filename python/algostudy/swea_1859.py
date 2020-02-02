import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for i in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))
    maxv = max(lst)
    result = 0
    maxidx = lst.index(maxv)

    s = 0
    while s < len(lst):
        if maxidx == len(lst)-1 and s == len(lst) - 1:
            break
        elif s == maxidx:
            maxv = lst[s+1]
            for k in range(s+1, len(lst)):
                if lst[k] > maxv:
                    maxv = lst[k]
            # maxv = max(lst[s+1:]) 둘 다 없으니까 pass
            for k in range(s+1, len(lst)):
                if lst[k] == maxv:
                    maxidx = k
                    break
            # maxidx = s + 1 + lst[s+1:].index(maxv) 하나 없애니까 7개 맞음
        else:
            result += maxv - lst[s]   
        s += 1
    
    print('#{0} {1}'.format(i, result))