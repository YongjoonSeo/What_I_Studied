N = int(input())
students = []
candi = [0 for i in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    students.append(temp)

for i in range(N-1):
    for j in range(i+1, N):
        for m in range(5):
            if students[i][m] == students[j][m]:
                candi[i] += 1
                candi[j] += 1
                break
print(candi.index(max(candi))+1)