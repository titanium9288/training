from collections import deque


def melt_iceberg(grid):
    # 깊은 복사
    new_grid = [row[:] for row in grid]
    remain_cells = 0

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                continue

            near_zero = 0

            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if grid[nr][nc] == 0:
                    near_zero += 1

            new_grid[r][c] = max(0, new_grid[r][c] - near_zero)
            if new_grid[r][c] > 0:
                remain_cells += 1

    return new_grid, remain_cells


def is_all_melted(grid):
    return all(cell == 0 for row in grid for cell in row)


R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
year = 0
ice_cells = sum(1 for row in grid for cell in row if cell > 0)


while ice_cells:
    icebergs = 0
    is_visited = [[False] * C for _ in range(R)]

    # BFS
    for sr in range(R):
        for sc in range(C):

            if is_visited[sr][sc] or grid[sr][sc] == 0:
                continue

            icebergs += 1
            queue = deque([(sr, sc)])
            is_visited[sr][sc] = True

            # BFS
            while queue:
                r, c = queue.popleft()

                for dr, dc in DIRECTIONS:
                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if is_visited[nr][nc] or grid[nr][nc] == 0:
                        continue

                    is_visited[nr][nc] = True
                    queue.append((nr, nc))

    if icebergs >= 2:
        break

    grid, ice_cells = melt_iceberg(grid)
    year += 1


if ice_cells:
    print(year)
else:
    print(0)
