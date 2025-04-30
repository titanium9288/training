# CCTV 타입과 방향이 들어오면, 시야 범위를 정한다
def find_direction(cctv_type, direction):
    valid_directions = []

    valid_directions.append(direction)
    if cctv_type in (3, 4, 5):
        valid_directions.append((direction + 1) % 4)
    if cctv_type in (2, 4, 5):
        valid_directions.append((direction + 2) % 4)
    if cctv_type == 5:
        valid_directions.append((direction + 3) % 4)

    return valid_directions


def find_sight(r, c, directions):
    sight = set()

    for d in directions:
        dr, dc = DIRECTIONS[d]
        nr = r + dr
        nc = c + dc

        while 0 <= nr < R and 0 <= nc < C:
            if grid[nr][nc] == 6:
                break

            # CCTV 그 자체는 감시대상으로 포함되지 않음
            if grid[nr][nc] == 0:
                sight.add((nr, nc))

            nr += dr
            nc += dc

    return sight


def backtrack(depth, seen: set):
    global max_seen

    # 가지치기용 상한선
    # 남은 CCTV 수 * (R + C)
    max_sight = (len(cctv) - depth) * (R + C)

    # 앞으로 볼 수 있는 최대치가 관측한 최대치보다 작으면
    # 현재 루트를 포기
    if len(seen) + max_sight <= max_seen:
        return

    if depth == len(cctv):
        max_seen = max(max_seen, len(seen))
        return

    r, c, cctv_type = cctv[depth]
    for i in range(4):
        directions = find_direction(cctv_type, i)
        sight = find_sight(r, c, directions)

        backtrack(depth + 1, seen | sight)


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

R, C = map(int, input().split())
grid = []
cctv = []

total_blank = 0
max_seen = 0

for r in range(R):
    row = list(map(int, input().split()))

    for c in range(C):
        if row[c] in range(1, 6):
            cctv.append((r, c, row[c]))

    total_blank += row.count(0)
    grid.append(row)

backtrack(0, set())
print(total_blank - max_seen)
