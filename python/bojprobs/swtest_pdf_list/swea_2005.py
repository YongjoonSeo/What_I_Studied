def pascal(lst):
    temp = lst
    if temp == [1]:
        return [1,1]
    result = [0] * (len(lst) + 1)
    for i in range(len(result)):
        if i == 0 or i == len(result) - 1:
            result[i] = 1
        else:
            result[i] = temp[i-1] + temp[i]
    return result

T = int(input())
for i in range(1, T+1):
    n = int(input())
    print('#{0}'.format(i))
    idxlst = []
    for j in range(1, n+1):
        if j == 1:
            print(1)
            idxlst.append(1)
        else:
            idxlst = pascal(idxlst)
            print(*idxlst)
