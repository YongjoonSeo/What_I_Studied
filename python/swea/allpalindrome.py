T = int(input())
for t in range(1, T+1):
    text = input()
    for i in range(len(text)//2):
        if text[i] != text[len(text)-1-i] and text[i] != '?' and text[len(text)-1-i] != '?':
            print('#{0} Not exist'.format(t))
            break
    else:
        print('#{0} Exist'.format(t))