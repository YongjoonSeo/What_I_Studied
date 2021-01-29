import sys
input = sys.stdin.readline

def solution(N):
    lst = []
    for i in range(N):
        s, e = map(int, input().split())
        lst.append((s, 1))
        lst.append((e, -1))
    lst.sort()
    maxval = now = 0
    for coor, se in lst:
        now += se
        if maxval < now: maxval = now
    print(maxval)

if __name__ == '__main__':
    solution(int(input()))