def Win(num1, card1, num2, card2):
    if card1 == card2:
        if num1 < num2: return num1, card1
        else: return num2, card2
    elif (card1 == 1 and card2 == 2) or (card1 == 2 and card2 == 3) or (card1 == 3 and card2 == 1):
        return num2, card2
    else:
        return num1, card1

def Game(start, end):
    mid = (start + end) // 2
    
    if mid == 0:
        
    if mid == 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))