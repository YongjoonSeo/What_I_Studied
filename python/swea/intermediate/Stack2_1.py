def Operate(char, int1, int2):
    if char == '+': return int1 + int2
    elif char == '-': return int1 - int2
    elif char == '/': return int1 // int2
    elif char == '*': return int1 * int2

T = int(input())
for t in range(1, T+1):
    oper = input().split()
    stack = []
    for one in range(len(oper)):
        try:
            if oper[one].isdigit():
                stack.append(int(oper[one]))
            elif oper[one] == '.':
                if one != len(oper) - 1:
                    print('#{0} error'.format(t))
                    break
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Operate(oper[one], left, right))
        except:
            print('#{0} error'.format(t))
            break
    else:
        if len(stack) == 1:
            print('#{0} {1}'.format(t, stack[-1]))
        else:
            print('#{0} error'.format(t))
