N = int(input())
rooms = []

for i in range(N):
    room = list(map(int, input().split()))
    rooms.append(room)

rooms.sort(key=lambda x: (x[1], x[0]))

finish_time = 0
answer = 0

for room in rooms:
    if finish_time <= room[0]:
        finish_time = room[1]
        answer += 1
        # print(room)

print(answer)
