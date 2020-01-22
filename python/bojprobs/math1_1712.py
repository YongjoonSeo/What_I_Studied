A, B, C = map(int, input().split())
print(A // (C - B) + 1 if C - B > 0 else -1)