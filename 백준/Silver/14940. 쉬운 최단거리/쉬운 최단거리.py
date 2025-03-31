from collections import deque


def find_start_pos():
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 2:
                return x, y
    return 0, 0


N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

# 시작 좌표 설정
sx, sy = find_start_pos()
queue = deque([(sx, sy)])
dist[sy][sx] = 0

# BFS
DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    x, y = queue.popleft()

    for dx, dy in DIRECTION:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < M) or not (0 <= ny < N):
            continue

        if dist[ny][nx] > -1:
            continue

        if grid[ny][nx] == 0:
            continue

        dist[ny][nx] = dist[y][x] + 1
        queue.append((nx, ny))

# 최단 거리 배열에서 벽 갱신
for y in range(N):
    for x in range(M):
        if grid[y][x] == 0:
            dist[y][x] = 0

# 출력 형식 맞추기
for row in dist:
    print(*row)
