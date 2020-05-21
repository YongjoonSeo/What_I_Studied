# 서로 다른 L개의 알파벳 소문자, 최소 한 개의 모음과 최소 두 개의 자음으로 구성.
# 암호 알파벳은 증가하는 순서
# C가지의 문자 종류를 사용해서 암호로 만든다.
# 전부 다 찾고 검사하자.
# 순서 늘어나지 않는 건 걸러내기.

def check(string):
    vowels = 'aeiou'
    vowelcnt = 0
    conscnt = 0
    for char in string:
        if char in vowels: vowelcnt += 1
        else: conscnt += 1
        if vowelcnt >= 1 and conscnt >= 2:
            return True
    return False

def BT(string, depth):
    if depth == 0:
        if check(string): print(string)
        return
    for i in range(len(alp)):
        if not string:
            BT(alp[i], depth-1)
        else:
            if string[-1] < alp[i]:
                BT(string + alp[i], depth-1)


L, C = map(int, input().split())
alp = list(input().split())
alp.sort()
visited = [0 for i in range(len(alp))]

BT('', L)