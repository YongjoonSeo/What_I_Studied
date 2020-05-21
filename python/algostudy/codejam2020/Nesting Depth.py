T = int(input())
for t in range(1, T+1):
    result = ''
    lst = list(map(int, input()))
    stack = []
    for num in lst:
        if num > len(stack):
            result += '(' * (num - len(stack)) + str(num)
            for i in range(num-len(stack)):
                stack.append(1)
        elif num == len(stack):
            result += str(num)
        else:
            result += ')' * (len(stack) - num) + str(num)
            for i in range(len(stack)-num):
                stack.pop()
    else:
        while stack:
            result += ')'
            stack.pop()
    print('Case #{0}: {1}'.format(t, result))


    # print(lst)