N = int(input())
idx = 1
multi_idx = 1
count = 1
while idx < N:
    count += 1
    if N >= idx + 1 and N <= idx + multi_idx * 6:
        break
    idx = idx + multi_idx * 6
    multi_idx += 1

print(count)


