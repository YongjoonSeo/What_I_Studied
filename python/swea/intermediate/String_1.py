T = int(input())
for t in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0

    if str1 in str2:
        result = 1
    
    print('#{0} {1}'.format(t, result))