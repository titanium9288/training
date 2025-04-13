from collections import deque


R, C = map(int, input().split())

grid = []
fires = []
JH = [(0, 0, 0)]

fire_visited = [[float("inf")] * C for _ in range(R)]
JH_visited = [[False] * C for _ in range(R)]


for r in range(R):
    row = list(input())

    for c in range(C):
        if row[c] == "F":
            fires.append((r, c, 0))
            fire_visited[r][c] = 0
            row[c] = "."

        if row[c] == "J":
            JH = [(r, c, 0)]
            JH_visited[r][c] = True
            row[c] = "."

    grid.append(row)


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 1차 BFS, 불의 퍼지는 위치 체크용
queue = deque(fires)

while queue:
    r, c, times = queue.popleft()

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if fire_visited[nr][nc] != float("inf") or grid[nr][nc] == "#":
            continue

        fire_visited[nr][nc] = times + 1
        queue.append((nr, nc, times + 1))


# 2차 BFS, 지훈이의 움직임 체크
queue = deque(JH)

while queue:
    r, c, times = queue.popleft()

    # 탈출 조건
    if r in (0, R - 1) or c in (0, C - 1):
        print(times + 1)
        break

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if JH_visited[nr][nc] or grid[nr][nc] == "#":
            continue
        # 만약 불이 이미 도달했거나, 불과 같은 턴에 움직이려고 한다면?
        if times + 1 >= fire_visited[nr][nc]:
            continue

        JH_visited[nr][nc] = True
        queue.append((nr, nc, times + 1))

else:
    print("IMPOSSIBLE")
