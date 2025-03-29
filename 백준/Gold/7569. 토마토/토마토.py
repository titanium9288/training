from collections import deque
import sys

input = sys.stdin.readline


# 구조적으로 z, x, y 순서로 접근하는게 짜증나서 get, set 만듦
def get_tomato(x, y, z):
    return tomatoes[z][y][x]


def set_tomato(x, y, z, n):
    tomatoes[z][y][x] = n


M, N, H = map(int, input().split())

tomatoes = []

for _ in range(H):
    level = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(level)

queue = deque()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if get_tomato(x, y, z) == 1:
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

        if get_tomato(nx, ny, nz) != 0:
            continue

        set_tomato(nx, ny, nz, get_tomato(x, y, z) + 1)
        max_day = max(max_day, get_tomato(nx, ny, nz))
        queue.append((nx, ny, nz))


if any(0 in row for level in tomatoes for row in level):
    print(-1)
else:
    print(max_day - 1)
