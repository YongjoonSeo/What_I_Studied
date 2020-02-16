def Infolst(string):
    if len(string) == 1: return [0]
    infolst = [0 for i in range(len(string))]
    start = 0
    dist = 1
    
    while start + dist < len(string):
        if string[start] == string[start + dist]:
            infolst[start + dist] = start + 1
            start += 1
        else:
            if start == 0:
                dist += 1
            else:
                dist += start - infolst[start - 1] # 현재 start + dist의 위치를 고정시키기 위함
                start = infolst[start - 1]
    return infolst

L = int(input())
inp = input()
print(L-Infolst(inp)[-1])