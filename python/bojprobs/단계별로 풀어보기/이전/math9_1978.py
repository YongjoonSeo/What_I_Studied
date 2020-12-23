N = int(input())
numbers = list(map(int, input().split()))
primes = [i for i in range(2,max(numbers)+1)]
result = []
idx = 2
while idx <= max(numbers):
    if idx in primes:
        for j in primes:
            if j % idx == 0:
                primes.remove(j) 
        primes.insert(0, idx)
    idx += 1

for k in numbers:
    if k in primes:
        result.append(k)

print(len(result))

# 리스트 내에서 for 문을 돌릴 때, 요소의 개수가 변하면 원하는 대로 실행되지 않을 수 있다.
