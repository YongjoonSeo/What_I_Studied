# N자리 가장 작은 좋은 수열 찾기
# N보다 길이 길면 자르기
# 한 문자열 검사하는데 최대 3240가지 가능성 -> N 충족했을 때 (N <= 80)
# 1. 검사해서 N 충족했을 때 결과값 넣기 -> 최소 결과 필요
# 2. 바로 전 숫자랑은 무조건 달라야 함. (1개가 겹치는지는 확인 불필요, 2개부터 N//2개짜리 까지 확인하기)
# 첫 숫자는 무조건 1 (최소니까) N=1 -> 1, N=2 -> 12, N=3 -> 121
# -> 1, 2조건으로 가지치기
#### 가장 작은 값부터 찾는 거라 하나 찾으면 사실상 끝이다.

# def check(string, n): #4이상
#     for i in range(2, n//2+1):
#         for j in range(len(string)-i+1):
#             if string[j:j+i] == string[j+i:j+i+i]:
#                 return False
#     return True

def check(string, n): # 4이상일때
    for i in range(2, n//2+1):
        if string[-(i*2):-i] == string[-i:len(string)]:
            return False
    return True

def BT(n, string):
    global result, N, isfound
    if int(string) >= result or n < 1: return
    if n == 1:
        result = min(result, int(string))
        isfound = True
        return
    for i in '123':
        if string[-1] == i: continue
        save = string
        string += i
        if len(string) >= 4:
            if not check(string, len(string)):
                string = save
                continue
        BT(n-1, string)
        string = save
        if isfound: return

N = int(input())
result = float('inf')
isfound = False
BT(N, '1')
print(result)
