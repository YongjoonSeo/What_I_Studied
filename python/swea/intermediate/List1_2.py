T = int(input())
for i in range(1, T+1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    bus = count = 0

    while bus < N:
        templist = [j for j in range(bus+1, bus+K+1) if j in stops]
        if templist == []:
            if bus + K < N:
                print('#{0} 0'.format(i))
                break
            else:
                bus += K
                count += 1
        else:
            if bus + K >= N:
                bus += K
                count += 1
            else:
                bus = max(templist)
                count += 1
    else:
        print('#{0} {1}'.format(i, count - 1))
        




# T = int(input())
# for i in range(T):
#     K, N, M = map(int, input().split())
#     charger = list(map(int, input().split()))
#     total = bus = idx = 0
    
#     while bus < N:
#         if idx < len(charger):
#             if bus+K >= charger[idx]:
#                 max_charger = max([j for j in charger if j <= bus+K])
#                 idx = charger.index(max_charger)
#                 for l in charger:
#                     if l <= max_charger:
#                         charger.remove(l)
#                 bus += max_charger
#                 total += 1
#                 print(bus)
#                 print(idx)
#             else:
#                 print('#{0} 0'.format(i+1))
#                 break
#         else:
#             if bus+K >= charger[-1]:
#                 total += 1
#                 bus += K
#             else:
#                 print('#{0} 0'.format(i+1))
#                 break
#     else:
#         print('#{0} {1}'.format(i+1, total))         


    
    
#     # and idx < len(charger):
#     #     if bus + K < charger[idx]:
#     #         print('#{0} 0'.format(i+1))
#     #         break
#     #     elif charger[idx] == charger[len(charger) - 1] and bus + K < N:
#     #         print('#{0} 0'.format(i+1))
#     #         break
        
#     #     bus += charger[0] if bus == 0 else charger[idx] - charger[idx-1] 
#     #     idx += 1
#     #     total += 1
    
#     # if bus >= N:
#     #     print('#{0} {1}'.format(i+1, total))

