from collections import deque

T = int(input())


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()

        # 상하좌우
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and field[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1

    return size


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
                cluster_count += bfs(i, j) > 0

    print(cluster_count)
