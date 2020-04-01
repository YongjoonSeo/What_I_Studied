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
    
    ansset = set()
    for R in range(1, 21):
        for C in range(1, 21):
            for S in range(1, 21):
                for data in dataset:
                    if R*data[0] + C*data[1] + S*data[2] == data[3]:
                        if not data[0]:
                            if not data[1]:
                                ansset.add((0,0,S))
                            else:
                                if data[1] == data[2]:
                                    temp = (C + S) / 2
                                    ansset.add((0, temp, temp))
                                else:
                                    ansset.add((0,C,S))
                        elif not data[1]:
                            if not data[2]:
                                ansset.add((R,0,0))
                            else:
                                if data[0] == data[2]:
                                    temp = (R + S) / 2
                                    ansset.add((0, temp, temp))
                                else:
                                    ansset.add((R,0,S))
                        elif not data[2]:
                            if not data[0]:
                                ansset.add((0,C,0))
                            else:
                                if data[1] == data[0]:
                                    temp = (C + R) / 2
                                    ansset.add((0, temp, temp))
                                else:
                                    ansset.add((R,C,0))
                        else:
                            if data[1] == data[2] == data[0]:
                                    temp = (C + S + R) / 3
                                    ansset.add((temp, temp, temp))
                            else:
                                ansset.add((R,C,S))
    
    stack = [[], [], []]
    result = []
    for _ in range(q):
        text = input()
        cnt = set()
        for ans in ansset:
            cnt.add(int(ans[0]*len(stack[0]) + ans[1]*len(stack[1]) + ans[2]*len(stack[2])))
        if len(cnt) == 1:
            result.append(cnt.pop())
        else:
            result.append(-1)
    
        for idx in range(len(text)):
            if text[idx] == '(': stack[0].append(text[idx])
            elif text[idx] == '{': stack[1].append(text[idx])
            elif text[idx] == '[': stack[2].append(text[idx])
            elif text[idx] == ')': stack[0].pop()
            elif text[idx] == '}': stack[1].pop()
            elif text[idx] == ']': stack[2].pop()
    
    print('#{0}'.format(t), end=' ')
    print(*result)

        

                

