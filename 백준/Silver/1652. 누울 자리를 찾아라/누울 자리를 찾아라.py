room_size = int(input())
room = []

for _ in range(room_size):
    room.append(list(input()))

# 가로로 누울 자리
horizon_seat = 0
# 세로로 누울 자리
vertical_seat = 0

for row in range(room_size):
    for column in range(room_size):
        # 현재 칸에 짐이 있다면 자리 성립 불가능.
        if room[row][column] == "X":
            continue

        # 가로로 누울 자리를 체크해보기.
        # 먼저, 바로 뒷 칸이 비어있는가?
        if column + 1 < room_size and room[row][column + 1] == ".":
            # 누울 자리의 뒷 칸이 벽이거나 짐인가?
            if column + 2 >= room_size or room[row][column + 2] == "X":
                horizon_seat += 1

        # 세로로 누울 자리를 체크해보기.
        # 먼저, 바로 뒷 칸이 비어있는가?
        if row + 1 < room_size and room[row + 1][column] == ".":
            # 누울 자리의 뒷 칸이 벽이거나 짐인가?
            if row + 2 >= room_size or room[row + 2][column] == "X":
                vertical_seat += 1

print(horizon_seat, vertical_seat)