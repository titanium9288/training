N, M = map(int, input().split())
y, x, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
clean = [[False] * M for _ in range(N)]

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def find_dirty_direction(x, y, nd):
    for _ in range(4):
        nd = rotate_ccw(nd)
        dx, dy = DIRECTIONS[nd]

        nx = x + dx
        ny = y + dy

        # 탐색 범위 제한
        if not (0 <= nx < M) or not (0 <= ny < N):
            continue

        # 벽일 경우 청소하지 않았다고 취급하지 않음
        if grid[ny][nx] == 1:
            continue

        if not clean[ny][nx]:
            return (nx, ny, nd)

    return None


def rotate_ccw(d):
    # 반시계 방향 회전
    return (d + 3) % 4


def get_back_pos(x, y, d):
    # 후진 가능여부 판단 후 좌표 제공
    back_d = (d + 2) % 4

    dx, dy = DIRECTIONS[back_d]

    nx = x + dx
    ny = y + dy

    # 탐색 범위 제한
    if not (0 <= nx < M) or not (0 <= ny < N):
        return None

    # 벽일 경우 후진 불가능
    if grid[ny][nx] == 1:
        return None

    return (nx, ny)


answer = 0

# 시뮬레이션
while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if not clean[y][x]:
        clean[y][x] = True
        answer += 1

    new_pos = find_dirty_direction(x, y, d)

    if new_pos is None:
        # 현재 칸의 주변 4칸 중, 청소되지 않은 빈 칸이 없는 경우

        back_pos = get_back_pos(x, y, d)
        if back_pos is None:
            # 후진 불가능, 작동 정지
            break
        else:
            x, y = back_pos
            continue

    else:
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        nx, ny, nd = new_pos
        x, y, d = nx, ny, nd

print(answer)
