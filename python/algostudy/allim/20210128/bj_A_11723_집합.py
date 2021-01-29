# 출력: check 연산마다 결과 출력

# 체크할 조건
# 1 <= M <= 3000000
# 1 <= x <= 20

# 21자리 비트를 만든 후 연산을 수행한다.

import sys
input = sys.stdin.readline

def solution(M):
    num = 1 << 21
    for_all = (1 << 21) - 1
    for i in range(M):
        inp = input().strip()
        if inp == 'all':
            num |= for_all
            continue
        elif inp == 'empty':
            num = 1 << 21
            continue
        op, n = inp.split()
        n = 1 << int(n)
        if op == 'add':
            num |= n
        elif op == 'remove':
            if num&n: num -= n
        elif op == 'check':
            print(1 if num&n else 0)
        elif op == 'toggle':
            num ^= n

if __name__ == '__main__':
    solution(int(input()))