def solution(n, lst):
    result = -float('inf')
    val = -1001
    for num in lst:
        if val < 0: val = num
        else: val += num
        if result < val: result = val
    print(result)

if __name__ == '__main__':
    solution(int(input()), list(map(int, input().split())))