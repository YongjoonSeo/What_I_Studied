T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    checked = [0 for i in range(N+1)]
    groups = [set()]
    groups[0].add(lst[0])
    groups[0].add(lst[1])
    checked[lst[0]] = 1
    checked[lst[1]] = 1
    for i in range(2, len(lst), 2):
        for group in groups:
            if lst[i] in group or lst[i+1] in group:
                group.add(lst[i])
                group.add(lst[i+1])
                checked[lst[i]] = 1
                checked[lst[i + 1]] = 1
                break
        else:
            groups.append(set())
            groups[-1].add(lst[i])
            groups[-1].add(lst[i + 1])
            checked[lst[i]] = 1
            checked[lst[i + 1]] = 1

    print('#{0} {1}'.format(t, N - checked.count(1) + len(groups)))

# 오답