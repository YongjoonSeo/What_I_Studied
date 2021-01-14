# 한번 입었던 옷 '조합'을 다시 입지 않는다.
# 같은 종류의 의상은 하나만 입을 수 있다.

# 출력: 각 테케마다 알몸이 아닌 상태로 의상을 입을 수 있는 경우의 수

# 체크할 조건
# 같은 이름을 가진 의상은 존재하지 않는다.
# 0 <= n <= 30

# 분류별로 개수를 저장한다.
# (각 분류별 개수) * (1 ~ 분류의 개수)만큼 선택해서 모두 더한다.
# A개, B개, C개라고 하면
    # A + B + C + AB + BC + CA + ABC
    # = (A + 1) * (B + 1) * (C + 1) - 1

import sys
input = sys.stdin.readline

def solution(T):
    for t in range(T):
        n = int(input())
        clothes = dict()
        for i in range(n):
            item, kind = input().split()
            if clothes.get(kind): clothes[kind] += 1
            else: clothes[kind] = 1
        
        result = 1
        nums = [clothes.get(key)+1 for key in clothes.keys()]
        for num in nums:
            result *= num
        print(result - 1) 

if __name__ == '__main__':
    solution(int(input()))

