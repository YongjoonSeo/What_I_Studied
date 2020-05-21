# 1~49에서 6개 고름
# k개의 수가 있는 집합 S 안에서 번호 선택
# 조합 그냥 풀듯이 풀어도 될테고 백트래킹도 가능할듯

# def combi(arr, start, r):
#     for i in range(start, len(arr)-r+1):
#         if r == 1:
#             yield [arr[i]]
#         else:
#             for j in combi(arr, i+1, r-1):
#                 yield [arr[i]] + j
#
# while True:
#     line = input()
#     if line == '0': break
#     line = list(map(int, line.split()))
#     lst = line[1:]
#     for i in combi(lst, 0, 6):
#         print(*i)
#     print()

def BT(start, r):
    if r == 0:
        print(*result)
        return
    for i in range(start, len(visited)-r+1):
        if not visited[i]:
            visited[i] = 1
            result.append(lst[i])
            BT(i+1, r-1)
            visited[i] = 0
            result.pop()

while True:
    line = input()
    if line == '0': break
    line = list(map(int, line.split()))
    lst = line[1:]
    visited = [0 for i in range(len(lst))]
    result = []
    BT(0, 6)
    print()