def toggle(char):
    if char == 'C': return 'J'
    elif char == 'J': return 'C'

T = int(input())
for t in range(1, T+1):
    N = int(input())
    time = [0 for i in range(1441)]
    result = []
    isnotpossible = False
    task = 'C'
    minuteset = []
    for i in range(N):
        s, e = map(int, input().split())
        minuteset.append((s,e,i))
    minuteset.sort(key=lambda x:x[0])

    for minute in minuteset:
        s, e, l = minute
        if not isnotpossible:
            for j in range(s, e):
                if task == 'C':
                    time[j] += 1
                    if time[j] == 2:
                        for k in range(s, j+1):
                            time[k] += 1
                            if time[k] > 3:
                                isnotpossible = True
                                break
                        else:
                            task = toggle(task)
                            continue
                elif task == 'J':
                    time[j] += 2
                    if time[j] == 4:
                        for k in range(s, j+1):
                            time[k] -= 1
                        else:
                            task = toggle(task)
                            continue
                if isnotpossible: break
                if time[j] > 3:
                    isnotpossible = True
                    break
            else:
                result.append(task)
    if isnotpossible: result = 'IMPOSSIBLE'

    if result == 'IMPOSSIBLE':
        print('Case #{0}: {1}'.format(t, result))
    else:
        final = ''
        for minute in minuteset:
            s, e, l = minute
            final += result[l]
        print('Case #{0}: {1}'.format(t, final))