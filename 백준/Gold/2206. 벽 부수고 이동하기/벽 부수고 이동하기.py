from collections import deque


N, M = map(int, input().split())

# map에 padding
grid = [[0] + list(map(int, input().strip())) for _ in range(N)]
grid = [[0] * (M + 1)] + grid

# 1-based 좌표 생성
visited = [[[0, 0] for _ in range(M + 1)] for _ in range(N + 1)]
queue = deque([(1, 1, 0)])
visited[1][1][0] = 1

# BFS
while queue:
    x, y, is_break = queue.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy

        if not (1 <= nx <= N) or not (1 <= ny <= M):
            continue

        # 앞에 벽이 있고 부순 적이 없을 때
        if is_break == 0 and grid[nx][ny] == 1:
            will_break = 1

        # 벽이 아닌 경우
        elif grid[nx][ny] == 0:
            will_break = is_break

        # 앞에 벽이 있고, 이미 부쉈다면
        else:
            continue

        # 방문 체크
        if visited[nx][ny][will_break] == 0:
            visited[nx][ny][will_break] = visited[x][y][is_break] + 1
            queue.append((nx, ny, will_break))


# A or B일때 A = 0 이면 B를 참조하는 or 연산자의 특성을 이용
print(min(visited[N][M]) or max(visited[N][M]) or -1)
