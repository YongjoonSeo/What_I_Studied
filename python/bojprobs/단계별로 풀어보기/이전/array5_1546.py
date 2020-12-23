N = int(input())
scores = list(map(int, input().split()))
sum = ave = 0

for i in scores:
    sum += i / max(scores) * 100
ave = sum / len(scores)
print(ave)