from collections import deque
import sys

sys.setrecursionlimit(10**6)


# 경계 체크용 함수
def in_range(r, c):
    return 0 <= r < N and 0 <= c < M


def generate_wall_combinations(wall_count, start):
    if wall_count == 3:
        # 벽이 완성되었을 때 안전구역의 크기를 반환
        return infection()

    max_safe = 0

    for idx in range(start, N * M):
        r = idx // M
        c = idx % M

        if grid[r][c] != 0:
            continue

        grid[r][c] = 1
        safe = generate_wall_combinations(wall_count + 1, idx + 1)
        grid[r][c] = 0

        max_safe = max(max_safe, safe)

    return max_safe


def infection():
    queue = deque(VIRUS)
    copy_grid = [row[:] for row in grid]

    while queue:
        r, c = queue.popleft()

        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc

            if not in_range(nr, nc):
                continue

            if copy_grid[nr][nc] == 0:
                copy_grid[nr][nc] = 2
                queue.append((nr, nc))

    safe = (
        (N * M)
        - ((sum(map(sum, copy_grid)) - (original_wall_count + 3)) // 2)
        - (original_wall_count + 3)
    )
    # safe = sum([copy_grid[r][c] == 0 for r in range(N) for c in range(M)])
    return safe


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
VIRUS = [(r, c) for r in range(N) for c in range(M) if grid[r][c] == 2]

original_wall_count = sum(map(sum, grid)) - (len(VIRUS) * 2)
# original_wall_count = sum([grid[r][c] == 1 for r in range(N) for c in range(M)])

print(generate_wall_combinations(0, 0))
