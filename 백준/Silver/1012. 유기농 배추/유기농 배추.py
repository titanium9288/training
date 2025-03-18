from collections import deque
import sys

sys.setrecursionlimit(10**6)


def dfs(x, y):
    if visited[x][y] or field[x][y] == 0:
        return 0

    # 방문 처리
    visited[x][y] = True
    size = 1

    # 상하좌우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < M and 0 <= ny < N:
            size += dfs(nx, ny)

    return size


T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    cluster_count = 0

    for i in range(K):
        X, Y = map(int, input().split())
        field[X][Y] = 1

    # for row in field:
    #     print("".join("■" if cell else "□" for cell in row))

    for i in range(M):
        for j in range(N):
            if not visited[i][j] and field[i][j] == 1:
                cluster_count += dfs(i, j) > 0

    print(cluster_count)
