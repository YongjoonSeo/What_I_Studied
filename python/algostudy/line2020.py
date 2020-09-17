# # 상품이 2개씩 (같은 종류일수도 아닐수도) 상자
# # 최대한 짝을 맞춰 재포장 -> 1+1행사

# # 출력: 짝 맞추기 위해 추가구매해야하는 최소 개수

# # 상자의 개수 마다 2개씩 물품이 있으면 된다.
# # -> 물건마다 개수를 모두 정리한 다음
# # -> // 2 해서 상자의 개수랑 비교.
# # -> 비는 만큼 추가구매

# def solution(boxes):
#     store = dict()
#     for box in boxes:
#         if store.get(box[0]):
#             store[box[0]] += 1
#         else:
#             store[box[0]] = 1
#         if store.get(box[1]):
#             store[box[1]] += 1
#         else:
#             store[box[1]] = 1
            
#     cnt = 0
#     for key in store.keys():
#         cnt += store.get(key) // 2
    
#     answer = len(boxes) - cnt    
    
#     return answer


# ------ 1번

def one(card, person):
    if person <= 10:
        return 11
    return 1

def solution(cards):
    answer = 0
    player = 0
    dealer = 0
    opencard = 0
    idx = 0
    step = 1

    while idx < len(cards):
        card = cards[idx]
        if card > 10: card = 10
        if step == 1 or step == 3:
            if card == 1:
                player += one(card, player)
            else:
                player += card
            step += 1
            idx += 1
        elif step == 2:
            if card == 1:
                dealer += one(card, dealer)
            else:
                dealer += card
            step += 1
            idx += 1
        elif step == 4:
            if card == 1:
                dealer += one(card, dealer)
            else:
                dealer += card
            opencard = card
            step += 1
            idx += 1
        elif step == 5:
            if player <= 21 and not (opencard in (4, 5, 6)):
                if (opencard == 1 or opencard >= 7) and player < 17: 
                    if card == 1:
                        player += one(card, player)
                    else:
                        player += card
                    idx += 1
                elif (opencard == 2 or opencard == 3) and player < 12: 
                    if card == 1:
                        player += one(card, player)
                    else:
                        player += card
                    idx += 1
                else:
                    step += 1
            elif player > 21:
                answer -= 2
                player, dealer, opencard, step = 0, 0, 0, 1
        elif step == 6:
            if dealer < 17:
                if card == 1:
                    dealer += one(card, dealer)
                else:
                    dealer += card
                idx += 1
            elif dealer > 21:
                answer += 2
                player, dealer, opencard, step = 0, 0, 0, 1
            else:
                step += 1
        elif step == 7:
            if abs(player - 21) > abs(dealer - 21):
                answer -= 2
            elif abs(player - 21) < abs(dealer - 21):
                if player == 21:
                    answer += 3
                else:
                    answer += 2
            player, dealer, opencard, step = 0, 0, 0, 1
        print(step, player, dealer, card, opencard, idx)
              
    return answer

print(solution([12, 7, 11, 6, 2, 12]))