# 출력: 비행기 종류의 최소 개수

# 체크할 조건
# T <= 100
# 2 <= N <= 1000
# 1 <= M <= 10000
# 국가는 1부터 시작

# Union-Find 자료구조를 활용한다.
# Union N-1번하면 끝
# 그냥 N-1번이 끝

import sys
input = sys.stdin.readline

def solution(N, M):
    for i in range(M):
        input()
    print(N-1)

if __name__ == '__main__':
    for t in range(int(input())):
        solution(*map(int, input().split()))