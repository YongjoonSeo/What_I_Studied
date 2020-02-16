def BT_powerset(times, inp):

    if times == inp:
        result.append(list(target[i] for i in range(inp) if cases[i]))
        return

    for j in range(2):
        cases[times] = j
        BT_powerset(times + 1, inp)
        cases[times] = 0

target = [1,2,3]
N = len(target)
cases = [0] * N
result = []

BT_powerset(0, N)
print(result)