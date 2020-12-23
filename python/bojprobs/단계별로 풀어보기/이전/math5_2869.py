# A, B, V = map(int, input().split())
# day = 1
# while True:
#     V -= A
#     if V <= 0:
#         break
#     V += B
#     day += 1
# print(day)

# A, B, V = map(int, input().split())
# by_day = A - B
# count = 0
# while V - A > 0:
#     V -= by_day
#     count += 1
# print(count + 1)

A, B, V = map(int, input().split())
day = 0
deno = A - B
nume = V - A

if nume % deno == 0:
    day = nume // deno + 1
else:
    day = nume // deno + 2

print(day)