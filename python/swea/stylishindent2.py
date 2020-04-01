T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())
    stackR, stackC, stackS = [], [], []
    dataset = []
    for _ in range(p):
        text = input()
        cnt = 0
        if text[0] == '.':
            while text[cnt] == '.': cnt += 1
            dataset.append([len(stackR), len(stackC), len(stackS), cnt])
        
        for idx in range(cnt, len(text)):
            if text[idx] == '(': stackR.append(text[idx])
            elif text[idx] == '{': stackC.append(text[idx])
            elif text[idx] == '[': stackS.append(text[idx])
            elif text[idx] == ')': stackR.pop()
            elif text[idx] == '}': stackC.pop()
            elif text[idx] == ']': stackS.pop()
    
    setR, setC, setS = set(), set(), set()
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                for data in dataset:
                    if R*data[0] + C*data[1] + S*data[2] != data[3]:
                        break
                    else:
                        if data[0]: setR.add(R)
                        if data[1]: setC.add(C)
                        if data[2]: setS.add(S)
                for data in dataset:
                    if not data[2]:
                        if not data[1]:
                            if R*data[0] == data[3]: setR.add(R)
                        else:
                            if R*data[0] + C*data[1] == data[3]:
                                setR.add(R)
                                setC.add(C)
                    elif not data[0]:
                        if not data[2]:
                            if C*data[1] == data[3]: setC.add(C)
                        else:
                            if C*data[1] + S*data[2] == data[3]:
                                setC.add(C)
                                setS.add(S)
                    elif not data[1]:
                        if not data[0]:
                            if S*data[2] == data[3]: setS.add(S)
                        else:
                            if S*data[2] + R*data[0] == data[3]:
                                setS.add(S)
                                setR.add(R)
    f = [setR, setC, setS]
    for i in range(len(f)):
        if len(f[i]) == 1:
            temp = f[i].pop()
            f[i] = temp
        else:
            f[i] = -1
    
    stack = [[], [], []]
    result = []
    for _ in range(q):
        text = input()
        cnt = 0
        for cidx in range(len(stack)):
            if stack[cidx]:
                deter = len(stack[cidx]) * f[cidx]
                if deter < 0: 
                    cnt = -1
                    break
                else:
                    cnt += deter

        for idx in range(len(text)):
            if text[idx] == '(': stack[0].append(text[idx])
            elif text[idx] == '{': stack[1].append(text[idx])
            elif text[idx] == '[': stack[2].append(text[idx])
            elif text[idx] == ')': stack[0].pop()
            elif text[idx] == '}': stack[1].pop()
            elif text[idx] == ']': stack[2].pop()

        result.append(cnt)
    
    print('#{0}'.format(t), end=' ')
    print(*result)

        

                

