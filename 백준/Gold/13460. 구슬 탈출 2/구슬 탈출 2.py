from collections import deque
from copy import deepcopy


# 축과 방향에 따라서 조건 중복을 줄이는 방법을 따로 함수로 작성했다가,
# 가독성이 좀 떨어지길래 그냥 원시적인 방법으로 해결하기로 했다
def marble_priority(direction, state):
    red_r, red_c = state["R"]
    blue_r, blue_c = state["B"]

    if direction == "N":
        return ["R", "B"] if red_r < blue_r else ["B", "R"]
    if direction == "W":
        return ["R", "B"] if red_c < blue_c else ["B", "R"]
    if direction == "S":
        return ["R", "B"] if red_r > blue_r else ["B", "R"]
    if direction == "E":
        return ["R", "B"] if red_c > blue_c else ["B", "R"]


# 입력 받은 방향으로 입력 받은 구슬을 움직인 후 구멍에 빠졌는지 여부를 반환
def move_one_marble(color, direction, state):
    # list의 얕은 복사 이용하기
    r, c = state[color]
    dr, dc = DIRECTIONS[direction]

    while True:
        nr = r + dr
        nc = c + dc

        if grid[nr][nc] == "O":
            state[color] = (nr, nc)
            return True

        # 벽 만나면 한 칸 덜가기
        elif grid[nr][nc] == "#":
            state[color] = (r, c)
            return False

        else:
            r, c = nr, nc


# 움직임은 얕은 복사로 처리하고,
# 결과는 dict 로 묶어서 구멍에 빠졌는지 여부를 반환
def move_until_stop(direction, state):
    first, second = marble_priority(direction, state)

    # 첫 번째 구슬을 먼저 움직이고
    first_result = move_one_marble(first, direction, state)

    r, c = state[first]
    if grid[r][c] != "O":
        # 구슬이 빠지지 않았다면, 임시로 벽을 세우기
        grid[r][c] = "#"

    # 두 번째 구슬을 움직이고
    second_result = move_one_marble(second, direction, state)

    # 임시로 세운 벽을 없애기
    if grid[r][c] == "#":
        grid[r][c] = "."

    # 구멍에 빠져있는지 eturn
    return {first: first_result, second: second_result}


R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

DIRECTION_ORDER = ["N", "W", "S", "E"]
DIRECTIONS = {"N": (-1, 0), "W": (0, -1), "S": (1, 0), "E": (0, 1)}

# 요소들 위치 초기화.
marble = {"R": (0, 0), "B": (0, 0)}

# 위치 저장 및 구슬 위치 초기화
for r in range(R):
    for c in range(C):
        if grid[r][c] in ("R", "B"):
            marble[grid[r][c]] = (r, c)
            grid[r][c] = "."

# 상태니까 방문 여부를 set으로 저장
visited = set()
queue = deque()

visited.add((marble["R"], marble["B"]))
queue.append((marble.copy(), 0))

answer = -1

# BFS
while queue:
    current, count = queue.popleft()

    if count >= 10:
        continue

    for direction in DIRECTION_ORDER:
        sim = deepcopy(current)
        result = move_until_stop(direction, sim)

        if (sim["R"], sim["B"]) in visited:
            continue
        if result["B"]:
            continue
        if result["R"]:
            answer = count + 1
            queue.clear()
            break

        visited.add((sim["R"], sim["B"]))
        queue.append((sim, count + 1))

print(answer)
