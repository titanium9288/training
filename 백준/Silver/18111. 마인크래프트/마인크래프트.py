import sys
from collections import Counter

N, M, B = map(int, input().split())

block_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
block_counter = Counter([cell for row in block_map for cell in row])
min_time = [sys.maxsize, 0]

for height in range(0, 257):
    # 높이마다 시간을 계산
    spend_time = 0

    # 빼야하는 블록, 더해야하는 블록
    sub_block, add_block = 0, 0

    for map_height, count in block_counter.items():
        if map_height > height:
            sub_block += (map_height - height) * count
        else:
            add_block += (height - map_height) * count

    if add_block > sub_block + B:
        continue

    spend_time = sub_block * 2 + add_block
    if spend_time <= min_time[0]:
        min_time = [spend_time, height]

# 시간이 가장 적게 걸리는 높이를 출력
print(f"{min_time[0]} {min_time[1]}")
