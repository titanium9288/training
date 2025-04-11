from collections import deque


def melt_cheese(air):
    melted_cheeses = set()

    for cheese in cheeses:
        r, c = cheese

        air_count = 0
        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if air[nr][nc]:
                air_count += 1

        if air_count >= 2:
            grid[r][c] = 0
            melted_cheeses.add(cheese)

    return cheeses - melted_cheeses


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cheeses = set((r, c) for r in range(R) for c in range(C) if grid[r][c] == 1)
turns = 0

while cheeses:
    external_air = [[False] * C for _ in range(R)]
    external_air[0][0] = True
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()

        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if external_air[nr][nc] or grid[nr][nc] == 1:
                continue

            external_air[nr][nc] = True
            queue.append((nr, nc))

    cheeses = melt_cheese(external_air)
    turns += 1

print(turns)
