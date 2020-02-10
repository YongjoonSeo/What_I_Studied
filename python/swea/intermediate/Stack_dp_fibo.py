def fibo_DP(n):
    table = [0,1]

    for i in range(2, n+1):
        table.append(table[i-2] + table[i-1])
    # 재귀처럼 자기 자신을 다시 호출해야만 하는 건 아니다.
    return table[n]

for i in range(1,11):
    print(fibo_DP(i), end=' ')