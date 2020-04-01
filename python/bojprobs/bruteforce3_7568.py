N = int(input())
people = [list(map(int, input().split())) for i in range(N)]
grades = [1 for i in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            grades[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            grades[i] += 1

print(*grades)