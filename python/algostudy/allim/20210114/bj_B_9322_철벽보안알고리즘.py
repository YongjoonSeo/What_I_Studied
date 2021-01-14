# 한 단어는 1~10개의 A-Z로 이루어진 문자열 
# 한 문장은 공백으로 구분된 단어들
# 제 1 공개키 - 최대 한 번 사용된 단어
# 제 2 공개키 - 제 1 공개치 재배치
# 암호문은 평문을 제 2 공개키 규칙 대로 재배치하여 만듬 

# 출력: 암호문을 해독한 평문

# 제 1 공개키를 딕셔너리에 본인위치를 저장
# 제 2 공개키를 딕셔너리에 본인위치를 저장
# 제 2 공개키의 값 -> 제 1 공개키의 값이 되도록 해독 list를 만들어 대입한다.

import sys
input = sys.stdin.readline

def solution(N):
    first, second, target = [list(input().split()) for i in range(3)]
    first_key, second_key = dict(), dict()
    for i in range(N):
        first_key[first[i]] = i
        second_key[second[i]] = i
    key = [0 for i in range(N)]
    for word in second_key.keys():
        key[second_key.get(word)] = first_key.get(word)
    result = [0 for i in range(N)]
    for i in range(len(target)):
        result[key[i]] = target[i]
    print(' '.join(result))

if __name__ == '__main__':
    for t in range(int(input())):
        solution(int(input()))