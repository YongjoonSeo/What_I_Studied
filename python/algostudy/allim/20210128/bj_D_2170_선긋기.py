import sys
input = sys.stdin.readline

def solution(N):
    lst = []
    for i in range(N):
        lst.append(tuple(map(int, input().split())))
    lst.sort()
    leng, now = 0, lst[0][0]
    for x, y in lst:
        s = now if now > x else x
        if now < y:
            leng += y - s
            now = y
    print(leng)

if __name__ == '__main__':
    solution(int(input()))