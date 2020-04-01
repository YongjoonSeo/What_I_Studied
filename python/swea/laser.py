T = int(input())
for t in range(1, T+1):
    stack = []
    cnt = 0
    lst = list(input())
    i = 0
    while i < len(lst) - 1:
        if lst[i] == '(':
            if lst[i+1] == ')':
                cnt += len(stack)
                i += 2
            else:
                stack.append(lst[i])
                cnt += 1
                i += 1
        else:
            stack.pop()
            i += 1
    
    print('#{0} {1}'.format(t, cnt))
