reference = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
word = input()
result = 0

for letter in word:
    for key in reference:
        if letter in key:
            result += reference.get(key)

print(result)