# 처음에 Run or triplet이 생기기만 하면 그것이 바로 전체 문제에 대한 최적해이다.

# 출력: 승자 번호 (무승부는 0 출력)

def Run(arr):
    for i in range(len(arr)-2):
        if arr[i] and arr[i+1] and arr[i+2]:
            return True
    return False

def triplet(arr):
    for i in range(len(arr)):
        if arr[i] >= 3:
            return True
    return False

T = int(input())
for t in range(1, T+1):
    inp = list(map(int, input().split()))
    num1 = [0 for i in range(10)]
    num2 = [0 for i in range(10)]
    result = 0
    for i in range(12):
        if i&1:
            num2[inp[i]] += 1
            if Run(num2) or triplet(num2):
                result = 2
                break
        else:
            num1[inp[i]] += 1
            if Run(num1) or triplet(num1):
                result = 1
                break
    print('#{0} {1}'.format(t, result))