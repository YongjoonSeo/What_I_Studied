def is_group(string):
    checker = set()
    tempword = string[0]
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            pass
        else:
            tempword += string[i]
    for letter in tempword:
        if letter not in checker:
            checker.add(letter)
        else:
            return False
    return True


N = int(input())
counter = 0
for _ in range(N):
    word = input()
    if is_group(word) == True:
        counter += 1

print(counter)