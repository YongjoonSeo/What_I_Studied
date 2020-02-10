def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

result = []
for i in range(1,11):
    result.append(fibo(i))

print(*result)