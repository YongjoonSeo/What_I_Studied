dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))
dwarfs.sort()
sub = [[i,j] for i in dwarfs for j in dwarfs if i != j and dwarfs.index(i) < dwarfs.index(j)]
compare = []
for i in range(len(sub)):
    temp = []
    for j in dwarfs:
        if j not in sub[i]:
            temp.append(j)
    compare.append(temp)

for k in compare:
    if sum(k) == 100:
        for m in k:
            print(m)
        break
    
# for _ in range(len(compare)):
#     print(compare[_])

# for _ in range(len(sub)):
#     print(sub[_])
