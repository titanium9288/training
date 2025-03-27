from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))

# BFS
while queue:
    x, y = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < N) or not (0 <= ny < M):
            continue

        if tomatoes[nx][ny] != 0:
            continue

        tomatoes[nx][ny] = tomatoes[x][y] + 1
        queue.append((nx, ny))


if any(0 in row for row in tomatoes):
    print(-1)
else:
    print(max(map(max, tomatoes)) - 1)
