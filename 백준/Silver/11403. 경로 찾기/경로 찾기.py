N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
dist = [row[:] for row in grid]


# 플로이드 - 워셜
for k in range(0, N):
    for start in range(0, N):
        for end in range(0, N):
            if dist[start][k] and dist[k][end]:
                dist[start][end] = 1

for row in dist:
    print(*row)