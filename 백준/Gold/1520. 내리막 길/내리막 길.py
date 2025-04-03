import sys

sys.setrecursionlimit(10**6)


# 경계 체크용 함수
def in_range(r, c):
    return 0 <= r < N and 0 <= c < M


# DFS
def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1

    if is_visited[r][c] != -1:
        return is_visited[r][c]

    # 경로 누적 시작
    is_visited[r][c] = 0

    for dr, dc in DIRECTIONS:
        nr = r + dr
        nc = c + dc

        if not in_range(nr, nc):
            continue

        if grid[nr][nc] < grid[r][c]:
            is_visited[r][c] += dfs(nr, nc)

    return is_visited[r][c]


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
is_visited = [[-1] * M for _ in range(N)]
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

print(dfs(0, 0))
