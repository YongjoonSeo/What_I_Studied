def solution(k, room_number):
    answer = []
    rooms = dict()
    for room in room_number:
        if not rooms.get(room):
            rooms[room] = room + 1
            answer.append(room)
        else:
            arrive = rooms.get(room)
            while rooms.get(arrive):
                arrive = rooms.get(arrive)
            rooms[arrive] = arrive + 1
            rooms[room] = arrive
            answer.append(arrive)
    return answer

print(solution(10, [1,3,4,1,3,1]))