primes = [0, 0]
for i in range(2, 10001):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0: 
            primes.append(0)
            break
    else:
        primes.append(1)

T = int(input())
for t in range(T):
    num = int(input())
    check = num // 2
    i = 0
    while True:
        if primes[check+i] and primes[check-i]:
            if (check+i) + (check-i) == num:
                print(check-i, check+i)
                break
        i += 1