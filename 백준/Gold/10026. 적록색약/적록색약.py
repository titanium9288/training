import sys

sys.setrecursionlimit(10**6)


# DFS
def dfs(x, y, mode):
    for dx, dy in DIRECTIONS:
        nx = x + dx
        ny = y + dy

        # 탐색 범위 제한
        if not (0 <= nx < N) or not (0 <= ny < N):
            continue

        # 방문한 노드 체크
        if visited[ny][nx][mode]:
            continue

        if is_same_color(paint[y][x], paint[ny][nx], mode):
            visited[ny][nx][mode] = True
            dfs(nx, ny, mode)


def is_same_color(color1, color2, mode):
    if mode == "colorblind":
        # 해당 구조 수정 가능해보이나, 아이디어 부족...
        if color1 in "RG":
            color1 = "R"
        if color2 in "RG":
            color2 = "R"

    return color1 == color2


N = int(input())
paint = [list(input().strip()) for _ in range(N)]
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[{"normal": False, "colorblind": False} for _ in range(N)] for _ in range(N)]
answer = {"normal": 0, "colorblind": 0}

for y in range(N):
    for x in range(N):
        for mode in ("normal", "colorblind"):
            if not visited[y][x][mode]:
                dfs(x, y, mode)
                answer[mode] += 1

print(answer["normal"], answer["colorblind"])
