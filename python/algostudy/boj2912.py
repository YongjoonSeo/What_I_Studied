# 난쟁이 N, 모자색상 C
# 절반보다 많은 색이 같은 색이라면 예쁜 사진.
# (난쟁이가 k명이고 k/2보다 많이 모자 색이 같으면 예쁜 사진)
# 출력: 예쁜 사진인 경우 yes (절반 넘는 모자 색상) 아니면 no
# 1부터 시작함 (첫 번째 난쟁이, B번째 난쟁이)
# 가장 많은 모자 색상이 절반만 넘겨도 될 것이다.
# 토너먼트 식으로, 동률이면 각 모자 색상에 갯수 포함해서 올리고 아니라면 이기는 것만 갯수 포함해서 올리기.
# 이러면 중간에 누락되는 경우 있을거같은데.. 알고리즘 다시 생각해보자.ㄴ
import sys
input = sys.stdin.readline

def check(s, e): # 1. if s == e 2. 쪼개기
    mid = (s + e) // 2
    if s == e:
        return lst[s], 1
    left = check(s, mid)
    right = check(mid+1, e)

    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            if len(left) <= i: continue
            if len(right) <= j: continue
            if left[i] == right[j]

    # if left[0] == right[0]:
    #     return left[0], left[1]+right[1]
    # elif

N, C = map(int, input().split())
lst = list(map(int, input().split()))
M = int(input().strip())
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
