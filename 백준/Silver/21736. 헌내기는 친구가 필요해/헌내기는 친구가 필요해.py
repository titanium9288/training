from collections import deque


R, C = map(int, input().split())
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

grid = []
pos_of_P = set()
start = (0, 0)

for r in range(R):
    row = list(input())
    grid.append(row)

    for c in range(C):
        if row[c] == "P":
            pos_of_P.add((r, c))
            grid[r][c] = "O"

        if row[c] == "I":
            start = (r, c)
            grid[r][c] = "O"

queue = deque([start])
visited = [[False] * C for _ in range(R)]
answer = 0

while queue:
    r, c = queue.popleft()

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if visited[nr][nc] or grid[nr][nc] == "X":
            continue

        if (nr, nc) in pos_of_P:
            answer += 1

        visited[nr][nc] = True
        queue.append((nr, nc))

print(answer if answer != 0 else "TT")
