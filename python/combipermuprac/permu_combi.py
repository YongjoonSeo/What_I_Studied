lst = [1,2,3,4,5]
r = 3
combi = []
permu = []

for i in range(len(lst)-2):
    for j in range(i+1, len(lst)-1):
        for k in range(j+1, len(lst)):
            temp = [lst[i], lst[j], lst[k]]
            combi.append(temp)

for i in range(len(lst)):
    lst[0], lst[i] = lst[i], lst[0]
    for j in range(1, len(lst)):
        lst[1], lst[j] = lst[j], lst[1]
        for k in range(2, len(lst)):
            lst[2], lst[k] = lst[k], lst[2]
            temp = [lst[0], lst[1], lst[2]]
            permu.append(temp)
            lst[2], lst[k] = lst[k], lst[2]
        lst[1], lst[j] = lst[j], lst[1]
    lst[0], lst[i] = lst[i], lst[0]

print(combi)
print()
print(permu)
