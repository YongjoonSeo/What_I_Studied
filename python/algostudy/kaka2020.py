#     infos = []
#     # index_dict = dict()
#     for i in range(len(info)):
#         item = list(info[i].split())
#         item[-1] = int(item[-1])
#         infos.append(item)
    
#     infos.sort(key=lambda x: x[-1])
#     # for i in range(len(infos)):
#     #     if not index_dict.get(infos[i][-1]):
#     #         index_dict[infos[i][-1]] = i
    
#     qs = [] # 0 언어 2 분야 4 직급 6 음식
#     for item in query:
#         temp = list(item.split())
#         temp[-1] = int(temp[-1])
#         qs.append(temp)
#     print(qs) 
    
#     print(infos)
#     print(index_dict)


def BT(board, cy, cx, card, val, dy, dx, num, result):
    # if num == 0: 
    print(cy, cx, card, val, num)
    for _ in range(len(board)):
        print(board[_])
    print('-----------------')
    if num == 0:
        result[0] = min(result[0], val)
        return 
    if val >= result[0]: return
    if not card:
        if board[cy][cx]:
            card_val = board[cy][cx]
            board[cy][cx] = 0
            BT(board, cy, cx, card_val, 1 + val, dy, dx, num-1, result)
            board[cy][cx] = 1
        else:
            for i in range(4):
                for a in range(3):
                    if i == 0 or i == 2:
                        js = [1, 3]
                    else:
                        js = [0, 2]
                    for j in js:
                        tempy, tempx = cy + dy[i] * a, cx + dx[i]
                        while 0 <= tempy < 4 and 0 <= tempx < 4:
                            if board[tempy][tempx]:
                                card_val = board[tempy][tempx]
                                board[tempy][tempx] = 0
                                BT(board, tempy, tempx, card_val, 2 + a + val, dy, dx, num-1, result)
                                board[tempy][tempx] = card_val
                                break
                            tempy += dy[j]
                            tempx += dx[j]

                    for j in js:
                        tempy, tempx = cy + dy[i], cx + dx[i] * a
                        while 0 <= tempy < 4 and 0 <= tempx < 4:
                            if board[tempy][tempx]:
                                card_val = board[tempy][tempx]
                                board[tempy][tempx] = 0
                                BT(board, tempy, tempx, card_val, 2 + a + val, dy, dx, num-1, result)
                                board[tempy][tempx] = card_val
                                break
                            tempy += dy[j]
                            tempx += dx[j]
    else:
        for i in range(4):
            for b in range(4):
                if i == 0 or i == 2:
                    js = [1, 3]
                else:
                    js = [0, 2]
                
                for j in js:
                    tempy, tempx = cy + dy[i] * b, cx + dx[i]
                    while 0 <= tempy < 4 and 0 <= tempx < 4:
                        if board[tempy][tempx] == card:
                            card_val = board[tempy][tempx]
                            board[tempy][tempx] = 0
                            BT(board, tempy, tempx, 0, 2 + b + val, dy, dx, num-1, result)
                            board[tempy][tempx] = card_val
                            break
                        tempy += dy[j]
                        tempx += dx[j]

                
                for j in js:
                    tempy, tempx = cy + dy[i], cx + dx[i] * b
                    while 0 <= tempy < 4 and 0 <= tempx < 4:
                        if board[tempy][tempx] == card:
                            card_val = board[tempy][tempx]
                            board[tempy][tempx] = 0
                            BT(board, tempy, tempx, 0, 2 + b + val, dy, dx, num-1, result)
                            board[tempy][tempx] = card_val
                            break
                        tempy += dy[j]
                        tempx += dx[j]

def solution(board, r, c):
    result = [987654321]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    num = 0
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                num += 1
    # print(num)
    
    BT(board, r, c, 0, 0, dy, dx, num, result)
    # for _ in range(len(board)):
    #     print(board[_])
    return result

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
# board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r= 1
c = 0

print(solution(board, r, c))