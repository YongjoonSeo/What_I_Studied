# def in_fifteen(num):
#     if ((num - 10) % 3 == 0) or (num - 10 == 0):
#         return (num // 5 ) + (num % 5) // 3

# N = int(input())
# count = N // 15
# rest = N % 15

# N = int(input())
# count = 0
# if (N % 5) % 3 == 0:
#     count += (N // 5) + ((N % 5) // 3)
# elif (N % 3) % 5 == 0:
#     count += (N // 3)
# else:
#     count = -1
# print(count)

# N = int(input())
# count = 0 
# odd_5 = [8, 1, 4, 7]
# even_5 = [3, 6, 9, 2]
# if N >= 10:
#     if N % 10 in odd_5:
#         count += (N // 10 * 2) + 
#     elif N % 10 in even_5:
#         count += ()

N = int(input())
count = 0
if N % 5 == 0:
    count += N // 5
elif N % 5 == 3 or N % 5 == 1:
    count += N // 5 + 1
    if N == 1:
        count = -1
elif N % 5 == 4 or N % 5 == 2:
    count += N // 5 + 2
    if N == 2 or N == 4 or N == 7:
        count = -1
else:
    count = -1

print(count)