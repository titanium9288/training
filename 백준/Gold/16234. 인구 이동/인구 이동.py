from collections import defaultdict, deque


N, L, R = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
days = 0


while True:
    # 연합 생성을 위한 그래프
    graph = defaultdict(list)
    is_visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            for dr, dc in DIRECTIONS:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                # 조건에 해당하는 칸을 연합으로 만듦
                if L <= abs(grid[r][c] - grid[nr][nc]) <= R:
                    graph[(r, c)].append((nr, nc))

    # 연합이 만들어지지 않았을 경우
    if not graph:
        break

    for sr in range(N):
        for sc in range(N):

            # 방문 체크
            if is_visited[sr][sc]:
                continue

            if not graph[(sr, sc)]:
                continue

            union_cells = [(sr, sc)]
            is_visited[sr][sc] = True
            queue = deque(union_cells)

            while queue:
                r, c = queue.popleft()
                for nr, nc in graph[(r, c)]:
                    if is_visited[nr][nc]:
                        continue

                    is_visited[nr][nc] = True
                    queue.append((nr, nc))
                    union_cells.append((nr, nc))

            # 인구 합 누적 및 평균 계산
            popularity_sum = 0
            for r, c in union_cells:
                popularity_sum += grid[r][c]

            popularity_avg = popularity_sum // len(union_cells)
            for r, c in union_cells:
                grid[r][c] = popularity_avg

    days += 1

print(days)
