import sys

input = sys.stdin.readline


def check_area(x, y, size):
    # 영역 내 모든 color가 동일한지 체크하는 함수
    color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != paper[i][j]:
                return False
    return color


def devide(x, y, size):
    # base case
    color = check_area(x, y, size)
    if color is not False:
        colors[color] += 1
        return

    half = size // 2
    for dx, dy in [(0, 0), (0, half), (half, 0), (half, half)]:
        nx = x + dx
        ny = y + dy

        devide(nx, ny, half)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
colors = [0, 0]

devide(0, 0, N)

print(colors[0])
print(colors[1])
