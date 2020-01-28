M = int(input())
N = int(input())
primes = []
for i in range(M, N+1):
    if i == 1:
        continue
    for a in range(2, i):
        if not i % a:
            break
    else:
        primes.append(i)
    
if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)

# 틀린 이유 - i==1 일때 고려하지 않았다.