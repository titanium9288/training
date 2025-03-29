from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatoes = []

for _ in range(H):
    level = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(level)

queue = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 1:
                queue.append((x, y, z))

max_day = 1

# BFS
while queue:
    x, y, z = queue.popleft()

    for dx, dy, dz in [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
    ]:
        nx = x + dx
        ny = y + dy
        nz = z + dz

        if not (0 <= nx < M) or not (0 <= ny < N) or not (0 <= nz < H):
            continue

        if tomatoes[nz][ny][nx] != 0:
            continue

        tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
        max_day = max(max_day, tomatoes[nz][ny][nx])
        queue.append((nx, ny, nz))


if any(0 in row for level in tomatoes for row in level):
    print(-1)
else:
    print(max_day - 1)
