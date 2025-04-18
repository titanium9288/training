K = int(input())
DIRECTIONS = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]
pos = [(0, 0)]


for _ in range(6):
    d, length = map(int, input().split())

    x, y = pos[-1]
    dx, dy = DIRECTIONS[d]
    nx, ny = x + dx * length, y + dy * length

    pos.append((nx, ny))

area = 0

# 신발끈 공식
for i in range(6):
    x1, y1 = pos[i]
    x2, y2 = pos[i + 1]

    area += x1 * y2 - x2 * y1

area = abs(area) // 2

print(area * K)
