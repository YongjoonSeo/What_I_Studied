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

def KMP(string, target):
    idx = 0
    info = Infolst(target)
    cnt = 0
    while idx < len(string) - len(target) + 1:
        step = 0
        for i in range(len(target)):
            cnt += 1
            if target[i] != string[idx + i]:
                if step == 0: 
                    idx += 1
                    break
                else:
                    idx += step - info[step - 1]
                    break
            step += 1
        else:
            return f'matched, {cnt} times'
    return f'not matched, {cnt} times'

def ComparePattern(string, target):
    cnt = 0
    loc = 0
    for i in range(len(string) - len(target)+1):
        loc += 1
        for j in range(len(target)):
            cnt += 1
            if string[i+j] != target[j]:
                break
        else:
            print('matched', end=', ')
            print(f'{cnt} times')
            break
    else:
        print('not matched', end=', ')
        print(f'{cnt} times')

string1 = 'Contrary to popular belief, Lorem Ipsum is not simply random text.'
target1 = 'random' 
string2 = 'abcdabcdabcdabcdabcdabcef'
target2 = 'abcdabcef'

ComparePattern(string1, target1)
print(KMP(string1, target1))
print(f'infolst of target1: {Infolst(target1)}')
ComparePattern(string2, target2)
print(KMP(string2, target2))
print(f'infolst of target2: {Infolst(target2)}')