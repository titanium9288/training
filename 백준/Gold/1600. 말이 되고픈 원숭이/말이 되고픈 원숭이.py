from collections import deque


K = int(input())
C, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
HORSE_MOVE = [
    (-2, -1),
    (-2, +1),
    (-1, -2),
    (-1, +2),
    (+1, -2),
    (+1, +2),
    (+2, -1),
    (+2, +1),
]

# 말처럼 이동할 수 있는 횟수를 차원으로 나눠 저장
visited = [[[float("inf")] * (K + 1) for _ in range(C)] for _ in range(R)]
visited[0][0][0] = 0
queue = deque([(0, 0, 0)])

while queue:
    r, c, horse = queue.popleft()
    moves = visited[r][c][horse]

    # 상하좌우 일반 이동
    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            continue

        if visited[nr][nc][horse] != float("inf") or grid[nr][nc] == 1:
            continue

        visited[nr][nc][horse] = moves + 1
        queue.append((nr, nc, horse))

    # 만약 말처럼 이동할 수 있는 횟수를 다 썼다면
    if horse == K:
        continue

    # 말처럼 움직이기
    for dr, dc in HORSE_MOVE:
        nr = r + dr
        nc = c + dc
        next_horse = horse + 1

        if not (0 <= nr < R and 0 <= nc < C):
            continue

        if visited[nr][nc][next_horse] != float("inf") or grid[nr][nc] == 1:
            continue

        visited[nr][nc][next_horse] = moves + 1
        queue.append((nr, nc, next_horse))

min_moves = min(visited[R - 1][C - 1])
if min_moves == float("inf"):
    print(-1)
else:
    print(min_moves)
