X = int(input())

total_count = 0
wholeline = 1
while total_count < X:
    total_count += wholeline
    wholeline += 1

idx = X - total_count + (wholeline - 1)
if idx == 0:
    if wholeline % 2:
        print('{0}/1'.format(wholeline-1))
    else:
        print('1/{0}'.format(wholeline-1))
else:
    if wholeline % 2:
        print('{0}/{1}'.format(idx, wholeline - idx))
    else:
        print('{0}/{1}'.format(wholeline - idx, idx))

# 1. X - total_count == 0
# 2. else

# switch = 1 -> 분자가 123 순서
# switch = 0 -> 분모가 123 순서
# => n이 홀수면 0 짝수면 1
# => wholeline이 짝수면 0 홀수면 1

# 1 2 3 4 5 6 7

# n*(n+1) / 2 < X인 n
# 그러면 n+1번째 줄에서 세면 된다.