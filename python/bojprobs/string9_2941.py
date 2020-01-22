word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
subcount = 0
for alphabet in croatian:
    if alphabet in word:
        if alphabet == 'dz=':
            subcount -= 2 * word.count(alphabet)
        elif alphabet == 'z=':
            subcount -= word.count(alphabet)
            if 'dz=' in word:
                subcount += word.count('dz=')
        else:
            subcount -= word.count(alphabet)

count = len(word) + subcount
print(count)