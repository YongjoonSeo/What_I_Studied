n = int(input())
stack = []
result = []
seq = [int(input()) for i in range(n)]
i = 1
j = 0
while stack or j < n:
    if i < seq[j]:
        stack.append(i)
        result.append('+')
        i += 1
    elif i == seq[j]:
        result.append('+')
        result.append('-')
        i += 1
        j += 1
    else:
        if stack[-1] == seq[j]:
            result.append('-')
            stack.pop()
            j += 1
        else:
            print('NO')
            break
else:
    for i in result:
        print(i)