def Oper(inplst, tarlst):
    if inplst[0] == 'I':
        tarlst.insert(int(inplst[1]), int(inplst[2]))
    elif inplst[0] == 'D':
        tarlst.pop(int(inplst[1]))
    elif inplst[0] == 'C':
        tarlst[int(inplst[1])] = int(inplst[2])

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))

    for _ in range(M):
        templst = list(input().split())
        Oper(templst, lst)
    
    if L >= len(lst):
        result = -1
    else:
        result = lst[L]
    
    print('#{0} {1}'.format(t, result))
