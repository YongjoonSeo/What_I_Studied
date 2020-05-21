def toggle(char):
    if char == 'C': return 'J'
    elif char == 'J': return 'C'

T = int(input())
for t in range(1, T+1):
    N = int(input())
    time = [0 for i in range(1441)]
    C = [0 for i in range(1441)]
    J = [0 for i in range(1441)]
    result = ''
    isnotpossible = False
    task = 'C'
    for i in range(N):
        s, e = map(int, input().split())
        if not isnotpossible:
            for j in range(s, e):
                ccheck = jcheck = 0
                if (C[j] and J[j]) or (ccheck and jcheck):
                    isnotpossible = True
                    break
                elif C[j]:
                    ccheck = 1
                    task = 'J'
                elif J[j]:
                    jcheck = 1
                    task = 'C'
            if isnotpossible: break
            for j in range(s, e):
                if task == 'C':
                    C[j] = 1
                else:
                    J[j] = 1
            else:
                result += task
    if isnotpossible: result = 'IMPOSSIBLE'

    print('Case #{0}: {1}'.format(t, result))