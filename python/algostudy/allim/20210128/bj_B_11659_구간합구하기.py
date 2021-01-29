import sys
input = sys.stdin.readline

def solution(N, M):
    lst = list(map(int, input().split()))
    min_sum = [0, lst[0]]
    for i in range(1, len(lst)):
        min_sum.append(min_sum[i] + lst[i])
    for j in range(M):
        s, e = map(int, input().split())
        print(min_sum[e] - min_sum[s-1])

if __name__ == '__main__':
    solution(*map(int, input().split()))