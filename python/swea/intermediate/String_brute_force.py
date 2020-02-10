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
            print('matched')
            print(cnt)
            break
    else:
        print('not matched')
        print(cnt)


string = 'a pattern matching algorithm'
target1 = 'rithm' # 본문에 있는 문자열
target2 = 'ritm' # 본문에 없는 문자열

ComparePattern(string, target1)
ComparePattern(string, target2)


