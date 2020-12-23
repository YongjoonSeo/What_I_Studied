string = input()
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
howmany = [0] * 26

for i in lowers:
    howmany[lowers.index(i)] = string.count(i)

for j in uppers:
    howmany[uppers.index(j)] += string.count(j)

howmanymax = 0
for k in howmany:
    if k == max(howmany):
        howmanymax += 1

if howmanymax == 1:
    print(uppers[howmany.index(max(howmany))])
else:
    print('?')