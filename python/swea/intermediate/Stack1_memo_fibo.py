def fibo_memo(n):
    global memo
    if n >= 2 and len(memo) <= n: 
        # 계산 값을 저장한 리스트(memo)의 길이로 제약조건을 걸어 
        # 한 번 계산한 값에 대해 다시 함수를 호출하지 않도록 한다.
        # 부등호를 정할 때, 계산 되기 이전에는 함수를 불러올 수 있도록 한다.
        memo.append(fibo_memo(n-1) + fibo_memo(n-2))
    return memo[n]

memo = [0, 1]
result = []
for i in range(1, 11):
    result.append(fibo_memo(i))
print(*result)