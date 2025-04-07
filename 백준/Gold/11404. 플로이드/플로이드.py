N = int(input())
M = int(input())


dist = [
    [0 if start == end else float("inf") for end in range(N + 1)]
    for start in range(N + 1)
]


for _ in range(M):
    start, end, cost = map(int, input().split())
    dist[start][end] = min(dist[start][end], cost)


# 플로이드-워셜
# 경유지를 고정하고 계산하기

for k in range(1, N + 1):
    for start in range(1, N + 1):
        for end in range(1, N + 1):
            dist[start][end] = min(dist[start][k] + dist[k][end], dist[start][end])

# 코드 출력
for row in dist[1:]:
    print(*(cell if cell != float("inf") else "0" for cell in row[1:]))
