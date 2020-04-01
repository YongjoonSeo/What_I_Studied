def det(arr):
    a1, a2, a3, a4, a5, a6, a7, a8, a9 = arr[0][0], arr[0][1], arr[0][2], arr[1][0], arr[1][1], arr[1][2], arr[2][0], arr[2][1], arr[2][2]
    return (a1*(a5*a9-a6*a8)-a2*(a4*a9-a6*a7)+a3*(a4*a8-a5*a7))

def multiply(arr, lst):
    if not arr: return False
    result = []
    for i in range(3):
        result.append(arr[i][0]*lst[0] + arr[i][1]*lst[1] + arr[i][2]*lst[2])
    return result

def inverse(arr):
    determinant = det(arr)
    if not determinant:
        return False
    
    imatrix = []
    for i in range(3):
        temprow = []
        for j in range(3):
            tempval = [0] * 4
            k = 0
            for m in range(3):
                for n in range(3):
                    if n == j or m == i:
                        continue
                    tempval[k] = arr[m][n]
                    k += 1
            val = (tempval[0]*tempval[3]-tempval[1]*tempval[2])/determinant
            if (i + j) &1: val *= (-1)
            temprow.append(val)
        imatrix.append(temprow)
    
    return list(zip(*imatrix))

T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())
    exps = []
    R = []
    C = []
    S = []
    f = [set(), set(), set()]
    for i in range(p):
        text = input()
        cnt = 0
        if text[0] == '.':
            while text[cnt] == '.':
                cnt += 1
            exps.append([[len(R), len(C), len(S)], cnt])
            if not C and not S: f[0].add(cnt//len(R))
            if not R and not S: f[1].add(cnt//len(C))
            if not R and not C: f[2].add(cnt//len(S))
        for idx in range(cnt, len(text)):
            if text[idx] == '(': R.append(text[idx])
            elif text[idx] == '{': C.append(text[idx])
            elif text[idx] == '[': S.append(text[idx])
            elif text[idx] == ')': R.pop()
            elif text[idx] == '}': C.pop()
            elif text[idx] == ']': S.pop()
    
    for i in range(len(exps)-2):
        for j in range(i+1, len(exps)-1):
            for k in range(j+1, len(exps)):
                array = [exps[i][0], exps[j][0], exps[k][0]]
                table = [exps[i][1], exps[j][1], exps[k][1]]
                resultval = multiply(inverse(array), table)
                if not resultval: continue
                for i in range(len(resultval)):
                    f[i].add(resultval[i])
    for i in range(len(f)):
        if len(f[i]) != 1:
            f[i] = -1
        else:
            temp = int(f[i].pop())
            f[i] = temp
    
    result = []
    brackets = [[], [], []]
    for i in range(q):
        text = input()
        cnt = 0
        for bidx in range(len(brackets)):
            if brackets[bidx]:
                cnt += len(brackets[bidx]) * f[bidx]
                if cnt < 0:
                    cnt = -1
                    break
        for idx in range(len(text)):
            if text[idx] == '(': brackets[0].append(text[idx])
            elif text[idx] == '{': brackets[1].append(text[idx])
            elif text[idx] == '[': brackets[2].append(text[idx])
            elif text[idx] == ')': brackets[0].pop()
            elif text[idx] == '}': brackets[1].pop()
            elif text[idx] == ']': brackets[2].pop()
        result.append(cnt)
    
    print('#{0}'.format(t), end=' ')
    print(*result)
