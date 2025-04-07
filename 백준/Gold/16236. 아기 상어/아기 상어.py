from collections import deque
import heapq


# 맨해튼 거리
# 거리 계산하려고 해당 함수를 넣었었는데, 막상 실제 계산 거리가 다르다!
# 이 함수는 장애물을 고려하지 않았기 때문. 실제로는 BFS를 이용해서 찾아야한다.
def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


# 거리, r, c 로 return
def bfs(shark_size):
    shark_r, shark_c = shark_pos

    is_visited = [[float("inf")] * N for _ in range(N)]
    is_visited[shark_r][shark_c] = 0
    queue = deque([(shark_r, shark_c)])

    while queue:
        r, c = queue.popleft()

        for dr, dc in DIRECTIONS:
            nr = r + dr
            nc = c + dc

            # 범위 조건부터 체크
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            # 상어보다 큰 물고기가 있을 때
            if is_visited[nr][nc] != float("inf") or grid[nr][nc] > shark_size:
                continue

            is_visited[nr][nc] = is_visited[r][c] + 1
            queue.append((nr, nc))

    return is_visited


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
queue = []
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 상태 저장
# 상어
shark_pos = (0, 0)
shark_size = 2
shark_feed = 0

# 물고기
fish_dict = {}
total_distance = 0

# 반복 방지를 위해 물고기를 dict로 관리
for r in range(N):
    for c in range(N):
        if grid[r][c] == 9:
            shark_pos = (r, c)
            grid[r][c] = 0

        elif grid[r][c] != 0:
            fish_dict[(r, c)] = grid[r][c]

# 우선순위 큐로 먹는걸 처리
while True:
    pq = []
    distances = bfs(shark_size)

    for fish_pos, fish_size in fish_dict.items():
        if fish_size >= shark_size:
            continue

        # 상어가 먹을 수 있는 물고기에 대해서만 heap에 push
        fish_r, fish_c = fish_pos
        fish_distance = distances[fish_r][fish_c]
        heapq.heappush(pq, (fish_distance, fish_r, fish_c))

    if pq:
        distance, r, c = heapq.heappop(pq)

        # 거리가 무한인 물고기가 먼저 큐에서 나왔다면
        if distance == float("inf"):
            break

        # 상어 위치 갱신
        shark_pos = (r, c)

        # 상어 크기 갱신
        shark_feed += 1
        if shark_feed == shark_size:
            shark_size += 1
            shark_feed = 0

        total_distance += distance
        del fish_dict[(r, c)]

    else:
        break

print(total_distance)
