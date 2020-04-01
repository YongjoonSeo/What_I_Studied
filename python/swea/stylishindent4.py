T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())
    R, C, S = [], [], []
    dataset = []
    for _ in range(p):
        text = input()
        if text[0] == '.':
            i = 0
            while i < len(text) and text[i] == '.': i += 1
            dataset.append((len(R), len(C), len(S), i))
        
        for char in text:
            if char == '(': R.append(char)
            elif char == '{': C.append(char)
            elif char == '[': S.append(char)
            elif char == ')': R.pop()
            elif char == '}': C.pop()
            elif char == ']': S.pop()
    
    anssets = []
    for data in dataset:
        isFound = False
        for r in range(1, 21):
            for c in range(1, 21):
                for s in range(1, 21): 
                    if r*data[0] + c*data[1] + s*data[2] == data[3]:
                        if not data[0]:
                            if not data[1]:
                                anssets.append((0, 0, s))
                            elif not data[2]:
                                anssets.append((0, c, 0))
                            else:
                                anssets.append((0, c, s))
                        elif not data[1]:
                            if not data[2]:
                                anssets.append((r, 0, 0))
                            else:
                                anssets.append((r, 0, s))
                        elif not data[2]:
                            anssets.append((r, c, 0))
                        else:
                            anssets.append((r,c,s))
                        isFound = True
                        break
                if isFound: break
            if isFound: break
    
    stack = [[], [] ,[]]
    result = []
    for _ in range(q):
        text = input()
        ans = set()

        for ansset in anssets:
            temp = -1
            for idx in range(3):
                if ansset[idx]: temp += ansset[idx]*len(stack[idx])
            if temp == -1: continue
            else: ans.add(temp+1)
        if len(ans) == 1:
            result.append(ans.pop())
        else:
            result.append(-1)
        
        for char in text:
            if char == '(': stack[0].append(char)
            elif char == '{': stack[1].append(char)
            elif char == '[': stack[2].append(char)
            elif char == ')': stack[0].pop()
            elif char == '}': stack[1].pop()
            elif char == ']': stack[2].pop()
    
    print('#{0}'.format(t), end=' ')
    print(*result)