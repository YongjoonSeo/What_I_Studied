def switch(n):
    if n == '0':
        return '1'
    return '0'

num = int(input())
lst = list(input().split())
times = int(input())
for i in range(times):
    stu = list(map(int, input().split()))
    if stu[0] == 1:
        for j in range(len(lst)):
            if (j+1) % stu[1] == 0:
                lst[j] = switch(lst[j])
    else:
        a = stu[1] - 1
        lst[a] = switch(lst[a])
        i = 1
        while a - i >= 0 and a + i + 1 <= len(lst):
            if lst[a-i] == lst[a+i]:
                lst[a-i] = switch(lst[a-i])
                lst[a+i] = switch(lst[a+i])
                i += 1
            else:
                break
j = 1
while 20*j + (j - 1) < len(lst):
    lst.insert(20*j + (j - 1), '2')
    j += 1
string = ' '.join(lst)
result = string.split(' 2 ')
for k in result:
    print(k)

# 문제 잘 읽기!!
# 출력 형식 리스트 or 문자열 사이에 끼워넣는 거 인덱스 조심.!!!!!