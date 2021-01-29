def solution(N, M):
    lst = list(map(int, input().split()))
    s = cnt = val = 0
    for e in range(N):
        val += lst[e]
        if val > M:
            while s <= e and val > M:
                val -= lst[s]
                s += 1
            if val == M: cnt += 1
        elif val == M: cnt += 1
    print(cnt)

if __name__ == '__main__':
    solution(*map(int, input().split()))