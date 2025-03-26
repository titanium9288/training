import sys

input = sys.stdin.readline

N, M = map(int, input().split())
table = []

for i in range(N):
    col = list(map(int, input().split()))
    table.append(col)

# 누적합
for i in range(N):
    for j in range(N):
        top, left, top_left = 0, 0, 0
        if i:
            top = table[i - 1][j]
        if j:
            left = table[i][j - 1]
        if i and j:
            top_left = table[i - 1][j - 1]

        table[i][j] = table[i][j] + top + left - top_left

# 누적합 계산
for i in range(M):
    x1, y1, x2, y2 = map(lambda x: x - 1, map(int, input().split()))

    total = table[x2][y2]
    if x1:
        total -= table[x1 - 1][y2]
    if y1:
        total -= table[x2][y1 - 1]
    if x1 and y1:
        total += table[x1 - 1][y1 - 1]

    print(total)